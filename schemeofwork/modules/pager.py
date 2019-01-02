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

        start_pager_at = 1
        ' start at beginning of the page group '
        if  self.page > self.pager_size:
            start_pager_at = (self.page - (self.page % self.pager_size)) * self.page_size

        print("start={}".format(start_pager_at))

        ' default end '
        end_pager_at = start_pager_at + (self.pager_size * self.page_size)

        print("end={}".format(end_pager_at))
        show_next = True

        ' unless there are fewer pages '
        if end_pager_at > self.display_records_end:
            end_pager_at = self.display_records_end
            show_next = False

        print("end={}, show_next = {}".format(end_pager_at, show_next))

        html = ""
        page_number = int(start_pager_at / self.page_size) + 1

        ' create previous '

        if start_pager_at > 1:
            html = html + create_list_item(url, self.page, page_number - 1, "&larr;")

        ' create list item '

        for x in range(start_pager_at, end_pager_at, self.pager_size):
            html = html + create_list_item(url, self.page, page_number, page_number)

            ' create next '
            if start_pager_at == end_pager_at and show_next == True:
                html = html + create_list_item(url, self.page, page_number + 1, "&rarr;")

            page_number = page_number + 1

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


