import React, { Fragment } from 'react';

const PaginationWidget = ({data, uri, pageSize = 10}) => {
    if(data === undefined || data.length === 0 || uri === undefined  || uri === "") {
        return (<Fragment></Fragment>);
    } else {
        let pager = []
            
        for(var i = 1; i < Math.ceil(data.length / pageSize) + 1; i++) {
            pager.push({
                pageNumber: i,
                to: `${uri}?page=${i}`,
            })
        }
        
        return (
            <ul className="pagination">
                {pager.map(item => (
                    <li key={item.pageNumber}>
                        <a href={item.to}>{item.pageNumber}</a>
                    </li>
                ))}
            </ul>
        );
    }
}

export default PaginationWidget;