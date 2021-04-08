import React from 'react';
import ReactDOM from 'react-dom';
import ReactTestUtils, { act } from 'react-dom/test-utils';
import { createContainer, withEvent } from '../helpers/domManipulators';
import CalendarWidget from '../widgets/CalendarWidget';
import  'whatwg-fetch';
import  { 
    fetchResponseOK,
    fetchResponseNotOK,
    fetchResponseError, 
    requestBodyOf 
} from '../helpers/spyHelpers';

describe('CalendarWidget', () => {
    let render, 
    container, 
    //form, 
    field, 
    //labelFor,
    //element, 
    //elements, 
    change; 
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


    describe('filter events ', () => {

        beforeEach(() => {
            ({render, container, field, change } = createContainer());
            render(<CalendarWidget events={events} onDateClick={onDateClick} onChangeFilter={onChangeFilter} />);

        })

        it('has control', () => {    
            expect(
                container.querySelector('#event-filter').textContent
            ).toMatch('');
        })

        it('has all option', () => {
            expect(
                container.querySelector('#event_filter--all').getAttribute('checked')
            ).toEqual('false');

            expect(
                container.querySelector('#event-filter .form-check label').textContent
            ).toEqual('show all events');
        })
    })
    
    describe.skip('when filter changed', () => {
        
        const onChangeFilterSpy = jest.fn();
        
        it('notifies onChange', async () => {
            
            let fieldName = "event_filter";
            
            render(<CalendarWidget 
                events={events} 
                onDateClick={onDateClick}
                onChangeFilter={onChangeFilterSpy}
            />);
            
            act(() => {
                change(
                    field('event-filter', fieldName),
                    withEvent(fieldName, 'newValue')
                );
            })
            
            expect(onChangeFilterSpy).toHaveBeenCalled();
        })
    })
})