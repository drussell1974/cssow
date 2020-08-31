import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

const BreadcrumbWidget = ({activePageName, breadcrumbItems = []}) => {
    if (activePageName == undefined){
        return <Fragment></Fragment>
    }
    return (
        <nav id="breadcrumb-nav" aria-label="breadcrumb">
            <ul className="breadcrumb">
                { breadcrumbItems.map(item => 
                    <li key={item.text} className="breadcrumb-item">
                        <Link key={item.text}  to={item.url}>{item.text}</Link>
                    </li>
                )}
                <li className="breadcrumb-item active" aria-current="page">{activePageName}</li>
            </ul>
        </nav>
    )
};

export default BreadcrumbWidget;