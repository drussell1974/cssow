import React, { Fragment } from 'react';

export const SpinnerWidget = ({loading}) => {
    if(loading === undefined || loading == 0 || loading == 100) {
        return <Fragment></Fragment>;
    } else {     
        let percentage = `${loading}%`;
        return (
            <Fragment>
                <div className="progress progress--css-animated" style={{ width: "0%" }}>
                </div>
                <div className="progress" style={{ width: percentage }}>
                </div>
            </Fragment>
        )
    }
}

