import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';


const LessonBoxLinkButton = ({data, typeButtonText, typeButtonClass, typeDisabledButtonText, typeDisabledButtonClass}) => {
    if (data.number_of_learning_objectives == 0 && data.number_of_resources == 0) {
        return ( <button className={typeDisabledButtonClass} data-poptrox="youtube,800x400" >{typeDisabledButtonText}</button>)
    } else {
        return ( <Link to={`/Course/${data.scheme_of_work_id}/Lesson/${data.id}`} className={typeButtonClass} data-poptrox="youtube,800x400" >{typeButtonText}</Link>)
    }
}


export const LessonsBoxMenuItem = ({data, typeLabelText, typeButtonText, typeButtonClass, typeDisabledButtonText, typeDisabledButtonClass}) => {
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
                    <LessonBoxLinkButton data={data} typeButtonClass={typeButtonClass} typeButtonText={typeButtonText} typeDisabledButtonClass={typeDisabledButtonClass} typeDisabledButtonText={typeDisabledButtonText}/>
                </div>
            </div>
        )
    }
}

export const LessonsBoxMenuWidget = ({data, typeLabelText, typeButtonText, typeButtonClass, typeDisabledButtonText, typeDisabledButtonClass}) => {
    if(data === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <Fragment>
                <h2>Lessons</h2>
                <div className="thumbnails lessons">
                    {data.map(item => (
                        <LessonsBoxMenuItem key={item.id} data={item} typeLabelText={typeLabelText}
                            typeButtonText={typeButtonText} typeButtonClass={typeButtonClass} 
                            typeDisabledButtonText={typeDisabledButtonText} typeDisabledButtonClass={typeDisabledButtonClass}
                        />
                    )
                    )}
                </div>
            </Fragment>
            
        )
    }
}

