

class Pager:



    def __init__(self, page = 1, page_size = 10, data = []):

        self.pager_size = 7

        self.page = int(page)
        self.page_size = int(page_size)
        self.data = data

        ' range of data to display '

        self.display_records_start = (self.page-1)*self.page_size
        self.display_records_end = self.display_records_start+self.page_size


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
        self.start_page = 1

        if self.page % self.pager_size == 0:
            self.start_page = self.page - 6
        else:
            self.start_page = self.page - (self.page % self.pager_size) + 1
        self.end_page = 0
        self.trailing_number_of_records = 0
        html = ""

        """ we find out where we need to start and end """

        self.total_number_of_records = len(self.data)
        first_record = (self.start_page * self.page_size) - self.page_size
        last_record = first_record + 1 * self.page_size * self.pager_size
        self.number_of_records = len(self.data[first_record:last_record]) # TODO: calculate from total length of data

        ' check for leading and trailing pages '

        self.leading_number_of_records = len(self.data[:first_record]) # TODO: calculate from total length of data
        self.trailing_number_of_records = len(self.data[last_record:]) # TODO: calculate from total length of data

        self.number_of_pages = self.number_of_records // self.page_size

        if self.total_number_of_records > self.page_size:
            """ We only show pagination if there are more than one page """

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


