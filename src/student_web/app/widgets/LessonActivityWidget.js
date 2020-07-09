import React, { Fragment }from 'react';
import { BrowserRouter as Router, Link } from 'react-router-dom';

export const LessonActivityWidget = ({lesson}) => {
    if(lesson === undefined)  {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <Router>
            <ul className="activities">
                {lesson.resources.map((resource) => (
                    <li key={resource.id}>
                        <Link to={`${lesson.id}/${resource.id}/${resource.md_document_name}`} className="button fit activity-link activity-link--markdown">{resource.title}</Link> 
                    </li>
                ))}
            </ul>
            </Router>
        );
    }
}