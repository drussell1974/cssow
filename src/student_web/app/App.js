import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import InstitutePage from './pages/InstitutePage';
import DepartmentPage from './pages/DepartmentPage';
import CoursePage from './pages/CoursePage';
import LessonPage from './pages/LessonPage';
import LessonsPage from './pages/LessonsPage';
import ActivityPage from './pages/ActivityPage';
import '../assets/css/main.css';    
import '../assets/css/custom.css';    
import '../node_modules/github-markdown-css/github-markdown.css';

ReactDOM.render(
    <Router>
        <Switch>
            <Route exact path="/" component={LoginPage} ></Route>
        
            <Route exact path="/institute/:institute_id/department/:department_id/course/:course_id/lesson/:lesson_id/ativity/:resource_id/:md_document_name/" component={ActivityPage} />
            
            <Route exact path="/institute/:institute_id/department/:department_id/course/:course_id/lesson/:lesson_id" component={LessonPage} />
            
            <Route exact path="/institute/:institute_id/department/:department_id/course/:course_id/lesson/" component={LessonsPage} />
            
            <Route exact path="/institute/:institute_id/department/:department_id/course/" component={CoursePage} />

            <Route exact path="/institute/:institute_id/department/" component={DepartmentPage} ></Route>
        
            <Route exact path="/institute/" component={InstitutePage} ></Route>
            
        </Switch>
    </Router>
, document.getElementById('app'));