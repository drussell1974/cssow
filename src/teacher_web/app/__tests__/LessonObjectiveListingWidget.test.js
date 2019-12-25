import React from 'react';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import FakeApiService from '../helpers/FakeApiService';

import { LessonObjectiveListingWidget, LessonObjectiveListingWidgetItem } from '../widgets/LessonObjectiveListingWidget';

describe('LessonObjectiveListingWidgetItem', () => {
    let render, container;

    let learningObjective;

    beforeEach(()=> {
        (
            { render, container} = createContainer()
        ),
        learningObjective = FakeApiService.getLessonEpisode().learning_objectives[0];
    })
    
    it('renders empty component', () => {
        render(<Router>
            <LessonObjectiveListingWidgetItem />
        </Router>);

        expect(
            container.textContent
        ).toEqual('');
    })

    it('has a title', () => {
        render(
        <Router>
            <LessonObjectiveListingWidgetItem row={learningObjective}/>
        </Router>);

        expect(
            container.querySelector('.post-preview h2.post-title').textContent
        ).toMatch('Describe the function of the Arithmetic Logic Unit (ALU)');
    })

    it('has a summary', () => {
        render(
        <Router>
            <LessonObjectiveListingWidgetItem row={learningObjective}/>
        </Router>);

        expect(
            container.querySelector('.post-preview h3.post-subtitle').textContent
        ).toEqual('CPU');
    })

    it('has keyword badges', () => {
        render(
            <Router>
                <LessonObjectiveListingWidgetItem row={learningObjective} />
            </Router>
        )

        expect(
            container.querySelectorAll('i.badge-info')
        ).toHaveLength(2);
    })
})

describe('LessonObjectiveListingWidget', () => {
    let render, container;

    let lesson;

    beforeEach(()=> {
        (
            { render, container} = createContainer()
        ),
        lesson = FakeApiService.getLessonEpisode()
    })

    it('renders empty component', () => {
        render(<LessonObjectiveListingWidget />);

        expect(
            container.textContent
        ).toEqual('');
    })

    it('renders alert if list empty', () => {
        render(
            <Router>
                <LessonObjectiveListingWidget data={[]} auth={true} />
            </Router>);

        expect(
            container.querySelector('div.alert span.small').textContent
        ).toEqual('There are no learning objectives for this lesson.');

        expect(
            container.querySelector('div.alert a.btn-warning').textContent
        ).toEqual('Click here to get started.');
        
        expect(
            container.querySelectorAll('.post-preview')
        ).toHaveLength(0);
    })

    it('has multiple item', () => {
        render(
            <Router>
                <LessonObjectiveListingWidget data={lesson} auth={true} />
            </Router>)

        expect(
            container.querySelectorAll('.post-preview')
        ).toHaveLength(5);
        
        // TODO: Fix when show headings

        expect(
            container.querySelectorAll('.group-heading')
        ).toHaveLength(0);
    })
})