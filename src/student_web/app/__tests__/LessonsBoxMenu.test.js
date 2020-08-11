import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter } from 'react-router-dom';

import { LessonsBoxMenuWidget } from '../widgets/LessonsBoxMenuWidget';
import { createContainer } from '../helpers/domManipulators';

let lessons = [{
    id: 1,
    title: "Curabitur id purus feugiat, porttitor.",
    summary: "In vitae arcu quis dolor porttitor bibendum in eu nisl. Etiam efficitur dictum elit a tempus. Etiam feugiat acrisus",
    image_url: "images/pic01.jpg",
    url: "https://youtu.be/s6zR2T9vn2a",
    number_of_learning_objective: 7,
    number_of_resource: 1,
},{
    id: 2,
    title: "Sed a ante placerat, porta.",
    summary: "Nullam quis malesuada mauris. Vivamus vitae augue eget quam porta pretium nec in ligula. Aenean ullamcorper leo at mi hendrerit.",
    image_url: "images/pic02.jpg",
    url: "https://youtu.be/s6zR2T9vn2b",
    number_of_learning_objective: 3,
    number_of_resource: 2,
},{
    id: 3,
    title: "Nullam bibendum hendrerit dolor, in.",
    summary: "Integer felis nunc, venenatis et hendrerit a, maximus nec orci. In hendrerit velit sem, id congue ante cursus id. Cras.",
    image_url: "images/pic03.jpg",
    url: "https://youtu.be/s6zR2T9vn2c",
    number_of_learning_objective: 4,
    number_of_resource: 0,
},{
    id: 4,
    title: "Donec pellentesque sit amet lorem",
    summary: "Integer felis nunc, venenatis et hendrerit a, maximus nec orci. In hendrerit velit sem, id congue ante cursus id. Cras.",
    image_url: "images/pic04.jpg",
    url: "https://youtu.be/s6zR2T9vn2d",
    number_of_learning_objective: 0,
    number_of_resource: 0,
},{
    id: 5,
    title: "Nullam a ultrices mi. Suspendisse",
    summary: "Nam at malesuada mi. Cras non consectetur sapien. Etiam eget justo egestas, sagittis mauris a, luctus quam. Quisque vitae sapien.",
    image_url: "images/pic05.jpg",
    url: "https://youtu.be/s6zR2T9vn2e",
    number_of_learning_objective: 2,
    number_of_resource: 3,
},{
    id: 6,
    title: "Donec sit amet felis id",
    summary: "Integer feugiat eget libero eu eleifend. Pellentesque molestie pellentesque urna non malesuada. Mauris blandit accumsan est, at aliquam mauris tempus.",
    image_url: "images/pic06.jpg",
    url: "https://youtu.be/s6zR2T9vn2f",
    number_of_learning_objective: 7,
    number_of_resource: 1,
}]

describe('LessonsBoxMenu', () => {
    let render, container;

    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(
            <MemoryRouter>
            <LessonsBoxMenuWidget data={lessons} />
            </MemoryRouter>
            );
        
        expect(container.textContent).toMatch('');
    })

    it('renders lessons container', () => {    
        render(
            <MemoryRouter>
            <LessonsBoxMenuWidget data={lessons} />
            </MemoryRouter>
            );
        
        expect(
            container.querySelector('.lessons').getAttribute('class')
        ).toMatch('');
    })

    it('has a heading', () => {
        render(
            <MemoryRouter>
                <LessonsBoxMenuWidget data={lessons} />
            </MemoryRouter>
        )

        expect(
            container.querySelector('h2').textContent
        ).toMatch('Lessons');
    })

    it('has a single box', () => {
        render(
            <MemoryRouter>
            <LessonsBoxMenuWidget data={lessons.slice(0,1)} />
            </MemoryRouter>);

        expect(
            container.querySelectorAll('.box')
        ).toHaveLength(1);
    })

    
    it('has a multiple boxes', () => {
        render(
            <MemoryRouter>
            <LessonsBoxMenuWidget data={lessons} />
            </MemoryRouter>);

        expect(
            container.querySelectorAll('.box')
        ).toHaveLength(5);
    })

    it('renders buttons with typeLabelText', () => {
        render(
            <MemoryRouter>
            <LessonsBoxMenuWidget data={lessons} typeLabelText="lesson" />
            </MemoryRouter>);

        expect(
            container.querySelector('.box .inner label.label').textContent
        ).toMatch('lesson');
    })

    
    it('renders buttons with ', () => {
        render(
            <MemoryRouter>
            <LessonsBoxMenuWidget data={lessons} typeButtonText="View" />
            </MemoryRouter>);

        expect(
            container.querySelector('.box .inner a.button').textContent
        ).toMatch('View');
    })
});