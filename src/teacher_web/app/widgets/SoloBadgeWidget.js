import React, { Fragment } from 'react';

const SoloBadge = ({solo_taxonomy_level}) => {
    if(solo_taxonomy_level === undefined) {
        return <Fragment></Fragment>;
    }
    switch(solo_taxonomy_level) {
        case "B": 
            return (<i className="far fa-star"></i>);
        case "C": 
            return (<i className="fas fa-star"></i>);
        case "D": 
            return (<i className="fas fa-trophy"></i>);
        default:
            return <Fragment></Fragment>;
    }
}

export default SoloBadge;