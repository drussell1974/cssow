import React, { useState } from 'react';
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from "@fullcalendar/interaction";

const CalendarWidget = ({events, onDateClick, onShowAllEventsChange, onShowWeekendChange, showAllEventsDefault=false, showWeekendsDefault=false}) => {

    const [ showAllIsChecked, setShowAllIsChecked ] = useState(showAllEventsDefault);
    const [ showWeekendsIsChecked, setShowWeekendsIsChecked ] = useState(showWeekendsDefault);

    const handleOnDateClick = async e => {
        onDateClick(e);
    };
    
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
                    initialView="dayGridMonth"
                    weekends={showWeekendsIsChecked}
                    events={events}
                    plugins={[ dayGridPlugin, interactionPlugin ]}
                    dateClick={handleOnDateClick}
                />
            </React.Fragment>
        )
    }
}

export default CalendarWidget;