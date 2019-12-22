import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Index from './pages/Index';
import Lessons from './pages/Lessons';

import '../assets/css/class_notes.css';    
import '../assets/css/clean-blog.css';    
import '../assets/css/my.css';    

import GoogleAnalyticsWidget from './widgets/GoogleAnalyticsWidget';
import SignInWidget from './widgets/SignInWidget';
import AlertMessageWidget from './widgets/AlertMessageWidget';
import NavbarWidget from './widgets/NavbarWidget';
import BannerWidget from './widgets/BannerWidget';
import FooterWidget from './widgets/FooterWidget';
let mastHeadStyle = {
    backgroundImage: "url('custom/img/computerscience-blackboard.jpg')",
};

ReactDOM.render(
    <Router>
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
                        <BannerWidget main_heading='Teach Computer Science' sub_heading='Computing Schemes of Work across all key stages'/>
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
        <Switch>
            <Route exact path="/" component={Index} />
            <Route exact path="/learningepisode/:learning_episode_id" component={Lessons} />
        </Switch>
        
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
    </Router>
, document.getElementById('app'));