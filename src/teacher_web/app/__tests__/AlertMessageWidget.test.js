import React from 'react';

import { createContainer } from '../helpers/domManipulators';
import AlertMessageWidget from '../widgets/AlertMessageWidget';

describe('AlertMessageWidget', () => {
    
    let render, container;

    beforeEach(() => (
         { render, container } = createContainer())
    )

    it('renders empty container', () => {
        render(<AlertMessageWidget />);

        expect(
            container.textContent
        ).toMatch('');
    })

    it('render empty container when message empty', () => {
        render(<AlertMessageWidget message='' />);

        expect(
            container.textContent
        ).toMatch('');
    })

    it('shows the message', () => {
        render(<AlertMessageWidget message='this is a warning' />);

        expect(
            container.querySelector('#alert').textContent
        ).toMatch('this is a warning');
    })

    it('has a close button', () => {
        render(<AlertMessageWidget message='this is a warning' />);

        let button = container.querySelector('#alert button.close');
           
        expect(
            button.textContent
        ).toMatch('');

        //type="button"
        expect(
            button.getAttribute('type')
        ).toMatch('button');

        //data-dismiss="alert"
        expect(
            button.getAttribute('data-dismiss')
        ).toMatch('alert');

        //aria-label="Close"
        expect(
            button.getAttribute('aria-label')
        ).toMatch('Close');
    })

    it('has x icon hidden by default', () => {
        render(<AlertMessageWidget message='this is an alert' />);

        //<span aria-hidden="true">&times;</span>
        expect(
            container.querySelector('#alert span').textContent
        ).toMatch('×');
        
        expect(
            container.querySelector('#alert span').getAttribute('aria-hidden')
        ).toMatch('true');
    })

    
})