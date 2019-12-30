import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Index from './pages/Index';
import Lessons from './pages/Lessons';
import Lesson from './pages/Lesson';
import SchemesOfWorkPage from './pages/SchemesOfWorkPage';

import '../assets/css/class_notes.css';    
import '../assets/css/clean-blog.min.css';    
import '../assets/css/my.css';    

import GoogleAnalyticsWidget from './widgets/GoogleAnalyticsWidget';
import LogInWidget from './widgets/LogInWidget';
import AlertMessageWidget from './widgets/AlertMessageWidget';
import NavbarWidget from './widgets/NavbarWidget';
import BannerWidget from './widgets/BannerWidget';
import FooterWidget from './widgets/FooterWidget';

let mastHeadStyle = {
    backgroundImage: "url('/custom/img/computerscience-blackboard.jpg')",
};

ReactDOM.render(
    <Router>
        <nav className="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
            <div className="container">
                <LogInWidget auth={false} />
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
            <Route exact path="/login" component={Index} />
            <Route exact path="/schemeofwork" component={SchemesOfWorkPage} />
            <Route exact path="/schemeofwork/:scheme_of_work_id/lessons/" component={Lessons} />
            <Route exact path="/schemeofwork/:scheme_of_work_id/lessons/:learning_episode_id" component={Lesson} />
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