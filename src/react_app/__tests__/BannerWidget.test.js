import React from 'react';
import ReactDOM from 'react-dom';

import { createContainer } from '../helpers/domManipulators';
import BannerWidget from '../widgets/BannerWidget';
    
describe ('BannerWidget', () => {
    let render, container;
    let schemesofwork = {
        id: 1,
        name: "CPU Architecture",
        description: "CPU components: ALU, Control Unit, Registers and Buses",
    };
    
     
    beforeEach(() => {
        (
            {render, container} = createContainer(container)
        )
    })

    it('renders empty model', () => {
        render(<BannerWidget />);
        
        expect(container.textContent).toMatch('');
    })
    
    it('is a data-video images/banner section', () => {
        render(<BannerWidget data={schemesofwork} />);

        expect(
            container.querySelector('section#banner').getAttribute('data-video')
        ).toMatch('images/banner');
    })

    it('has a heading', () => {
        render(<BannerWidget data={schemesofwork} />);

        expect(
            container.querySelector('section#banner .inner header h1').textContent
        ).toMatch('CPU Architecture');
    })

    it('has a summary', () => {
        render(<BannerWidget data={schemesofwork} />);

        expect(
            container.querySelector('section#banner .inner header p').textContent
        ).toMatch('CPU components: ALU, Control Unit, Registers and Buses');
    })

    it('has a jump to #main link', () => {
        render(<BannerWidget data={schemesofwork} />);
        
        const elem = container.querySelector('section#banner .inner a.more');

        expect(
            elem.getAttribute('href')
        ).toMatch('#main');

        expect(
            elem.textContent
        ).toMatch('Learn More');
    })
})