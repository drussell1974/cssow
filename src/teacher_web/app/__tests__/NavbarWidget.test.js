import React from 'react';

import { createContainer } from '../helpers/domManipulators';
import NavbarWidget from '../widgets/NavbarWidget';

describe('NavbarWidget', () => {
    
    let render, container;

    beforeEach(() => {
        (
            { render, container } = createContainer()
        )
    })
    
    it('renders default component', () => {
        render(<NavbarWidget />);
        
        expect(
            container.textContent
        ).toMatch('MenuHomeSchemes of WorkKey termsAbout');
    })

    it('has toggle menu button', () => {
        render(<NavbarWidget />);
        
        let button = container.querySelector('.navbar-toggler, .navbar-toggler-right');

        expect(
            button.textContent
        ).toMatch('Menu')

        //type="button" 
        expect(
            button.getAttribute('type')
        ).toMatch('button')
        //data-toggle="collapse" 
        expect(
            button.getAttribute('data-toggle')
        ).toMatch('collapse')
        //data-target="#navbarResponsive" 
        expect(
            button.getAttribute('data-target')
        ).toMatch('#navbarResponsive')
        //aria-controls="navbarResponsive" 
        expect(
            button.getAttribute('aria-controls')
        ).toMatch('navbarResponsive')
        //aria-expanded="false" 
        expect(
            button.getAttribute('aria-expanded')
        ).toMatch('false')
        //aria-label="Toggle navigation"
        expect(
            button.getAttribute('aria-label')
        ).toMatch('Toggle navigation')
    })

    it('has responsive menu', () => {
        render(<NavbarWidget />);

        expect(
            container.querySelector('#navbarResponsive').textContent
        ).toMatch('HomeSchemes of WorkKey termsAbout');

        expect(
            container.querySelector('.nav-item > a.home').textContent
        ).toMatch('Home')

        
        expect(
            container.querySelector('.nav-item > a.schemeofwork').textContent
        ).toMatch('Schemes of Work')

        
        expect(
            container.querySelector('.nav-item > a.keywords').textContent
        ).toMatch('Key terms')
        
        expect(
            container.querySelector('.nav-item > a.about').textContent
        ).toMatch('About')
    })
})