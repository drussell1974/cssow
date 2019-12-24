import React from 'react';
import { createContainer } from '../helpers/domManipulators';
import FakeApiService from '../helpers/FakeApiService';
import { MemoryRouter as Router } from 'react-router-dom';

import { LatestSchemesOfWorkJumbotronWidgetItem, LatestSchemesOfWorkJumbotronWidget } from '../widgets/LatestSchemesOfWorkJumbotronWidget';

describe('LatestSchemesOfWorkJumbotronWidgetItem', () => {
    let render, container;
    let schemeofwork;
    
    beforeEach(() => {
        (
            {render, container} = createContainer()
        )
        schemeofwork = FakeApiService.getSchemeOfWork();
    })

    it('renders empty container', () => {
        render(
            <Router>
                <LatestSchemesOfWorkJumbotronWidgetItem />
            </Router>);

        expect(
            container.textContent
        ).toMatch('');
    })

    it('has link to schemeofwork', () => {
        render(
            <Router>
                <LatestSchemesOfWorkJumbotronWidgetItem data={schemeofwork} />
            </Router>);

        expect(
            container.querySelector('.post-preview a').getAttribute('href')
        ).toMatch('/learningepisode/1');
    })

    it('has a title', () => {
        render(
            <Router>
                <LatestSchemesOfWorkJumbotronWidgetItem data={schemeofwork} />
            </Router>);

        expect(
            container.querySelector('.post-preview a h2.post-title').textContent
        ).toMatch('GCSE Computer Science');
    })

    it('has a subtitle for keystage', () => {
        render(
            <Router>
                <LatestSchemesOfWorkJumbotronWidgetItem data={schemeofwork} />
            </Router>);

        expect(
            container.querySelector('.post-preview a h3.post-subtitle').textContent
        ).toMatch('Key Stage 4');
    })

    it('has new label', () => {
        // explicitly change for testing
        schemeofwork.is_recent = true;
        
        render(
            <Router>
                <LatestSchemesOfWorkJumbotronWidgetItem data={schemeofwork} />
            </Router>);

        expect(
            container.querySelector('.post-preview a i').textContent
        ).toMatch('New');
    })

    it('hides new label', () => {
        // explicitly change for testing
        schemeofwork.is_recent = false;
        
        render(
            <Router>
                <LatestSchemesOfWorkJumbotronWidgetItem data={schemeofwork} />
            </Router>);

        expect(
            container.querySelector('.post-preview a i').textContent
        ).not.toMatch('New');
    })

    it('has created by', () => {
        render(
            <Router>
                <LatestSchemesOfWorkJumbotronWidgetItem data={schemeofwork} auth={false}/>
            </Router>);     

        expect(
            container.querySelector('.post-preview p.post-meta').textContent
        ).toMatch('Created by Dave Russell on 21st December 2019');
    })

    it('hides editable links if not authenticated', () => {
        render(
            <Router>
                <LatestSchemesOfWorkJumbotronWidgetItem data={schemeofwork} auth={false}/>
            </Router>);            

        expect(
            container.querySelector('.post-preview p.post-meta i.editable').getAttribute('style')
        ).toMatch('display: none');
    })

    it('show editable links if authenticated', () => {
        render(
            <Router>
                <LatestSchemesOfWorkJumbotronWidgetItem data={schemeofwork} auth={true}/>
            </Router>);        

        expect(
            container.querySelector('.post-preview p.post-meta').textContent
        ).toMatch('Created by Dave Russell on 21st December 2019 - Delete - Edit');

        expect(
            container.querySelector('.post-preview p.post-meta i.editable').getAttribute('style')
        ).toMatch('display: inline');
        
        expect(
            container.querySelector('.post-preview p.post-meta i.editable a.edit').getAttribute('href')
        ).toMatch('/schemeofwork/edit/1');
        
        expect(
            container.querySelector('.post-preview p.post-meta i.editable a.delete').getAttribute('href')
        ).toMatch('/schemeofwork/delete_item/1');
    })
})

describe('LatestSchemesOfWorkJumbotronWidget', () => {
    let render, container;
    let schemesofwork;

    beforeEach(() => {
        (
            {render, container} = createContainer()
        ),
        schemesofwork = FakeApiService.getSchemesOfWork();
    })

    it('renders empty container', () => {
        render(<LatestSchemesOfWorkJumbotronWidget />);

        expect(
            container.textContent
        ).toMatch('');
    })

    it('has heading', () => {
        render(<LatestSchemesOfWorkJumbotronWidget data={[]} />);

        expect(
            container.querySelector('section.jumbotron span.subheading').textContent
        ).toMatch('Latest Schemes of Work');
    })

    it('has show all button', () => {
        render(<LatestSchemesOfWorkJumbotronWidget data={[]} />);
        
        let button = container.querySelector('section.jumbotron #btn-all-schemes-of-work');

        expect(
            button.textContent
        ).toMatch('Show all →');

        expect(
            button.getAttribute('href')
        ).toMatch('/schemeofwork');
    })

    it('show a list of schemes of work', () => {
        render(
            <Router>
                <LatestSchemesOfWorkJumbotronWidget data={schemesofwork} />
            </Router>);

        expect(
            container.querySelectorAll('section.jumbotron .post-preview')
        ).toHaveLength(3);
    })
})