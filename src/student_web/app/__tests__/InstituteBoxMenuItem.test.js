import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter } from 'react-router-dom';

import { InstituteBoxMenuItem } from '../widgets/InstituteBoxMenuWidget';
import { createContainer } from '../helpers/domManipulators';

let institute = {
    id: 1277611,
    name: "KS3 Computing",
    description: "Lorem ipsum dolor sit amet.",
    number_of_departments: 12,
    image_url: "images/pic03.jpg",
    url: "https://youtu.be/s6zR2er9vn2a",
}

describe ('InstituteBoxMenuItem', () => {
    let render, container;

    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(
            <MemoryRouter>
                <InstituteBoxMenuItem />
            </MemoryRouter>
            );

        expect(container.textContent).toMatch('');
    })

    it('has a link from image', () => {
        render(
            <MemoryRouter>
                <InstituteBoxMenuItem data={institute} />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.box a').getAttribute('href')
        ).toMatch('https://youtu.be/s6zR2er9vn2a');
    })

    it('has a image', () => {
        render(
            <MemoryRouter>
            <InstituteBoxMenuItem  data={institute} />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.box a img').getAttribute('src')
        ).toMatch('images/pic03.jpg');
    })

    it('has a title', () => {
        render(
            <MemoryRouter>
            <InstituteBoxMenuItem  data={institute} />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner h3').textContent
        ).toMatch('KS3 Computing');
    })

    it('has a summary', () => {
        render(
            <MemoryRouter>
            <InstituteBoxMenuItem  data={institute} />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner p').textContent
        ).toMatch('Lorem ipsum dolor sit amet.');
    })

    it('has a view button', () => {
        render(
            <MemoryRouter>
            <InstituteBoxMenuItem 
                data={institute} 
                uri='/Institute/99/'
                typeButtonText='View'
                typeButtonClass='button fit' />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner a.button').textContent
        ).toMatch('View');

        expect(
            container.querySelector('div.inner a.button').getAttribute('href')
        ).toMatch('/institute/1277611');
    })

    it('has a disabled view button', () => {
        // arrange zero lessons for this test
        institute.number_of_departments = 0;

        render(
            <MemoryRouter>
            <InstituteBoxMenuItem 
                data={institute} 
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
            <InstituteBoxMenuItem data={institute} typeLabelText="Institute" />
            </MemoryRouter>
            );

        expect(
            container.querySelector('div.inner label.label').textContent
        ).toMatch('Institute');
    })
})