import React from 'react';
import ReactDOM from 'react-dom';

import { LessonBoxMenuWidget, LessonBoxMenuItem } from '../widgets/LessonBoxMenuWidget';
import { createContainer } from '../helpers/domManipulators';

let lessons = [{
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
    },{
        id: 2,
        title: "Sed a ante placerat, porta.",
        summary: "Nullam quis malesuada mauris. Vivamus vitae augue eget quam porta pretium nec in ligula. Aenean ullamcorper leo at mi hendrerit.",
        image_url: "images/pic02.jpg",
        url: "https://youtu.be/s6zR2T9vn2b",
        learning_objectives: [
            {
                id: 465,
                description: "Explain the steps carried out by the Fetch Decode Execute cycle",
                notes: " ",
                scheme_of_work_name: "",
                solo_taxonomy_id: 3,
                solo_taxonomy_name: "Relational: Explain, Compare, Justify and Give Reasons (evaluate or assess)",
                solo_taxonomy_level: "C",
            },
        ],
        resources: 
        [
            {
                id: 27,
                reference_type_id: 7,
                reference_type_name: "Video",
                title: "Computer Science channel",
                publisher: "YouTube",
                year_published: 2019,
                authors: "Computer Science",
                uri: "https://www.youtube.com/channel/UCSX3MR0gnKDxyXAyljWzm0Q",
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
                image_url: "images/pic27.jpg",
            },
        ]
    },{
        id: 3,
        title: "Nullam bibendum hendrerit dolor, in.",
        summary: "Integer felis nunc, venenatis et hendrerit a, maximus nec orci. In hendrerit velit sem, id congue ante cursus id. Cras.",
        image_url: "images/pic03.jpg",
        url: "https://youtu.be/s6zR2T9vn2c",
        learning_objectives: [
            {
                id: 466,
                description: "Give the reasons why a branch in the program may occur",
                notes: " ",
                scheme_of_work_name: "",
                solo_taxonomy_id: 2,
                solo_taxonomy_name: "Multistructural: Describe, List (give an account or give examples of)",
                solo_taxonomy_level: "B",
            },
        ]
    },{
        id: 4,
        title: "Donec pellentesque sit amet lorem",
        summary: "Integer felis nunc, venenatis et hendrerit a, maximus nec orci. In hendrerit velit sem, id congue ante cursus id. Cras.",
        image_url: "images/pic04.jpg",
        url: "https://youtu.be/s6zR2T9vn2d",
        learning_objectives: [
            {
                id: 467,
                description: "Describe the effects of a program branch on the Program Counter (PC)",
                notes: " ",
                scheme_of_work_name: "",
                solo_taxonomy_id: 2,
                solo_taxonomy_name: "Multistructural: Describe, List (give an account or give examples of)",
                solo_taxonomy_level: "B",
            }
        ],
        resources: [
            {            
                id: 31,
                reference_type_id: 7,
                reference_type_name: "Video",
                title: "John Phillip Jones",
                publisher: "YouTube",
                year_published: 2019,
                authors: "John Phillip Jones",
                uri: "https://www.youtube.com/user/johnphilipjones",
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
                image_url: "images/pic31.jpg",
            }
        ]
    },
    {
        id: 5,
        title: "Nullam a ultrices mi. Suspendisse",
        summary: "Nam at malesuada mi. Cras non consectetur sapien. Etiam eget justo egestas, sagittis mauris a, luctus quam. Quisque vitae sapien.",
        image_url: "images/pic05.jpg",
        url: "https://youtu.be/s6zR2T9vn2e",
        learning_objectives: [
            {
                id: 493,
                description: "Define how the Central Processing Unit (CPU) is connected to the main memory",
                notes: " ",
                scheme_of_work_name: "",
                solo_taxonomy_id: 1,
                solo_taxonomy_name: "A Unistructural: Identify, Name, Define (give, recall or state)",
                solo_taxonomy_level: "A",
            },
        ],
        resources: [
            {
                id: 21,
                reference_type_id: 8,
                reference_type_name: "Website",
                title: "Computing at School",
                publisher: "National Centre for Computing",
                year_published: 2019,
                authors: "",
                uri: "https://www.computingatschool.org.uk/",
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
                image_url: "images/pic21.jpg",
            },
        ]
    },{
        id: 6,
        title: "Donec sit amet felis id",
        summary: "Integer feugiat eget libero eu eleifend. Pellentesque molestie pellentesque urna non malesuada. Mauris blandit accumsan est, at aliquam mauris tempus.",
        image_url: "images/pic06.jpg",
        url: "https://youtu.be/s6zR2T9vn2f",
        learning_objectives: [
            {
                id: 494,
                description: "Define how data and control signals are transmitted across the system bus",
                notes: "The system bus consists of the address bus for sending the address location to memory; the data bus for returning data to the CPU; the control bus for sending control signals. ",
                scheme_of_work_name: "",
                solo_taxonomy_id: 1,
                solo_taxonomy_name: "A Unistructural: Identify, Name, Define (give, recall or state)",
                solo_taxonomy_level: "A",
            },
            {
                id: 495,
                description: "Describe the purpose of control lines on the Control Bus",
                notes: "Control lines are Bus Request, Bus Grant, Memory Write, Memory Read, Interrupt request, Clock. ",
                scheme_of_work_name: "",
                solo_taxonomy_id: 2,
                solo_taxonomy_name: "Multistructural: Describe, List (give an account or give examples of)",
                solo_taxonomy_level: "B",
            }
        ],
        resources:[
            {
                id: 23,
                reference_type_id: 8,
                reference_type_name: "Website",
                title: "Higher Computer Science",
                publisher: "BBC Bitesize",
                year_published: 2019,
                authors: "",
                uri: "https://www.bbc.com/bitesize/subjects/zxmh34j",
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
                image_url: "images/pic23.jpg",
            },
            {
                id: 20,
                reference_type_id: 8,
                reference_type_name: "Website",
                title: "Other websites",
                publisher: "Academic resources",
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
                page_note: "",
                page_uri: "",
                task_icon: "",
                image_url: "images/pic20.jpg",
            },
            {
                id: 26,
                reference_type_id: 8,
                reference_type_name: "Website",
                title: "Programiz",
                publisher: "Parewa Labs Pvt Ltd",
                year_published: 2019,
                authors: "",
                uri: "https://www.programiz.com",
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
                image_url: "images/pic26.jpg",
            },
        ]
    }]

