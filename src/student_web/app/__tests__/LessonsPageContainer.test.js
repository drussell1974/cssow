import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import { LessonsPageContainer} from '../pages/LessonsPage';

describe("LessonsPageContainer", () =>{
    let render, container;

    let socialmediadata = undefined;

    let site = {
            name:"Dave Russell",
            description:"Eu hendrerit felis rhoncus vel. In hac habitasse"
        }

    let institute = {
            id: 1276711,
            name:"Lorem Ipsum",
            description:"Phasellus eu tincidunt sapien, ac laoreet dui. In hac habitasse platea dictumst. Ut molestie nibh nec hendrerit posuere."
        }

    let department = {
            id:67,
            name:"Computer Science",
            description:"Morbi ipsum tellus, porta non congue condimentum, fermentum sed nisl."
        }

    let course = {
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
        number_of_resources: 1,
        scheme_of_work_id: 76,
        department_id: 67,
        institute_id: 1276711
    },{
        id: 2,
        title: "Sed a ante placerat, porta.",
        summary: "Nullam quis malesuada mauris. Vivamus vitae augue eget quam porta pretium nec in ligula. Aenean ullamcorper leo at mi hendrerit.",
        image_url: "images/pic02.jpg",
        url: "https://youtu.be/s6zR2T9vn2b",
        number_of_learning_objective: 3,
        number_of_resources: 2,
        scheme_of_work_id: 76,
        department_id: 67,
        institute_id: 1276711
    },{
        id: 3,
        title: "Nullam bibendum hendrerit dolor, in.",
        summary: "Integer felis nunc, venenatis et hendrerit a, maximus nec orci. In hendrerit velit sem, id congue ante cursus id. Cras.",
        image_url: "images/pic03.jpg",
        url: "https://youtu.be/s6zR2T9vn2c",
        number_of_learning_objectives: 4,
        number_of_resources: 0,
        scheme_of_work_id: 76,
        department_id: 67,
        institute_id: 1276711
    },{
        id: 4,
        title: "Donec pellentesque sit amet lorem",
        summary: "Integer felis nunc, venenatis et hendrerit a, maximus nec orci. In hendrerit velit sem, id congue ante cursus id. Cras.",
        image_url: "images/pic04.jpg",
        url: "https://youtu.be/s6zR2T9vn2d",
        number_of_learning_objective: 0,
        number_of_resources: 0,
        scheme_of_work_id: 76,
        department_id: 67,
        institute_id: 1276711
    },{
        id: 5,
        title: "Nullam a ultrices mi. Suspendisse",
        summary: "Nam at malesuada mi. Cras non consectetur sapien. Etiam eget justo egestas, sagittis mauris a, luctus quam. Quisque vitae sapien.",
        image_url: "images/pic05.jpg",
        url: "https://youtu.be/s6zR2T9vn2e",
        number_of_learning_objectives: 2,
        number_of_resources: 3,
        scheme_of_work_id: 76,
        department_id: 67,
        institute_id: 1276711
    },{
        id: 6,
        title: "Donec sit amet felis id",
        summary: "Integer feugiat eget libero eu eleifend. Pellentesque molestie pellentesque urna non malesuada. Mauris blandit accumsan est, at aliquam mauris tempus.",
        image_url: "images/pic06.jpg",
        url: "https://youtu.be/s6zR2T9vn2f",
        number_of_learning_objectives: 7,
        number_of_resources: 1,
        scheme_of_work_id: 76,
        department_id: 67,
        institute_id: 1276711
    }]

    beforeEach(() => {
        (
            {render, container} = createContainer(container)
        )
    })

    describe('renders empty model', () => {
        
        it('with no parameters', () => {
            render(<LessonsPageContainer />);
            
            expect(container.textContent).toMatch('');
        })

        it('with no site', () => {
            render(<LessonsPageContainer lessons course department institute />);
            
            expect(container.textContent).toMatch('');
        })

        it('with no institute', () => {
            render(<LessonsPageContainer lessons course department site />);
            
            expect(container.textContent).toMatch('');
        })

        it('with no department', () => {
            render(<LessonsPageContainer lessons course institute site />);
            
            expect(container.textContent).toMatch('');
        })

        it('with no course', () => {
            render(<LessonsPageContainer lessons department institute site />);
            
            expect(container.textContent).toMatch('');
        })

        it('with no lessons', () => {
            render(<LessonsPageContainer course department institute site />);
            
            expect(container.textContent).toMatch('');
        })

    })

    describe('has a banner', () => {
        
        it('with heading', () => {
            render(<Router><LessonsPageContainer lessons={lessons} course={course} department={department} institute={institute} site={site} socialmediadata /></Router>);

            expect(
                container.querySelector('section#banner .inner header h1').textContent
            ).toMatch('KS3 Computing');
        })

        it('with description', () => {
            render(<Router><LessonsPageContainer lessons={lessons} course={course} department={department} institute={institute} site={site} socialmediadata /></Router>);

            expect(
                container.querySelector('section#banner .inner header p').textContent
            ).toMatch('Lorem ipsum dolor sit amet.');
        })
    })

    describe('has breadcrumb', () => {

        it('with home link', () => {
            render(
                <Router>
                    <LessonsPageContainer lessons={lessons} course={course} department={department} institute={institute} site={site} socialmediadata />
                </Router>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(1)').textContent
            ).toEqual('Home');

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(1) > a').getAttribute("href")
            ).toEqual('/');
        })

        it('with current page text only', () => {
            render(
                <Router>
                    <LessonsPageContainer lessons={lessons} course={course} department={department} institute={institute} site={site} socialmediadata />
                </Router>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(2)').textContent
            ).toEqual('KS3 Computing');
        })
    })

    describe('has footer', () => {

        it('with scheme of work name as heading', () => {
            render(<Router><LessonsPageContainer lessons={lessons} course={course} department={department} institute={institute} site={site} socialmediadata /></Router>);

            expect(
                container.querySelector('footer#footer h2').textContent
            ).toMatch('KS3 Computing');
        })

        it('with scheme of work overview summary', () => {
            render(<Router><LessonsPageContainer lessons={lessons} course={course} department={department} institute={institute} site={site} socialmedia /></Router>);

            expect(
                container.querySelector('footer#footer p').textContent
            ).toMatch('Lorem ipsum dolor sit amet.');
        })
    })

    describe('has lessons widget', () => {

        it('with lessons', () => {
            render(<Router><LessonsPageContainer lessons={lessons} course={course} department={department} institute={institute} site={site} socialmedia /></Router>);

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
            ).toMatch("/institute/1276711/department/67/course/76/lesson/1");

            // Last
            expect(
                container.querySelector("#main .inner div.lessons > .box:nth-last-child(1) .inner label.label u").textContent
            ).toMatch("Lesson");

            expect(
                container.querySelector("#main .inner div.lessons > .box:nth-last-child(1) .inner h3").textContent
            ).toMatch("Donec sit amet felis id");

            expect(
                container.querySelector("#main .inner div.lessons > .box:nth-last-child(1) .inner a").getAttribute('href')
            ).toMatch("/institute/1276711/department/67/course/76/lesson/6");
        })
    })
});


