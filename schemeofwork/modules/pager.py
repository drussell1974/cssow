import math

class Pager:

    list_item = "<li><a href='{{=URL('schemesofwork', 'index', vars=dict(page=1))}}' class='btn {{if page == 1:}} btn-primary {{ pass }}'>1</a></li>"


    def __init__(self, page = 1, page_size = 10, pager_size = 10, data = []):
        self.page = int(page)
        self.page_size = int(page_size)
        self.pager_size = int(pager_size)
        self.data = data
        ' range of data to display '
        self.start = (self.page-1)*self.page_size
        self.end = self.start+self.page_size

        ' find the number of pages '
        self.no_of_pages = int(math.ceil(len(self.data) / self.page_size))

        ' find the number of pages remaining from the trailing data '
        self.no_of_pages_remaining = int(len(self.data[self.start:]) / self.page_size)


    def data_to_display(self):
        """
        Displays e.g. only 10 records at a time
        """
        return self.data[self.start:self.end]


    def pager_pages(self):
        """
        Display e.g only 5 groups of 10 records (1 - 5, 6 - 10, 11 - 12)
        :return: where the pager should start and end
        """
        print("\n\n\nfunction pager_pages")

        ' start at page 1 by default '
        start_page = 1
        ' If the page number should be in the next group start the pager at the beginning of the next group '
        if self.page > self.pager_size:
            start_page = self.page - ((self.page % self.pager_size)-1)

        end_page = start_page + self.pager_size



        if self.no_of_pages_remaining == 0:
            ' only show the remaining pages '
            end_page = start_page + self.no_of_pages_remaining + 1

        return start_page, end_page, self.no_of_pages


