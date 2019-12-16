import React from 'react';

const BannerWidget = ({data}) => {
    if(data === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <section id="banner" data-video="images/banner">
                <div className="inner">
                    <header>
                        <h2 className="h2">Course</h2>
                        <h1 className="h1">{data.name}</h1>
                        <p>{data.description}</p>
                    </header>
                    <a href="#main" className="more">Learn More</a>
                </div>
            </section>

        )
    }
}

export default BannerWidget;