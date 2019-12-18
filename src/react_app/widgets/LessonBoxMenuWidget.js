import React, { Fragment } from 'react';

export const LessonBoxMenuItem = ({data, typeButtonText}) => {
    if(data === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <div className="box">
                <a href={data.uri} className="image fit">
                    <img src={data.image_url} alt="" />
                </a>
                <div className="inner">
                    <label className="label"><u>{data.reference_type_name}</u></label>
                    <h3>{data.title}</h3>
                    <p>{data.publisher}</p>
                    <a href={data.uri} className="button fit" data-poptrox="youtube,800x400">{typeButtonText}</a>
                </div>
            </div>
        )
    }
}

export const LessonBoxMenuWidget = ({data, typeLabelText, typeButtonText}) => {
    if(data === undefined || data.resources === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        
        let resources = data.resources; // TODO: get resources from lesson
        
        return (
            <Fragment>
                <h2>Objectives</h2>
                <div className="thumbnails lessons">
                    {resources.filter(item => item.page_uri !== "").map(item => (
                        <LessonBoxMenuItem key={item.id} data={item} typeLabelText={typeLabelText} typeButtonText={typeButtonText} />
                    ))}
                </div>
            </Fragment>
        )
    }
}