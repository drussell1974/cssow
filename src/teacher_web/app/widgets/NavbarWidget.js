import React, { Fragment } from 'react';

const NavbarWidget = () => {
    return (
        <Fragment>
            <button className="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            Menu
            <i className="fas fa-bars"></i>
        </button>
            <div className="collapse navbar-collapse" id="navbarResponsive">
            <ul className="navbar-nav ml-auto">
                <li className="nav-item">
                    <a className="nav-link home" href="/">Home</a>
                </li>
                <li className="nav-item">
                    <a className="nav-link schemeofwork" href="/schemesofwork">Schemes of Work</a>
                </li>
                <li className="nav-item">
                    <a className="nav-link keywords" href="/keyword">Key terms</a>
                </li>
                <li className="nav-item">
                    <a className="nav-link about" href="/about">About</a>
                </li>
            </ul>
        </div>
        </Fragment>
    )
}

export default NavbarWidget;
