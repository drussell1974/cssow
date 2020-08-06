import React from 'react';
import ReactDOM from 'react-dom';

import { createContainer } from '../helpers/domManipulators';
import { LessonKeywordsWidget } from '../widgets/LessonKeywordsWidget';

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
            }
        ],
    };

describe('LessonKeywordsWidget', () => {
    let render, container;
    
    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(<LessonKeywordsWidget />);
       
        expect(
            container.textContent
        ).toMatch("");
    })

    it.skip('renders list of keywords', () => {
        render(<LessonKeywordsWidget keywords={lesson.key_words} />);

        expect(
            container.querySelectorAll('ul.keywords li')
        ).toHaveLength(3);
    })
})