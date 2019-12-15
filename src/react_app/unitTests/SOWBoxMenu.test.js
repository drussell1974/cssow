import { SOWBoxMenuWidget, SOWBoxMenuItem } from '../widgets/SOWBoxMenuWidget';

import React from 'react';
import ReactDOM from 'react-dom';

let lessons = [{
    id:1,
    title: "Curabitur id purus feugiat, porttitor.",
    summary: "In vitae arcu quis dolor porttitor bibendum in eu nisl. Etiam efficitur dictum elit a tempus. Etiam feugiat acrisus",
    image_url: "images/pic01.jpg",
    url: "https://youtu.be/s6zR2T9vn2a",
},{
    id:2,
    title: "Sed a ante placerat, porta.",
    summary: "Nullam quis malesuada mauris. Vivamus vitae augue eget quam porta pretium nec in ligula. Aenean ullamcorper leo at mi hendrerit.",
    image_url: "images/pic02.jpg",
    url: "https://youtu.be/s6zR2T9vn2b",
},{
    id:3,
    title: "Nullam bibendum hendrerit dolor, in.",
    summary: "Integer felis nunc, venenatis et hendrerit a, maximus nec orci. In hendrerit velit sem, id congue ante cursus id. Cras.",
    image_url: "images/pic03.jpg",
    url: "https://youtu.be/s6zR2T9vn2c",
},{
    id:4,
    title: "Donec pellentesque sit amet lorem",
    summary: "Integer felis nunc, venenatis et hendrerit a, maximus nec orci. In hendrerit velit sem, id congue ante cursus id. Cras.",
    image_url: "images/pic04.jpg",
    url: "https://youtu.be/s6zR2T9vn2d",
},{
    id:5,
    title: "Nullam a ultrices mi. Suspendisse",
    summary: "Nam at malesuada mi. Cras non consectetur sapien. Etiam eget justo egestas, sagittis mauris a, luctus quam. Quisque vitae sapien.",
    image_url: "images/pic05.jpg",
    url: "https://youtu.be/s6zR2T9vn2e",
},{
    id:6,
    title: "Donec sit amet felis id",
    summary: "Integer feugiat eget libero eu eleifend. Pellentesque molestie pellentesque urna non malesuada. Mauris blandit accumsan est, at aliquam mauris tempus.",
    image_url: "images/pic06.jpg",
    url: "https://youtu.be/s6zR2T9vn2f",
}]

describe('SOWBoxMenu', () => {
    let container;

    beforeEach(() => {
        container = document.createElement('div');
    })

    it('renders empty model', () => {
        ReactDOM.render(<SOWBoxMenuWidget data={lessons} />, container);
        
        expect(container.textContent).toMatch('');
    })

    it('renders lessons container', () => {    
        ReactDOM.render(<SOWBoxMenuWidget data={lessons} />, container);
        
        expect(
            container.querySelector('.lessons').getAttribute('class')
        ).toMatch('');
    })

    it('has a single box', () => {
        ReactDOM.render(<SOWBoxMenuWidget data={lessons.slice(0,1)} />, container);

        expect(
            container.querySelectorAll('.box')
        ).toHaveLength(1);
    })

    
    it('has a multiple boxes', () => {
        ReactDOM.render(<SOWBoxMenuWidget data={lessons} />, container);

        expect(
            container.querySelectorAll('.box')
        ).toHaveLength(6);
    })

    it('renders buttons with typeLabelText', () => {
        ReactDOM.render(<SOWBoxMenuWidget data={lessons} typeLabelText="lesson" />, container);

        expect(
            container.querySelector('.box .inner label.label').textContent
        ).toMatch('lesson');
    })

    
    it('renders buttons with typeButtonText', () => {
        ReactDOM.render(<SOWBoxMenuWidget data={lessons} typeButtonText="View" />, container);

        expect(
            container.querySelector('.box .inner a.button').textContent
        ).toMatch('View');
    })
});