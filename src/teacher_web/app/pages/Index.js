import React, { Fragment } from 'react';
import GoogleAnalyticsWidget from '../widgets/GoogleAnalyticsWidget';
import SignInWidget from '../widgets/SignInWidget';
import AlertMessageWidget from '../widgets/AlertMessageWidget';
import NavbarWidget from '../widgets/NavbarWidget';
import BannerWidget from '../widgets/BannerWidget';
import FooterWidget from '../widgets/FooterWidget';

class Index extends React.Component {
    render() {
        let mastHeadStyle = {
            "background-image": "url('custom/img/computerscience-blackboard.jpg')",
        };

        return (        
            <Fragment>
                <nav className="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
                    <div className="container">
                        <SignInWidget />
                        <NavbarWidget />
                    </div>
                </nav>
                <header className="masthead" style={mastHeadStyle}>
                    <div className="overlay"></div>
                    <div className="container">
                        <div className="row">
                            <div className="col-lg-8 col-md-10 mx-auto">
                                <BannerWidget main_heading='Computer Science' sub_heading='Schemes of Work for Computer Science'/>
                            </div>
                        </div>
                    </div>
                </header>
                <div className="container-fluid main-container">
                    <div className="row">
                        <div className="col-lg-8 col-md-10 mx-auto">
                            <AlertMessageWidget message='' />
                        </div>
                    </div>
                </div>
                
                <footer>
                <div className="container">
                    <div className="row">
                        <div className="col-lg-8 col-md-10 mx-auto">
                            <FooterWidget />
                        </div>
                    </div>
                </div>
                </footer>

                <GoogleAnalyticsWidget trackingId='' />
            </Fragment>
        )
    }
};

export default Index;