import React, { Fragment } from 'react';

const PaginationWidget = ({uri, pager}) => {
    if(pager === undefined || pager.allData === undefined || pager.pagerSize === 1 || uri === undefined  || uri === "") {
        return (<Fragment></Fragment>);
    } else {
        let bookmarks = [];

        for(var i = 1; i < pager.pagerSize + 1; i++) {
            bookmarks.push({            
                pageNumber: i,
                to: `${uri}?page=${i}`,
            })
        }
        
        return (
            <ul className="pagination">
                {bookmarks.map(item => (
                    <li key={item.pageNumber}>
                        <a href={item.to}>{item.pageNumber}</a>
                    </li>
                ))}
            </ul>
        );
    }
}

export default PaginationWidget;