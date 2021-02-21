import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

const InstituteBoxLinkButton = ({data, typeButtonText, typeButtonClass, typeDisabledButtonText, typeDisabledButtonClass}) => {
    if (data.number_of_departments === 0) {
        return ( <button className={typeDisabledButtonClass} data-poptrox="youtube,800x400" >{typeDisabledButtonText}</button>)
    } else {
        return ( <Link to={`/institute/${data.id}/department`} className={typeButtonClass} data-poptrox="youtube,800x400" >{typeButtonText}</Link>)
    }
}

export const InstituteBoxMenuItem = ({data, typeLabelText, typeButtonText, typeButtonClass, typeDisabledButtonText, typeDisabledButtonClass}) => {
    if(data === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        if (data.number_of_departments === 0) {
            // disable
            typeButtonText = typeDisabledButtonText;
            typeButtonClass = typeDisabledButtonClass;
        }
        return (
            <div className="box">
                <a href={data.url} className="image fit">
                    <img src={data.image_url} alt="" />
                </a>
                <div className="inner">
                    <label className="label"><u>{typeLabelText}</u></label>
                    <h3>{data.name}</h3>
                    <p>{data.description}</p>
                    <InstituteBoxLinkButton data={data} typeButtonClass={typeButtonClass} typeButtonText={typeButtonText} typeDisabledButtonClass={typeDisabledButtonClass} typeDisabledButtonText={typeDisabledButtonText}/>
                </div>
            </div>
        )
    }
}

export const InstituteBoxMenuWidget = ({data, typeLabelText, typeButtonText, typeButtonClass, typeDisabledButtonText, typeDisabledButtonClass}) => {
    if(data === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <Fragment>
                <h2>Institutes</h2>
                <div className="thumbnails institutes">
                    {data.map(item => (
                        <InstituteBoxMenuItem key={item.id} data={item} typeLabelText={typeLabelText}
                            typeButtonText={typeButtonText} typeButtonClass={typeButtonClass} 
                            typeDisabledButtonText={typeDisabledButtonText} typeDisabledButtonClass={typeDisabledButtonClass}
                        />
                    )
                )}
                </div>
            </Fragment>
        )}
    }
