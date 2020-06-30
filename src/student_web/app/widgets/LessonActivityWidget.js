import React, { Fragment }from 'react';

export const LessonActivityWidget = ({data, markdown_html}) => {
    if(markdown_html === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <Fragment>
                <h2>Activity</h2>
                <div className="markdown-body" dangerouslySetInnerHTML={{ __html: markdown_html }} />  
            </Fragment>
        );
    }
}