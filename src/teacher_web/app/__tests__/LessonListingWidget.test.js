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
        ).toEqual('/lesson/1/learningobjective');

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
})

describe('LessonListingWidget', () => {
    let render, container;

    let learningEpisodes;

    beforeEach(()=> {
        (
            { render, container} = createContainer()
        ),
        learningEpisodes = FakeApiService.getLessonEpisodes()
    })

    it('renders empty component', () => {
        render(<LessonListingWidget />);

        expect(
            container.textContent
        ).toEqual('');
    })

    it('renders alert if list empty', () => {
        render(<Router>
            <LessonListingWidget data={[]} auth={true} />
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

    it('has multiple item', () => {
        render(<Router>
            <LessonListingWidget data={learningEpisodes} auth={true} />
        </Router>)

        expect(
            container.querySelectorAll('.post-preview')
        ).toHaveLength(4);
        
        // TODO: Fix when show headings

        expect(
            container.querySelectorAll('.group-heading')
        ).toHaveLength(0);
    })
})