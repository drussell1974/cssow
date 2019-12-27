import React from "react";
import { MemoryRouter as Router } from "react-router-dom";

import { createContainer } from "../../helpers/domManipulators";
import FakeApiService from "../../helpers/FakeApiService";

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

    beforeEach(() => {
        (
            { render, container } = createContainer()
        ),
        lessons = FakeApiService.getLessonEpisodes();
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
        
        schemesofwork = FakeApiService.getSchemesOfWork();
        
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