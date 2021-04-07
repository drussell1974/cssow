import React from 'react';
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from "@fullcalendar/interaction";

const CalendarWidget = ({events, handleDateClick}) => {
    if (events === undefined) {
        return(<React.Fragment></React.Fragment>)
    } else {
        return (
            <FullCalendar
                plugins={[ dayGridPlugin ]}
                initialView="dayGridMonth"
                weekends={false}
                events={events}
                plugins={[ dayGridPlugin, interactionPlugin ]}
                dateClick={handleDateClick.bind(this)}
            />
        )
    }
}

export default CalendarWidget;