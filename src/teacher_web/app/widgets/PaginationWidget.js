import React, { Fragment } from 'react';

const PaginationWidget = ({pager}) => {
    if(pager === undefined || pager.length === 0) {
        return (<Fragment></Fragment>);
    } else {
        return (
            <ul class="pagination">
                {pager.map(item => (
                    <li>1</li>
                ))}
            </ul>
        );
    }
}

export default PaginationWidget;