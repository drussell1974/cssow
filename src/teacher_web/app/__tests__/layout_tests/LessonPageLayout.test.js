import React from 'react';
import { MemoryRouter as Router } from 'react-router-dom';
import ReactTestUtils, { act } from 'react-dom/test-utils';

import { createContainer } from '../../helpers/domManipulators';
import { spy, setUpSpy, cleanUpSpy } from '../../helpers/jest.extend.spy';
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

    describe('LessonPageLayout Content', () => {
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
            ).toEqual('There are no learning objectives for this lesson.');
        })

        it('has content heading', () => {
            render(
                <Router>
                    <LessonPageLayout lesson={lesson} />
                </Router>);

            expect(
                getContentHeading().textContent
            ).toEqual('Components of the CPU');
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

    describe("LessonPageLayout Callback", () => {
        
        beforeEach(() => {
            (
                { render, container } = createContainer()
            ),
            lesson = FakeApiService.getLessonEpisode();
            lessons = FakeApiService.getLessonEpisodes();
            setUpSpy();
        })

        afterEach(() => {
            cleanUpSpy();
        })

        it('notify when first item clicked', async () => {
            // Arrange

            const itemClickSpy = spy();

            // Act
            render(
                <Router>
                    <LessonPageLayout lessons={lessons} onSidebarNavItemClicked={itemClickSpy.fn} />
                </Router>
            )

            let item = container.querySelector('#sidebarResponsive .navbar-nav .nav-item:first-child .nav-link');
            
            await act(async () => {
                ReactTestUtils.Simulate.click(item);
            });

            // Assert: check item has been clicked...

            expect(
                itemClickSpy
            ).toHaveBeenCalled();

            // ... and returned id value
            expect(
            itemClickSpy.receivedArgument(0)
            ).toEqual(397);
        })

        
        it('notify when last item clicked', async () => {
            // Arrange

            const itemClickSpy = spy();

            // Act
            render(
                <Router>
                    <LessonPageLayout lessons={lessons} onSidebarNavItemClicked={itemClickSpy.fn} />
                </Router>
            )

            let item = container.querySelector('#sidebarResponsive .navbar-nav .nav-item:last-child .nav-link');
            
            await act(async () => {
                ReactTestUtils.Simulate.click(item);
            });

            // Assert: check item has been clicked...

            expect(
                itemClickSpy
            ).toHaveBeenCalled();

            // ... and returned id value
            expect(
            itemClickSpy.receivedArgument(0)
            ).toEqual(408);
        })
        
    })

});