import React from 'react';

import { createContainer } from '../helpers/domManipulators';
import FooterWidget from '../widgets/FooterWidget';

describe('FooterWidget', () => {
    
    let render, container;

    beforeEach(() => {
       ( { render, container } = createContainer())
    })

    it('renders default component', () => {
        render(<FooterWidget />);

        expect(
            container.textContent
        ).toMatch("Copyright' © Dave Russell ");
    })

    it('has list items', () => {
        render(<FooterWidget />);

        expect(
            container.querySelectorAll('li.list-inline-item')
        ).toHaveLength(2);
    })

    it('has copyright text', () => {
        render(<FooterWidget />);

        expect(
            container.querySelector('p.copyright').textContent
        ).toMatch("Copyright' © Dave Russell ");
    })
})