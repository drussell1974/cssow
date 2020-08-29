from shared.models.core.basemodel import try_int

class Pager:
    page = 1
    pagesize = 20
    page_direction = 0
    is_valid = False
    validation_errors = {}

    def __init__(self, pagesize_options, page, pagesize, page_direction):
        """
        """
        self.pagesize_options =  pagesize_options 
        self.page = page
        self.pagesize = pagesize
        self.page_direction = page_direction
        self.validation_errors = {}
        self.is_valid = False
    

    def pager(self, page, page_direction):
        """
        update the page number
        """
        page = try_int(page, return_value=1)
        page_direction = try_int(page_direction, return_value=0)
    
        page = page + page_direction 
        
        self.page = page if page > 1 else 1
        self.page_direction = page_direction
        self.page_direction_reset = -self.page
        return self.page


    def validate(self):
        """ 
        validate override call super().validate() 
        """
        self.validation_errors.clear()
        self.is_valid = False
