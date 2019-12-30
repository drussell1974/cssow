import React, { Fragment } from 'react';

const LogInFormWidget = ({auth, onSubmit}) => {
    const handleSubmit = async () => {
        const result = await window.fetch('/login', {
            body: JSON.stringify(customer),
            method: 'POST',
            credentials: 'same-origin',
            headers: {'Content-Type': 'application/json'}
        });
        const auth = await result.json();
        onSubmit(auth);
    }

    if(auth === undefined) {
        return(<Fragment></Fragment>);
    } else {
        return(
            <form id="login" action="#" encType="multipart/form-data" method="post" onSubmit={(e) => {handleSubmit(e)}}>
                <div className="form-group row" id="auth_user_email__row">
                    <label className="form-control-label col-sm-3" htmlFor="auth_user_email" id="auth_user_email__label">email</label>
                    <div className="col-sm-9">
                        <input className="form-control string" id="auth_user_email" name="email" type="text" autoComplete="off" />
                        <span className="help-block"></span>
                    </div>
                </div>
                <div className="form-group row" id="auth_user_password__row">
                    <label className="form-control-label col-sm-3" htmlFor="auth_user_password" id="auth_user_password__label">Password</label>
                    <div className="col-sm-9">
                        <input className="form-control password" id="auth_user_password" name="password" type="password" autoComplete="off" />
                        <span className="help-block"></span>
                    </div>    
                </div>
                <div className="form-group row" id="auth_user_remember_me__row">
                    <div className="sm-hidden col-sm-3"></div>
                    <div className="col-sm-9">
                    <div className="form-check">
                        <label className="form-check-label" htmlFor="auth_user_remember_me" id="auth_user_remember_me__label">
                            <input className="boolean form-check-input" id="auth_user_remember_me" name="remember_me" type="checkbox" />Remember me (for 30 days)
                        </label>
                        <span className="help-block"></span>
                    </div>
                </div>
            </div>
                <div className="form-group row" id="submit_record__row">
                    <div className="col-sm-9 col-sm-offset-3">            
                        <input className="btn btn-primary" type="submit" value="Log In" />
                    </div>
                </div>
            </form>    
        );
    }
}

export default LogInFormWidget;