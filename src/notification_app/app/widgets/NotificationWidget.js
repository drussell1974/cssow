import React from 'react';

const NotificationWidget = ({messages, deleteMessageCallback}) => {
    if(messages !== undefined) {
        return (
            <React.Fragment>
                <button className="badge badge-info dropdown-toggle" type="button" id="dropdownNotificationsMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i className="fa fa-inbox"></i> {Object.keys(messages).length}</button>
                <div className="dropdown-menu" aria-labelledby="dropdownNotificationsMenuButton">
                    {Object.keys(messages).map(id => (
                        <div key={id} className="dropdown-item alert alert-warning alert-dismissible fade show" role="alert">
                            <strong>{messages[id].message}</strong> <a className="dropdown-link" href={messages[id].action}>action now</a> <button onClick={deleteMessageCallback.bind(this, id)} type="button" className="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                        </div>
                    ))}
                </div>
            </React.Fragment>
        )
    } else {
        return (
            <React.Fragment></React.Fragment>
        )
    }
}

export default NotificationWidget;