import React, { Fragment, useState } from 'react';
import { Link } from 'react-router-dom';

export const LoginForm = ({class_code, onSubmit, fetch}) => {
    const [ student, setClassCode ] = useState({class_code});
    const handleChangeClassCode = ({ target }) => {
        setClassCode(student => ({
            ...student,
            class_code: target.value
        }));
    }
    // TODO: change post location
    const handleSubmit = () => {
        //onSubmit(class_code);
        fetch('/customers', {
            method: 'POST',
            credentials: 'same-origin',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(student)
        })
    }

    return (
        <form id="frm-login-form" onSubmit={handleSubmit}>
            <div className="controls-group align-center">
                <div className="form-group form-group--auto controls p-25">
                    <h2 htmlFor="class_code">Enter your class code</h2>
                    <p><a href="http://teacher.daverussell.co.uk">I am a teacher</a></p>
                    <input type="text" id="class_code" name="class_code" value={class_code} onChange={handleChangeClassCode} />
                    <input type="submit" value="Enter" className="btn btn-primary w-100" />
                </div>
            </div>
        </form>
    )
}

// mimic fetch api

LoginForm.defaultProps = {
    fetch: async () => {},
}

export const LoginWidget = ({class_code, onSubmit, fetch}) => {
    
    if(onSubmit === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <Fragment>
                <LoginForm class_code={class_code} onSubmit={onSubmit} fetch={fetch} />
            </Fragment>
        );
    }
}

export default LoginWidget;