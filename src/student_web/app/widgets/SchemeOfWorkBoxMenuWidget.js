import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

export const SchemeOfWorkBoxMenuItem = ({data, uri, typeLabelText, typeButtonText, typeButtonClass}) => {
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
                    
                    <Link to={uri} className={typeButtonClass} data-poptrox="youtube,800x400">{typeButtonText}</Link>
                </div>
            </div>
        )
    }
}

export const SchemeOfWorkBoxMenuWidget = ({data, typeLabelText, typeButtonText, typeButtonClass, typeDisabledButtonText, typeDisabledButtonClass}) => {
    if(data === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <Fragment>
                <h2>Courses</h2>
                <div className="thumbnails lessons">
                    {data.map(item => 
                        {
                            if (item.number_of_lessons === 0) {
                                let uri = ``
                                return <SchemeOfWorkBoxMenuItem key={item.id} data={item} uri={uri} typeLabelText={typeLabelText} typeButtonText={typeDisabledButtonText} typeButtonClass={typeDisabledButtonClass} />
                            } else {
                                let uri = `/Course/${item.id}`;
                                return <SchemeOfWorkBoxMenuItem key={item.id} data={item} uri={uri} typeLabelText={typeLabelText} typeButtonText={typeButtonText} typeButtonClass={typeButtonClass} />
                            }
                        }

                    )}
                </div>
            </Fragment>
        )
    }
}