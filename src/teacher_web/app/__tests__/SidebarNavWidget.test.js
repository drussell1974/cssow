import React from "react";
import { MemoryRouter as Router } from "react-router-dom";
import ReactTestUtils, { act } from "react-dom/test-utils";

import { createContainer } from "../helpers/domManipulators";
import FakeApiService from "../helpers/FakeApiService";
import { spy, setUpSpy, cleanUpSpy } from "../helpers/jest.extend.spy";

import SidebarNavWidget, { SidebarNavWidgetItem, Mapper } from "../widgets/SidebarNavWidget";

describe("SidebarNavWidget", () => {
    
    let render, container;

    let schemesOfWork, lessons

    beforeEach(() => {
        (
            { render, container } = createContainer()
        ),
        schemesOfWork = FakeApiService.getSchemesOfWork();
        lessons = FakeApiService.getLessonEpisodes();
    })
    
    it("renders default component", () => {
        render(<SidebarNavWidget buttonText="scheme of work" />);
        
        expect(
            container.textContent
        ).toMatch("");
    })

    it("has toggle menu button", () => {
        render(
            <Router>
                <SidebarNavWidget buttonText="scheme of work" data={Mapper.TransformSchemesOfWork([schemesOfWork[0]])} />
            </Router>);
        
        let button = container.querySelector("button.navbar-toggler");

        expect(
            button.textContent
        ).toMatch("scheme of work")

        //type="button" 
        expect(
            button.getAttribute("type")
        ).toMatch("button")
        //data-toggle="collapse" 
        expect(
            button.getAttribute("data-toggle")
        ).toMatch("collapse")
        //data-target="#navbarResponsive" 
        expect(
            button.getAttribute("data-target")
        ).toMatch("#sidebarResponsive")
        //aria-controls="navbarResponsive" 
        expect(
            button.getAttribute("aria-controls")
        ).toMatch("sidebarResponsive")
        //aria-expanded="true" 
        expect(
            button.getAttribute("aria-expanded")
        ).toMatch("true")
        //aria-label="Toggle navigation"
        expect(
            button.getAttribute("aria-label")
        ).toMatch("Toggle navigation")
    })

    it("has single item", () => {
        render(
            <Router>
                <SidebarNavWidget data={Mapper.TransformSchemesOfWork([schemesOfWork[0]])} />
            </Router>);

        let list = container.querySelector("#sidebarResponsive ul.navbar-nav");

        expect(
            list.querySelectorAll(".nav-item")
        ).toHaveLength(1);
    })
    
    it("renders empty component if data is empty", () => {
        render(<SidebarNavWidget buttonText="scheme of work" data={[]} />);
        
        expect(
            container.textContent
        ).toEqual("");
    })

    it("has multiple schemesofwork", () => {
        render(
            <Router>
                <SidebarNavWidget data={Mapper.TransformSchemesOfWork(schemesOfWork)} />       
            </Router>);
            
        let list = container.querySelector("#sidebarResponsive ul.navbar-nav");
    
        expect(
            list.querySelectorAll(".nav-item")
        ).not.toBeNull();
    
        expect(
            list.querySelectorAll(".nav-item")
        ).toHaveLength(3);
    })
   
    it("has single schemesofwork", () => {
        render(
            <Router>
                <SidebarNavWidget data={Mapper.TransformSchemesOfWork([schemesOfWork[0]])} />       
            </Router>);
            
        let item = container.querySelector("#sidebarResponsive ul.navbar-nav");
    
        expect(
            item.querySelector(".nav-item .nav-link").textContent
        ).toEqual("Computing Key Stage 3");

        expect(
            item.querySelector(".nav-item .nav-link").getAttribute("href")
        ).toEqual("/schemeofwork/1/lessons");
    })

    it("has multiple lessons", () => {

        render(
            <Router>
                <SidebarNavWidget data={Mapper.TransformLessons(lessons)} />       
            </Router>);
            
        let list = container.querySelector("#sidebarResponsive ul.navbar-nav");

        expect(
            list.querySelectorAll(".nav-item")
        ).toHaveLength(12);
    })
    
    it("has single lessons", () => {

        render(
            <Router>
                <SidebarNavWidget data={Mapper.TransformLessons(lessons)} />       
            </Router>);
        
        let item = container.querySelector("#sidebarResponsive ul.navbar-nav");
        
        expect(
            item.querySelector(".nav-item .nav-link").textContent
        ).toEqual("Memory Lesson 1");

        expect(
            item.querySelector(".nav-item .nav-link").getAttribute("href")
        ).toEqual("/schemeofwork/76/lessons/397");
    })
})

