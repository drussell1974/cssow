import React, { Fragment } from 'react';

export const SpinnerWidget = ({loading}) => {
    if(loading === undefined) {
        return <Fragment></Fragment>;
    } else if (loading == true) {
        return (
            <div className="spinner-border text-light" role="status">
                <span className="sr-only">loading...</span>
            </div>
        )
    } else {
        return <Fragment></Fragment>;
    }
}

