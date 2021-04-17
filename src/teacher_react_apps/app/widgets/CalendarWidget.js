import React, { useState } from 'react';
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from "@fullcalendar/interaction";

const CalendarWidget = ({events, academicYear, ctx, onDateClick, onShowAllEventsChange, onShowWeekendChange, onAddScheduledLessonClick, showAllEvents=false, showWeekends=false}) => {

    const [ showAllIsChecked, setShowAllIsChecked ] = useState(showAllEvents);
    const [ showWeekendsIsChecked, setShowWeekendsIsChecked ] = useState(showWeekends);

    const handleOnDateClick = async e => {
        onDateClick(e);
    };

    const handleEventClick = async e => {
        // console.log(e);
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

    const handleOnAddScheduledLessonClick = async e => {
        onAddScheduledLessonClick(e);
    };

    const fnEventContent = (arg) => {
        // NOTE: #447 - TODO to prevent overlapping, set badge-event with css width:100%, remove col-12
        return { html: `<button class="${arg.event.extendedProps.button_class}" course: "${arg.event.extendedProps.course_name}" title="${arg.event.extendedProps.lesson_details}">${arg.event.title}</button>` }
    }
    
    const headerToolbar = {
        // TODO: #view options // left: 'dayGridMonth,timeGridWeek,timeGridDay custom1',
        left:  ctx !== undefined && ctx.schemeofwork_id > 0 ? 'add_scheduled_lesson' : '',
        center: 'title',
        right: 'today,prev,next' // see customButtons
    }

    const customButtons = {
        add_scheduled_lesson: {
            text: 'Add Event',
            click: handleOnAddScheduledLessonClick
          }
    }

    if (events === undefined) {
        return(<React.Fragment></React.Fragment>)
    } else {
        return (
            <React.Fragment>
                <div  id="event_filter--control">
                    <div className="form-check form-switch form-check-inline event_filter--all" >
                        <input className="form-check-input" type="checkbox" name="show_all" checked={showAllIsChecked} onChange={handleOnShowAllEventsChange} id="event_filter--all" />
                        <label className="form-check-label" htmlFor="event_filter--all">show all lessons</label>
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
                    headerToolbar={headerToolbar}  
                    customButtons={customButtons}
                />
            </React.Fragment>
        )
    }
}

export default CalendarWidget;