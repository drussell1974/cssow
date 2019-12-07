import { LessonBoxMenu, LessonBoxMenuItem } from '../pages/LessonBoxMenu';

import React from 'react';
import ReactDOM from 'react-dom';

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
        ReactDOM.render(<LessonBoxMenuItem />, container);

        expect(
            container.querySelector('div.box a').getAttribute('href')
        ).toMatch('https://youtu.be/s6zR2T9vn2c');
    })

    it('has a image', () => {
        ReactDOM.render(<LessonBoxMenuItem />, container);

        expect(
            container.querySelector('div.box a img').getAttribute('src')
        ).toMatch('images/pic01.jpg');
    })

    it('has a title', () => {
        ReactDOM.render(<LessonBoxMenuItem />, container);

        expect(
            container.querySelector('.inner h3').textContent
        ).toMatch('Nascetur nunc varius commodo')
    })

    it('has a summary', () => {
        ReactDOM.render(<LessonBoxMenuItem />, container);

        expect(
            container.querySelector('.inner p').textContent
        ).toMatch('Interdum amet accumsan placerat commodo ut amet aliquam blandit nunc tempor lobortis nunc non. Mi accumsan.')
    })
})

describe('LessonBoxMenu', () => {
    let container;

    beforeEach(() => {
        container = document.createElement('div');
    })

    it('renders empty model', () => {
        ReactDOM.render(<LessonBoxMenu />, container);
        
        expect(container.textContent).toMatch('')
    })

    it('renders lessons container', () => {    
        ReactDOM.render(<LessonBoxMenu />, container);
        
        expect(
            container.querySelector('.lessons').getAttribute('class')
        ).toMatch('')
    })
});