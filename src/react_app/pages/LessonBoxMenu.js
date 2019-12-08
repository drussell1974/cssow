import React from 'react';

export const LessonBoxMenuItem = ({data}) => {
    return (
         <div className="box">
            <a href={data.url} className="image fit">
                <img src={data.image_url} alt="" />
            </a>
            <div className="inner">
                <h3>{data.title}</h3>
                <p>{data.summary}</p>
                <a href={data.url} className="button fit" data-poptrox="youtube,800x400">Watch</a>
            </div>
        </div>
    )
}

export const LessonBoxMenu = ({data}) => {

    return (
        <div className="thumbnails lessons">
            {data.map(item => (
                <LessonBoxMenuItem data={item} />
            ))}
        </div>
    )
}