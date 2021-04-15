import React, { useState } from 'react';
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from "@fullcalendar/interaction";

const CalendarWidget = ({events, academicYear, onDateClick, onShowAllEventsChange, onShowWeekendChange, showAllEvents=false, showWeekends=false}) => {

    const [ showAllIsChecked, setShowAllIsChecked ] = useState(showAllEvents);
    const [ showWeekendsIsChecked, setShowWeekendsIsChecked ] = useState(showWeekends);

    const handleOnDateClick = async e => {
        onDateClick(e);
    };

    const handleEventClick = async e => {
        console.log(e);
    }
    
    const handleOnShowAllEventsChange = async e => {
        e.preventDefault();
        setShowAllIsChecked(!showAllIsChecked)
        onShowAllEventsChange(e);
    };
    
    const handleOnChangeShowWeekend = async e => {
        // e.preventDefault();
        setShowWeekendsIsChecked(!showWeekendsIsChecked);
        onShowWeekendChange(e);
    };

    const fnEventContent = (arg) => {
        // NOTE: #447 - add col-12 to prevent overlapping
        return { html: `<button class="badge badge-info col-12" title="${arg.event.extendedProps.lesson_details}">${arg.event.title}</button>` }
    }

    if (events === undefined) {
        return(<React.Fragment></React.Fragment>)
    } else {
        return (
            <React.Fragment>
                <div  id="event_filter--control">
                    <div className="form-check form-switch form-check-inline event_filter--all" >
                        <input className="form-check-input" type="checkbox" name="show_all" checked={showAllIsChecked} onChange={handleOnShowAllEventsChange} id="event_filter--all" />
                        <label className="form-check-label" htmlFor="event_filter--all">show all events</label>
                    </div>
                    <div className="form-check form-switch form-check-inline event_filter--weekend" >
                        <input className="form-check-input" type="checkbox" name="show_weekends" checked={showWeekendsIsChecked} onChange={handleOnChangeShowWeekend} id="event_filter--weekend" />
                        <label className="form-check-label" htmlFor="event_filter--weekend">show weekends</label>
                    </div>
                </div>
                <FullCalendar
                    plugins={[ dayGridPlugin ]}
                    // TODO: make the following options available 'dayGridMonth', 'dayGridWeek', 'timeGridDay', 'listWeek'
                    initialView="dayGridMonth"
                    weekends={showWeekendsIsChecked}
                    events={events}
                    validRange={academicYear}
                    plugins={[ dayGridPlugin, interactionPlugin ]}
                    eventContent={fnEventContent}
                    dateClick={handleOnDateClick}
                    eventClick={handleEventClick}
                />
            </React.Fragment>
        )
    }
}

export default CalendarWidget;