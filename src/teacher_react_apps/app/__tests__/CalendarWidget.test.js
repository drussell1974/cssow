import React from 'react';
import ReactDOM from 'react-dom';

import { createContainer } from '../helpers/domManipulators';
import CalendarWidget from '../widgets/NotificationWidget';

import  { 
    fetchResponseOK,
    fetchResponseNotOK,
    fetchResponseError, 
    requestBodyOf 
} from '../helpers/spyHelpers';

describe('CalendarWidget', () => {
    let render, container;

    beforeEach(() => {
        ({render, container} = createContainer());
    })

    let handleDateClick = () => {
        
    }

    it('renders empty widget', () => {
        render(<CalendarWidget />);

        expect(
            container.textContent
        ).toMatch('');
    })

    it('renders events on calendar', () => {
        
        let events= [
            { title: 'event 1', date: '2019-04-01' },
            { title: 'event 2', date: '2019-04-02' }
        ]

        render(<CalendarWidget events={events} handleDateClick={handleDateClick} />);
        
        expect(
            container.textContent
        ).toMatch('');
    })

    describe.skip('when item added', () => {
        
        beforeEach(() => {
            jest
                .spyOn(window, 'fetch')
                .mockReturnValue(fetchResponseOK({}));
        })
        
        afterEach(() => {
            //window.fetch.mockRestore(); // = originalFetch;
        })

        it('notifies onDelete', async () => {
            const notification = { id: 123 };
            window.fetch.mockReturnValue(fetchResponseOK(notification));
            
            const saveSpy = jest.fn(); //spy();
            
            render(<NotificationWidget 
                    { ...validClassCode } 
                    onClick={window.fetch} //.fn} 
                />);

            //await act(async () => {
            //    submit(form('frm-login-form'));
            //})
            
            expect(window.fetch).toHaveBeenCalled();
            //expect(saveSpy).toHaveBeenCalledWith(notification);
            //expect(saveSpy).toHaveBeenCalled();
        })
    })
})