import React, { Fragment }from 'react';
import { BrowserRouter as Router, Link } from 'react-router-dom';

export const LessonActivityWidgetItem = ({lesson, resource}) => {
    if(lesson === undefined || resource === undefined)  {
        return <React.Fragment></React.Fragment>;
    } else {
        return(
            <li>
                <Link to={`/institute/${lesson.institute_id}/department/${lesson.department_id}/course/${lesson.course_id}/lesson/${lesson.id}/activity/${resource.id}/${resource.md_document_name}`} className="button fit activity-link activity-link--markdown">{resource.title}</Link> 
            </li>
        )
    }
}

export const LessonActivityWidget = ({lesson}) => {
    if(lesson === undefined)  {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <ul className="activities">
                {lesson.resources.map((resource) => (
                    <LessonActivityWidgetItem lesson={lesson} resource={resource} key={resource.id} />
                ))}
            </ul>
        );
    }
}