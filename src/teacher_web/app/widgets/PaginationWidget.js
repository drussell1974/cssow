import React, { Fragment } from 'react';

const PaginationWidget = ({uri, pager, onBookmarkClicked}) => {
    
    const handleClick = (e, page) => {
        
        //e.stopPropagation();

        if(onBookmarkClicked !== undefined){
            onBookmarkClicked(page);
        }
    }

    if(pager === undefined || pager.allData === undefined || pager.pagerSize === 1 || uri === undefined  || uri === "") {
        return (<Fragment></Fragment>);
    } else {
        let bookmarks = [];

        for(var i = 1; i < pager.pagerSize + 1; i++) {
            bookmarks.push({            
                pageNumber: i
            })
        }
        
        return (
            <ul className="pagination">
                {bookmarks.map(item => (
                    <li key={item.pageNumber} className={`page-item ${pager.page == item.pageNumber ? "active" : ""}`}>
                        <div id={`page${item.pageNumber}`} className="page-link" onClick={(e) => handleClick(e, item.pageNumber)}>{item.pageNumber}</div>
                    </li>
                ))}
            </ul>
        );
    }
}

export default PaginationWidget;