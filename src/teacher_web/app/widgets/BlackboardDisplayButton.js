import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

const BlackboardDisplayButton = ({lesson}) => {
    if(lesson === undefined) {
        return (<Fragment></Fragment>);
    } else {
        let to_blackboardView = `/schemeofwork/${lesson.scheme_of_work_id}/lesson/${lesson.id}/whiteboard_view`;
        let to_lessonPlan = `/schemeofwork/${lesson.scheme_of_work_id}/lesson/${lesson.id}/lesson-plan`;
        
        return(
            <section class="alert alert-secondary blackboard">
                <Link to={to_blackboardView} target="_blank" class="btn btn-dark" id="lnk-whiteboard_view">Blackboard display</Link>
                <Link to={to_lessonPlan} target="_blank" class="btn btn-light" id="lnk-lesson_plan">Lesson plan</Link>
            </section>
        )
    }
}

export default BlackboardDisplayButton;