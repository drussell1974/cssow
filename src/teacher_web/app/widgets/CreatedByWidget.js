import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

const AdminOptions = ({row, auth, request}) => {
    if(auth === undefined || auth === false ) {
        return (<Fragment />);
    } else if (row.published == false) {
        return ( 
          <Fragment>
              &nbsp;-&nbsp;<Link className="publish" to={`/learningepisode/publish_item/${row.id}?_next=${request.url}`} className="small badge badge-danger">not published</Link>
              &nbsp;-&nbsp;<Link className="delete" to="/learningepisode/delete_item/row.id/row.scheme_of_work_id">Delete</Link>
              &nbsp;-&nbsp;<Link className="edit" to="/learningepisode/edit/row.id/row.scheme_of_work_id?_next=request.url">Edit</Link>
              &nbsp;-&nbsp;<Link className="copy" to="/learningepisode/edit/row.id/row.scheme_of_work_id?duplicate=1">Copy</Link>
          </Fragment>
          );
    } else {
        return (
          <Fragment>
              &nbsp;-&nbsp;<Link className="delete" to="/learningepisode/delete_item/row.id/row.scheme_of_work_id">Delete</Link>
              &nbsp;-&nbsp;<Link className="edit" to="/learningepisode/edit/row.id/row.scheme_of_work_id?_next=request.url">Edit</Link>
              &nbsp;-&nbsp;<Link className="copy" to="/learningepisode/edit/row.id/row.scheme_of_work_id?duplicate=1">Copy</Link>
          </Fragment>
        );
    }
}

const CreatedByWidget = ({row, auth, request}) => {

    if(row === undefined) {
      return (<Fragment></Fragment>)
    } else {
      return(
        <p className="post-meta">Created by <a href="#">{row.created_by_name}</a> {row.created} Learning objectives {row.number_of_learning_objective}
            <AdminOptions row={row} auth={auth} request={request} />
        </p>
      )
    }
}

export default CreatedByWidget;
