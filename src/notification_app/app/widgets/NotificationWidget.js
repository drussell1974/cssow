import React from 'react';

const NotificationWidget = ({messages}) => {
    if(messages !== undefined) {
        return (
            <div className="alert alert-info small" role="alert">
                You have messages 
                <button className="badge badge-info dropdown-toggle" type="button" id="dropdownNotificationsMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">{messages.length}</button>
                <div className="dropdown-menu" aria-labelledby="dropdownNotificationsMenuButton">
                    {messages.map(item => (
                        <a key={item.id} className="dropdown-item" href={item.action}>{item.message}</a>
                    ))}
                </div>
            </div>
        )
    } else {
        return (
            <React.Fragment></React.Fragment>
        )
    }
}

export default NotificationWidget;