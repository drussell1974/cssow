import React from 'react';

const BannerWidget = ({heading, description}) => {
    if(heading === undefined || description === undefined) {
        return <React.Fragment></React.Fragment>;
    } else {
        return (
            <section id="banner" data-video="assets/images/banner">
                <div className="inner">
                    <header>
                        <h1 className="h1">{heading}</h1>
                        <p>{description}</p>
                    </header>
                    <a href="#main" className="more">Learn More</a>
                </div>
            </section>

        )
    }
}

export default BannerWidget;