describe('LessonBoxMenu', () => {
    let render, container;

    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(<LessonBoxMenuWidget data={lessons[0]} />);
        
        expect(container.textContent).toMatch('');
    })

    it('renders lessons container', () => {    
        render(<LessonBoxMenuWidget data={lessons[0]} />);
        
        expect(
            container.querySelector('.lessons').getAttribute('class')
        ).toMatch('');
    })

    it('renders no lesson containers when there are no resources', () => {    
        render(<LessonBoxMenuWidget data={lessons[2]} />);
        
        expect(
            container.querySelector('.lessons')
        ).toBeNull();
    })

    it('has a heading', () => {
        render(<LessonBoxMenuWidget data={lessons[0]} />);

        expect(
            container.querySelector('h2').textContent
        ).toMatch('Objectives');
    })

    it('has a single box', () => {
        render(<LessonBoxMenuWidget data={lessons[1]} />);

        expect(
            container.querySelectorAll('.box')
        ).toHaveLength(1);
    })

    
    it('has multiple boxes', () => {
        render(<LessonBoxMenuWidget data={lessons[0]} />);

        expect(
            container.querySelectorAll('.box')
        ).toHaveLength(3);
    })

    it('renders buttons with typeLabelText', () => {
        render(<LessonBoxMenuWidget data={lessons[0]} />);

        expect(
            container.querySelector('.box .inner label.label').textContent
        ).toMatch('Book');
    })

    
    it('renders buttons with typeButtonText', () => {
        render(<LessonBoxMenuWidget data={lessons[0]} typeButtonText="View" />);

        expect(
            container.querySelector('.box .inner a.button').textContent
        ).toMatch('View');
    })
});