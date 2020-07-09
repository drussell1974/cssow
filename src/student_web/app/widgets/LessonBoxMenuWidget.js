import React, { Fragment } from 'react';
import { BrowserRouter as Router, Link } from 'react-router-dom';

export const LessonBoxMenuExternalLinkItem = ({data, typeButtonText}) => {
    if(data === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <div className="box">
                <a href={data.page_uri} className="image fit">
                    <img src={data.image_url} alt="" />
                </a>
                <div className="inner">
                    <label className="label"><u>{data.type_name}</u></label>
                    <h3>{data.page_note}</h3>
                    <p>{data.title}</p>
                    <a href={data.page_uri} className="button fit" data-poptrox="youtube,800x400">{typeButtonText}</a>
                </div>
            </div>
        )
    }
}

export const LessonBoxMenuMarkdownPageLinkItem = ({data, lesson, typeButtonText}) => {
    if(data === undefined || lesson === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        //const uri = `${data.lesson_id}/${data.id}/${data.md_document_name}`;
        const uri = `/Lesson/${lesson.id}/Activity/${data.scheme_of_work_id}/${data.id}/${data.md_document_name}`;
        
        return (

            <div className="box">
                <Link to={uri} className="image fit">
                    <img src={data.image_url} alt="" />
                </Link>
                <div className="inner">
                    <label className="label"><u>{data.type_name}</u></label>
                    <h3>{data.page_note}</h3>
                    <p>{data.title}</p>
                    <Link to={uri} className="button fit">{typeButtonText}</Link> 
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
                <h2>Resources</h2>
                <div className="thumbnails lessons">
                    {resources.filter(item => item.page_uri !== "").map(item => (
                        <LessonBoxMenuExternalLinkItem key={item.id} data={item} typeLabelText={typeLabelText} typeButtonText={typeButtonText} />
                    ))}
                    {resources.filter(item => item.type_name === "Markdown" && item.md_document_name !== "").map(item => (
                        <LessonBoxMenuMarkdownPageLinkItem key={item.id} data={item} lesson={data} typeLabelText={typeLabelText} typeButtonText={typeButtonText} />
                    ))}
                </div>
            </Fragment>
        )
    }
}