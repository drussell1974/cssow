import math

class Pager:



    def __init__(self, page = 1, page_size = 10, pager_size = 10, data = []):
        import datetime
        print("***************************************************")
        print("***Pager.__init__ @ {} ***".format(datetime.datetime.now()))

        self.page = int(page)
        self.page_size = int(page_size)
        self.pager_size = int(pager_size)
        self.data = data

        ' range of data to display '

        self.display_records_start = (self.page-1)*self.page_size
        self.display_records_end = self.display_records_start+self.page_size

        ' show page group '

        total_number_of_pages = len(self.data) / self.pager_size
        if total_number_of_pages <= 1.0:
            """ there is only one page of records """

            self.start_page_in_current_group = 1
            self.show_prev_group_of_pages = False
            self.end_page_in_current_group = 1
            self.show_next_group_of_pages = False

        else:
            """ there is more than one page """

            if self.page <= self.pager_size:
                """ first group """
                self.start_page_in_current_group = 1
                self.show_prev_group_of_pages = False
            elif self.page % self.pager_size == 0:
                """ last page in group """
                self.start_page_in_current_group = self.page + 1 - self.pager_size
                self.show_prev_group_of_pages = True
            else:
                """ not first page in group """
                self.start_page_in_current_group = self.page + 1 - (self.page % self.pager_size)
                self.show_prev_group_of_pages = True


            ' check if there are more pages '

            self.starting_record_in_group = (self.start_page_in_current_group - 1) * self.page_size
            self.remaining_number_of_records = len(self.data[self.starting_record_in_group:])
            self.remaining_number_of_pages = int(math.ceil(self.remaining_number_of_records / self.page_size))

            """ Debug
            print("self.starting_record_in_group={}".format(self.starting_record_in_group))
            print("self.remaining_number_of_records={}".format(self.remaining_number_of_records))
            print("self.remaining_number_of_pages={}".format(self.remaining_number_of_pages))
            """

            if self.remaining_number_of_pages > self.pager_size:
                """ there are more groups """
                self.show_next_group_of_pages = True
                self.end_page_in_current_group = self.start_page_in_current_group + (self.pager_size - 1)
            elif self.start_page_in_current_group == 1:
                """ handle first page group """
                self.show_next_group_of_pages = False
                self.end_page_in_current_group = self.start_page_in_current_group + self.remaining_number_of_pages - 1
            else:
                self.show_next_group_of_pages = False
                self.end_page_in_current_group = self.start_page_in_current_group + self.remaining_number_of_pages


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
        ' show previous group of pages if not in first group and number of pages '

        if self.show_prev_group_of_pages:
            html = html + create_list_item(url, self.page, self.start_page_in_current_group - 1, "&larr;")

        ' create list items '
        last_page_number = 1
        for page_number in range(self.start_page_in_current_group, int(self.end_page_in_current_group) + 1):
            ' create numbered list item'

            html = html + create_list_item(url, self.page, page_number, page_number)
            last_page_number = page_number


        ' create next '

        if self.show_next_group_of_pages == True:
            html = html + create_list_item(url, self.page, page_number + 1, "&rarr;")

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


