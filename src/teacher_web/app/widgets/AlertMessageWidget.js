import React, { Fragment } from 'react';

const AlertMessageWidget = ({message}) => {
    if(message === undefined || message === "") {
        return (<Fragment></Fragment>);
    } else {
        return (
            <div id="alert" className="alert alert-warning alert-dismissible fade show" role="alert">
                { message }
                <button type="button" className="close" data-dismiss="alert" aria-label="Close"/>
                <span aria-hidden="true">&times;</span>
            </div>
        );
    }
};

export default AlertMessageWidget;