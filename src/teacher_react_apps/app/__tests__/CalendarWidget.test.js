import React from 'react';
import ReactDOM from 'react-dom';

import { createContainer } from '../helpers/domManipulators';
import CalendarWidget from '../widgets/NotificationWidget';

describe('NotificationWidget', () => {
    let render, container;

    beforeEach(() => {
        ({render, container} = createContainer());
    })

    let deleteMessageCallback = () => {
        
    }

    it('renders empty widget', () => {
        render(<CalendarWidget />);

        expect(
            container.textContent
        ).toMatch('');
    })

    it.skip('renders empty calendar', () => {
        
        let events=[
            {"date":"2021-04-06"}
        ]
        
        render(<CalendarWidget events={events} />);

        expect(
            container.querySelector('#calendar .title').textContent
        ).toMatch('xxx');
    })
})