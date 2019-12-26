module.exports = class Pager {
    constructor(data, pageSize = 10, initialPage = 1) {
        this.allData = data;
        this.page = initialPage;
        this.pageIndex = initialPage - 1; // Needs to work with index based values
        this.pageSize = pageSize;    
        this.pagerSize = Math.ceil(this.allData.length / this.pageSize);

        this.GetPagedData = function(page) {
            this.page = page;
            this.pageIndex = page - 1; // Needs to work with index based values
            // Get the section of data to show on the page
            let startIndex = this.pageIndex * this.pageSize;
            let endIndex = this.pageIndex * this.pageSize + this.pageSize;

            return this.allData.slice(startIndex, endIndex);
        }
    }
}