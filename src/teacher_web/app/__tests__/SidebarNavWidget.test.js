import React from 'react';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import FakeApiService from '../helpers/FakeApiService';

import SidebarNavWidget, { SidebarNavWidgetItem } from '../widgets/SidebarNavWidget';

describe('SidebarNavWidget', () => {
    
    let render, container;

    let schemesOfWork

    beforeEach(() => {
        (
            { render, container } = createContainer()
        ),
        schemesOfWork = FakeApiService.getSchemesOfWork();
    })
    
    it('renders default component', () => {
        render(<SidebarNavWidget buttonText='scheme of work' />);
        
        expect(
            container.textContent
        ).toMatch('');
    })

    it('has toggle menu button', () => {
        render(<SidebarNavWidget buttonText='scheme of work' data={[0]} />);
        
        let button = container.querySelector('button.navbar-toggler');

        expect(
            button.textContent
        ).toMatch('scheme of work')

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
        ).toMatch('#sidebarResponsive')
        //aria-controls="navbarResponsive" 
        expect(
            button.getAttribute('aria-controls')
        ).toMatch('sidebarResponsive')
        //aria-expanded="true" 
        expect(
            button.getAttribute('aria-expanded')
        ).toMatch('true')
        //aria-label="Toggle navigation"
        expect(
            button.getAttribute('aria-label')
        ).toMatch('Toggle navigation')
    })

    it('has single item', () => {
        render(
            <Router>
                <SidebarNavWidget data={[schemesOfWork[0]]} />
            </Router>);

        let list = container.querySelector('#sidebarResponsive ul.navbar-nav');

        expect(
            list.querySelectorAll('.nav-item')
        ).toHaveLength(1);
    })

    it('has multiple items', () => {
        render(
            <Router>
                <SidebarNavWidget data={schemesOfWork} />       
            </Router>);
            
        let list = container.querySelector('#sidebarResponsive ul.navbar-nav');

        expect(
            list.querySelectorAll('.nav-item')
        ).toHaveLength(3);
    })

    it('renders empty component if data is empty', () => {
        render(<SidebarNavWidget buttonText='scheme of work' data={[]} />);
        
        expect(
            container.textContent
        ).toMatch('');
    })
})

describe('SidebarNavWidgetItem', () =>{
    let render, container;

    beforeEach(() => {
        (
            { render, container } = createContainer()
        )
    })
    
    it('renders empty component', () => {
        render(<SidebarNavWidgetItem />);
        
        expect(
            container.textContent
        ).toMatch('');
    })

    it('has displayName', () => {
        render(
            <Router>
                <SidebarNavWidgetItem displayName='Lorum' subName='x' />
            </Router>);

        expect(
            container.querySelector('li.nav-item a.nav-link').textContent
        ).toMatch('Lorum');
    })

    it('has subName', () => {
        render(
            <Router>
                <SidebarNavWidgetItem displayName='Lorum' subName="ipsum"/>
            </Router>);

        expect(
            container.querySelector('li.nav-item a.nav-link .small').textContent
        ).toMatch('ipsum');
    })

    it('has url', () => {
        render(
            <Router>
                <SidebarNavWidgetItem displayName='Lorum' subName="ipsum" to='/esconte' />
            </Router>);

        expect(
            container.querySelector('li.nav-item a.nav-link').getAttribute('href')
        ).toEqual('/esconte');
    })
})