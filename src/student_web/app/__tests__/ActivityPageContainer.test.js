import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import { ActivityPageContainer } from '../pages/ActivityPage';

describe("ActivityPageContainer", () =>{
    let render, container;

    let socialmediadata = undefined;

    let schemesofwork = {
        id: 1,
        institute_id: 5,
        department_id: 2,
        name: "CPU Architecture",
        description: "CPU components: ALU, Control Unit, Registers and Buses",
    };

    let lesson = {
        id: 1,
        institute_id: 5,
        department_id: 2,
        title: "Types of CPU Architecture",
    };

    let resource = 
    {
        "id": 119,
        "title": "OCR AS and A Level Computer Science",
        "publisher": "PM Heathcote and RSU Heathcote, PG Online, 2016",
        "page_note": "The TCP/IP Protocol Stack - pages 122 - 123",
        "page_uri": "",
        "md_document_name": "The-TCP_IP-Protocol-Stack.md",
        "type_id": 10,
        "type_name": "Markdown",
        "type_icon": "fa-book",
        "lesson_id": 220,
        "course_id": 11,
        "last_accessed": "",
        "created": "2020-02-17T06:48:00",
        "created_by_id": 2,
        "created_by_name": " ",
        "published": 1,
        "is_expired": false
    
    }
    
     
    beforeEach(() => {
        (
            {render, container} = createContainer(container)
        )
    })

    it('renders empty model', () => {
        render(
            <MemoryRouter>
                <ActivityPageContainer />
            </MemoryRouter>);
        
        expect(container.textContent).toMatch('');
    })

    describe('has a banner', () => {
        
        it('with heading', () => {
            render(
                <MemoryRouter>
                    <ActivityPageContainer resource={resource} lesson={lesson} schemeofwork={schemesofwork} socialmediadata />
                </MemoryRouter>);

            expect(
                container.querySelector('section#banner .inner header h1').textContent
            ).toMatch('OCR AS and A Level Computer Science');
        })

        it('with description', () => {
            render(
                <MemoryRouter>
                    <ActivityPageContainer resource={resource} lesson={lesson} schemeofwork={schemesofwork} socialmediadata />
                </MemoryRouter>);

            expect(
                container.querySelector('section#banner .inner header p').textContent
            ).toMatch('The TCP/IP Protocol Stack - pages 122 - 123');
        })
    })

    describe('has breadcrumb', () => {

        it('with home link', () => {
            render(
                <MemoryRouter>
                    <ActivityPageContainer resource={resource} lesson={lesson} schemeofwork={schemesofwork} socialmediadata />
                </MemoryRouter>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(1) > a').textContent
            ).toEqual('Home');

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(1) a').getAttribute("href")
            ).toEqual('/');
        })


        it('with Course link', () => {
            render(
                <MemoryRouter>
                    <ActivityPageContainer resource={resource} lesson={lesson} schemeofwork={schemesofwork} socialmediadata />
                </MemoryRouter>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(2)').textContent
            ).toEqual('CPU Architecture');

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(2) > a').getAttribute("href")
            ).toEqual('/course/');
        })

        it('with Lesson link', () => {
            render(
                <MemoryRouter>
                    <ActivityPageContainer resource={resource} lesson={lesson} schemeofwork={schemesofwork} socialmediadata />
                </MemoryRouter>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(3)').textContent
            ).toEqual('Types of CPU Architecture');

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(3) > a').getAttribute("href")
            ).toEqual('/course/1/lesson/1');

        })

        it('with current page text only', () => {
            render(
                <MemoryRouter>
                    <ActivityPageContainer resource={resource} lesson={lesson} schemeofwork={schemesofwork} socialmediadata />
                </MemoryRouter>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(4)').textContent
            ).toEqual('OCR AS and A Level Computer Science');
        })
    })

    describe('has footer', () => {

        it('with scheme of work name as heading', () => {
            render(
                <MemoryRouter>
                    <ActivityPageContainer schemeofwork={schemesofwork} lesson={lesson} resource={resource} socialmediadata />
                </MemoryRouter>);

            expect(
                container.querySelector('footer#footer h2').textContent
            ).toMatch('CPU Architecture');
        })

        it('with scheme of work overview summary', () => {
            render(
                <MemoryRouter>
                    <ActivityPageContainer schemeofwork={schemesofwork} lesson={lesson} resource={resource} socialmedia />
                </MemoryRouter>);

            expect(
                container.querySelector('footer#footer p').textContent
            ).toMatch('CPU components: ALU, Control Unit, Registers and Buses');
        })
    })

    describe('has markdown widget', () => {
        
        it('with heading', () => {
            
            const markdown_html = "<h1>Test ActivityPageContainer displays markdown widget</h1>";

            render(
                <MemoryRouter>
                    <ActivityPageContainer schemeofwork={schemesofwork} lesson={lesson} resource={resource} markdown_html={markdown_html} socialmedia />
                </MemoryRouter>);

            expect(
                container.querySelector("#main .inner section.markdown h2").textContent
            ).toMatch('Activity');
        })

        it('with markdown-body', () => {
            
            const markdown_html = "<h1>Test ActivityPageContainer displays markdown widget</h1>";

            render(
                <MemoryRouter>
                    <ActivityPageContainer schemeofwork={schemesofwork} lesson={lesson} resource={resource} markdown_html={markdown_html} socialmedia />
                </MemoryRouter>);

            expect(
                container.querySelector("#main .inner section.markdown div.markdown-body").textContent
            ).toMatch('Test ActivityPageContainer displays markdown widget');
        })
    })
});


