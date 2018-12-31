import math

class Pager:

    list_item = "<li><a href='{{=URL('schemesofwork', 'index', vars=dict(page=1))}}' class='btn {{if page == 1:}} btn-primary {{ pass }}'>1</a></li>"


    def __init__(self, page_size = 10):
        self.page_size = page_size


    def data_to_display(self, page, data):
        """ slices the data """
        self.start = (page-1)*self.page_size
        self.end = (self.start)+self.page_size

        data = data[self.start:self.end]
        return data


    def page_collection(self, records):
        pages = []
        number_of_records = len(records)

        pages_to_show = int(number_of_records / self.page_size)

        for c in range(pages_to_show):
            pages.append(c+1)

        if number_of_records % self.page_size > 0:
            pages.append(len(pages)+1)

        return pages


