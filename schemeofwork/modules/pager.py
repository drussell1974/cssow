import math

class Pager:

    list_item = "<li><a href='{{=URL('schemesofwork', 'index', vars=dict(page=1))}}' class='btn {{if page == 1:}} btn-primary {{ pass }}'>1</a></li>"


    def __init__(self, page = 1, page_size = 10, pager_size = 10, data = []):
        self.page = page
        self.page_size = page_size
        self.pager_size = pager_size
        self.data = data


    def data_to_display(self):
        """
        Displays e.g. only 10 records at a time

        :param data: the full data set
        :return: the data to display
        """

        self.start = (self.page-1)*self.page_size
        self.end = self.start+self.page_size

        return self.data[self.start:self.end]


    def pager_pages(self):
        """
        Display e.g only 5 groups of 10 records (1 - 5, 6 - 10, 11 - 12)

        :param data: the full data set
        :return: start and end
        """

        start_page = 1

        if self.page > self.pager_size:
            start_page = self.page - self.page % self.pager_size

        number_of_records = int(len(self.data_to_display()) / self.page_size)
        end_page = start_page + number_of_records

        if number_of_records % self.page_size > 0:
          end_page = end_page + 1

        return start_page, end_page


