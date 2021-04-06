import React from 'react';
// import { getEvents } from '../services/apiReactServices';
import CalendarWidget from '../widgets/CalendarWidget';

class CalendarPage extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            Events: [],
            hasError: false,
        }
        // this.handleDeleteMessageClick = this.handleDeleteMessageClick.bind(this);
    }

    handleDeleteMessageClick(id) {
    }
    
    componentDidMount() {
        // getEvents(this);
        // setInterval(() => getNotifications(this), 30000);
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
                <CalendarWidget />
            </React.Fragment>
        )
    }
};

export default CalendarPage