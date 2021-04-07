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
        
        // TODO: #358 get params from page and handle if not available
        this.institute_id = document.querySelector("#teacher_react_apps.institute_id");
    }

    handleDateClick(arg) {
        console.log(arg.dateStr);
        // TODO: #358 add scheduled lesson
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
                    handleDateClick={this.handleDateClick}
                />
            </React.Fragment>
        )
    }
};

export default CalendarPage