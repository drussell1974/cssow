from shared.models.core.basemodel import try_int

class Pager:
    page = 1
    pagesize = 20
    page_direction = 0

    def __init__(self, page, pagesize, page_direction):
        self.page = page
        self.pagesize = pagesize
        self.page_direction = page_direction
    

    def pager(self, page, page_direction):
        page = try_int(page, return_value=1)
        page_direction = try_int(page_direction, return_value=0)
    
        page = page + page_direction 
        
        self.page = page if page > 1 else 1
        self.page_direction = page_direction
        
        return self.page