import React from 'react';
import ReactDOM from 'react-dom';

import { createContainer } from '../helpers/domManipulators';
import { ActivityPageContainer } from '../pages/ActivityPage';

describe("ActivityPageContainer", () =>{
    let render, container;

    let socialmediadata = undefined;

    let schemesofwork = {
        id: 1,
        name: "CPU Architecture",
        description: "CPU components: ALU, Control Unit, Registers and Buses",
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
        "scheme_of_work_id": 11,
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
        render(<ActivityPageContainer />);
        
        expect(container.textContent).toMatch('');
    })

    describe('has a banner', () => {
        
        it('with heading', () => {
            render(<ActivityPageContainer resource={resource} schemeofwork={schemesofwork} socialmediadata />);

            expect(
                container.querySelector('section#banner .inner header h1').textContent
            ).toMatch('OCR AS and A Level Computer Science');
        })

        it('with description', () => {
            render(<ActivityPageContainer resource={resource} schemeofwork={schemesofwork} socialmediadata />);

            expect(
                container.querySelector('section#banner .inner header p').textContent
            ).toMatch('The TCP/IP Protocol Stack - pages 122 - 123');
        })
    })

    describe('has footer', () => {

        it('with scheme of work name as heading', () => {
            render(<ActivityPageContainer schemeofwork={schemesofwork} resource={resource} socialmediadata />);

            expect(
                container.querySelector('footer#footer h2').textContent
            ).toMatch('CPU Architecture');
        })

        it('with scheme of work overview summary', () => {
            render(<ActivityPageContainer schemeofwork={schemesofwork} resource={resource} socialmedia />);

            expect(
                container.querySelector('footer#footer p').textContent
            ).toMatch('CPU components: ALU, Control Unit, Registers and Buses');
        })
    })

    describe('has markdown widget', () => {
        
        it('with heading', () => {
            
            const markdown_html = "<h1>Test ActivityPageContainer displays markdown widget</h1>";

            render(<ActivityPageContainer schemeofwork={schemesofwork} resource={resource} markdown_html={markdown_html} socialmedia />);

            expect(
                container.querySelector("#main .inner section.markdown h2").textContent
            ).toMatch('Activity');
        })

        it('with markdown-body', () => {
            
            const markdown_html = "<h1>Test ActivityPageContainer displays markdown widget</h1>";

            render(<ActivityPageContainer schemeofwork={schemesofwork} resource={resource} markdown_html={markdown_html} socialmedia />);

            expect(
                container.querySelector("#main .inner section.markdown div.markdown-body").textContent
            ).toMatch('Test ActivityPageContainer displays markdown widget');
        })
    })
});


