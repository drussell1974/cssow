import React, { Fragment } from 'react';

const PaginationWidget = ({pager}) => {
    if(pager === undefined || pager.length === 0) {
        return (<Fragment></Fragment>);
    } else {
        return (
            <ul className="pagination">
                {pager.map(item => (
                    <li key={item}>1</li>
                ))}
            </ul>
        );
    }
}

export default PaginationWidget;