import React, { Fragment }from 'react';

export const MarkdownWidget = ({markdown_html}) => {
    if(markdown_html === undefined || markdown_html === "") {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <section className="markdown">
                <h2>Activity</h2>
                <div className="markdown-body" dangerouslySetInnerHTML={{ __html: markdown_html }} />  
            </section>
        );
    }
}