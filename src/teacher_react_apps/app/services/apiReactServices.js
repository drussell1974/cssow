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
                Institutes: [],
                hasError: true,
            });
        }
    )
}

export { getNotifications };