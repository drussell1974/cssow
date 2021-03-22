import React, { Fragment, useState } from 'react';
import { Link, useHistory } from 'react-router-dom';
import { Redirect } from 'react-router-dom/cjs/react-router-dom.min';

export const LoginForm = ({class_code, onSave}) => {
    const [ lesson, setClassCode ] = useState({class_code});
    const [ error, setError ] = useState(false);

    let history = useHistory();
    let error_message = "Class code must be 6 letters and numbers. Please ensure they match correctly."
    let setErrorMsg = (msg)  => {
        error_message = msg;
    }

    // Default lesson

    const redirectToLesson = (url) => {
        // TODO: Redirect to lesson page
        history.push(url);
    }
        
    const handleChangeClassCode = ({ target }) => {
        setClassCode(lesson => ({
            ...lesson,
            class_code: target.value
        }));
        if (target.value.length > 6) {
            setError(true);
        } else {
            setError(false);
        }
    }

    const handleFetch = (payload) => {
        
        if (payload.schedule) {
            // get lesson from payload
            let scheduled_lesson = payload.schedule;
            // create url TODO: get from route
            let url = `/institute/${scheduled_lesson.institute_id}/department/${scheduled_lesson.department_id}/course/${scheduled_lesson.scheme_of_work_id}/lesson/${scheduled_lesson.lesson_id}`
            console.log(url);
            redirectToLesson(url);
        } else if (payload.detail) {
            // display detail
            console.log("payload.detail setting error...");
            setError(true);
            setErrorMsg(payload.detail);
        } else {
            // TODOL set error from detail
            setError(true);
        }
    }

    const handleSubmit = async e => {
        e.preventDefault();
        console.log("LoginWidget.handleSubmit: handing submit in child...")

        if (lesson.class_code !== undefined) {
            if(lesson.class_code.length == 6) {
                // 6 digits entered fetch lesson
                onSave(lesson, handleFetch);
            } else {
                setError(true);
            }
        }
    };

    return (
        <form id="frm-login-form" onSubmit={handleSubmit}>
            <div className="controls-group align-center">
                <div className="form-group form-group--auto controls p-25">
                    <h2 htmlFor="class_code">Enter your class code</h2>
                    <p><a href="http://teacher.daverussell.co.uk">I am a teacher</a></p>
                    <input type="text" id="class_code" name="class_code" className="input-lg" value={class_code} onChange={handleChangeClassCode} />
                    <input type="submit" value="Enter" className="btn btn-primary w-100" />
                    { error ? <div className="error">{error_message}</div> : null }
                </div>
            </div>
        </form>
    )
}

export const LoginWidget = ({class_code, onSave}) => {
    
    if(onSave === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <Fragment>
                <LoginForm 
                    class_code={class_code}
                    onSave={onSave}
                />
            </Fragment>
        );
    }
}

export default LoginWidget;