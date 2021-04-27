import React from 'react';

const NotificationWidget = ({messages, deleteMessageCallback}) => {
    if(messages !== undefined) {
        return (
            <React.Fragment>
                    {Object.keys(messages).map(id => (
                        <div key={id} className="alert alert-warning" role="alert">
                            <strong>{messages[id].notify_message}</strong> <a className="alert-link" href={messages[id].action}>action now</a> <button onClick={deleteMessageCallback.bind(this, id)} type="button" className="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                        </div>
                    ))}
                
            </React.Fragment>
        )
    } else {
        return (
            <React.Fragment></React.Fragment>
        )
    }
}

export default NotificationWidget;