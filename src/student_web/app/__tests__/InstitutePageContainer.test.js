import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import { InstitutePageContainer } from '../pages/InstitutePage';

describe("InstitutePageContainer", () =>{
    let render, container;

    let socialmediadata = undefined;

    let site = {
        name:"Dave Russell",
        description:"Eu hendrerit felis rhoncus vel. In hac habitasse"
    }

    let institutes = [
        {
            id: 10343434075976,
            name: "Lorem Ipsum",
            description: "Lorem ipsum, Lorem Ipsum"
        },
        {
            id: 1034343127,
            name: "Sit Amet",
            description: " "
        },
        {
            id: 1099742911,
            name: "Dolor sit Amet",
            description: "Lorem Ipsum, Dolor sit Amet"
        }
    ]
    
    beforeEach(() => {
        (
            {render, container} = createContainer(container)
        )
    })

    it('renders empty model', () => {
        render(<InstitutePageContainer />);
        
        expect(container.textContent).toMatch('');
    })

    describe('has a banner', () => {
        
        it('with heading', () => {
            render(<Router><InstitutePageContainer site={site} institutes={institutes} socialmediadata /></Router>);

            expect(
                container.querySelector('section#banner .inner header h1').textContent
            ).toMatch('Dave Russell');
        })

        it('with description', () => {
            render(<Router><InstitutePageContainer site={site} institutes={institutes} socialmediadata /></Router>);

            expect(
                container.querySelector('section#banner .inner header p').textContent
            ).toMatch('Eu hendrerit felis rhoncus vel. In hac habitasse');
        })
    })


    describe('has breadcrumb', () => {

        it('with current page text only', () => {
            render(<Router><InstitutePageContainer site={site} institutes={institutes} socialmediadata /></Router>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(1)').textContent
            ).toEqual('Home');
        })
    })

    describe('has footer', () => {

        it('with scheme of work name as heading', () => {
            render(<Router><InstitutePageContainer institutes={institutes} site={site} socialmediadata /></Router>);

            expect(
                container.querySelector('footer#footer h2').textContent
            ).toMatch('Dave Russell');
        })

        it('with scheme of work overview summary', () => {
            render(<Router><InstitutePageContainer institutes={institutes} site={site} socialmedia /></Router>);

            expect(
                container.querySelector('footer#footer p').textContent
            ).toMatch('Eu hendrerit felis rhoncus vel. In hac habitasse');
        })
    })

    describe('has institute widget', () => {

        it('with institutes', () => {
            render(<Router><InstitutePageContainer institutes={institutes} site={site} socialmedia /></Router>);

            // Heading
            expect(
                container.querySelector("#main .inner h2").textContent
            ).toMatch('Institutes');

            // First
            expect(
                container.querySelector("#main .inner div.institutes > .box:nth-child(1) .inner label.label u").textContent
            ).toMatch("Institute");

            expect(
                container.querySelector("#main .inner div.institutes > .box:nth-child(1) .inner h3").textContent
            ).toMatch("Lorem Ipsum");

            // Last
            expect(
                container.querySelector("#main .inner div.institutes > .box:nth-last-child(1) .inner label.label u").textContent
            ).toMatch("Institute");

            expect(
                container.querySelector("#main .inner div.institutes > .box:nth-last-child(1) .inner h3").textContent
            ).toMatch("Dolor sit Amet");

        })
    })
});


