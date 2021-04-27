import React from 'react';
import { getNotifications, deleteNotification } from '../services/apiReactServices';
import AlertWidget from '../widgets/AlertWidget';

class AlertPage extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            Messages: {},
            Alert: "",
        }
        this.handleDeleteMessageClick = this.handleDeleteMessageClick.bind(this);
    }

    handleDeleteMessageCli  ck(id) {
        deleteNotification(this, id);
        
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
                <AlertWidget messages={this.state.Messages} deleteMessageCallback={this.handleDeleteMessageClick} />
            </React.Fragment>
        )
    }
};

export default AlertPage