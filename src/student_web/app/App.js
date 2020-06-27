import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Index from './pages/Index';
import Lesson from './pages/Lesson';
import Activity from './pages/Activity';
import '../assets/css/main.css';    
import '../assets/css/custom.css';    
import '../node_modules/github-markdown-css/github-markdown.css';

ReactDOM.render(
    <Router>
        <Switch>
            <Route exact path="/" component={Index} ></Route>
            <Route path="/Lesson/:learning_episode_id" component={Lesson} />
            <Route path="/Activity:learning_episode_id" component={Activity} />
        </Switch>
    </Router>
, document.getElementById('app'));