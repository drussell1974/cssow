import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

export const LoginWidget = ({redirect}) => {

    if(redirect === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <Fragment>
                <form method="post" action="/login" id="frm-login-form">
                    <div className="controls-group align-center">
                        <div className="form-group form-group--auto controls p-25">
                            <h2>Enter your class code</h2>
                            <p><a href="http://teacher.daverussell.co.uk">I am a teacher</a></p>
                            <input type="text" name="classcode" />
                            <input type="submit" value="Enter" className="btn btn-primary w-100"></input>
                        </div>
                    </div>
                    <input type="hidden" name="redirect_url" value={redirect.url} />
                </form>
            </Fragment>
        );
    }
}