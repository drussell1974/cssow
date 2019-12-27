import React from "react";
import ReactTestUtils, {act} from 'react-dom/test-utils';

import { createContainer } from "../helpers/domManipulators";
import FakeApiService from "../helpers/FakeApiService";
import { spy, setUpSpy, cleanUpSpy } from '../helpers/jest.extend.spy';
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

describe("PaginationWidget Callback", () => {
    let render, container;
    
    beforeEach(() => {(
        { render, container} = createContainer(),
        setUpSpy()
    )})

    afterEach(() => {
        cleanUpSpy();
    })

    it('notify when first bookmark clicked', async () => {
        // Arrange
        const bookmarkSpy = spy();
        pager.init(["A","B","C","D","M","L","N","O","W","X","Y","Z"], 4, 1);
        
        // Act
        render(<PaginationWidget onBookmarkClicked={bookmarkSpy.fn} pager={pager} uri="lesson" />);

        const bookmark = container.querySelector('ul.pagination li:first-child div');
        
        await act(async () => {
            ReactTestUtils.Simulate.click(bookmark);
        });

        // Assert: callback triggered function
        expect(
            bookmarkSpy
        ).toHaveBeenCalled();
        
        // ... and returned page value
        expect(
            bookmarkSpy.receivedArgument(0)
        ).toEqual(1);
    })
    
    it('notify when last bookmark clicked', async () => {
        // Arrange
        const bookmarkSpy = spy();
        pager.init(["A","B","C","D","M","L","N","O","W","X","Y","Z"], 4);
        
        // Act
        render(<PaginationWidget onBookmarkClicked={bookmarkSpy.fn} pager={pager} uri="/lesson" />);

        const bookmark = container.querySelector('ul.pagination li:last-child div');
        
        await act(async () => {
            ReactTestUtils.Simulate.click(bookmark);
        });

        // Assert: callback triggered function
        expect(
            bookmarkSpy
        ).toHaveBeenCalled();
        
        // ... and returned page value
        expect(
            bookmarkSpy.receivedArgument(0)
        ).toEqual(3);
    })
})