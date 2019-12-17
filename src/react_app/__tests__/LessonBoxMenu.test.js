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
    ],
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
},{
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
}]

describe('LessonBoxMenu', () => {
    let render, container;

    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(<LessonBoxMenuWidget data={lessons} />);
        
        expect(container.textContent).toMatch('');
    })

    it('renders lessons container', () => {    
        render(<LessonBoxMenuWidget data={lessons} />);
        
        expect(
            container.querySelector('.lessons').getAttribute('class')
        ).toMatch('');
    })

    it('has a single box', () => {
        render(<LessonBoxMenuWidget data={lessons.slice(0,1)} />);

        expect(
            container.querySelectorAll('.box')
        ).toHaveLength(1);
    })

    
    it('has a multiple boxes', () => {
        render(<LessonBoxMenuWidget data={lessons} />);

        expect(
            container.querySelectorAll('.box')
        ).toHaveLength(6);
    })

    it('renders buttons with typeLabelText', () => {
        render(<LessonBoxMenuWidget data={lessons} typeLabelText="lesson" />);

        expect(
            container.querySelector('.box .inner label.label').textContent
        ).toMatch('lesson');
    })

    
    it('renders buttons with typeButtonText', () => {
        render(<LessonBoxMenuWidget data={lessons} typeButtonText="View" />);

        expect(
            container.querySelector('.box .inner a.button').textContent
        ).toMatch('View');
    })
});