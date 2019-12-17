import React from 'react';
import ReactDOM from 'react-dom';

import { LessonBoxMenuWidget, LessonBoxMenuItem } from '../widgets/LessonBoxMenuWidget';
import { createContainer } from '../helpers/domManipulators';

let lesson = {
    id: 1,
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
        reference_type_id: 6,
        reference_type_name: "Book",
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
        reference_type_id: 7,
        reference_type_name: "Video",
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
        page_note: "",
        page_uri: "",
        task_icon: "",
        image_url: "images/pic07.jpg",
    },
    {
        id: 30,
        reference_type_id: 7,
        reference_type_name: "Video",
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
        page_note: "",
        page_uri: "",
        task_icon: "",
        image_url: "images/pic30.jpg",
    },
    ]
}

describe ('LessonBoxMenuItem', () => {
    let render, container;
    
    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(<LessonBoxMenuItem />);

        expect(container.textContent).toMatch('');
    })

    it('has a link from image', () => {
        render(<LessonBoxMenuItem data={lesson.resources[1]} />);

        expect(
            container.querySelector('div.box a').getAttribute('href')
        ).toMatch('https://www.youtube.com/playlist?list=PLCiOXwirraUBj7HtVHfNZsnwjyZQj97da');
    })

    it('has a image', () => {
        render(<LessonBoxMenuItem  data={lesson.resources[1]} />);

        expect(
            container.querySelector('div.box a img').getAttribute('src')
        ).toMatch('images/pic07.jpg');
    })

    it('has a title', () => {
        render(<LessonBoxMenuItem  data={lesson.resources[1]} />);

        expect(
            container.querySelector('div.inner h3').textContent
        ).toMatch('A level: OCR Specification Order');
    })

    it('has a publisher', () => {
        render(<LessonBoxMenuItem  data={lesson.resources[1]} />);

        expect(
            container.querySelector('div.inner p').textContent
        ).toMatch('YouTube');
    })

    it('has a view button', () => {
        render(<LessonBoxMenuItem data={lesson.resources[1]} typeButtonText='View'/>);

        expect(
            container.querySelector('div.inner a.button').textContent
        ).toMatch('View');

        expect(
            container.querySelector('div.inner a.button').getAttribute('href')
        ).toMatch('https://www.youtube.com/playlist?list=PLCiOXwirraUBj7HtVHfNZsnwjyZQj97da');
    })

    it('has type label heading from reference type name', () => {
        render(<LessonBoxMenuItem data={lesson.resources[1]} />);

        expect(
            container.querySelector('div.inner label.label').textContent
        ).toMatch('Video');
    })
})