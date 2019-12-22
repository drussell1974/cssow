import React, { Fragment } from 'react';

export const SidebarNavWidgetItem = ({displayName, subName}) => {
    if(displayName === undefined) {
        return (<Fragment></Fragment>);
    } else {
        return (
            <li class="nav-item">
                <a class="nav-link {{ if opt.id == scheme_of_work_id: }} mark {{ pass }}" href="{{=URL('learningepisode', 'index', args=[opt.id])}}">{displayName} <div class="small">{subName}</div></a>
            </li>
        )
    }
}

const SidebarNavWidget = ({buttonText, data}) => {
    if(data === undefined || data.length === 0) {
        return (<Fragment></Fragment>);
    } else {
        return (
            <nav class="navbar navbar-expand-lg navbar-light" id="sidebarNav">
                <button class="navbar-toggler btn" type="button" data-toggle="collapse" data-target="#sidebarResponsive" aria-controls="sidebarResponsive" aria-expanded="true" aria-label="Toggle navigation">
                    {buttonText} <i class="fas fa-bars"></i>
                </button>
                <div class="collapse navbar-collapse" id="sidebarResponsive">
                    <ul class="navbar-nav flex-column fillspace">
                    {data.map(item => (
                        <SidebarNavWidgetItem displayName={item.displayName} subName={item.subName} url={item.url} />
                    ))}
                    </ul>
                    <hr />
                </div>
            </nav>
        )
    }
}

export default SidebarNavWidget;