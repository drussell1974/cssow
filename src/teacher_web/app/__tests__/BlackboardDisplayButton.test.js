import React from 'react';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import FakeApiService from '../helpers/FakeApiService';

import BlackbaordDisplayButton from '../widgets/BlackboardDisplayButton.js';
import BlackboardDisplayButton from '../widgets/BlackboardDisplayButton.js';

describe('BlackbaordDisplayButton', () => {
    let render, container;
    let lesson;

    beforeEach(() => {
            (
                { render, container} = createContainer()
            ),
            lesson = FakeApiService.getLessonEpisode();
        }
    )

    it('renders empty component', () => {
        render(
            <Router>
                <BlackbaordDisplayButton />
            </Router>);

        expect(
            container.textContent
        ).toEqual('');
    })
    
    it('renders empty component without lesson', () => {
        render(
            <Router>
                <BlackbaordDisplayButton lesson={undefined} />
            </Router>);

        expect(
            container.textContent
        ).toEqual('');
    })

    it('has blackboard display', () => {
        render(
            <Router>
                <BlackboardDisplayButton lesson={lesson} />
            </Router>)

        expect(
            container.querySelector('.blackboard #lnk-whiteboard_view').textContent
        ).toEqual('Blackboard display');

        expect(
            container.querySelector('.blackboard #lnk-whiteboard_view').getAttribute('class')
        ).toEqual('btn btn-dark');
        
        expect(
            container.querySelector('.blackboard #lnk-whiteboard_view').getAttribute('href')
        ).toEqual('/schemeofwork/99/lesson/1/whiteboard_view');
    })

    it('has lesson plan display', () => {
        render(<Router>
            <BlackboardDisplayButton lesson={lesson} />
        </Router>)

        expect(
            container.querySelector('.blackboard #lnk-lesson_plan').textContent
        ).toEqual('Lesson plan');
        
        expect(
            container.querySelector('.blackboard #lnk-lesson_plan').getAttribute('class')
        ).toEqual('btn btn-light');
        
        expect(
            container.querySelector('.blackboard #lnk-lesson_plan').getAttribute('href')
        ).toEqual('/schemeofwork/99/lesson/1/lesson-plan');
    })
})