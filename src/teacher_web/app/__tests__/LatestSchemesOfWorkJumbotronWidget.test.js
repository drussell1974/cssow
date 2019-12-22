import React from 'react';
import { createContainer } from '../helpers/domManipulators';
import FakeApiService from '../helpers/FakeApiService';

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
        render(<LatestSchemesOfWorkJumbotronWidgetItem />);

        expect(
            container.textContent
        ).toMatch('');
    })

    it('has link to schemeofwork', () => {
        render(<LatestSchemesOfWorkJumbotronWidgetItem data={schemeofwork} />);

        expect(
            container.querySelector('.post-preview a').getAttribute('href')
        ).toMatch('/learningepisode/1');
    })

    it('has a title', () => {
        render(<LatestSchemesOfWorkJumbotronWidgetItem data={schemeofwork} />);

        expect(
            container.querySelector('.post-preview a h2.post-title').textContent
        ).toMatch('GCSE Computer Science');
    })

    it('has a subtitle for keystage', () => {
        render(<LatestSchemesOfWorkJumbotronWidgetItem data={schemeofwork} />);

        expect(
            container.querySelector('.post-preview a h3.post-subtitle').textContent
        ).toMatch('Key Stage 3');
    })

    it('has new label', () => {
        // explicitly change for testing
        schemeofwork.is_recent = true;
        
        render(<LatestSchemesOfWorkJumbotronWidgetItem data={schemeofwork} />);

        expect(
            container.querySelector('.post-preview a i').textContent
        ).toMatch('New');
    })

    it('hides new label', () => {
        // explicitly change for testing
        schemeofwork.is_recent = false;
        
        render(<LatestSchemesOfWorkJumbotronWidgetItem data={schemeofwork} />);

        expect(
            container.querySelector('.post-preview a i').textContent
        ).not.toMatch('New');
    })

    it('has created by', () => {
        render(<LatestSchemesOfWorkJumbotronWidgetItem data={schemeofwork} auth={false} />);

        expect(
            container.querySelector('.post-preview p.post-meta').textContent
        ).toMatch('Created by Dave Russell on 22nd December 2019');
    })

    it('hides editable links if not authenticated', () => {
        render(<LatestSchemesOfWorkJumbotronWidgetItem data={schemeofwork} auth={false} />);        

        expect(
            container.querySelector('.post-preview p.post-meta i.editable').getAttribute('style')
        ).toMatch('display: none');
    })

    it('show editable links if authenticated', () => {
        render(<LatestSchemesOfWorkJumbotronWidgetItem data={schemeofwork} auth={true}/>);        

        expect(
            container.querySelector('.post-preview p.post-meta').textContent
        ).toMatch('Created by Dave Russell on 22nd December 2019 - Delete - Edit');

        expect(
            container.querySelector('.post-preview p.post-meta i.editable').getAttribute('style')
        ).toMatch('display: inline');
        
        expect(
            container.querySelector('.post-preview p.post-meta i.editable a.edit').getAttribute('href')
        ).toMatch('/schemesofwork/edit/1');
        
        expect(
            container.querySelector('.post-preview p.post-meta i.editable a.delete').getAttribute('href')
        ).toMatch('/schemesofwork/delete_item/1');
    })
})

describe('LatestSchemesOfWorkJumbotronWidget', () => {
    let render, container;

    beforeEach(() => (
        {render, container} = createContainer()
    ))

    it('renders empty container', () => {
        render(<LatestSchemesOfWorkJumbotronWidget />);

        expect(
            container.textContent
        ).toMatch('');
    })
})