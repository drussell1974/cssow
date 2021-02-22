import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import { DepartmentPageContainer } from '../pages/DepartmentPage';

describe("DepartmentPageContainer", () =>{
    let render, container;

    let socialmediadata = undefined;

    let site = {
        name:"Dave Russell",
        description:"Eu hendrerit felis rhoncus vel. In hac habitasse"
    }

    let institute = {
        id: 1276711,
        name:"Lorem Ipsum",
        description:"Phasellus eu tincidunt sapien, ac laoreet dui. In hac habitasse platea dictumst. Ut molestie nibh nec hendrerit posuere."
    }

    let departments = [
        {
            id: 10976,
            name: "Geography",
            description: "Lorem ipsum dolor sit amet.",
            number_of_schemes_of_work: 0,
        },
        {
            id: 109127,
            name: "Computer Science",
            description: " ",
            number_of_schemes_of_work: 25,
        },
        {
            id: 10911,
            name: "English",
            description: "English department",
            number_of_schemes_of_work: 101,
        }
    ]
    
    beforeEach(() => {
        (
            {render, container} = createContainer(container)
        )
    })

    describe('renders empty model', () => {
        
        it('with no parameters', () => {
            render(<DepartmentPageContainer />);
            
            expect(container.textContent).toMatch('');
        })

        it('with no site', () => {
            render(<DepartmentPageContainer schemeofwork departments institute />);
            
            expect(container.textContent).toMatch('');
        })

        it('with no institute', () => {
            render(<DepartmentPageContainer schemeofwork departments site />);
            
            expect(container.textContent).toMatch('');
        })

        it('with no departments', () => {
            render(<DepartmentPageContainer schemeofwork institute={institute} site={site} />);
            
            expect(container.textContent).toMatch('');
        })
    })

    describe('has a banner', () => {
        
        it('with heading', () => {
            render(<Router><DepartmentPageContainer site={site} institute={institute} departments={departments} socialmediadata /></Router>);

            expect(
                container.querySelector('section#banner .inner header h1').textContent
            ).toMatch('Lorem Ipsum');
        })

        it('with description', () => {
            render(<Router><DepartmentPageContainer site={site} institute={institute} departments={departments} socialmediadata /></Router>);

            expect(
                container.querySelector('section#banner .inner header p').textContent
            ).toMatch('Phasellus eu tincidunt sapien, ac laoreet dui. In hac habitasse platea dictumst. Ut molestie nibh nec hendrerit posuere.');
        })
    })


    describe('has breadcrumb', () => {
        it('with home link', () => {
            render(
                <Router>
                    <DepartmentPageContainer departments={departments} institute={institute} site={site} socialmediadata />
                </Router>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(1)').textContent
            ).toEqual('Home');

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(1) > a').getAttribute("href")
            ).toEqual('/');
        })

        it('with institute link', () => {
            render(
                <Router>
                    <DepartmentPageContainer departments={departments} institute={institute} site={site} socialmediadata />
                </Router>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(2)').textContent
            ).toEqual('Lorem Ipsum');

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(2) > a').getAttribute("href")
            ).toEqual('/institute/');
        })

        it('with current page text', () => {
            render(<Router><DepartmentPageContainer departments={departments} institute={institute} site={site} socialmediadata /></Router>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(3)').textContent
            ).toEqual('Lorem Ipsum');
        })
    })

    describe('has footer', () => {

        it('with scheme of work name as heading', () => {
            render(<Router><DepartmentPageContainer departments={departments} institute={institute} site={site} socialmediadata /></Router>);

            expect(
                container.querySelector('footer#footer h2').textContent
            ).toMatch('Dave Russell');
        })

        it('with scheme of work overview summary', () => {
            render(<Router><DepartmentPageContainer departments={departments} institute={institute} site={site} socialmedia /></Router>);

            expect(
                container.querySelector('footer#footer p').textContent
            ).toMatch('Eu hendrerit felis rhoncus vel. In hac habitasse');
        })
    })

    describe('has department widget', () => {

        it('with departments', () => {
            render(<Router><DepartmentPageContainer departments={departments} institute={institute} site={site} socialmedia /></Router>);

            // Heading
            expect(
                container.querySelector("#main .inner h2").textContent
            ).toMatch('Departments');

            // First
            expect(
                container.querySelector("#main .inner div.departments > .box:nth-child(1) .inner label.label u").textContent
            ).toMatch("Department");

            expect(
                container.querySelector("#main .inner div.departments > .box:nth-child(1) .inner h3").textContent
            ).toMatch("Geography");

            // Last
            expect(
                container.querySelector("#main .inner div.departments > .box:nth-last-child(1) .inner label.label u").textContent
            ).toMatch("Department");

            expect(
                container.querySelector("#main .inner div.departments > .box:nth-last-child(1) .inner h3").textContent
            ).toMatch("English");

        })
    })
});


