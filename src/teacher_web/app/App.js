import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Index from './pages/Index';
import '../assets/css/class_notes.css';    
import '../assets/css/clean-blog.css';    
import '../assets/css/my.css';    

ReactDOM.render(
    <Router>
        <Switch>
            <Route exact path="/" component={Index} />
        </Switch>
    </Router>
, document.getElementById('app'));