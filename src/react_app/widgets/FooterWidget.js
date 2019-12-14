import React from 'react';

const FooterWidget = ({heading, summary}) => {
    if(heading !== undefined && summary !== undefined) {
        return (
            <footer id="footer">
                <div className="inner">
                    <h2>{heading}</h2>
                    <p>{summary}</p>

                    <ul className="icons">
                        <li><a href="#" className="icon fa-twitter"><span className="label">Twitter</span></a></li>
                        <li><a href="#" className="icon fa-facebook"><span className="label">Facebook</span></a></li>
                        <li><a href="#" className="icon fa-instagram"><span className="label">Instagram</span></a></li>
                        <li><a href="#" className="icon fa-envelope"><span className="label">Email</span></a></li>
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