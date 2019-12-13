import React from 'react';

const BannerWidget = ({heading, summary}) => {
    return (
            <section id="banner" data-video="images/banner">
                <div className="inner">
                    <header>
                        <h1>{heading}</h1>
                        <p>{summary}</p>
                    </header>
                    <a href="#main" className="more">Learn More</a>
                </div>
            </section>

        )
}

export default BannerWidget;