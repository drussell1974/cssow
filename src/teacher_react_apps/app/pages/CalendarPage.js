import React, { useState } from 'react';
import getParams from '../helpers/host_page';
import { getSchedule } from '../services/apiReactServices';
import CalendarWidget from '../widgets/CalendarWidget';

class CalendarPage extends React.Component {
    
    constructor(props){
        super(props);

        this.state = {
            Params: getParams(false),
            Events: [],
            hasError: false,
        }
        // bind the handler to the component
        this.handleChangeFilter = this.handleChangeFilter.bind(this);
        // this.handleDateClick = this.handleDateClick.bind(this);
    }   

    handleDateClick(e) {
        console.log(e.dateStr);
        // TODO: #358 add scheduled lesson
      }

    handleChangeFilter(e) {
        this.state = { 
            Params: getParams(e.target.checked)
        };
        
        getSchedule(this, this.state.Params.institute_id, this.state.Params.department_id, this.state.Params.schemeofwork_id, this.state.Params.lesson_id);
    }

    componentDidMount() {
        getSchedule(this, this.state.Params.institute_id, this.state.Params.department_id, this.state.Params.schemeofwork_id, this.state.Params.lesson_id);
        // get schedule every 30 seconds
        setInterval(() => getSchedule(this, this.state.Params.institute_id, this.state.Params.department_id, this.state.Params.schemeofwork_id, this.state.Params.lesson_id), 30000);
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
      
    render() {

        return (
            <React.Fragment>
                <CalendarWidget 
                    events={this.state.Events} 
                    showAllDefault={false}
                    onDateClick={this.handleDateClick}
                    onChangeFilter={this.handleChangeFilter}
                />
            </React.Fragment>
        )
    }
};

export default CalendarPage