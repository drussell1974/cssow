import React, { useState } from 'react';
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from "@fullcalendar/interaction";

const FilterCheckbox = ({onChange, showAllDefault}) => {
    
    
    return (
        <React.Fragment>
            
        </React.Fragment>
    )
}

const CalendarWidget = ({events, onDateClick, onChangeFilter, showAllDefault=false}) => {

    const  [ isChecked, setIsChecked ] = useState(showAllDefault);

    const handleOnDateClick = async e => {
        onDateClick(e);
    };

    const handleOnChangeFilter = async e => {
    
        e.preventDefault();
        setIsChecked(!isChecked)
        onChangeFilter(e);
    };

    if (events === undefined) {
        return(<React.Fragment></React.Fragment>)
    } else {
        return (
            <React.Fragment>
                <FilterCheckbox showAllDefault={showAllDefault} onChange={handleOnChangeFilter} />
                <div id="event-filter">
                    <div className="form-check form-switch form-check-inline" >
                        <input className="form-check-input" type="checkbox" name="event_filter" checked={isChecked} onChange={handleOnChangeFilter} id="event_filter--all"/>
                        <label className="form-check-label" htmlFor="event_filter--all">show all events</label>
                    </div>
                </div>
                <FullCalendar
                    plugins={[ dayGridPlugin ]}
                    initialView="dayGridMonth"
                    weekends={true}
                    events={events}
                    plugins={[ dayGridPlugin, interactionPlugin ]}
                    dateClick={handleOnDateClick}
                />
            </React.Fragment>
        )
    }
}

export default CalendarWidget;