import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter } from 'react-router-dom';
import { CourseBoxMenuWidget } from '../widgets/CourseBoxMenuWidget';
import { createContainer } from '../helpers/domManipulators';

let schemesofwork = [{
    id: 76,
    name: "KS3 Computing",
    description: "Lorem ipsum dolor sit amet.",
    number_of_lessons: 26,
    number_of_learning_objectives: 154,
    number_of_resources: 34,
    image_url: "images/pic06.jpg",
    url: "https://youtu.be/s6zR2T9vn2f",
},{
    id: 127,
    name: "GCSE Computer Science 9-1",
    description: " ",
    number_of_lessons: 1,
    number_of_learning_objectives: 202,
    number_of_resources: 37,
    image_url: "images/pic03.jpg",
    url: "https://youtu.be/s6zR2T9vn2c",
},{
    id: 769,
    name: "Introduction to computing",
    description: "BTEC Award",
    number_of_lessons: 0,
    number_of_learning_objectives: 0,
    number_of_resources: 0,
    image_url: "images/pic10.jpg",
    url: "https://youtu.be/s6uu343rT9vn2b",
},{
    id: 11,
    name: "A-Level Computer Science",
    description: "Computing curriculum for A-Level",
    number_of_lessons: 67,
    number_of_learning_objectives: 434,
    number_of_resources: 303,
    image_url: "images/pic02.jpg",
    url: "https://youtu.be/s6zR2T9vn2b",
}]

describe('SchemesOfWorkBoxMenu', () => {
    let render, container;

    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(
            <MemoryRouter>
            <CourseBoxMenuWidget data={schemesofwork} />
            </MemoryRouter>
            );
        
        expect(container.textContent).toMatch('');
    })

    it('renders courses container', () => {    
        render(
            <MemoryRouter>
            <CourseBoxMenuWidget data={schemesofwork} />
            </MemoryRouter>
            );
        
        expect(
            container.querySelector('.courses').getAttribute('class')
        ).toMatch('');
    })

    it('has a heading', () => {
        render(
            <MemoryRouter>
                <CourseBoxMenuWidget data={schemesofwork} />
            </MemoryRouter>
        )

        expect(
            container.querySelector('h2').textContent
        ).toMatch('Courses');
    })

    it('has a single box', () => {
        render(
            <MemoryRouter>
            <CourseBoxMenuWidget data={schemesofwork.slice(0,1)} />
            </MemoryRouter>);

        expect(
            container.querySelectorAll('.box')
        ).toHaveLength(1);
    })

    
    it('has a multiple boxes', () => {
        render(
            <MemoryRouter>
            <CourseBoxMenuWidget data={schemesofwork} />
            </MemoryRouter>);

        expect(
            container.querySelectorAll('.box')
        ).toHaveLength(4);
    })

    it('renders buttons with typeLabelText', () => {
        render(
            <MemoryRouter>
            <CourseBoxMenuWidget data={schemesofwork} typeLabelText="lesson" />
            </MemoryRouter>);

        expect(
            container.querySelector('.box:nth-child(1) .inner label.label').textContent
        ).toMatch('lesson');
    })

    it('renders buttons with link', () => {
        render(
            <MemoryRouter>
            <CourseBoxMenuWidget
                data={schemesofwork}
                typeButtonText="View" 
                typeButtonClass='button fit'
                typeDisabledButtonText="Coming soon" 
                typeDisabledButtonClass='button fit disabled'
                 />
            </MemoryRouter>);

        expect(
            container.querySelector('.box:nth-last-child(1) .inner a.button').getAttribute('class')
        ).toEqual('button fit');

        expect(
            container.querySelector('.box:nth-last-child(1) .inner a.button').textContent
        ).toMatch('View');
    })

    it('renders coming soon disabled button when scheme of work has no lessons', () => {

        schemesofwork[2].number_of_lessons = 0

        render(
            <MemoryRouter>
            <CourseBoxMenuWidget
                data={schemesofwork}
                typeButtonText="View" 
                typeButtonClass='button fit'
                typeDisabledButtonText="Coming soon" 
                typeDisabledButtonClass='button fit disabled'
                 />
            </MemoryRouter>);

        expect(
            container.querySelector('.box:nth-child(3) .inner button.button').getAttribute('class')
        ).toMatch('button fit disabled');

        expect(
            container.querySelector('.box:nth-child(3) .inner button.button').textContent
        ).toMatch('Coming soon');
    })

    it('renders coming soon disabled button when scheme of work has lesson with no resources and no learning objectives', () => {

        schemesofwork[2].number_of_lessons = 5
        schemesofwork[2].number_of_learning_objectives = 0
        schemesofwork[2].number_of_resources = 0

        render(
            <MemoryRouter>
            <CourseBoxMenuWidget
                data={schemesofwork}
                typeButtonText="View" 
                typeButtonClass='button fit'
                typeDisabledButtonText="Coming soon" 
                typeDisabledButtonClass='button fit disabled'
                 />
            </MemoryRouter>);

        expect(
            container.querySelector('.box:nth-child(3) .inner button.button').textContent
        ).toMatch('Coming soon');

        expect(
            container.querySelector('.box:nth-child(3) .inner button.button').getAttribute('class')
        ).toMatch('button fit disabled');

    })


    it('renders view button when scheme of work has lessons with resources but no learning objectives', () => {

        schemesofwork[2].number_of_lessons = 3
        schemesofwork[2].number_of_learning_objectives = 0
        schemesofwork[2].number_of_resources = 1

        render(
            <MemoryRouter>
            <CourseBoxMenuWidget
                data={schemesofwork}
                typeButtonText="View" 
                typeButtonClass='button fit'
                typeDisabledButtonText="Coming soon" 
                typeDisabledButtonClass='button fit disabled'
                 />
            </MemoryRouter>);

        expect(
            container.querySelector('.box:nth-child(3) .inner a.button').getAttribute('class')
        ).toMatch('button fit');

        expect(
            container.querySelector('.box:nth-child(3) .inner a.button').textContent
        ).toMatch('View');
    })


    it('renders view button when scheme of work has lessons with learning objectives but no resources', () => {

        schemesofwork[2].number_of_lessons = 1
        schemesofwork[2].number_of_learning_objectives = 1
        schemesofwork[2].number_of_resources = 0

        render(
            <MemoryRouter>
            <CourseBoxMenuWidget
                data={schemesofwork}
                typeButtonText="View" 
                typeButtonClass='button fit'
                typeDisabledButtonText="Coming soon" 
                typeDisabledButtonClass='button fit disabled'
                 />
            </MemoryRouter>);

        expect(
            container.querySelector('.box:nth-child(3) .inner a.button').getAttribute('class')
        ).toMatch('button fit');

        expect(
            container.querySelector('.box:nth-child(3) .inner a.button').textContent
        ).toMatch('View');
    })
});