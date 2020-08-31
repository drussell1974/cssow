import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import { LessonPageContainer } from '../pages/LessonPage';

describe("LessonPageContainer", () =>{
    let render, container;

    let socialmediadata = undefined;

    let schemesofwork = {
        id: 1,
        name: "CPU Architecture",
        description: "CPU components: ALU, Control Unit, Registers and Buses",
    };

    let lesson = 
    {
        id: 1,
        title: "Curabitur id purus feugiat, porttitor.",
        summary: "In vitae arcu quis dolor porttitor bibendum in eu nisl. Etiam efficitur dictum elit a tempus. Etiam feugiat acrisus",
        image_url: "images/pic01.jpg",
        url: "https://youtu.be/s6zR2T9vn2a",
        key_words: [
            { id: 12, term: "Memory Data Register (MDR)"},
            { id: 7,  term: "Registers"},
            { id: 13, term: "Accumulator (ACC)"}
        ],
        learning_objectives: [
            {
                id: 462,
                description: "Describe the function of the Arithmetic Logic Unit (ALU)",
                notes: " ",
                scheme_of_work_name: "",
                solo_taxonomy_id: 2,
                solo_taxonomy_name: "Multistructural: Describe, List (give an account or give examples of)",
                solo_taxonomy_level: "B",
            },
            {
                id: 463,
                description: "Describe how the Control Unit manages the other CPU components",
                notes: " ",
                scheme_of_work_name: "",
                solo_taxonomy_id: 2,
                solo_taxonomy_name: "Multistructural: Describe, List (give an account or give examples of)",
                solo_taxonomy_level: "B",
            },
            {
                id: 464,
                description: "Explain how the different registers are used to store data and carry data over the buses",
                notes: " ",
                scheme_of_work_name: "",
                solo_taxonomy_id: 3,
                solo_taxonomy_name: "Relational: Explain, Compare, Justify and Give Reasons (evaluate or assess)",
                solo_taxonomy_level: "C",
            }
        ],
        resources: [
            {
                id: 4,
                type_id: 6,
                type_name: "Book",
                title: "OCR AS and A Level Computer Science",
                publisher: "PG Online",
                year_published: 2016,
                authors: "PM Heathcote and RSU Heathcote",
                uri: "",
                scheme_of_work_id: 11,
                last_accessed: "",
                created: "",
                created_by_id: 0,
                created_by_name: "",
                published: 1,
                page_id: null,
                page_note: "OCR A'Level CISC vs RISC",
                page_uri: "https://www.youtube.com/watch?v=BJpMmq9gQE8&list=PLCiOXwirraUBj7HtVHfNZsnwjyZQj97da&index=6",
                task_icon: "",
                image_url: "images/pic04.jpg",
            },
            {
                id: 7,
                type_id: 7,
                type_name: "Video",
                title: "A level: OCR Specification Order",
                publisher: "YouTube",
                year_published: 2019,
                authors: "Craig and Dave",
                uri: "https://www.youtube.com/playlist?list=PLCiOXwirraUBj7HtVHfNZsnwjyZQj97da",
                scheme_of_work_id: 11,
                last_accessed: "",
                created: "",
                created_by_id: 0,
                created_by_name: "",
                published: 1,
                page_id: null,
                page_note: "OCR A'Level von Neumann and Harvard",
                page_uri: "https://www.youtube.com/watch?v=4WFzOyUNkaM&list=PLCiOXwirraUBj7HtVHfNZsnwjyZQj97da&index=6&t=0s",
                task_icon: "",
                image_url: "images/pic07.jpg",
            },
            {
                id: 31,
                type_id: 10,
                type_name: "Markdown",
                title: "Coding Tech",
                publisher: "Dave Russell",
                md_document_name:"FromRESTToGraphQL.md",
                year_published: 2019,
                authors: "",
                uri: "",
                scheme_of_work_id: 11,
                last_accessed: "",
                created: "",
                created_by_id: 0,
                created_by_name: "",
                published: 1,
                page_id: null,
                page_note: "From REST To GraphQL",
                page_uri: "",
                task_icon: "",
                image_url: "images/pic30.jpg",
            },
        ]
    };
    
     
    beforeEach(() => {
        (
            {render, container} = createContainer(container)
        )
    })

    it('renders empty model', () => {
        render(<LessonPageContainer />);
        
        expect(container.textContent).toMatch('');
    })

    describe('has a banner', () => {
        
        it('with heading', () => {
            render(<Router><LessonPageContainer lesson={lesson} schemeofwork={schemesofwork} keywords={lesson.key_words} socialmediadata /></Router>);

            expect(
                container.querySelector('section#banner .inner header h1').textContent
            ).toMatch('Curabitur id purus feugiat, porttitor.');
        })

        it('with description', () => {
            render(<Router><LessonPageContainer lesson={lesson} schemeofwork={schemesofwork} keywords={lesson.key_words} socialmediadata /></Router>);

            expect(
                container.querySelector('section#banner .inner header p').textContent
            ).toMatch('In vitae arcu quis dolor porttitor bibendum in eu nisl. Etiam efficitur dictum elit a tempus. Etiam feugiat acrisus');
        })
    })


    describe('has breadcrumb', () => {

        it('with home link', () => {
            
            render(<Router><LessonPageContainer lesson={lesson} schemeofwork={schemesofwork} keywords={lesson.key_words} socialmediadata /></Router>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(1) > a').textContent
            ).toEqual('Home');

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(1) a').getAttribute("href")
            ).toEqual('/');
        })


        it('with Course link', () => {

            render(<Router><LessonPageContainer lesson={lesson} schemeofwork={schemesofwork} keywords={lesson.key_words} socialmediadata /></Router>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(2)').textContent
            ).toEqual('CPU Architecture');

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(2) > a').getAttribute("href")
            ).toEqual('/course/1');
        })

       it('with current page text only', () => {
            
            render(<Router><LessonPageContainer lesson={lesson} schemeofwork={schemesofwork} keywords={lesson.key_words} socialmediadata /></Router>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(3)').textContent
            ).toEqual('Curabitur id purus feugiat, porttitor.');
 
        })
    })
    
    describe('has footer', () => {

        it('with scheme of work name as heading', () => {
            render(<Router><LessonPageContainer schemeofwork={schemesofwork} lesson={lesson} keywords={lesson.key_words} socialmediadata /></Router>);

            expect(
                container.querySelector('footer#footer h2').textContent
            ).toMatch('CPU Architecture');
        })

        it('with scheme of work overview summary', () => {
            render(<Router><LessonPageContainer schemeofwork={schemesofwork} lesson={lesson} keywords={lesson.key_words} socialmedia /></Router>);

            expect(
                container.querySelector('footer#footer p').textContent
            ).toMatch('CPU components: ALU, Control Unit, Registers and Buses');
        })
    })

    describe('has lesson widget', () => {

        it('with lesson objectives', () => {
            
            render(<Router><LessonPageContainer schemeofwork={schemesofwork} lesson={lesson} keywords={lesson.key_words} socialmedia /></Router>);

            expect(
                container.querySelector("#main .inner section.objectives h2").textContent
            ).toMatch('Objectives');

            // First
            expect(
                container.querySelector("#main .inner section.objectives ul.objectives li:nth-child(1)").textContent
            ).toMatch("Describe the function of the Arithmetic Logic Unit (ALU)");

            // Last
            expect(
                container.querySelector("#main .inner section.objectives ul.objectives li:nth-last-child(1)").textContent
            ).toMatch("Explain how the different registers are used to store data and carry data over the buses");
        })


        it('with resources', () => {
            render(<Router><LessonPageContainer schemeofwork={schemesofwork} lesson={lesson} keywords={lesson.key_words} socialmedia /></Router>);

            // Heading
            expect(
                container.querySelector("#main .inner section.resources h2").textContent
            ).toMatch('Resources');

            // First
            expect(
                container.querySelector("#main .inner section.resources div.box:nth-child(1) .inner label u").textContent
            ).toMatch("Book")

            expect(
                container.querySelector("#main .inner section.resources div.box:nth-child(1) .inner p").textContent
            ).toMatch("OCR AS and A Level Computer Science")

            expect(
                container.querySelector("#main .inner section.resources div.box:nth-child(1) .inner a").textContent
            ).toMatch("View")

            expect(
                container.querySelector("#main .inner section.resources div.box:nth-child(1) .inner a").getAttribute("href")
            ).toMatch("https://www.youtube.com/watch?v=BJpMmq9gQE8&list=PLCiOXwirraUBj7HtVHfNZsnwjyZQj97da&index=6")


            // Last (Markdown)
            expect(
                container.querySelector("#main .inner section.resources div.box:nth-last-child(1) .inner label u").textContent
            ).toMatch("Markdown")

            expect(
                container.querySelector("#main .inner section.resources div.box:nth-last-child(1) .inner p").textContent
            ).toMatch("Coding Tech")

            expect(
                container.querySelector("#main .inner section.resources div.box:nth-last-child(1) .inner a").textContent
            ).toMatch("View")

            expect(
                container.querySelector("#main .inner section.resources div.box:nth-last-child(1) .inner a").getAttribute("href")
            ).toMatch("/lesson/1/activity/31/FromRESTToGraphQL.md/")
        })

        it('with keywords', () => {
            
            render(<Router><LessonPageContainer schemeofwork={schemesofwork} lesson={lesson} keywords={lesson.key_words} socialmedia /></Router>);

            // Heading
            expect(
                container.querySelector("#main .inner section.keywords h2").textContent
            ).toMatch("Keywords");
            
            // First
            expect(
                container.querySelector("#main .inner section.keywords ul.keywords li:nth-child(1)").textContent
            ).toMatch("Memory Data Register (MDR)");

            // Last
            expect(
                container.querySelector("#main .inner section.keywords ul.keywords li:nth-last-child(1)").textContent
            ).toMatch("Accumulator (ACC)");
        })
    })
});


