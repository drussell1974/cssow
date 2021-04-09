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


const getSchedule = (reactComponent, institute_id, department_id, schemeofwork_id, lesson_id) => {
    let uri = `/api/schedule/institute/${institute_id}/department/${department_id}/schemesofwork/${schemeofwork_id}/lessons/${lesson_id}/events?format=json`;
    fetch(uri)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            let scheduled_events = []
            // map scheduled lessons to fulcalendar event
            data.schedule.map(sch => {
                scheduled_events.push({title: `${sch.class_name} - ${sch.title}`, start: sch.start_date, url: sch.whiteboard_url })
            })

            reactComponent.setState({
                Events: scheduled_events,
                hasError: false,
            });
        },
        (error) => {
            reactComponent.setState({
                Events: [],
                Alert: error,
                hasError: true,
            });
        }
    )
}


export { getNotifications, deleteNotification, getSchedule };