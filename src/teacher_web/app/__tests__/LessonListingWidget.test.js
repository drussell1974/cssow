import React from 'react';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import FakeApiService from '../helpers/FakeApiService';

import { LessonListingWidget, LessonListingWidgetItem } from '../widgets/LessonListingWidget';

describe('LessonListingWidgetItem', () => {
    let render, container;

    let learningEpisode;

    beforeEach(()=> {
        (
            { render, container} = createContainer()
        ),
        learningEpisode = FakeApiService.getLessonEpisode()
    })
    
    it('renders empty component', () => {
        render(<Router>
            <LessonListingWidgetItem />
        </Router>);

        expect(
            container.textContent
        ).toEqual('');
    })

    it('has a title', () => {
        render(
        <Router>
            <LessonListingWidgetItem row={learningEpisode}/>
        </Router>);

        expect(
            container.querySelector('.post-preview a h2.post-title').textContent
        ).toEqual('Lesson 1 - Components of the CPU');
    })

    it('has a title link', () => {
        render(
        <Router>
            <LessonListingWidgetItem row={learningEpisode}/>
        </Router>);

        expect(
            container.querySelector('.post-preview a').getAttribute('href')
        ).toEqual('/schemeofwork/99/lessons/1');

        expect(
            container.querySelector('.post-preview a').getAttribute('name')
        ).toEqual('lesson1');
    })

    it('has a summary', () => {
        render(
        <Router>
            <LessonListingWidgetItem row={learningEpisode}/>
        </Router>);

        expect(
            container.querySelector('.post-preview a h3.post-subtitle').textContent
        ).toEqual('Program Counter, ALU, Cache');
    })

    it('has keyword badges', () => {
        render(
            <Router>
                <LessonListingWidgetItem row={learningEpisode} />
            </Router>
        )

        expect(
            container.querySelector('i.badge-info').textContent
        ).toEqual('Arithmetic Logic Unit (ALU)');

        expect(
            container.querySelector('i.badge-info:nth-child(3)').textContent
        ).toEqual('Cache');

        expect(
            container.querySelectorAll('i.badge-info')
        ).toHaveLength(3);
    })
})

describe('LessonListingWidget', () => {
    let render, container;

    let learningEpisodes;
    var Pager = require('../services/Pager.js');
    let pager;

    beforeEach(()=> {
        (
            { render, container} = createContainer()
        ),
        learningEpisodes = FakeApiService.getLessonEpisodes();
    })

    it('renders empty component', () => {
        render(<LessonListingWidget />);

        expect(
            container.textContent
        ).toEqual('');
    })

    it('renders alert if list empty', () => {
        pager = new Pager([]);

        render(<Router>
            <LessonListingWidget pager={pager} page={1} auth={true} />
        </Router>);

        expect(
            container.querySelector('div.alert span.small').textContent
        ).toEqual('There are no lessons for this scheme of work.');

        expect(
            container.querySelector('div.alert a.btn-warning').textContent
        ).toEqual('Click here to get started.');
        
        expect(
            container.querySelectorAll('.post-preview')
        ).toHaveLength(0);
    })

    it('has multiple items (default paging 10 per page)', () => {
        pager = new Pager(learningEpisodes);
        
        render(<Router>
            <LessonListingWidget pager={pager} page={1} auth={true} />
        </Router>)

        expect(
            container.querySelectorAll('.post-preview')
        ).toHaveLength(10);
        
        // TODO: Fix when show headings

        expect(
            container.querySelectorAll('.group-heading')
        ).toHaveLength(0);

        expect(
            container.querySelector('.paging-info').textContent
        ).toEqual('Showing page 1 of 2 (total records: 12)');
    })

    it('has paged items 1 of 3', () => {
        pager = new Pager(learningEpisodes, 4, 1);

        render(<Router>
            <LessonListingWidget pager={pager} page={1} auth={true} />
        </Router>)

        expect(
            container.querySelectorAll('.post-preview')
        ).toHaveLength(4);

        expect(
            container.querySelector('.post-preview h2.post-title').textContent
        ).toEqual('Lesson 1 - Memory')

        expect(
            container.querySelectorAll('.post-preview h2.post-title')[3].textContent
        ).toEqual('Lesson 4 - Types of software')
        
        expect(
            container.querySelector('.paging-info').textContent
        ).toEqual('Showing page 1 of 3 (total records: 12)');

        // TODO: Fix when show headings

        expect(
            container.querySelectorAll('.group-heading')
        ).toHaveLength(0);
    })

    
    it('has paged items 3 of 3', () => {
        pager = new Pager(learningEpisodes, 4, 3);

        render(
            <Router>
                <LessonListingWidget pager={pager} page = {3} auth={true} />
            </Router>)
        
        //TODO: fire event GetPagedData(3);

        expect(
            container.querySelectorAll('.post-preview')
        ).toHaveLength(4);

        expect(
            container.querySelector('.post-preview h2.post-title').textContent
        ).toEqual('Lesson 9 - Variables and constants')

        expect(
            container.querySelectorAll('.post-preview h2.post-title')[3].textContent
        ).toEqual("Lesson 12 - Logic and Truth Tables");
        
        // TODO: Fix when show headings

        expect(
            container.querySelectorAll('.group-heading')
        ).toHaveLength(0);
    })
})