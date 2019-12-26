import React from "react";

import { createContainer } from "../helpers/domManipulators";
import FakeApiService from "../helpers/FakeApiService";

import PaginationWidget, { Mapper } from "../widgets/PaginationWidget";

describe("PaginationWidget", () => {
    let render, container;

    beforeEach(() => {
        (
            { render, container} = createContainer()
        )
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
            render(<PaginationWidget data={[]} uri="/schemeofwork/127/lessons" />);

            expect(
                container.textContent
            ).toEqual("");
        })
        
        it("renders empty container if uri empty", () => {
            render(<PaginationWidget data={[1,2,3,4]} uri="" pageSize={2} />);

            expect(
                container.textContent
            ).toEqual("");
        })

        it("shows a single page", () => {
            render(<PaginationWidget data={lessons.slice(0, 1)} uri="/schemeofwork/127/lessons" />);

            expect(
                container.querySelectorAll("ul.pagination li")
            ).toHaveLength(1);

            expect(
                container.textContent
            ).toEqual("1");

            expect(
                container.querySelector("ul.pagination li a").getAttribute("href")
            ).toEqual("/schemeofwork/127/lessons?page=1");
        })

        it("shows multiple pages for lessons (default pageSize)", () => {
            render(<PaginationWidget data={lessons} uri="/schemeofwork/127/lessons" />);
            
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
            render(<PaginationWidget data={lessons} uri="/schemeofwork/127/lessons" pageSize={4} />);

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
            render(<PaginationWidget data={lessons} uri="/schemeofwork/127/lessons" pageSize={5} />);

            expect(
                container.querySelectorAll("ul.pagination li")
            ).toHaveLength(3);
            
            expect(
                container.textContent
            ).toEqual("123");
        })

        it("show 12 records over 1 page (12 per page)", () => {
            render(<PaginationWidget data={lessons} uri="/schemeofwork/127/lessons" pageSize={12} />);

            expect(
                container.querySelectorAll("ul.pagination li")
            ).toHaveLength(1);

            expect(
                container.textContent
            ).toEqual("1");
        })

        it("show 12 records over 1 page (20 per page)", () => {
            render(<PaginationWidget data={lessons} uri="/schemeofwork/127/lessons" pageSize={20} />);

            expect(
                container.querySelectorAll("ul.pagination li")
            ).toHaveLength(1);

            expect(
                container.textContent
            ).toEqual("1");
        })
    })
})