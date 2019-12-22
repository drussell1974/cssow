import React, { Fragment }from 'react';

const ContentHeadingWidget = ({main_heading, sub_heading, strap_line}) => {
    if(main_heading === undefined) {
        return (<Fragment></Fragment>);
    } else {
        return (
            <div class="alert alert-secondary">
                <h5 class="secondary-heading">{main_heading}</h5>
                <b>{sub_heading}</b>
                <p class="lead">{strap_line}</p>
            </div>
        )
    }
}

export default ContentHeadingWidget;