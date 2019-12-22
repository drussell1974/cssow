import React from 'react';

import { createContainer } from '../helpers/domManipulators';
import ContentHeadingWidget from '../widgets/ContentHeadingWidget';

describe('ContentHeadingWidget', () => {
    let render, container;

    beforeEach(() => (
        {render, container} = createContainer()
    ))

    it('renders empty container', () => {
        render(<ContentHeadingWidget />);

        expect(
            container.textContent
        ).toMatch('');
    })

    it('has main heading', () => {
        render(<ContentHeadingWidget main_heading='Test Main Heading' />);

        expect(
            container.querySelector('.alert h5.secondary-heading').textContent
        ).toMatch('Test Main Heading');
    })

    it('has sub heading', () => {
        render(<ContentHeadingWidget main_heading="TEST" sub_heading="Test Subheading"/>);

        expect(
            container.querySelector('.alert b').textContent
        ).toMatch('Test Subheading');
    })
    
    it('has strapline', () => {
        render(<ContentHeadingWidget main_heading="TEST" strap_line="Lorum ipsum"/>);

        expect(
            container.querySelector('.alert p.lead').textContent
        ).toMatch('Lorum ipsum');
    })
})