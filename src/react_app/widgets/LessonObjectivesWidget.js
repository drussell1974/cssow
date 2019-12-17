import React from 'react';

export const LessonObjectivesWidget = ({data}) => {
    if(data === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        const learning_objectives = data.lesson.learning_objectives;
        return (
            <ul className="objectives">
            {learning_objectives.map(item => (
                    <li>{item.description}</li>
                ))}
            </ul>
        );
    }
}