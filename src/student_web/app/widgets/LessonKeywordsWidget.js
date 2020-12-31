import React, { Fragment } from 'react';

export const LessonKeywordsWidget = ({keywords}) => {

    if(keywords === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <Fragment>
                <h2>Keywords</h2>
                <div className="keywords">
                {keywords.map(item => (
                    
                        <div className="block-text" key={item.id}>
                            <b>{item.term}</b>
                            <p className="preserve-linebreak">{item.definition}</p>
                        </div>
                    
                    ))}
                </div>
            </Fragment>
        );
    }
}