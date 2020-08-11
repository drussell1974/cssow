import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter } from 'react-router-dom';
import { SchemeOfWorkBoxMenuWidget } from '../widgets/SchemeOfWorkBoxMenuWidget';
import { createContainer } from '../helpers/domManipulators';

let schemesofwork = [{
    id: 76,
    name: "KS3 Computing",
    description: "Lorem ipsum dolor sit amet.",
    number_of_lessons: 26,
    image_url: "images/pic06.jpg",
    url: "https://youtu.be/s6zR2T9vn2f",
},{
    id: 127,
    name: "GCSE Computer Science 9-1",
    description: " ",
    number_of_lessons: 1,
    image_url: "images/pic03.jpg",
    url: "https://youtu.be/s6zR2T9vn2c",
},{
    id: 769,
    name: "Introduction to computing",
    description: "BTEC Award",
    number_of_lessons: 0,
    image_url: "images/pic10.jpg",
    url: "https://youtu.be/s6uu343rT9vn2b",
},{
    id: 11,
    name: "A-Level Computer Science",
    description: "Computing curriculum for A-Level",
    number_of_lessons: 67,
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
            <SchemeOfWorkBoxMenuWidget data={schemesofwork} />
            </MemoryRouter>
            );
        
        expect(container.textContent).toMatch('');
    })

    it('renders lessons container', () => {    
        render(
            <MemoryRouter>
            <SchemeOfWorkBoxMenuWidget data={schemesofwork} />
            </MemoryRouter>
            );
        
        expect(
            container.querySelector('.lessons').getAttribute('class')
        ).toMatch('');
    })

    it('has a heading', () => {
        render(
            <MemoryRouter>
                <SchemeOfWorkBoxMenuWidget data={schemesofwork} />
            </MemoryRouter>
        )

        expect(
            container.querySelector('h2').textContent
        ).toMatch('Courses');
    })

    it('has a single box', () => {
        render(
            <MemoryRouter>
            <SchemeOfWorkBoxMenuWidget data={schemesofwork.slice(0,1)} />
            </MemoryRouter>);

        expect(
            container.querySelectorAll('.box')
        ).toHaveLength(1);
    })

    
    it('has a multiple boxes', () => {
        render(
            <MemoryRouter>
            <SchemeOfWorkBoxMenuWidget data={schemesofwork} />
            </MemoryRouter>);

        expect(
            container.querySelectorAll('.box')
        ).toHaveLength(4);
    })

    it('renders buttons with typeLabelText', () => {
        render(
            <MemoryRouter>
            <SchemeOfWorkBoxMenuWidget data={schemesofwork} typeLabelText="lesson" />
            </MemoryRouter>);

        expect(
            container.querySelector('.box:nth-child(1) .inner label.label').textContent
        ).toMatch('lesson');
    })

    it('renders buttons with link', () => {
        render(
            <MemoryRouter>
            <SchemeOfWorkBoxMenuWidget
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

    it('renders coming soon disabled button', () => {
        render(
            <MemoryRouter>
            <SchemeOfWorkBoxMenuWidget
                data={schemesofwork}
                typeButtonText="View" 
                typeButtonClass='button fit'
                typeDisabledButtonText="Coming soon" 
                typeDisabledButtonClass='button fit disabled'
                 />
            </MemoryRouter>);

        expect(
            container.querySelector('.box:nth-child(3) .inner a.button').getAttribute('class')
        ).toMatch('button fit disabled');

        expect(
            container.querySelector('.box:nth-child(3) .inner a.button').textContent
        ).toMatch('Coming soon');
    })
});