import React from "react";
import { MemoryRouter as Router } from "react-router-dom";
import ReactTestUtils, { act} from 'react-dom/test-utils';

import { createContainer } from "../../helpers/domManipulators";
import FakeApiService from "../../helpers/FakeApiService";
import { spy, setUpSpy, cleanUpSpy } from '../../helpers/jest.extend.spy';

import { LessonsPageLayout } from "../../pages/Lessons";

describe("LessonsPageLayout", () => {

    let render, container;
    let schemeofwork, schemesofwork, lessons;

    const getContentHeading = function() {
        return container.querySelector("div.container > .col-lg-12, .col-md-14, .content-heading");
    }

    const getLeftColumm = function() {
        return container.querySelector("div.container > div.col-lg-4, div.col-md-4");
    }

    const getMainContent = function() {
        return container.querySelector("div.container > div.col-lg-8, div.col-md-10, div.mx-auto");
    }

    describe("LessonsPageLayout Content", () => {

        beforeEach(() => {
            (
                { render, container } = createContainer()
            ),
            lessons = FakeApiService.getLessonEpisodes();
            schemesofwork = FakeApiService.getSchemesOfWork();
        })

        it("renders empty content", () => {
            render(<LessonsPageLayout />);

            expect(
                getContentHeading().textContent
            ).toEqual("");

            expect(
                getLeftColumm().textContent
            ).toEqual("");

            expect(
                getMainContent().textContent
            ).toEqual("There are no lessons for this scheme of work.");
        })

        it("has content heading", () => {
            
            schemeofwork = FakeApiService.getSchemeOfWork();

            render(
                <Router>
                    <LessonsPageLayout schemeofwork={schemeofwork} />
                </Router>);

            expect(
                getContentHeading().textContent
            ).toEqual("GCSE Computer Science");
        })

        it("has pagination at top", () => {
            render(
                <Router>
                    <LessonsPageLayout lessons={lessons} />
                </Router>);

            expect(
                getMainContent().querySelectorAll(".pagination-top .pagination li")
            ).toHaveLength(2);
        })

        it("has pagination at bottom", () => {
            render(
                <Router>
                    <LessonsPageLayout lessons={lessons} />
                </Router>);

            expect(
                getMainContent().querySelectorAll(".pagination-bottom .pagination li")
            ).toHaveLength(2);
        })

        it("has two columns", () => {
            render(
                <Router>
                    <LessonsPageLayout schemesOfWork={[]} lessons={lessons} />
                </Router>);

            expect(
                getLeftColumm()
            ).not.toBeNull();

            expect(
                getMainContent()
            ).not.toBeNull();
        })

        it("has schemes of work in sidebar", () => {
            
            render(
                <Router>
                    <LessonsPageLayout schemesOfWork={schemesofwork} />
                </Router>);

            expect(
                getLeftColumm().querySelectorAll("ul > li.nav-item")
            ).toHaveLength(3);
        })

        it("has lessons in main content", () => {
            
            lessons = FakeApiService.getLessonEpisodes();
            
            render(
                <Router>
                    <LessonsPageLayout lessons={lessons} />
                </Router>);

            expect(
                getMainContent().querySelectorAll(".post-preview")
            ).toHaveLength(10);
        })
    })

    describe.skip("LessonsPageLayout Callback", () => {
        beforeEach(() => {
            (
                { render, container } = createContainer()
            ),
            lessons = FakeApiService.getLessonEpisodes();
            schemesofwork = FakeApiService.getSchemesOfWork();
            schemeofwork = FakeApiService.getSchemeOfWork();
            
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
                    <LessonsPageLayout schemesofwork={schemesofwork} onSidebarNavItemClicked={itemClickSpy.fn} />
                </Router>
            )
            
            let item = container.querySelector('#sidebarResponsive .navbar-nav .nav-item:first-child .nav-link');
            
            console.log(`item:${item}`);

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
                    <LessonsPageLayout schemeofwork={schemesofwork} onSidebarNavItemClicked={itemClickSpy.fn} />
                </Router>
            )
            
            let item =  container.querySelector('#sidebarResponsive .navbar-nav .nav-item:last-child .nav-link');
            
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