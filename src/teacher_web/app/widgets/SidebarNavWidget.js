import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

export const Mapper = {
    TransformSchemesOfWork: (list, activeItemId) => {
        return list.map(
            function(item) {
                return {
                    id: item.id,
                    displayName: item.name,
                    subName: item.key_stage_name,
                    active: item.id == activeItemId ? true : false,
                }
            }
        )
    },

    TransformLessons: (list, activeItemId) => {
        return list.map( 
            function(item) {
                var subName = `Lesson ${item.order_of_delivery_id}`;
                return {
                    id: item.id,
                    displayName: item.title,
                    subName: subName,
                    active: item.id == activeItemId ? true : false,
                }
            }
        );
    },
}

export const SidebarNavWidgetItem = ({id, displayName, subName, to, active=false}) => {
    if(displayName === undefined) {
        return (<Fragment></Fragment>);
    } else {
        return (
            <li className={`nav-item ${active ? "active" : ""}`}>
                <Link className='nav-link' to={to}>
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
                            active = {item.active} />
                    ))}
                    </ul>
                    <hr />
                </div>
            </nav>
        )
    }
}

export default SidebarNavWidget;