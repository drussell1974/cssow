import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter } from 'react-router-dom';

import { DepartmentBoxMenuItem } from '../widgets/DepartmentBoxMenuWidget';
import { createContainer } from '../helpers/domManipulators';

let department = {
    id: 76,
    name: "KS3 Computing",
    description: "Lorem ipsum dolor sit amet.",
    number_of_schemes_of_work: 12,
    image_url: "images/pic03.jpg",
    url: "https://youtu.be/s6zR2er9vn2a",
    institute_id: 1277611,
}

describe ('DepartmentBoxMenuItem', () => {
    let render, container;

    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(
            <MemoryRouter>
                <DepartmentBoxMenuItem />
            </MemoryRouter>
            );

        expect(container.textContent).toMatch('');
    })

    it('has a link from image', () => {
        render(
            <MemoryRouter>
                <DepartmentBoxMenuItem data={department} />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.box a').getAttribute('href')
        ).toMatch('https://youtu.be/s6zR2er9vn2a');
    })

    it('has a image', () => {
        render(
            <MemoryRouter>
            <DepartmentBoxMenuItem  data={department} />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.box a img').getAttribute('src')
        ).toMatch('images/pic03.jpg');
    })

    it('has a title', () => {
        render(
            <MemoryRouter>
            <DepartmentBoxMenuItem  data={department} />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner h3').textContent
        ).toMatch('KS3 Computing');
    })

    it('has a summary', () => {
        render(
            <MemoryRouter>
            <DepartmentBoxMenuItem  data={department} />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner p').textContent
        ).toMatch('Lorem ipsum dolor sit amet.');
    })

    it('has a view button', () => {
        render(
            <MemoryRouter>
            <DepartmentBoxMenuItem 
                data={department} 
                uri='/Institute/99/Department/99/Course/'
                typeButtonText='View'
                typeButtonClass='button fit' />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner a.button').textContent
        ).toMatch('View');

        expect(
            container.querySelector('div.inner a.button').getAttribute('href')
        ).toMatch('/institute/1277611/department/76');
    })

    it('has a disabled view button', () => {
        // arrange zero lessons for this test
        department.number_of_schemes_of_work = 0;

        render(
            <MemoryRouter>
            <DepartmentBoxMenuItem 
                data={department} 
                typeButtonText='View' 
                typeButtonClass='button fit'
                typeDisabledButtonText='Coming soon' 
                typeDisabledButtonClass='button fit disabled'/>
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner button.button').textContent
        ).toMatch('Coming soon');
    })

    it('has type label heading', () => {
        render(
            <MemoryRouter>
            <DepartmentBoxMenuItem data={department} typeLabelText="Department" />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner label.label').textContent
        ).toMatch('Department');
    })
})