import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import { LoginPageContainer } from '../pages/LoginPage';

describe("LoginPageContainer", () =>{
    let render, container;

    let socialmediadata = undefined;

    let site = {
        name:"Dave Russell",
        description:"Eu hendrerit felis rhoncus vel. In hac habitasse"
    }
    
    // TODO: read from query string
    let redirect = { url:"http://localhost/institute/2/department/5/course/11" };

    beforeEach(() => {
        (
            {render, container} = createContainer(container)
        )
    })

    it('renders empty model', () => {
        render(
            <MemoryRouter>
                <LoginPageContainer />
            </MemoryRouter>);
        
        expect(container.textContent).toMatch('');
    })

    describe('has a banner', () => {
        
        it('with heading', () => {
            render(
                <MemoryRouter>
                    <LoginPageContainer site={site} redirect={redirect} socialmediadata />
                </MemoryRouter>);

            expect(
                container.querySelector('section#banner .inner header h1').textContent
            ).toMatch('Dave Russell');
        })

        it('with description', () => {
            render(
                <MemoryRouter>
                    <LoginPageContainer site={site} redirect={redirect} socialmediadata />
                </MemoryRouter>);

            expect(
                container.querySelector('section#banner .inner header p').textContent
            ).toMatch('Eu hendrerit felis rhoncus vel. In hac habitasse');
        })
    })

    describe('has breadcrumb', () => {

        it('with home link', () => {
            render(
                <MemoryRouter>
                    <LoginPageContainer site={site} redirect={redirect} socialmediadata />
                </MemoryRouter>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(1) > a').textContent
            ).toEqual('Home');

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(1) a').getAttribute("href")
            ).toEqual('/');
        })


        it.skip('with Course link', () => {
            render(
                <MemoryRouter>
                    <LoginPageContainer site={site} redirect={redirect} socialmediadata />
                </MemoryRouter>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(2)').textContent
            ).toEqual('CPU Architecture');

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(2) > a').getAttribute("href")
            ).toEqual('/course/');
        })

        it.skip('with Lesson link', () => {
            render(
                <MemoryRouter>
                    <LoginPageContainer site={site} redirect={redirect} socialmediadata />
                </MemoryRouter>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(3)').textContent
            ).toEqual('Types of CPU Architecture');

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(3) > a').getAttribute("href")
            ).toEqual('/course/1/lesson/');

        })

        it.skip('with current page text only', () => {
            render(
                <MemoryRouter>
                    <LoginPageContainer site={site} redirect={redirect} socialmediadata />
                </MemoryRouter>);

            expect(
                container.querySelector('nav#breadcrumb-nav > ul > li:nth-child(4)').textContent
            ).toEqual('OCR AS and A Level Computer Science');
        })
    })

    describe('has footer', () => {

        it('with scheme of work name as heading', () => {
            render(
                <MemoryRouter>
                    <LoginPageContainer site={site} redirect={redirect} socialmediadata />
                </MemoryRouter>);

            expect(
                container.querySelector('footer#footer h2').textContent
            ).toMatch('Dave Russell');
        })

        it('with scheme of work overview summary', () => {
            render(
                <MemoryRouter>
                    <LoginPageContainer site={site} redirect={redirect} socialmedia />
                </MemoryRouter>);
            expect(
                container.querySelector('footer#footer p').textContent
            ).toMatch('Eu hendrerit felis rhoncus vel. In hac habitasse');
        })
    })
});


