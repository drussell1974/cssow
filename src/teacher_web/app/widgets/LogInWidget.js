import React, { Fragment } from 'react';

const LogInWidget = ({auth}) => {
    if(auth === undefined) { 
        return (<Fragment></Fragment>);
    }
    else if(auth === true) {
        return (
            <Fragment>
                <a className="navbar-brand profile" href="user/profile">Profile</a>
                <a className="navbar-brand change-password" href="user/change_password">Change password</a>
                <a className="navbar-brand logout" id="btn-logout" href="user/logout">Logout</a>
            </Fragment>
        ); 
    } else {
        return (
            <Fragment>
                <a className="navbar-brand login" id="btn-login" href="user/login?_next=request.url">Login</a>
                <a className="navbar-brand register" href="user/register">Sign up</a>
                <a className="navbar-brand retrieve-password" href="user/retrieve_password">Lost password</a>
            </Fragment>
        )
    }
};

export default LogInWidget;