import React from 'react';
import ReactDOM from 'react-dom';
import ReactTestUtils, { act } from 'react-dom/test-utils';
import { createContainer, withEvent } from '../helpers/domManipulators';
import CalendarWidget from '../widgets/CalendarWidget';
import  'whatwg-fetch';

describe('CalendarWidget', () => {
    let render, 
    container, 
    //form, 
    //
    field, 
    input,
    //labelFor,
    //element, 
    //elements, 
    change, 
    click;
    //submit;

    let events= [
        { title: 'event 1', date: '2019-04-01' },
        { title: 'event 2', date: '2019-04-02' }
    ]

    beforeEach(() => {
        ({render, container} = createContainer());
    })

    let handleDateClick = () => {
        
    }

    let handleShowAllEventsChange = () => {

    }

    let handleShowWeekendChange = () => {

    }

    it('renders empty widget', () => {
        render(<CalendarWidget />);

        expect(
            container.textContent
        ).toMatch('');
    })

    it('renders events on calendar', () => {

        render(<CalendarWidget 
            events={events}
            onDateClick={handleDateClick}
            onShowAllEventsChange={handleShowAllEventsChange}
            onShowWeekendChange={handleShowWeekendChange}
        />);
        
        expect(
            container.querySelector('.fc-today-button').textContent
        ).toMatch('');
    })

    describe('renders filter control', () => {
        describe('renders filter show all events', () => {
    
            it('has show all option', () => {
                
                render(<CalendarWidget 
                    events={events} 
                    onDateClick={handleDateClick} 
                    onShowAllEventsChange={handleShowAllEventsChange} 
                    onShowWeekendChange={handleShowWeekendChange}
                />);
            
                expect(
                    container.querySelector('#event_filter--control .event_filter--all input').checked
                ).toEqual(false);

                expect(
                    container.querySelector('#event_filter--control .event_filter--all label').textContent
                ).toEqual('show all events');
            })
            
            describe('when filter changes', () => {
                
                const onShowAllEventsChangeSpy = jest.fn();

                beforeEach(() => {
                    ({render, container, input, change } = createContainer());
                })

                it('notifies onChange', async () => {
                    
                    // arrange

                    let original_checked_state = true;
                    
                    render(<CalendarWidget 
                        events={events} 
                        showAllEventsDefault={original_checked_state}
                        showWeekendsDefault={false}
                        onDateClick={handleDateClick}
                        onShowAllEventsChange={onShowAllEventsChangeSpy}
                        onShowWeekendChange={handleShowWeekendChange}
                    />);
                    
                    // act
                    
                    await act(async () => {
                        change(
                            input('event_filter--all')
                        );
                    })
                    
                    // assert 
                    
                    expect(onShowAllEventsChangeSpy).toHaveBeenCalled();

                    expect(
                        container.querySelector('#event_filter--control .event_filter--all input').checked
                    ).toEqual(!original_checked_state); // should have changed the check state
                })
            })
        })

        describe('renders filter show weekend', () => {

            it('has show all option', () => {
                
                render(<CalendarWidget 
                    events={events} 
                    onDateClick={handleDateClick}
                    onShowAllEventsChange={handleShowAllEventsChange}
                    onShowWeekendChange={handleShowWeekendChange}
                />);
            
                expect(
                    container.querySelector('#event_filter--control .event_filter--weekend input').checked
                ).toEqual(false);

                expect(
                    container.querySelector('#event_filter--control .event_filter--weekend label').textContent
                ).toEqual('show weekends');
            })
            

            describe('when filter changes', () => {
                
                const onShowWeekendChangeSpy = jest.fn();

                beforeEach(() => {
                    ({render, container, input, change } = createContainer());
                })

                it('notifies onChange', async () => {
                    
                    // arrange

                    let original_checked_state = true;
                    
                    render(<CalendarWidget 
                        events={events} 
                        showAllEventsDefault={false}
                        showWeekendsDefault={original_checked_state}
                        onDateClick={handleDateClick}
                        onShowAllEventsChange={handleShowAllEventsChange}
                        onShowWeekendChange={onShowWeekendChangeSpy}
                    />);
                    
                    // act
                    
                    await act(async () => {
                        change(
                            input('event_filter--weekend')
                        );
                    })
                    
                    // assert 
                    
                    expect(onShowWeekendChangeSpy).toHaveBeenCalled();

                    expect(
                        container.querySelector('#event_filter--control .event_filter--weekend input').checked
                    ).toEqual(!original_checked_state); // should have changed the check state
                })
            })
        })
    })
})