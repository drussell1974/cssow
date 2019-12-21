import React, { Fragment } from 'react';

const FooterWidget = () => {
    let year = Date.now();

    return (
        <Fragment>
            <ul className="list-inline text-center">
                <li className="list-inline-item">
                    <a href="/">
                    <span className="fa-stack fa-lg">
                        <i className="fas fa-circle fa-stack-2x"></i>
                        <i className="fab fa-twitter fa-stack-1x fa-inverse"></i>
                    </span>
                    </a>
                </li>
                <li className="list-inline-item">
                    <a href="/">
                    <span className="fa-stack fa-lg">
                        <i className="fas fa-circle fa-stack-2x"></i>
                        <i className="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                    </span>
                    </a>
                </li>
            </ul>
            <p className="copyright text-muted">Copyright' &#169; Dave Russell { year }</p>
        </Fragment>
    )
};

export default FooterWidget;