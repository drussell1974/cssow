import React from 'react';
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from "@fullcalendar/interaction";

const CalendarWidget = ({events, onDateClick, onChangeFilter}) => {
    
    const handleOnDateClick = async e => {
        onDateClick(e);
    };

    const handleOnChangeFilter = async e => {
    //const handleOnChangeFilter = e => {
        e.preventDefault();
        onChangeFilter(e);
    };

    if (events === undefined) {
        return(<React.Fragment></React.Fragment>)
    } else {
        return (
            <React.Fragment>
                <div id="event-filter">
                    <div className="form-check form-check-inline" >
                        <input className="form-check-input" type="checkbox" name="event_filter" value="all" onChange={handleOnChangeFilter} id="event_filter--all"/>
                        <label className="form-check-label" htmlFor="event_filter">show all events</label>
                    </div>
                </div>
                <FullCalendar
                    plugins={[ dayGridPlugin ]}
                    initialView="dayGridMonth"
                    weekends={false}
                    events={events}
                    plugins={[ dayGridPlugin, interactionPlugin ]}
                    dateClick={handleOnDateClick}
                />
            </React.Fragment>
        )
    }
}

export default CalendarWidget;