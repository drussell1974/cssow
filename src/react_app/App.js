import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Index from './pages/Index';
import Lesson from './pages/Lesson';
import '../assets/css/main.css';    

ReactDOM.render(
    <Router>
        <Switch>
            <Route exact path="/" component={Index} />
            <Route path="/Lesson" component={Lesson} />
        </Switch>
    </Router>
, document.getElementById('app'));