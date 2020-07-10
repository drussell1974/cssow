import React from 'react';

const FooterWidget = ({heading, summary, socialmedia}) => {
    if(heading !== undefined && summary !== undefined) {

        let socialmediadata = socialmedia === undefined || socialmedia.length === undefined  ? [] : socialmedia;
        
        return (
            <footer id="footer">
                <div className="inner">
                    <h2>{heading}</h2>
                    <p>{summary}</p>

                    <ul className="icons">
                        {
                            socialmediadata.map((item) => (
                                <li key={item.name}><a href={item.url} className={item.iconClass}><span className="label">{item.name}</span></a></li>
                               )
                            )}
                    </ul>
                    <p className="copyright">&copy; Untitled. Design: <a href="https://templated.co">TEMPLATED</a>. Images: <a href="https://unsplash.com/">Unsplash</a>. Videos: <a href="http://coverr.co/">Coverr</a>.</p>
                </div>
            </footer>
        )
    } else {
        return (
            <React.Fragment></React.Fragment>
        )
    }
}

export default FooterWidget;