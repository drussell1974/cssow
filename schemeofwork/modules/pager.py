

class Pager:



    def __init__(self, page = 1, page_size = 10, data = []):

        self.pager_size = 7

        self.page = int(page)
        self.page_size = int(page_size)
        self.data = data

        ' range of data to display '

        self.display_records_start = (self.page-1)*self.page_size
        self.display_records_end = self.display_records_start+self.page_size


        #self.set_pagination()


    def data_to_display(self):
        """
        Displays e.g. only 10 records at a time
        """
        return self.data[self.display_records_start:self.display_records_end]


    def render_html(self, url = ""):
        """
        Display e.g only 5 groups of 10 records (1 - 5, 6 - 10, 11 - 12)
        :return: html
        """


        self.start_page = self.page - (self.page % self.pager_size) + 1
        self.end_page = 0
        self.trailing_number_of_records = 0
        html = ""

        """ we find out where we need to start and end """

        self.total_number_of_records = len(self.data)

        first_record = (self.start_page * self.page_size) - self.page_size
        last_record = first_record + 1 * self.page_size * self.pager_size
        self.number_of_records = len(self.data[first_record:last_record]) # TODO: calculate
        ' check for leading and trailing pages '
        self.leading_number_of_records = len(self.data[:first_record]) # TODO: calculate
        self.trailing_number_of_records = len(self.data[last_record:]) # TODO: calculate
        self.number_of_pages = self.number_of_records // self.page_size

        if self.total_number_of_records > self.page_size:

            ' add the remainder '

            remainder = self.number_of_records - (self.number_of_pages * self.page_size)

            if remainder > 0 and remainder < self.page_size:
               self.number_of_pages = self.number_of_pages + 1

            self.end_page = self.start_page + self.number_of_pages

            """ create list items """
            if self.leading_number_of_records > 0:
                    """ create previous option """
                    html = html + create_list_item(url, self.page, self.start_page - 1, "&larr;")


            for page_number in range(self.start_page, self.end_page):
                    """ create the numbered pages """
                    html = html + create_list_item(url, self.page, page_number, page_number)


            if self.trailing_number_of_records > 0:
                """ create next option """
                html = html + create_list_item(url, self.page, self.end_page, "&rarr;")


        return html




    def __render_html(self, url = ""):
        """
        Display e.g only 5 groups of 10 records (1 - 5, 6 - 10, 11 - 12)
        :return: html
        """
        html = ""

        if self.show_previous_pages:
            """ show previous group """
            html = html + create_list_item(url, self.page, self.start_page, "&larr;")

        display_page_number_as = 0
        for page_number in range(self.start_page, int(self.end_page)):
            display_page_number_as = page_number + 1
            """ create list items """
            html = html + create_list_item(url, self.page, display_page_number_as, display_page_number_as)

        if self.show_more_pages == True:
            """ create next """
            html = html + create_list_item(url, self.page, display_page_number_as + 1, "&rarr;")

        return html


    def set_pagination(self):
        """ ********** """
        """ pagination """
        """ ********** """
        ' number of pages '
        _total_no_of_records = len(self.data)
        full_pages = _total_no_of_records // self.page_size
        trailing_pages1 = _total_no_of_records % self.page_size
        no_pages = full_pages + trailing_pages1
        _full_groups = full_pages // self.pager_size
        pages_in_full_group = _full_groups * self.pager_size
        trailing_pages2 = no_pages - pages_in_full_group
        if no_pages <= self.pager_size:
            self.start_page = 0
            self.end_page = no_pages
            self.show_previous_pages = False
            self.show_more_pages = False
        else:
            """ deal with pagination """

            self.show_previous_pages = True
            self.show_more_pages = True

            if self.page <= self.pager_size:
                """ first group """
                print("FIRST GROUP")

                self.start_page = 0
                self.show_previous_pages = False

                if full_pages < no_pages:
                    self.end_page = self.pager_size
                    self.show_more_pages = True
                else:
                    self.end_page = self.start_page + trailing_pages1
                    self.show_more_pages = False
            else:
                """ subsequent group """

                self.start_page = self.page - (self.page % self.pager_size)
                self.end_page = self.start_page + self.pager_size
                self.show_previous_pages = True

                if self.start_page >= pages_in_full_group:
                    """ last group """
                    print("LAST GROUP")
                    self.start_page = self.page - (self.page % self.pager_size)
                    self.end_page = self.start_page + trailing_pages2
                    self.show_more_pages = False
                    self.show_previous_pages = True


        print("_total_no_of_records = {}".format(_total_no_of_records))
        print("full_pages = {}".format(full_pages))
        print("trailing_pages1 = {}".format(trailing_pages1))
        print("no_pages = {}".format(no_pages))
        print("**********************************************")
        print("_full_groups = {}".format(_full_groups))
        print("pages_in_full_group = {}".format(pages_in_full_group))
        print("trailing_pages2 = {}".format(trailing_pages2))
        print("**********************************************")


#list_item = "<li><a href='{{=URL('schemesofwork', 'index', vars=dict(page=1))}}' class='btn {{if page == 1:}} btn-primary {{ pass }}'>1</a></li>"

def create_list_item(url, current_page, page_number, text):
    html = "<li><a href='{}".format(url)
    ' append url with ? or &'
    if "?" in url:
        html = html + "&"
    else:
        html = html + "?"
    ' add page number to url '
    html = html + "page={}' class='btn".format(page_number)
    if current_page == page_number:
        html = html + " btn-primary"
    html = html + "'>{}</a></li>".format(text)
    return html


