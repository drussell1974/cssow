import math

class Pager:

    list_item = "<li><a href='{{=URL('schemesofwork', 'index', vars=dict(page=1))}}' class='btn {{if page == 1:}} btn-primary {{ pass }}'>1</a></li>"


    def __init__(self, page = 1, page_size = 10, pager_size = 5, data = []):
        self.page = int(page)
        self.page_size = int(page_size)
        self.pager_size = int(pager_size)
        self.data = data

        ' range of data to display '

        self.display_records_start = (self.page-1)*self.page_size
        self.display_records_end = self.display_records_start+self.page_size


        ' start page in current group '

        self.start_page_in_current_group = 1
        self.show_prev_group_of_pages = False

        if self.page > self.pager_size:
            self.start_page_in_current_group = self.page - (self.page % self.pager_size)
            self.show_prev_group_of_pages = True

        ' number of pages in current group '
        total_number_of_records = len(self.data)
        total_number_of_pages = total_number_of_records / self.page_size + total_number_of_records % self.page_size
        number_of_pages_remaining = total_number_of_pages - self.start_page_in_current_group

        ' end page in current group '

        if number_of_pages_remaining <= self.pager_size:
            self.end_page_in_current_group = self.start_page_in_current_group + number_of_pages_remaining
            self.show_next_group_of_pages = False
        else:
            self.end_page_in_current_group = self.start_page_in_current_group + self.pager_size - 1
            self.show_next_group_of_pages = True
        import datetime
        print("******************** {} *******************".format(datetime.datetime.now()))
        print("self.start_page = {}, self.end_page = {}, self.show_prev = {}, self.show_next = {}, total_number_of_records = {}, total_number_of_pages = {}, number_of_pages_remaining = {}"
              .format(self.start_page_in_current_group, self.end_page_in_current_group, self.show_prev_group_of_pages, self.show_next_group_of_pages, total_number_of_records, total_number_of_pages, number_of_pages_remaining))




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


