import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

export const SOWBoxMenuItem = ({data, typeLabelText, typeButtonText}) => {
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
                    <h3>{data.title}</h3>
                    <p>{data.summary}</p>
                    <Link to={`/Lesson/${data.id}`} className="button fit" data-poptrox="youtube,800x400">{typeButtonText}</Link>
                </div>
            </div>
        )
    }
}

export const SOWBoxMenuWidget = ({data, typeLabelText, typeButtonText}) => {
    if(data === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <Fragment>
                <h2>Lessons</h2>
                <div className="thumbnails lessons">
                    {data.filter(item => item.number_of_learning_objective > 0 && item.number_of_resource > 0).map(item => (
                        <SOWBoxMenuItem key={item.id} data={item} typeLabelText={typeLabelText} typeButtonText={typeButtonText} />
                    ))}
                </div>
            </Fragment>
            
        )
    }
}