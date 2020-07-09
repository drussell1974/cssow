import React from 'react';
import ReactDOM from 'react-dom';

import { createContainer } from '../helpers/domManipulators';
import { LessonObjectivesWidget } from '../widgets/LessonObjectivesWidget';

let lesson = 
    {
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
    };

describe('LessonObjectivesWidgetItem', () => {
    let render, container;
    
    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(<LessonObjectivesWidget />);
       
        expect(
            container.textContent
        ).toMatch("");
    })

    it('renders list of objectives', () => {
        render(<LessonObjectivesWidget data={lesson} />);

        expect(
            container.querySelectorAll('ul.objectives li')
        ).toHaveLength(3);
    })
})