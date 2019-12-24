import React from 'react';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../../helpers/domManipulators';
import FakeApiService from '../../helpers/FakeApiService';

import { LessonPageLayout } from '../../pages/Lesson';

describe('LessonPageLayout', () => {
    let render, container;
    let lesson, lessons;

    const getContentHeading = function() {
        return container.querySelector("div.container > .col-lg-12, .col-md-14, .content-heading");
    }

    const getLeftColumm = function() {
        return container.querySelector("div.container > div.col-lg-4, div.col-md-4");
    }

    const getMainContent = function() {
        return container.querySelector("div.container > div.col-lg-8, div.col-md-10, div.mx-auto");
    }

    beforeEach(() => {
        (
            { render, container } = createContainer()
        )
    })

    it('renders empty content', () => {
        render(<LessonPageLayout />);

        expect(
            getContentHeading().textContent
        ).toEqual('');

        expect(
            getLeftColumm().textContent
        ).toEqual('');

        expect(
            getMainContent().textContent
        ).toEqual('');
    })

    it('has two columns', () => {
        render(<LessonPageLayout lessons={[]} lesson={[]}/>);

        expect(
            getContentHeading()
        ).not.toBeNull();

        expect(
            getLeftColumm()
        ).not.toBeNull();

        expect(
            getMainContent()
        ).not.toBeNull();
    })
})