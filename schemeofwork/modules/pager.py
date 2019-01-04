import math

class Pager:



    def __init__(self, page = 1, page_size = 10, data = []):
        import datetime

        self.page = int(page)
        self.page_size = int(page_size)
        self.pager_size = 7
        self.data = data

        ' range of data to display '

        self.display_records_start = (self.page-1)*self.page_size
        self.display_records_end = self.display_records_start+self.page_size

        """ ********** """
        """ pagination """
        """ ********** """

        ' number of pages '
        total_no_of_records = len(self.data)
        total_no_of_full_pages = total_no_of_records // self.page_size
        total_no_of_pages = total_no_of_full_pages + total_no_of_records % self.page_size
        total_no_of_full_groups = total_no_of_full_pages // self.pager_size
        total_no_of_full_pages_in_group = total_no_of_full_groups * self.pager_size
        total_no_of_trailing_pages = total_no_of_pages - total_no_of_full_pages_in_group


        if total_no_of_pages <= self.pager_size:
            self.start_page = 0
            self.end_page = total_no_of_pages
            self.show_previous_pages = False
            self.show_more_pages = False
        else:
            """ deal with pagination """

            self.show_previous_pages = True
            self.show_more_pages = True

            if self.page <= self.pager_size:
                """ first group """

                self.start_page = 0
                self.show_previous_pages = False

                if total_no_of_full_pages < total_no_of_pages:
                    self.end_page = self.pager_size
                    self.show_more_pages = True
                else:
                    self.end_page = self.start_page + total_no_of_trailing_pages
                    self.show_more_pages = False
            else:
                """ subsequent group """

                self.start_page = self.page - (self.page % self.pager_size)
                self.end_page = self.start_page + self.pager_size
                self.show_previous_pages = True

                if self.start_page >= total_no_of_full_pages_in_group:
                    """ last group """

                    self.start_page = self.page - (self.page % self.pager_size)
                    self.end_page = self.start_page + total_no_of_trailing_pages
                    self.show_more_pages = False
                    self.show_previous_pages = True


            print("**********************************************")
            print("*******{}********".format(datetime.datetime.now()))
            print("start_page = {}".format(self.start_page))
            print("end_page = {}".format(self.end_page))
            print("page = {}".format(self.page))
            print("show_previous_pages = {}".format(self.show_previous_pages))
            print("show_more_pages = {}".format(self.show_more_pages))
            print("display_records_start = {}".format(self.display_records_start))
            print("display_records_end = {}".format(self.display_records_end))
            print("total_no_of_records = {}".format(total_no_of_records))
            print("total_no_of_full_pages = {}".format(total_no_of_full_pages))
            print("total_no_of_trailing_pages = {}".format(total_no_of_trailing_pages))
            print("total_no_of_pages = {}".format(total_no_of_pages))
            print("**********************************************")


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


