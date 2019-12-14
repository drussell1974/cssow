import React from 'react';

const BannerWidget = ({data}) => {
    if(data === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <section id="banner" data-video="images/banner">
                <div className="inner">
                    <header>
                        <h1>{data.title}</h1>
                        <p>{data.description}</p>
                    </header>
                    <a href="#main" className="more">Learn More</a>
                </div>
            </section>

        )
    }
}

export default BannerWidget;