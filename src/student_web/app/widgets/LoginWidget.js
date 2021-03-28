import React, { Fragment, useState } from 'react';
import { render } from 'react-dom/cjs/react-dom.development';
import { Link, useHistory } from 'react-router-dom';
import { Redirect } from 'react-router-dom/cjs/react-router-dom.min';

export const LoginForm = ({class_code, onSave}) => {
    const [ lesson, setClassCode ] = useState({class_code});
    const [ error, setError ] = useState(false);

    let history = useHistory();
    let invalidated = false;

    const Error = (lesson)  => {
        var len = lesson.class_code.length
        if (len > 6) {
            // must be invalidated before showing too short
            return (
                <div className="error h2">Too Long. Must be 6 characters.</div>
            )
        } else if (len < 6) {
            return (
                <div className="warning h2">Too short. Must be 6 characters.</div>
            )
        } else {
            return (<div className="error h2">Check your class code.</div>)
        }
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
        if (target.value.length != 6) {
            setError(true);
        } else {
            setError(false);
        }
    }

    const handleFetch = (payload) => {
        //console.log(payload);
        if (payload.schedule) {
            // get lesson from payload
            let scheduled_lesson = payload.schedule;
            // create url TODO: get from route
            redirectToLesson(`/institute/${scheduled_lesson.institute_id}/department/${scheduled_lesson.department_id}/course/${scheduled_lesson.scheme_of_work_id}/lesson/${scheduled_lesson.lesson_id}`);
        } else if(payload.detail) {
            // display detail
            setError(true);
        } else {
            setError(true);
        }
    }

    const handleSubmit = async e => {
        e.preventDefault();

        if (lesson.class_code !== undefined) {
            if(lesson.class_code.length != 6) {
                setError(true);
            } else {
                onSave(lesson, handleFetch);
                setError(false);
            }
        }
    };

    return (
        <form id="frm-login-form" onSubmit={handleSubmit}>
            <div className="controls-group align-center">
                <div className="form-group form-group--auto controls p-25">
                    <h2 htmlFor="class_code">Enter your class code</h2>
                    <p><a href="http://teacher.daverussell.co.uk">I am a teacher</a></p>
                    <input type="text" id="class_code" name="class_code" className="align-center text-upper  h3" value={class_code} onChange={handleChangeClassCode} />
                    <input type="submit" value="Enter" className="btn btn-primary w-100 h3" />
                    { error ? <Error class_code={lesson.class_code} /> : null }
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