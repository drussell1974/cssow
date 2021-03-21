import React, { Fragment, useState } from 'react';
import { Link } from 'react-router-dom';

export const LoginForm = ({class_code, onSubmit}) => {
    const [ student, setClassCode ] = useState({class_code});
    const handleChangeClassCode = ({ target }) => {
        setClassCode(student => ({
            ...student,
            class_code: target.value
        }));
    }
    return (
        <form id="frm-login-form" onSubmit={() => onSubmit(student)}>
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

export const LoginWidget = ({class_code, onSubmit}) => {

    if(onSubmit === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <Fragment>
                <LoginForm class_code={class_code} onSubmit={onSubmit} />
            </Fragment>
        );
    }
}

export default LoginWidget;