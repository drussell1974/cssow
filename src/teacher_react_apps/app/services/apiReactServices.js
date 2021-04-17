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


const getSchedule = (reactComponent, institute_id, department_id, schemeofwork_id, lesson_id, ctx) => {
    let uri = `/api/schedule/institute/${institute_id}/department/${department_id}/schemesofwork/${schemeofwork_id}/lessons/${lesson_id}/events?format=json`;
    fetch(uri)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            let scheduled_events = []
            // map scheduled lessons to fullcalendar event
            data.schedule.map(sch => {
                scheduled_events.push({
                    title: `${sch.start_date_ui_time}: ${sch.class_name} - ${sch.title}`, 
                    start: sch.start_date, 
                    extendedProps: {
                        lesson_details: `time: ${sch.start_date_ui_time}, class: ${sch.class_name}, title: '${sch.title}', code: ${sch.class_code}`,
                        edit_url: sch.edit_url,
                        whiteboard_url: sch.whiteboard_url,
                        button_class: sch.scheme_of_work_id == ctx.schemeofwork_id ? 'badge badge-primary badge-event' : 'badge badge-secondary badge-event',
                    },
                    url: sch.edit_url 
                })
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