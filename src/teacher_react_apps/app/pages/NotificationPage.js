import React from 'react';
import { getNotifications } from '../services/apiReactServices';
import NotificationWidget from '../widgets/NotificationWidget';

class NotificationPage extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            Messages: {},
        }
        this.handleDeleteMessageClick = this.handleDeleteMessageClick.bind(this);
    }

    handleDeleteMessageClick(id) {
        const copyMessages = {...this.state.Messages}
        delete copyMessages[id]
        this.setState({
            Messages: copyMessages,
        })
    }
    

    componentDidMount() {
        getNotifications(this);
        setInterval(() => getNotifications(this), 30000);
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
                <NotificationWidget messages={this.state.Messages} deleteMessageCallback={this.handleDeleteMessageClick} />
            </React.Fragment>
        )
    }
};

export default NotificationPage