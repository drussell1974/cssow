import React from 'react';
import ReactDOM from 'react-dom';
import NotificationPage from './pages/NotificationPage';
import CalendarPage from './pages/CalendarPage';
import { showAllEvents } from './helpers/host_page';

ReactDOM.render(
    <NotificationPage />
, document.querySelector('#notification-app'));

ReactDOM.render(
    <CalendarPage showAllEvents={showAllEvents} showWeekends={false} />
, document.querySelector('#calendar-app'));