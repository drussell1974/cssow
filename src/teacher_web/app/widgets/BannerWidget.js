import React, { Fragment } from 'react';

const BannerWidget = ({main_heading, sub_heading}) => {

    if(main_heading === undefined && sub_heading === undefined) {
        return (<Fragment></Fragment>);
    } else {
        return(
            <div className="site-heading">
                <h1>{main_heading}</h1>
                <span className="subheading">{sub_heading}</span>
            </div>
        );
    }
};

export default BannerWidget;