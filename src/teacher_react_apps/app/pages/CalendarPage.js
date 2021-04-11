import React, { useState } from 'react';
import getParams from '../helpers/host_page';
import { getSchedule } from '../services/apiReactServices';
import CalendarWidget from '../widgets/CalendarWidget';

class CalendarPage extends React.Component {
    
    constructor(props){
        super(props);

        this.state = {
            Params: getParams(props.showAllEvents),
            Events: [],
            AcademicYear: props.academicYear,
            ShowAllEvents: props.showAllEvents,
            ShowWeekends: props.showWeekends,
            hasError: false,
        }
        // bind the handler to the component
        this.handleShowAllEventsChange = this.handleShowAllEventsChange.bind(this);
        this.handleDateClick = this.handleDateClick.bind(this);
        this.handleShowWeekendChange = this.handleShowWeekendChange.bind(this);
    }   

    static getDerivedStateFromError(error) {
        // Update state so the next render will show the fallback UI.
        return { hasError: true };
      }

    componentDidCatch(error, errorInfo) {
        // You can also log the error to an error reporting service
        console.log(error, errorInfo);
        
        this.state = {
            hasError: true,
        }
      }

      componentDidMount() {
        getSchedule(this, this.state.Params.institute_id, this.state.Params.department_id, this.state.Params.schemeofwork_id, this.state.Params.lesson_id);
        // get schedule every 30 seconds
        // setInterval(() => getSchedule(this, this.state.Params.institute_id, this.state.Params.department_id, this.state.Params.schemeofwork_id, this.state.Params.lesson_id), 30000);
      }

    /** Event Handlers >>> **/

    handleDateClick(e) {
        console.log(e.dateStr);
        // TODO: #358 add scheduled lesson
      }

    handleShowAllEventsChange(e) {
        e.preventDefault();
        this.state = { 
            Params: getParams(e.target.checked),
            ShowAllEvents: e.target.checked
        };
        getSchedule(this, this.state.Params.institute_id, this.state.Params.department_id, this.state.Params.schemeofwork_id, this.state.Params.lesson_id);
    }

    handleShowWeekendChange(e) {
        // NOTE: do not NOT e.preventDefault();, as it causes conflict with calendar
        this.state = {
            ShowWeekends: e.target.checked
        }
    }
  
    /** <<< Event Handlers END **/
        
    render() {
        return (
            <React.Fragment>
                <CalendarWidget 
                    events={this.state.Events} 
                    showAllEvents={this.state.ShowAllEvents}
                    academicYear={this.state.AcademicYear}
                    showWeekends={this.state.ShowWeekends}
                    onDateClick={this.handleDateClick}
                    onShowAllEventsChange={this.handleShowAllEventsChange}
                    onShowWeekendChange={this.handleShowWeekendChange}
                />
            </React.Fragment>
        )
    }
};

export default CalendarPage