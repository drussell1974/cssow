import React from 'react';

import { createContainer } from '../helpers/domManipulators';
import BannerWidget from '../widgets/BannerWidget';

describe('BannerWidget', () => {
    let render, container;
    beforeEach(() => (
        { render, container} = createContainer()
    ))

    it('renders empty component', () =>{
        render(<BannerWidget />);
        
        expect(
            container.textContent
        ).toMatch('');
    })

    it('has a main heading', () =>{
        render(<BannerWidget main_heading='This is the main heading' />);    

        expect(
            container.querySelector('.site-heading h1').textContent
        ).toMatch('This is the main heading')
    })

    
    it('has a sub heading', () =>{
        render(<BannerWidget sub_heading='This is the sub heading' />);    

        expect(
            container.querySelector('.site-heading span.subheading').textContent
        ).toMatch('This is the sub heading')
    })
})