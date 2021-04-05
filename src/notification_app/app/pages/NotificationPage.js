import React from 'react';
import { getNotifications } from '../services/apiReactServices';
import NotificationWidget from '../widgets/NotificationWidget';

class NotificationPage extends React.Component {
    
    onProgress() {
        return this.state.loading + 100 / 3;
    }

    constructor(props){
        super(props);
        this.state = {
            messages: [],
        }
    }

    componentDidMount() {
        getNotifications(this);
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
                <NotificationWidget messages={this.state.messages} />
            </React.Fragment>
        )
    }
};

export default NotificationPage