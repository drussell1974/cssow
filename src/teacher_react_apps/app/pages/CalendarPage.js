import React, { useState } from 'react';
import getParams, { openModal, getCtx } from '../helpers/host_page';
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
            Ctx: getCtx(),
            hasError: false,
        }
        // bind the handler to the component
        this.handleShowAllEventsChange = this.handleShowAllEventsChange.bind(this);
        this.handleDateClick = this.handleDateClick.bind(this);
        this.handleShowWeekendChange = this.handleShowWeekendChange.bind(this);
        this.handleAddScheduledLessonClick = this.handleAddScheduledLessonClick.bind(this);
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
        getSchedule(this, this.state.Params.institute_id, this.state.Params.department_id, this.state.Params.schemeofwork_id, this.state.Params.lesson_id, this.state.Ctx);
      }

    /** Event Handlers >>> **/

    handleDateClick(e) {
        if (this.state.Params.institute_id > 0 && this.state.Params.department_id > 0 &&  this.state.Params.schemeofwork_id > 0 && this.state.Params.lesson_id > 0) {
            window.open(`/institute/${this.state.Params.institute_id}/department/${this.state.Params.department_id}/schemesofwork/${this.state.Params.schemeofwork_id}/lessons/${this.state.Params.lesson_id}/schedules/new?start_date=${e.dateStr}`, '_self');
        } else {
            openModal('', e.dateStr);
        }
    }

    handleShowAllEventsChange(e) {
        e.preventDefault();
        this.state = { 
            Params: getParams(e.target.checked),
            Ctx: getCtx(),
            ShowAllEvents: e.target.checked
        };
        getSchedule(this, this.state.Params.institute_id, this.state.Params.department_id, this.state.Params.schemeofwork_id, this.state.Params.lesson_id, this.state.Ctx);
    }

    handleShowWeekendChange(e) {
        this.state = {
            ShowWeekends: e.target.checked
        }
    }

    handleAddScheduledLessonClick(e) {
        openModal();
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
                    onAddScheduledLessonClick={this.handleAddScheduledLessonClick}
                />
            </React.Fragment>
        )
    }
};

export default CalendarPage