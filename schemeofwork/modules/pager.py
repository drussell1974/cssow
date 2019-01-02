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

        start_page = 1
        ' start at beginning of the page group '
        if self.page > self.pager_size:
            start_page = (self.page - (self.page % self.pager_size)) + 1

        total_number_of_records = len(self.data)
        remaining = total_number_of_records % (self.pager_size * self.page_size)

        end_page = start_page + self.pager_size
        if remaining <= end_page:
            end_page = start_page + int(math.ceil(remaining / self.pager_size))

        print("start {} end {} remaining {}".format(start_page, end_page, remaining))
        html = ""

        ' create list items '
        for page_number in range(start_page, end_page):
            if page_number > 1 and page_number % self.pager_size == 1:
                ' create previous '
                html = html + create_list_item(url, self.page, page_number - 1, "&larr;")

            html = html + create_list_item(url, self.page, page_number, page_number)

            ' create next '
            if page_number % self.pager_size == 0:
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


