import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import { CoursePageContainer} from '../pages/CoursePage';

describe("CoursePageContainer", () =>{
    let render, container;

    let socialmediadata = undefined;

    let site = {
            name:"Dave Russell",
            description:"Eu hendrerit felis rhoncus vel. In hac habitasse"
        }

    let schemeofwork = {
            id: 76,
            name: "KS3 Computing",
            description: "Lorem ipsum dolor sit amet."
        }
    
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
    beforeEach(() => {
        (
            {render, container} = createContainer(container)
        )
    })

    it('renders empty model', () => {
        render(<CoursePageContainer />);
        
        expect(container.textContent).toMatch('');
    })

    describe('has a banner', () => {
        
        it('with heading', () => {
            render(<Router><CoursePageContainer lessons={lessons} schemeofwork={schemeofwork} site={site} socialmediadata /></Router>);

            expect(
                container.querySelector('section#banner .inner header h1').textContent
            ).toMatch('KS3 Computing');
        })

        it('with description', () => {
            render(<Router><CoursePageContainer lessons={lessons} schemeofwork={schemeofwork} site={site} socialmediadata /></Router>);

            expect(
                container.querySelector('section#banner .inner header p').textContent
            ).toMatch('Lorem ipsum dolor sit amet.');
        })
    })

    describe('has footer', () => {

        it('with scheme of work name as heading', () => {
            render(<Router><CoursePageContainer lessons={lessons} schemeofwork={schemeofwork} site={site} socialmediadata /></Router>);

            expect(
                container.querySelector('footer#footer h2').textContent
            ).toMatch('Dave Russell');
        })

        it('with scheme of work overview summary', () => {
            render(<Router><CoursePageContainer lessons={lessons} schemeofwork={schemeofwork} site={site} socialmedia /></Router>);

            expect(
                container.querySelector('footer#footer p').textContent
            ).toMatch('Eu hendrerit felis rhoncus vel. In hac habitasse');
        })
    })

    describe('has lessons widget', () => {

        it('with courses', () => {
            render(<Router><CoursePageContainer lessons={lessons} schemeofwork={schemeofwork} site={site} socialmedia /></Router>);

            // Heading
            expect(
                container.querySelector("#main .inner h2").textContent
            ).toMatch('Lessons');

            // First
            expect(
                container.querySelector("#main .inner div.lessons > .box:nth-child(1) .inner label.label u").textContent
            ).toMatch("Lesson");

            expect(
                container.querySelector("#main .inner div.lessons > .box:nth-child(1) .inner h3").textContent
            ).toMatch("Curabitur id purus feugiat, porttitor.");

            expect(
                container.querySelector("#main .inner div.lessons > .box:nth-child(1) .inner a").getAttribute('href')
            ).toMatch("/Lesson/1");

            // Last
            expect(
                container.querySelector("#main .inner div.lessons > .box:nth-last-child(1) .inner label.label u").textContent
            ).toMatch("Lesson");

            expect(
                container.querySelector("#main .inner div.lessons > .box:nth-last-child(1) .inner h3").textContent
            ).toMatch("Donec sit amet felis id");

            expect(
                container.querySelector("#main .inner div.lessons > .box:nth-last-child(1) .inner a").getAttribute('href')
            ).toMatch("Lesson/6");
        })
    })
});


