const getNotifications = (reactComponent) => {
    let uri = `/api/notifications/?format=json`;
    fetch(uri)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            let messages = {};
            data.messages.map(m => {
                messages[m.id] = m
            })
            reactComponent.setState({
                Messages: messages,
                hasError: false,
            });
        },  
        (error) => {
            reactComponent.setState({
                Messages: [],
                hasError: true,
            });
        }
    )
}

const deleteNotification = (reactComponent, id) => {
    let uri = `/api/notifications/${id}/delete?format=json`;
    fetch(uri)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            reactComponent.setState({
                hasError: false,
                Alert: data
            });
        },
        (error) => {
            reactComponent.setState({
                Alert: error,
                hasError: true,
            });
        }
    )
}

export { getNotifications, deleteNotification };