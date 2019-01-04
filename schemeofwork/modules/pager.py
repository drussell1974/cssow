import math

class Pager:



    def __init__(self, page = 1, page_size = 10, pager_size = 10, data = []):
        import datetime

        self.page = int(page)
        self.page_size = int(page_size)
        self.pager_size = int(pager_size)
        self.data = data

        ' range of data to display '

        self.display_records_start = (self.page-1)*self.page_size
        self.display_records_end = self.display_records_start+self.page_size

        """ ********** """
        """ pagination """
        """ ********** """

        ' number of pages '
        total_no_of_full_pages = len(self.data) // self.page_size
        total_no_of_trailing_pages = len(self.data) % self.page_size
        total_no_of_pages = total_no_of_full_pages + total_no_of_trailing_pages

        ' number of page groups '
        total_no_of_full_page_groups = total_no_of_pages // self.pager_size
        total_no_of_trailing_page_groups = total_no_of_full_page_groups % self.pager_size
        total_no_of_page_groups = total_no_of_full_page_groups + total_no_of_trailing_page_groups

        ' selected page '
        self.start_page = self.page // self.pager_size + 1
        self.end_page = self.page % self.pager_size

        ' check if first page group '
        self.is_first_page_group = True if self.page <= self.pager_size else False
        ' check if last page group '
        self.is_last_page_group = True if total_no_of_page_groups - self.start_page == 0 else False

        if self.is_first_page_group == True:
            """ if first page group then there are previous pages and possibly more pages """
            self.show_prev_group_of_pages = False
            self.show_next_group_of_pages = True
            self.end_page = self.pager_size

        if self.is_last_page_group == True:
            """ if last group then there are no more pages and possibly previous pages """
            self.show_next_group_of_pages = False
            self.show_prev_group_of_pages = True
            self.end_page = self.start_page + total_no_of_trailing_page_groups

        if self.is_first_page_group == True and self.is_last_page_group == True:
            """ unless the group is both first and last """
            self.show_prev_group_of_pages = False
            self.show_next_group_of_pages = False
        else:
            """ otherwise we must be somewhere in the middle """
            self.show_prev_group_of_pages = True
            self.show_next_group_of_pages = True
            """ """
            self.end_page = self.start_page + self.pager_size

        """ DEBUG """
        print("start_page = {}".format(self.start_page))
        print("end_page = {}".format(self.end_page))
        print("show_prev_group_of_pages = {}".format(self.show_prev_group_of_pages))
        print("show_next_group_of_pages = {}".format(self.show_next_group_of_pages))
        print("display_records_start = {}".format(self.display_records_start))
        print("display_records_end = {}".format(self.display_records_end))


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
            html = html + create_list_item(url, self.page, self.start_page - 1, "&larr;")

        ' create list items '
        last_page_number = 1
        for page_number in range(self.start_page, int(self.end_page) + 1):
            ' create numbered list item'

            html = html + create_list_item(url, self.page, page_number + 1, page_number + 1)
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


