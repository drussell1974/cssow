import React from "react";

import { createContainer } from "../helpers/domManipulators";
import FakeApiService from "../helpers/FakeApiService";

import PaginationWidget from "../widgets/PaginationWidget";

describe("PaginationWidget", () => {
    let render, container;
    let Pager;
    
    beforeEach(() => {
        (
            { render, container} = createContainer()
        ),
        Pager = require('../services/Pager.js');
    })
    
    it("renders empty container", () => {
        render(<PaginationWidget />);

        expect(
            container.textContent
        ).toMatch("");
    })

    describe("for Lessons", () => {
        
        let lessons;

        beforeEach(() => {
            (
                { render, container} = createContainer()
            ),
            lessons = FakeApiService.getLessonEpisodes();
        })

        it("renders empty container", () => {
            render(<PaginationWidget />);

            expect(
                container.textContent
            ).toEqual("");
        })

        it("renders empty container when data items empty", () => {
            render(<PaginationWidget uri="/schemeofwork/127/lessons" pager={new Pager([], 1)} />);

            expect(
                container.textContent
            ).toEqual("");
        })
        
        it("renders empty container when number of data items is less than page size", () => {
            render(<PaginationWidget uri="/schemeofwork/127/lessons" pager={new Pager([1,2], 3, 1)} />);

            expect(
                container.textContent
            ).toEqual("");
        })

        it("renders empty container when number of data items is equal to page size", () => {
            render(<PaginationWidget uri="/schemeofwork/127/lessons" pager={new Pager([1,2,3], 3, 1)} />);

            expect(
                container.textContent
            ).toEqual("");
        })

        it("renders empty container if uri empty", () => {
            render(<PaginationWidget uri="" pager={new Pager(1)} />);

            expect(
                container.textContent
            ).toEqual("");
        })

        it("renders empty container if pager empty", () => {
            render(<PaginationWidget uri="schemeofwork/127/lessons" />);

            expect(
                container.textContent
            ).toEqual("");
        })

        it("shows multiple pages for lessons (default pageSize)", () => {
            render(<PaginationWidget uri="/schemeofwork/127/lessons" pager={new Pager(lessons)} />);
            
            expect(
                container.querySelectorAll("ul.pagination li")
            ).toHaveLength(2);

            expect(
                container.textContent
            ).toEqual("12");

            expect(
                container.querySelector("ul.pagination li a").getAttribute("href")
            ).toEqual("/schemeofwork/127/lessons?page=1");

            expect(
                container.querySelector("ul.pagination li:last-child a").getAttribute("href")
            ).toEqual("/schemeofwork/127/lessons?page=2");
        })

        it("show 12 records over 3 pages (4 per page)", () => {
            render(<PaginationWidget uri="/schemeofwork/127/lessons" pager={new Pager(lessons, 4, 1)} />);

            expect(
                container.querySelectorAll("ul.pagination li")
            ).toHaveLength(3);
            
            expect(
                container.textContent
            ).toEqual("123");
            
            expect(
                container.querySelector("ul.pagination li a").getAttribute("href")
            ).toEqual("/schemeofwork/127/lessons?page=1");
            
            expect(
                container.querySelector("ul.pagination li:last-child a").getAttribute("href")
            ).toEqual("/schemeofwork/127/lessons?page=3");
        })

        
        it("show 12 records over 3 pages (5 per page)", () => {
            render(<PaginationWidget uri="/schemeofwork/127/lessons" pager={new Pager(lessons, 5, 1)} />);

            expect(
                container.querySelectorAll("ul.pagination li")
            ).toHaveLength(3);
            
            expect(
                container.textContent
            ).toEqual("123");
        })

        it("show 12 records over 2 pages (6 per page)", () => {
            render(<PaginationWidget uri="/schemeofwork/127/lessons" pager={new Pager(lessons, 6, 1)} />);

            expect(
                container.querySelectorAll("ul.pagination li")
            ).toHaveLength(2);

            expect(
                container.textContent
            ).toEqual("12");
        })
    })
})