import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import { SchemeOfWorkPageContainer } from '../pages/SchemeOfWorkPage';

describe("SchemeOfWorkPageContainer", () =>{
    let render, container;

    let socialmediadata = undefined;

    let site = {
        name:"Dave Russell",
        description:"Eu hendrerit felis rhoncus vel. In hac habitasse"
    }

    let schemesofwork = [
        {
            id: 76,
            name: "KS3 Computing",
            description: "Lorem ipsum dolor sit amet."
        },
        {
            id: 127,
            name: "GCSE Computer Science 9-1",
            description: " "
        },
        {
            id: 11,
            name: "A-Level Computer Science",
            description: "Computing curriculum for A-Level"
        }
    ]
    
    beforeEach(() => {
        (
            {render, container} = createContainer(container)
        )
    })

    it('renders empty model', () => {
        render(<SchemeOfWorkPageContainer />);
        
        expect(container.textContent).toMatch('');
    })

    describe('has a banner', () => {
        
        it('with heading', () => {
            render(<Router><SchemeOfWorkPageContainer site={site} schemesofwork={schemesofwork} socialmediadata /></Router>);

            expect(
                container.querySelector('section#banner .inner header h1').textContent
            ).toMatch('Dave Russell');
        })

        it('with description', () => {
            render(<Router><SchemeOfWorkPageContainer site={site} schemesofwork={schemesofwork} socialmediadata /></Router>);

            expect(
                container.querySelector('section#banner .inner header p').textContent
            ).toMatch('Eu hendrerit felis rhoncus vel. In hac habitasse');
        })
    })

    describe('has footer', () => {

        it('with scheme of work name as heading', () => {
            render(<Router><SchemeOfWorkPageContainer schemesofwork={schemesofwork} site={site} socialmediadata /></Router>);

            expect(
                container.querySelector('footer#footer h2').textContent
            ).toMatch('Dave Russell');
        })

        it('with scheme of work overview summary', () => {
            render(<Router><SchemeOfWorkPageContainer schemesofwork={schemesofwork} site={site} socialmedia /></Router>);

            expect(
                container.querySelector('footer#footer p').textContent
            ).toMatch('Eu hendrerit felis rhoncus vel. In hac habitasse');
        })
    })

    describe('has schemeofwork widget', () => {

        it('with courses', () => {
            render(<Router><SchemeOfWorkPageContainer schemesofwork={schemesofwork} site={site} socialmedia /></Router>);

            // Heading
            expect(
                container.querySelector("#main .inner h2").textContent
            ).toMatch('Courses');

            // First
            expect(
                container.querySelector("#main .inner div.lessons > .box:nth-child(1) .inner label.label u").textContent
            ).toMatch("Course");

            expect(
                container.querySelector("#main .inner div.lessons > .box:nth-child(1) .inner h3").textContent
            ).toMatch("KS3 Computing");

            // Last
            expect(
                container.querySelector("#main .inner div.lessons > .box:nth-last-child(1) .inner label.label u").textContent
            ).toMatch("Course");

            expect(
                container.querySelector("#main .inner div.lessons > .box:nth-last-child(1) .inner h3").textContent
            ).toMatch("A-Level Computer Science");

        })
    })
});


