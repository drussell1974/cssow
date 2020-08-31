import React, { Fragment } from 'react';

export const SpinnerWidget = ({loading}) => {
    if(loading === undefined || loading == 0 || loading == 100) {
        return <div className="progress"></div>;
    } else {     
        let percentage = `${loading}%`;
        return (
            <div className="progress" style={{ width: percentage }}>
                <div className="progress-bar progress-bar-striped" role="progressbar" aria-valuenow={loading} aria-valuemin="0" aria-valuemax="100">
                    <i className="sr-only">{percentage}</i>
                </div>
            </div>
        )
    }
}

