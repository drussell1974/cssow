import { LessonBoxMenuWidget, LessonBoxMenuItem } from '../widgets/LessonBoxMenuWidget';

import React from 'react';
import ReactDOM from 'react-dom';

let lesson = {
    id:1,
    title: "Curabitur id purus feugiat, porttitor.",
    summary: "In vitae arcu quis dolor porttitor bibendum in eu nisl. Etiam efficitur dictum elit a tempus. Etiam feugiat acrisus",
    image_url: "images/pic01.jpg",
    url: "https://youtu.be/s6zR2T9vn2a",
}

describe ('LessonBoxMenuItem', () => {
    let container;
    
    beforeEach(() => {
        container = document.createElement('div');
    })

    it('renders empty model', () => {
        ReactDOM.render(<LessonBoxMenuItem />, container);

        expect(container.textContent).toMatch('');
    })

    it('has a link from image', () => {
        ReactDOM.render(<LessonBoxMenuItem data={lesson} />, container);

        expect(
            container.querySelector('div.box a').getAttribute('href')
        ).toMatch('https://youtu.be/s6zR2T9vn2a');
    })

    it('has a image', () => {
        ReactDOM.render(<LessonBoxMenuItem  data={lesson} />, container);

        expect(
            container.querySelector('div.box a img').getAttribute('src')
        ).toMatch('images/pic01.jpg');
    })

    it('has a title', () => {
        ReactDOM.render(<LessonBoxMenuItem  data={lesson} />, container);

        expect(
            container.querySelector('div.inner h3').textContent
        ).toMatch('Curabitur id purus feugiat, porttitor.')
    })

    it('has a summary', () => {
        ReactDOM.render(<LessonBoxMenuItem  data={lesson} />, container);

        expect(
            container.querySelector('div.inner p').textContent
        ).toMatch('In vitae arcu quis dolor porttitor bibendum in eu nisl. Etiam efficitur dictum elit a tempus. Etiam feugiat acrisus')
    })

    it('has a watch button', () => {
        ReactDOM.render(<LessonBoxMenuItem data={lesson} />, container);

        expect(
            container.querySelector('div.inner a.button').textContent
        ).toMatch('Watch')

        expect(
            container.querySelector('div.inner a.button').getAttribute('href')
        ).toMatch('https://youtu.be/s6zR2T9vn2a')
    })
})