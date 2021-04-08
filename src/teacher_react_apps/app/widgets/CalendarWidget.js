import React, { useState } from 'react';
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from "@fullcalendar/interaction";

const FilterCheckbox = ({onChange, showAllDefault, showWeekendsDefault}) => {

    const  [ showAllIsChecked, setShowAllIsChecked ] = useState(showAllDefault);
    const [ showWeekendsIsChecked, setShowWeekendsIsChecked ] = useState(showWeekendsDefault);

    const handleOnChangeShowAll = async e => {
        e.preventDefault();
        setShowAllIsChecked(!showAllIsChecked)
        onChange(e);
    };

    const handleOnChangeShowWeekends = async e => {
        e.preventDefault();
        setShowWeekendsIsChecked(!showWeekendsIsChecked)
        onChange(e);
    };

    return (
        <React.Fragment>
            <div  id="event_filter--control">
                <div className="form-check form-switch form-check-inline event_filter--all" >
                    <input className="form-check-input" type="checkbox" name="show_all" checked={showAllIsChecked} onChange={handleOnChangeShowAll} id="event_filter--all" />
                    <label className="form-check-label" htmlFor="event_filter--all">show all events</label>
                </div>
                <div className="form-check form-switch form-check-inline event_filter--weekend" >
                    <input className="form-check-input" type="checkbox" name="show_weekends" checked={showWeekendsIsChecked} onChange={handleOnChangeShowWeekends} id="event_filter--weekend" />
                    <label className="form-check-label" htmlFor="event_filter--weekend">show weekends</label>
                </div>
            </div>
        </React.Fragment>
    )
}

const CalendarWidget = ({events, onDateClick, onChangeFilter, showAllDefault=false, showWeekendsDefault=false}) => {

    const handleOnDateClick = async e => {
        onDateClick(e);
    };

    if (events === undefined) {
        return(<React.Fragment></React.Fragment>)
    } else {
        return (
            <React.Fragment>
                <FilterCheckbox 
                    onChange={onChangeFilter} 
                    showAllDefault={showAllDefault} 
                    showWeekendsDefault={showWeekendsDefault}
                />
                <FullCalendar
                    plugins={[ dayGridPlugin ]}
                    initialView="dayGridMonth"
                    weekends={showWeekendsDefault}
                    events={events}
                    plugins={[ dayGridPlugin, interactionPlugin ]}
                    dateClick={handleOnDateClick}
                />
            </React.Fragment>
        )
    }
}

export default CalendarWidget;