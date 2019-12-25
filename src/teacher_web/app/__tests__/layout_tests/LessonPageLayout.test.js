import React from 'react';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../../helpers/domManipulators';
import FakeApiService from '../../helpers/FakeApiService';

import Lesson, { LessonPageLayout } from '../../pages/Lesson';

describe('LessonPageLayout', () => {
    let render, container;
    let lesson, lessons;

    const getContentHeading = function() {
        return container.querySelector("div.container > .col-lg-12, .col-md-14, .content-heading");
    }

    const getLeftColumm = function() {
        return container.querySelector("div.container > div.col-lg-4, div.col-md-4");
    }

    const getMainContent = function() {
        return container.querySelector("div.container > div.col-lg-8, div.col-md-10, div.mx-auto");
    }

    beforeEach(() => {
        (
            { render, container } = createContainer()
        ),
        lesson = FakeApiService.getLessonEpisode();
        lessons = FakeApiService.getLessonEpisodes();
    })

    it('renders empty content', () => {
        render(
            <Router>
                <LessonPageLayout />
            </Router>);

        expect(
            getContentHeading().textContent
        ).toEqual('');

        expect(
            getLeftColumm().textContent
        ).toEqual('');

        expect(
            getMainContent().textContent
        ).toEqual('');
    })

    it('has blackboard display buttons', () => {
        render(
            <Router>
                <LessonPageLayout lesson={lesson} />
            </Router>)

        expect(
            getLeftColumm().querySelector('.blackboard')
        ).not.toBeNull();
    })

    it('has sideNav', () => {
        render(
            <Router>
                <LessonPageLayout lessons={lessons} />
            </Router>);
            
        expect(
            getLeftColumm().querySelector('#sidebarNav')
        ).not.toBeNull();
    })

    it('has pagination', () => {
        render(
            <Router>
                <LessonPageLayout lessons={lessons} />
            </Router>);
        
        expect(
            getMainContent().querySelectorAll('.pagination')
        ).toHaveLength(2);
    })

    it('has lesson objectives listing', () => {
        render(
            <Router>
                <LessonPageLayout lessons={lessons} />
            </Router>);

        expect(
            getMainContent().querySelectorAll('.post-preview')
        ).toHaveLength(0);
    })
})