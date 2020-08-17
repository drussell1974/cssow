import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter } from 'react-router-dom';

import { SchemeOfWorkBoxMenuItem } from '../widgets/SchemeOfWorkBoxMenuWidget';
import { createContainer } from '../helpers/domManipulators';

let schemeofwork = {
    id: 76,
    name: "KS3 Computing",
    description: "Lorem ipsum dolor sit amet.",
    number_of_lessons: 67,
    number_of_learning_objectives: 285,
    number_of_resources: 132,
    image_url: "images/pic03.jpg",
    url: "https://youtu.be/s6zR2er9vn2a",
}

describe ('SchemeOfWorkBoxMenuItem', () => {
    let render, container;

    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(
            <MemoryRouter>
                <SchemeOfWorkBoxMenuItem />
            </MemoryRouter>
            );

        expect(container.textContent).toMatch('');
    })

    it('has a link from image', () => {
        render(
            <MemoryRouter>
                <SchemeOfWorkBoxMenuItem data={schemeofwork} />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.box a').getAttribute('href')
        ).toMatch('https://youtu.be/s6zR2er9vn2a');
    })

    it('has a image', () => {
        render(
            <MemoryRouter>
            <SchemeOfWorkBoxMenuItem  data={schemeofwork} />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.box a img').getAttribute('src')
        ).toMatch('images/pic03.jpg');
    })

    it('has a title', () => {
        render(
            <MemoryRouter>
            <SchemeOfWorkBoxMenuItem  data={schemeofwork} />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner h3').textContent
        ).toMatch('KS3 Computing');
    })

    it('has a summary', () => {
        render(
            <MemoryRouter>
            <SchemeOfWorkBoxMenuItem  data={schemeofwork} />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner p').textContent
        ).toMatch('Lorem ipsum dolor sit amet.');
    })

    it('has a view button', () => {
        render(
            <MemoryRouter>
            <SchemeOfWorkBoxMenuItem 
                data={schemeofwork} 
                uri='/Course/'
                typeButtonText='View'
                typeButtonClass='button fit' />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner a.button').textContent
        ).toMatch('View');

        expect(
            container.querySelector('div.inner a.button').getAttribute('href')
        ).toMatch('/Course');
    })

    it('has a disabled view button', () => {
        // arrange zero lessons for this test
        schemeofwork.number_of_lessons = 0;

        render(
            <MemoryRouter>
            <SchemeOfWorkBoxMenuItem 
                data={schemeofwork} 
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
            <SchemeOfWorkBoxMenuItem data={schemeofwork} typeLabelText="scheme of work" />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner label.label').textContent
        ).toMatch('scheme of work');
    })
})