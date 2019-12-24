import React from 'react';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import AdminButtonWidget from '../widgets/AdminButtonWidget';

describe('AdminButtonWidget', () => {
    let render, container;
    let button;
    
    beforeEach(() =>(
        { render, container } = createContainer()
    ))
    
    it('render empty component', () => {
        render(
            <Router>
                <AdminButtonWidget buttonText='' to={`/schemeofwork/edit/{${9999}`} />
            </Router>);

        expect(
            container.querySelector('a#btn-new')
        ).toBeNull();
    })

    it('render empty component if not authorised', () => {
        render(
            <Router>
                <AdminButtonWidget auth={false} to={`/schemeofwork/edit/{${9999}`}/>
            </Router>);

        expect(
            container.querySelector('a#btn-new')
        ).toBeNull();
    })

    it('shows new button if authorised', () => {
        render(
            <Router>
                <AdminButtonWidget buttonText='New' auth={true} to={`/schemeofwork/new/{${9999}`} />
            </Router>);

        expect(
            container.querySelector('a#btn-new').textContent
        ).toMatch('New');
        
        expect(
            container.querySelector('a#btn-new').getAttribute('class')
        ).toMatch('btn');
    })

    it('is aligned right', () => {
        render(
            <Router>
                <AdminButtonWidget buttonText='New' auth={true} to={`/schemeofwork/edit/{${9999}`} />
            </Router>);

        expect(
            container.querySelector('a#btn-new').getAttribute('class')
        ).toMatch('float-right');
    })

    it('is a warning button', () => {
        render(
            <Router>
                <AdminButtonWidget buttonText='New' auth={true} to={`/schemeofwork/edit/{${9999}`}/>
            </Router>);

        expect(
            container.querySelector('a#btn-new').getAttribute('class')
        ).toMatch('btn-warning');
    })
    
    it('has jump to', () => {
        render(
            <Router>
                <AdminButtonWidget buttonText='New' auth={true} to={`/schemeofwork/new/{${9999}`} />
            </Router>);

        expect(
            container.querySelector('a#btn-new').getAttribute('href')
        ).toMatch('/new');
    })
})