import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter } from 'react-router-dom';
import { DepartmentBoxMenuWidget } from '../widgets/DepartmentBoxMenuWidget';
import { createContainer } from '../helpers/domManipulators';


let departments = [
    {
        id: 10976,
        name: "Geography",
        description: "Lorem ipsum dolor sit amet.",
        number_of_schemes_of_work: 0,
    },
    {
        id: 109127,
        name: "Computer Science",
        description: " ",
        number_of_schemes_of_work: 25,
    },
    {
        id: 10911,
        name: "English",
        description: "English department",
        number_of_schemes_of_work: 101,
    }
]

describe('DepartmentBoxMenu', () => {
    let render, container;

    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(
            <MemoryRouter>
            <DepartmentBoxMenuWidget data={departments} />
            </MemoryRouter>
            );
        
        expect(container.textContent).toMatch('');
    })

    it('renders departments container', () => {    
        render(
            <MemoryRouter>
            <DepartmentBoxMenuWidget data={departments} />
            </MemoryRouter>
            );
        
        expect(
            container.querySelector('.departments').getAttribute('class')
        ).toMatch('');
    })

    it('has a heading', () => {
        render(
            <MemoryRouter>
                <DepartmentBoxMenuWidget data={departments} />
            </MemoryRouter>
        )

        expect(
            container.querySelector('h2').textContent
        ).toMatch('Departments');
    })

    it('has a single box', () => {
        render(
            <MemoryRouter>
            <DepartmentBoxMenuWidget data={departments.slice(0,1)} />
            </MemoryRouter>);

        expect(
            container.querySelectorAll('.box')
        ).toHaveLength(1);
    })

    
    it('has a multiple boxes', () => {
        render(
            <MemoryRouter>
            <DepartmentBoxMenuWidget data={departments} />
            </MemoryRouter>);

        expect(
            container.querySelectorAll('.box')
        ).toHaveLength(3);
    })

    it('renders buttons with typeLabelText', () => {
        render(
            <MemoryRouter>
            <DepartmentBoxMenuWidget data={departments} typeLabelText="department" />
            </MemoryRouter>);

        expect(
            container.querySelector('.box:nth-child(1) .inner label.label').textContent
        ).toMatch('department');
    })

    it('renders buttons with link', () => {
        render(
            <MemoryRouter>
            <DepartmentBoxMenuWidget
                data={departments}
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

    it('renders view button when no schemes of work', () => {

        departments[2].number_of_schemes_of_work = 0

        render(
            <MemoryRouter>
            <DepartmentBoxMenuWidget
                data={departments}
                typeButtonText="View" 
                typeButtonClass='button fit'
                typeDisabledButtonText="Coming soon" 
                typeDisabledButtonClass='button fit disabled'
                 />
            </MemoryRouter>);

        expect(
            container.querySelector('.box:nth-child(2) .inner a.button').getAttribute('class')
        ).toMatch('button fit');

        expect(
            container.querySelector('.box:nth-child(2) .inner a.button').textContent
        ).toMatch('View');
    })
});