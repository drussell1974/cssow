import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter as Router } from 'react-router-dom';
import { createContainer } from '../helpers/domManipulators';
import BreadcrumbWidget from '../widgets/BreadcrumbWidget';

let show = false

describe('SpinnerWidget', () => {
    let render, container;
    
    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(
            <Router>
                <BreadcrumbWidget />
            </Router>);

        expect(
            container.textContent
        ).toEqual("");
    })

    it('renders with current page only', () => {
        
        render(
            <Router>
                <BreadcrumbWidget activePageName="Resources" />
            </Router>
        );

        expect(
            container.querySelector("nav ul.breadcrumb li.active").textContent
        ).toEqual("Resources");
    })

    it('renders with single breadcrumb item', () => {
        
        let fake_breadcrumbItems = [{text:"Home", url:"/"}]

        render(
        <Router>
            <BreadcrumbWidget breadcrumbItems = {fake_breadcrumbItems} activePageName="Resources" />
        </Router>);

        // Home Link

        expect(
            container.querySelector("nav ul.breadcrumb li:nth-child(1)").textContent
        ).toEqual("Home");

        expect(
            container.querySelector("nav ul.breadcrumb li:nth-child(1) a").getAttribute("href")
        ).toEqual("/");

        // Active page

        expect(
            container.querySelector("nav ul.breadcrumb li.active").textContent
        ).toEqual("Resources");
    })

    it('renders with single breadcrumb item', () => {
        
        let fake_breadcrumbItems = [
            {text:"Home", url:"/"},
            {text:"Courses", url:"/courses/12"}
        ]

        render(
            <Router>
                <BreadcrumbWidget breadcrumbItems = {fake_breadcrumbItems} activePageName="Resources" />
            </Router>
        );

        // Home Link

        expect(
            container.querySelector("nav ul.breadcrumb li:nth-child(1)").textContent
        ).toEqual("Home");

        expect(
            container.querySelector("nav ul.breadcrumb li:nth-child(1) a").getAttribute("href")
        ).toEqual("/");

        // Active page

        expect(
            container.querySelector("nav ul.breadcrumb li:nth-child(2)").textContent
        ).toEqual("Courses");
        
        expect(
            container.querySelector("nav ul.breadcrumb li:nth-child(2) a").getAttribute("href")
        ).toEqual("/courses/12");

        expect(
            container.querySelector("nav ul.breadcrumb li.active").textContent
        ).toEqual("Resources");
    })
})