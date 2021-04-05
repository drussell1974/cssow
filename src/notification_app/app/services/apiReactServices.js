const getNotifications = (reactComponent) => {
    let uri = `${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/notifications/?format=json`;
    fetch(uri)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            reactComponent.setState({
                Messages: data.messages, 
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

export { getNotifications };