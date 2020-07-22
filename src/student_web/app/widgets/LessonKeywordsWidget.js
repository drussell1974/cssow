import React, { Fragment } from 'react';

export const LessonKeywordsWidget = ({keywords}) => {

    if(keywords === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <Fragment>
                <h2>Keywords</h2>
                <ul className="keywords">
                {keywords.map(item => (
                        <li key={item.id}>{item.term}</li>
                    ))}
                </ul>
            </Fragment>
        );
    }
}