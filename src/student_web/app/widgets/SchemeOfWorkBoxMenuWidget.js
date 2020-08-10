import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

export const SchemeOfWorkBoxMenuItem = ({data, typeLabelText, typeButtonText}) => {
    if(data === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <div className="box">
                <a href={data.url} className="image fit">
                    <img src={data.image_url} alt="" />
                </a>
                <div className="inner">
                    <label className="label"><u>{typeLabelText}</u></label>
                    <h3>{data.name}</h3>
                    <p>{data.description}</p>
                    <Link to={`/Course/${data.id}`} className="button fit" data-poptrox="youtube,800x400">{typeButtonText}</Link>
                </div>
            </div>
        )
    }
}

export const SchemeOfWorkBoxMenuWidget = ({data, typeLabelText, typeButtonText}) => {
    if(data === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <Fragment>
                <h2>Courses</h2>
                <div className="thumbnails lessons">
                    {data.map(item => (
                        <SchemeOfWorkBoxMenuItem key={item.id} data={item} typeLabelText={typeLabelText} typeButtonText={typeButtonText} />
                    ))}
                </div>
            </Fragment>
        )
    }
}