import React from 'react';
import ReactDOM from 'react-dom';
import NotificationPage from './pages/NotificationPage';
import CalendarPage from './pages/CalendarPage';

ReactDOM.render(
    <NotificationPage />
, document.querySelector('#notification-app'));

ReactDOM.render(
    <CalendarPage />
, document.querySelector('#calendar-app'));