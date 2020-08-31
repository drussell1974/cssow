import React from 'react';
import ReactDOM from 'react-dom';

import { createContainer } from '../helpers/domManipulators';
import { SpinnerWidget } from '../widgets/SpinnerWidget';

let show = false

describe('SpinnerWidget', () => {
    let render, container;
    
    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(<SpinnerWidget />);

        expect(
            container.textContent
        ).toEqual("");
    })

    it('renders empty if not explicitly loading', () => {

        let status = 0;

        render(<SpinnerWidget loading={status} />);

        expect(
            container.textContent
        ).toEqual("");
    })

    it('renders empty when loaded', () => {

        let status = 100;

        render(<SpinnerWidget loading={status} />);

        expect(
            container.textContent
        ).toEqual("");
    })

    it('renders empty while loading is false', () => {
        
        let status = 0;
        
        render(<SpinnerWidget loading={status} />);

        expect(
            container.textContent
        ).toEqual("");
    })

    it('renders spinner while loading', () => {
        
        let status = 70;

        render(<SpinnerWidget loading={status} />);

        expect(
            container.textContent
        ).toEqual("70%");
    })

})