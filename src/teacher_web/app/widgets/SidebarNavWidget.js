import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

export const Mapper = {
    TransformSchemesOfWork: (list) => {
        return list.map(
            function(item) {
                return {
                    id: item.id,
                    displayName: item.name,
                    subName: item.key_stage_name,
                }
            }
        )
    },

    TransformLessons: (list) => {
        return list.map( 
            function(item) {
                var subName = `Lesson ${item.order_of_delivery_id}`;
                return {
                    id: item.id,
                    displayName: item.title,
                    subName: subName,
                }
            }
        );
    },
}

export const SidebarNavWidgetItem = ({id, displayName, subName, to, highlight=false}) => {
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
                            displayName={item.displayName} 
                            subName={item.subName} 
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