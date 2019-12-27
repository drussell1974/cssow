import React from "react";

import { createContainer } from "../helpers/domManipulators";
import FakeApiService from "../helpers/FakeApiService";
import pager from '../services/Pager';

import PaginationWidget from "../widgets/PaginationWidget";

describe("PaginationWidget", () => {
    let render, container;
    
    beforeEach(() => (
        { render, container} = createContainer()
    ))
    
    it("renders empty container", () => {
        // Act
        render(<PaginationWidget />);
        // Assert
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
            // Act
            render(<PaginationWidget />);
            // Assert
            expect(
                container.textContent
            ).toEqual("");
        })

        it("renders empty container when data items empty", () => {
            // Arrange
            pager.init([], 1);
            // Act
            render(<PaginationWidget uri="/schemeofwork/127/lessons" pager={pager} />);
            // Assert
            expect(
                container.textContent
            ).toEqual("");
        })
        
        it("renders empty container when number of data items is less than page size", () => {
            // Arrange
            pager.init([1,2], 3, 1);
            // Act
            render(<PaginationWidget uri="/schemeofwork/127/lessons" pager={pager} />);
            // Assert
            expect(
                container.textContent
            ).toEqual("");
        })

        it("renders empty container when number of data items is equal to page size", () => {
            // Arrange
            pager.init([1,2,3], 3, 1);
            // Act
            render(<PaginationWidget uri="/schemeofwork/127/lessons" pager={pager} />);
            // Assert
            expect(
                container.textContent
            ).toEqual("");
        })

        it("renders empty container if uri empty", () => {
            // Arrange
            pager.init(1);
            // Act
            render(<PaginationWidget uri="" pager={pager} />);
            // Assert
            expect(
                container.textContent
            ).toEqual("");
        })

        it("renders empty container if pager empty", () => {

            // Act
            render(<PaginationWidget uri="schemeofwork/127/lessons" />);

            // Assert
            expect(
                container.textContent
            ).toEqual("");
        })

        it("shows multiple pages for lessons (default pageSize)", () => {
            
            // Arramge
            pager.init(lessons);

            // Act
            render(<PaginationWidget uri="/schemeofwork/127/lessons" pager={pager} />);
            
            // Assert
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

            // Arrange
            pager.init(lessons, 4, 1);

            // Act
            render(<PaginationWidget uri="/schemeofwork/127/lessons" pager={pager} />);

            // Assert
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

            // Arrange
            pager.init(lessons, 5, 1);

            // Act
            render(<PaginationWidget uri="/schemeofwork/127/lessons" pager={pager} />);

            // Assert
            expect(
                container.querySelectorAll("ul.pagination li")
            ).toHaveLength(3);
            
            expect(
                container.textContent
            ).toEqual("123");
        })

        it("show 12 records over 2 pages (6 per page)", () => {
            
            // Arrange
            pager.init(lessons, 6, 1)

            // Act
            render(<PaginationWidget uri="/schemeofwork/127/lessons" pager={pager} />);

            // Assert
            expect(
                container.querySelectorAll("ul.pagination li")
            ).toHaveLength(2);

            expect(
                container.textContent
            ).toEqual("12");
        })
    })
})