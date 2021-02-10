import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

export const LoginWidget = ({redirect}) => {

    if(redirect === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <Fragment>
                <h2>Login</h2>
                <form method="post" action="/login" id="frm-login-form">
                    <div className="controls-group">
                        <div className="form-group form-group--auto controls">
                            <label>Email:</label>
                            <input type="text" name="username" />
                        </div>
                    </div>
                    <div className="controls-group">
                        <div className="form-group form-group--auto controls">
                            <label>Password:</label>
                            <input type="password" name="password" />
                        </div>
                    </div>
                    <input type="hidden" name="redirect_url" value={redirect.url} />
                    <input type="submit" value="login" class="btn btn-primary"></input>
                    <Link className="btn btn-secondary" to={redirect.url}>Cancel</Link>
                </form>
            </Fragment>
        );
    }
}