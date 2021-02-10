import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import CoursePage from './pages/CoursePage';
import SchemeOfWorkPage from './pages/SchemeOfWorkPage';
import LessonPage from './pages/LessonPage';
import ActivityPage from './pages/ActivityPage';
import '../assets/css/main.css';    
import '../assets/css/custom.css';    
import '../node_modules/github-markdown-css/github-markdown.css';

ReactDOM.render(
    <Router>
        <Switch>
            <Route exact path="/" component={SchemeOfWorkPage} ></Route>
            <Route path="/login" component={LoginPage} ></Route>
            <Route path="/course/:scheme_of_work_id/lesson/:lesson_id/ativity/:resource_id/:md_document_name/" component={ActivityPage} />
            <Route path="/course/:scheme_of_work_id/lesson/:lesson_id" component={LessonPage} />
            <Route path="/course/:scheme_of_work_id" component={CoursePage} />
        </Switch>
    </Router>
, document.getElementById('app'));