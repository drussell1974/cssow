import React, { useState } from 'react';
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from "@fullcalendar/interaction";

const FilterCheckbox = ({onChange, showAllDefault}) => {

    const  [ isChecked, setIsChecked ] = useState(showAllDefault);

    const handleOnChangeFilter = async e => {
        e.preventDefault();
        setIsChecked(!isChecked)
        onChange(e);
    };

    return (
        <React.Fragment>
            <div  id="event_filter--control">
                <div className="form-check form-switch form-check-inline" >
                    <input className="form-check-input" type="checkbox" name="show_all" checked={isChecked} onChange={handleOnChangeFilter} id="event_filter--toggle-show-all" />
                    <label className="form-check-label" htmlFor="event_filter--all">show all events</label>
                </div>
            </div>
        </React.Fragment>
    )
}

const CalendarWidget = ({events, onDateClick, onChangeFilter, showAllDefault=false}) => {

    const handleOnDateClick = async e => {
        onDateClick(e);
    };

    if (events === undefined) {
        return(<React.Fragment></React.Fragment>)
    } else {
        return (
            <React.Fragment>
                <FilterCheckbox onChange={onChangeFilter} showAllDefault={showAllDefault} />
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