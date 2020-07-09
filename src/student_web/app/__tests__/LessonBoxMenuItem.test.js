import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter as Router } from 'react-router-dom';

import { LessonBoxMenuWidget, LessonBoxMenuExternalLinkItem, LessonBoxMenuMarkdownPageLinkItem } from '../widgets/LessonBoxMenuWidget';
import { createContainer } from '../helpers/domManipulators';

let lesson = {
    id: 123,
    title: "Curabitur id purus feugiat, porttitor.",
    summary: "In vitae arcu quis dolor porttitor bibendum in eu nisl. Etiam efficitur dictum elit a tempus. Etiam feugiat acrisus",
    image_url: "images/pic01.jpg",
    url: "https://youtu.be/s6zR2T9vn2a",
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
        page_note: "",
        page_uri: "",
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
        page_note: "OCR A'Level Multicore and parallel systems",
        page_uri: "https://www.youtube.com/watch?v=CntADU-4_Gw&list=PLCiOXwirraUBj7HtVHfNZsnwjyZQj97da&index=9&t=0s",
        task_icon: "",
        image_url: "images/pic07.jpg",
    },
    {
        id: 30,
        type_id: 7,
        type_name: "Video",
        title: "Coding Tech",
        publisher: "YouTube",
        year_published: 2019,
        authors: "",
        uri: "https://www.youtube.com/channel/UCtxCXg-UvSnTKPOzLH4wJaQ",
        scheme_of_work_id: 11,
        last_accessed: "",
        created: "",
        created_by_id: 0,
        created_by_name: "",
        published: 1,
        page_id: null,
        page_note: "From REST To GraphQL",
        page_uri: "https://www.youtube.com/watch?v=ntBU5UXGbM8",
        task_icon: "",
        image_url: "images/pic30.jpg",
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
}

describe ('LessonBoxMenuExternalLinkItem', () => {
    let render, container;
    
    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(<LessonBoxMenuExternalLinkItem />);

        expect(container.textContent).toMatch('');
    })

    it('has a link from image', () => {
        render(<LessonBoxMenuExternalLinkItem data={lesson.resources[1]} />);

        expect(
            container.querySelector('div.box a').getAttribute('href')
        ).toMatch('https://www.youtube.com/watch?v=CntADU-4_Gw&list=PLCiOXwirraUBj7HtVHfNZsnwjyZQj97da&index=9&t=0s');
    })

    it('has a image', () => {
        render(<LessonBoxMenuExternalLinkItem  data={lesson.resources[1]} />);

        expect(
            container.querySelector('div.box a img').getAttribute('src')
        ).toMatch('images/pic07.jpg');
    })

    it('has a title', () => {
        render(<LessonBoxMenuExternalLinkItem  data={lesson.resources[1]} />);

        expect(
            container.querySelector('div.inner h3').textContent
        ).toMatch('OCR A\'Level Multicore and parallel systems');
    })

    it('has a master heading', () => {
        render(<LessonBoxMenuExternalLinkItem  data={lesson.resources[1]} />);

        expect(
            container.querySelector('div.inner p').textContent
        ).toMatch('A level: OCR Specification Order');
    })

    it('has a view button', () => {
        render(<LessonBoxMenuExternalLinkItem data={lesson.resources[1]} typeButtonText='View'/>);

        expect(
            container.querySelector('div.inner a.button').textContent
        ).toMatch('View');

        expect(
            container.querySelector('div.inner a.button').getAttribute('href')
        ).toMatch('https://www.youtube.com/watch?v=CntADU-4_Gw&list=PLCiOXwirraUBj7HtVHfNZsnwjyZQj97da&index=9&t=0s');
    })

    it('has type label heading from reference type name', () => {
        render(<LessonBoxMenuExternalLinkItem data={lesson.resources[1]} />);

        expect(
            container.querySelector('div.inner label.label').textContent
        ).toMatch('Video');
    })
})


describe('LessonBoxMenuMarkdownPageLinkItem', () => {
    let render, container;

    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(<Router><LessonBoxMenuMarkdownPageLinkItem /></Router>);

        expect(container.textContent).toMatch('');
    })

    it('has a link from image', () => {
        render(<Router><LessonBoxMenuMarkdownPageLinkItem data={lesson.resources[3]} lesson={lesson} /></Router>);

        expect(
            container.querySelector('div.box a').getAttribute('href')
            ).toMatch('/Lesson/123/Activity/11/31/FromRESTToGraphQL.md');
    })

    it('has a image', () => {
        render(<Router><LessonBoxMenuMarkdownPageLinkItem  data={lesson.resources[3]} lesson={lesson} /></Router>);

        expect(
            container.querySelector('div.box a img').getAttribute('src')
        ).toMatch('images/pic30.jpg');
    })

    it('has a title', () => {
        render(<Router><LessonBoxMenuMarkdownPageLinkItem  data={lesson.resources[3]} lesson={lesson} /></Router>);

        expect(
            container.querySelector('div.inner h3').textContent
        ).toMatch('From REST To GraphQL');
    })

    it('has a master heading', () => {
        render(<Router><LessonBoxMenuMarkdownPageLinkItem  data={lesson.resources[3]} lesson={lesson} /></Router>);

        expect(
            container.querySelector('div.inner p').textContent
        ).toMatch('Coding Tech');
    })

    it('has a view button', () => {
        render(<Router><LessonBoxMenuMarkdownPageLinkItem data={lesson.resources[3]} lesson={lesson} typeButtonText='View'/></Router>);

        expect(
            container.querySelector('div.inner a.button').textContent
        ).toMatch('View');

        expect(
            container.querySelector('div.inner a.button').getAttribute('href')
        ).toMatch('/Lesson/123/Activity/11/31/FromRESTToGraphQL.md');
    })

    it('has type label heading from reference type name', () => {
        render(<Router><LessonBoxMenuMarkdownPageLinkItem data={lesson.resources[3]} lesson={lesson} /></Router>);

        expect(
            container.querySelector('div.inner label.label').textContent
        ).toMatch('Markdown');
    })
})