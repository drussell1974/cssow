import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

const AddLearningMaterials = ({scheme_of_work_id, return_url}) => {
    
    if(scheme_of_work_id === undefined) {
        return <Fragment></Fragment>;
    } else {
        // See References views convert ajax calls to React
        let content = 'TODO: get references for editing';
        let link_to = `reference:/${scheme_of_work_id}?_next=${return_url}`;

        return (
            <section className="alert alert-info" >
                <div id="div-references">
                    {content}
                </div>
                <Link to={link_to} style={{'marginTop':'30px'}} className="btn btn-info" id="add-reference">Add learning materials</Link>
            </section>
        )
    }
}

export default AddLearningMaterials;