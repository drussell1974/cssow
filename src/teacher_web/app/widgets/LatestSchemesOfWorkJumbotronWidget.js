import React, { Fragment } from 'react';

export const LatestSchemesOfWorkJumbotronWidgetItem = ({data, auth}) => {
    
    if(data === undefined){
        return (<Fragment></Fragment>)
    } else {
        let row = data;
        let link = `/learningepisode/${row.id}`;
        let edit_link = `/schemesofwork/edit/${row.id}`;
        let del_link = `/schemesofwork/delete_item/${row.id}`;
        let editable = auth == true ? {display:'inline'} : {display:'none'};
        
        return (
            <Fragment>
                <div className="post-preview post-preview-schemeofwork">
                    <a id="lnk-schemeofwork-{row.id}" href={link}>
                        <h2 className="post-title">
                            {row.name}
                        </h2>{row.is_recent == true ? <i className="small badge badge-success float-right">New</i> : <i></i>}
                        <h3 className="post-subtitle">
                            {row.key_stage_name}
                        </h3>
                    </a>
                    <p className="post-meta">
                       Created by <a href="#">{row.created_by_name}</a> on {row.created} - <i className="editable" style={editable}><a href={del_link} className="delete">Delete</a> - <a href={edit_link} className="edit">Edit</a></i>
                    </p>
                </div>
                <hr />
            </Fragment>
        )
    }
}

export const LatestSchemesOfWorkJumbotronWidget = ({data}) => {
    
    if(data === undefined){
        return (<Fragment></Fragment>)
    } else {
        return (
            <section id="section-latest_schemesofwork" className="jumbotron">
                <span className="subheading">Latest Schemes of Work</span>
                {data.map(row => (
                    <LatestSchemesOfWorkJumbotronWidgetItem data={row} />
                ))}
                <div className="clearfix">
                    <a className="btn btn-primary float-right" href="/schemesofwork" id="btn-all-schemes-of-work">Show all &rarr;</a>
                </div>
            </section>
        );
    }
}
