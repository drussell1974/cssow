import React from 'react';
import { getSchedule } from '../services/apiReactServices';
// import { getEvents } from '../services/apiReactServices';
import CalendarWidget from '../widgets/CalendarWidget';

class CalendarPage extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            Events: [],
            hasError: false,
        }
        // required for getting parameters
        // this.handleDateClick = this.handleDateClick.bind(this);
        
        // #358 get params from page TODO: handle if not available
        this.institute_id = document.querySelector("input#teacher_react_apps__institute_id").value;
        //this.department_id = document.querySelector("input#teacher_react_apps__department_id").value;
        //this.schemeofwork_id = document.querySelector("input#teacher_react_apps__scheme_of_work_id").value;
        //this.lesson_id = document.querySelector("input#teacher_react_apps__lesson_id").value;
    }

    handleDateClick(e) {
        console.log(e.dateStr);
        // TODO: #358 add scheduled lesson
      }

    handleChangeFilter(e) {
        console.log(e);
    }

    componentDidMount() {
        getSchedule(this, this.institute_id);
        // get schedule every 30 seconds
        setInterval(() => getSchedule(this, this.institute_id), 30000);
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
                    onDateClick={this.handleDateClick}
                    onChangeFilter={this.handleChangeFilter}
                />
            </React.Fragment>
        )
    }
};

export default CalendarPage