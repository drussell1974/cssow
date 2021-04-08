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

    let onDateClick = () => {
        
    }

    let onChangeFilter = () => {

    }

    it('renders empty widget', () => {
        render(<CalendarWidget />);

        expect(
            container.textContent
        ).toMatch('');
    })

    it('renders events on calendar', () => {

        render(<CalendarWidget events={events} onDateClick={onDateClick} onChangeFilter={onChangeFilter} />);
        
        expect(
            container.querySelector('.fc-today-button').textContent
        ).toMatch('');
    })

    describe('renders filter control', () => {

        it('has all option', () => {
            
            render(<CalendarWidget events={events} onDateClick={onDateClick} onChangeFilter={onChangeFilter} />);
        
            expect(
                container.querySelector('#event_filter--control input').checked
            ).toEqual(false);

            expect(
                container.querySelector('#event_filter--control label').textContent
            ).toEqual('show all events');
        })
        
        describe('when filter changes', () => {
            
            const onChangeFilterSpy = jest.fn();

            beforeEach(() => {
                ({render, container, input, change } = createContainer());
            })

            it('notifies onChange', async () => {
                
                // arrange

                let original_checked_state = true;
                
                render(<CalendarWidget 
                    events={events} 
                    showAllDefault={original_checked_state}
                    onDateClick={onDateClick}
                    onChangeFilter={onChangeFilterSpy}
                />);
                
                // act
                
                await act(async () => {
                    change(
                        input('event_filter--toggle-show-all')
                    );
                })
                
                // assert 
                
                expect(onChangeFilterSpy).toHaveBeenCalled();

                expect(
                    container.querySelector('#event_filter--control input').checked
                ).toEqual(!original_checked_state); // should have changed the check state
            })
        })
    })
})