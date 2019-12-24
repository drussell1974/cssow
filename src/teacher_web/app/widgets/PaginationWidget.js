import React, { Fragment } from 'react';

export const Mapper = {
    TransformLessons: (list) => {
        return list.map(
            function(item) {
                
                let to_SchemeOfWork = `/schemeofwork/${item.scheme_of_work_id}/lesson/${item.id}`;
                
                return {
                    id: item.id,
                    pageNumber: "x",
                    to: to_SchemeOfWork,
                }
            }
        )
    }
}

const PaginationWidget = ({data, page, pageSize = 10}) => {
    if(data === undefined || data.length === 0) {
        return (<Fragment></Fragment>);
    } else {
        return (
            <ul className="pagination">
                {data.map(item => (
                    <li key={item.id}>
                        {item.pageNumber}
                    </li>
                ))}
            </ul>
        );
    }
}

export default PaginationWidget;