import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

export const SidebarNavWidgetItem = ({displayName, subName, to, highlight}) => {
    if(displayName === undefined) {
        return (<Fragment></Fragment>);
    } else {
        let navlinkClass = highlight === true ? 'nav-link' : 'nav-link mark';
        return (
            <li className="nav-item">
                <Link className={navlinkClass} to={to}>
                    {displayName} <div className="small">{subName}</div>
                </Link>
            </li>
        )
    }
}

const SidebarNavWidget = ({buttonText, data}) => {
    if(data === undefined || data.length === 0) {
        return (<Fragment></Fragment>);
    } else {
        return (
            <nav className="navbar navbar-expand-lg navbar-light" id="sidebarNav">
                <button className="navbar-toggler btn" type="button" data-toggle="collapse" data-target="#sidebarResponsive" aria-controls="sidebarResponsive" aria-expanded="true" aria-label="Toggle navigation">
                    {buttonText} <i className="fas fa-bars"></i>
                </button>
                <div className="collapse navbar-collapse" id="sidebarResponsive">
                    <ul className="navbar-nav flex-column fillspace">
                    {data.map(item => (
                        <SidebarNavWidgetItem 
                            key={item.id} 
                            displayName={item.name} 
                            subName={item.summary} 
                            to={`/schemeofwork/${item.id}/lessons`}
                            highlight = {item.scheme_of_work_id == 127} />
                    ))}
                    </ul>
                    <hr />
                </div>
            </nav>
        )
    }
}

export default SidebarNavWidget;