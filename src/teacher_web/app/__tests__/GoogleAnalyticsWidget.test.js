import React from 'react';
import ReactDOM from 'react-dom';

import { createContainer } from '../helpers/domManipulators';
import GoogleAnalyticsWidget from '../widgets/GoogleAnalyticsWidget';

describe('render GoogleAnalyticsWidget', () => {
    let container, render;

    beforeEach(() =>{
        (
            { render, container } = createContainer(container)
        )
    })

    it('renders empty component', () => {
        render(<GoogleAnalyticsWidget />);

        expect(
            container.textContent
        ).not.toMatch('analytics.initialize(ga);');
    })

    it('renders empty component', () => {
        render(<GoogleAnalyticsWidget trackingId='' />);

        expect(
            container.textContent
        ).not.toMatch('analytics.initialize(ga);');
    })

    it('renders ga code', () => {
        render(<GoogleAnalyticsWidget trackingId='abcdef123456' />);

        expect(
            container.querySelector('script').textContent
        ).toMatch('analytics.initialize(ga);');
    })
})