describe("SidebarNavWidgetItem", () =>{
    let render, container;

    beforeEach(() => {
        (
            { render, container } = createContainer()
        )
    })
    
    it("renders empty component", () => {
        render(<SidebarNavWidgetItem />);
        
        expect(
            container.textContent
        ).toMatch("");
    })

    it("has displayName", () => {
        render(
            <Router>
                <SidebarNavWidgetItem displayName="Lorum" subName="x" to="/home" />
            </Router>);

        expect(
            container.querySelector("li.nav-item a.nav-link").textContent
        ).toMatch("Lorum");
    })

    it("has subName", () => {
        render(
            <Router>
                <SidebarNavWidgetItem displayName="Lorum" subName="ipsum" to="/home" />
            </Router>);

        expect(
            container.querySelector("li.nav-item a.nav-link .small").textContent
        ).toMatch("ipsum");
    })

    it("has url", () => {
        render(
            <Router>
                <SidebarNavWidgetItem displayName="Lorum" subName="ipsum" to="/schemeofwork/78" />
            </Router>);

        expect(
            container.querySelector("li.nav-item a.nav-link").getAttribute("href")
        ).toEqual("/schemeofwork/78");
    })
})

describe("SidebarNavWidget onItemClick", () => {
    let render, container;
    let schemesOfWork;
    
    beforeEach(() => {
        (
            {render, container} = createContainer()
        );
        schemesOfWork = FakeApiService.getSchemesOfWork();
        setUpSpy();
    })

    afterEach(() => {
        cleanUpSpy();
    })

    it("first link active", () => {
        // Act
        render(
            <Router>
                <SidebarNavWidget data={Mapper.TransformSchemesOfWork(schemesOfWork, 1)} />
            </Router>);
        
        // Assert
        expect(
            container.querySelector("#sidebarResponsive .navbar-nav .nav-item:first-child").getAttribute("class")
        ).toEqual("nav-item active");
        
        expect(
            container.querySelector("#sidebarResponsive .navbar-nav .nav-item:last-child").getAttribute("class")
        ).toEqual("nav-item ");
    })

    it("last link active", () => {
        // Act
        render(
            <Router>
                <SidebarNavWidget data={Mapper.TransformSchemesOfWork(schemesOfWork, 3)} />
            </Router>);
        
        // Assert
        expect(
            container.querySelector("#sidebarResponsive .navbar-nav .nav-item:first-child").getAttribute("class")
        ).toEqual("nav-item ");
        
        expect(
            container.querySelector("#sidebarResponsive .navbar-nav .nav-item:last-child").getAttribute("class")
        ).toEqual("nav-item active");
    })

    it("notify when first item clicked", async () => {
        // Arrange
        const itemClickSpy = spy();

        // Act
        render(
            <Router>
                <SidebarNavWidget data={Mapper.TransformSchemesOfWork(schemesOfWork, 1)} onItemClicked={itemClickSpy.fn} />
            </Router>
        )

        let item = container.querySelector("#sidebarResponsive .navbar-nav .nav-item:first-child .nav-link");
        
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
        ).toEqual(1);

    })
    
    it("notify when last item clicked", async () => {
        // Arrange
        const itemClickSpy = spy();

        // Act
        render(
            <Router>
                <SidebarNavWidget data={Mapper.TransformSchemesOfWork(schemesOfWork, 1)} onItemClicked={itemClickSpy.fn} />
            </Router>
        )

        let item = container.querySelector("#sidebarResponsive .navbar-nav .nav-item:last-child .nav-link");
        
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
        ).toEqual(3);

    })
})