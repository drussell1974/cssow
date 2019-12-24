import React, { Fragment }from 'react';

const ContentHeadingWidget = ({main_heading, sub_heading, strap_line}) => {
    if(main_heading === undefined) {
        return (<Fragment></Fragment>);
    } else {
        return (
            <div className="alert alert-secondary">
                <h5 className="secondary-heading">{main_heading}</h5>
                <b>{sub_heading}</b>
                <p className="lead">{strap_line}</p>
            </div>
        )
    }
}

export default ContentHeadingWidget;