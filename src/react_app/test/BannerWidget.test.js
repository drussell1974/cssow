import React from 'react';
import ReactDOM from 'react-dom';

import BannerWidget from '../widgets/BannerWidget';

describe ('BannerWidget', () => {
    let container;

    beforeEach(() => {
        container = document.createElement('div');
    })

    it('renders empty model', () => {
        ReactDOM.render(<BannerWidget />, container);
        
        expect(container.textContent).toMatch('');
    })
    
    it('is a data-video images/banner section', () => {
        ReactDOM.render(<BannerWidget />, container);

        expect(
            container.querySelector('section#banner').getAttribute('data-video')
        ).toMatch('images/banner');
    })

    it('has an heading', () => {
        ReactDOM.render(<BannerWidget heading="CPU Architecture" />, container);

        expect(
            container.querySelector('section#banner .inner header h1').textContent
        ).toMatch('CPU Architecture');
    })

    it('has a summary', () => {
        ReactDOM.render(<BannerWidget summary='CPU components: ALU, Control Unit, Registers and Buses'/>, container);

        expect(
            container.querySelector('section#banner .inner header p').textContent
        ).toMatch('CPU components: ALU, Control Unit, Registers and Buses');
    })

    it('has a jump to #main link', () => {
        ReactDOM.render(<BannerWidget />, container);
        
        const elem = container.querySelector('section#banner .inner a.more');

        expect(
            elem.getAttribute('href')
        ).toMatch('#main');

        expect(
            elem.textContent
        ).toMatch('Learn More');
    })
})