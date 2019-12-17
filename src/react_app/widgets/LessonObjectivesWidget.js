import React from 'react';

export const LessonObjectivesWidget = ({data}) => {
    if(data === undefined) {
        return <React.Fragment></React.Fragment>;
    } else if(data.learning_objectives === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        const learning_objectives = data.learning_objectives;
        
        return (
            <ul className="objectives">
            {learning_objectives.map(item => (
                    <li key={item.id} >{item.description}</li>
                ))}
            </ul>
        );
    }
}