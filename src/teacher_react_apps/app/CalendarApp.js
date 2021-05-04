import React from 'react';
import ReactDOM from 'react-dom';
import CalendarPage from './pages/CalendarPage';
import { getAcademicYear } from './helpers/host_page';

ReactDOM.render(
    <CalendarPage showAllEvents={true} academicYear={getAcademicYear} showWeekends={false} />
, document.querySelector('#calendar-app'));