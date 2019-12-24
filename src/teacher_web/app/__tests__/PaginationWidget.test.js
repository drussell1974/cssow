import React from 'react';

import { createContainer } from '../helpers/domManipulators';
import FakeApiService from '../helpers/FakeApiService';

import PaginationWidget, { Mapper } from '../widgets/PaginationWidget';

describe('PaginationWidget', () => {
    let render, container;
    let lessons;

    beforeEach(() => {
        (
            { render, container} = createContainer()
        ),
        lessons = FakeApiService.getLessonEpisodes();
    })

    it('renders empty container', () => {
        render(<PaginationWidget />);

        expect(
            container.textContent
        ).toMatch('');
    })

    it('renders empty container when data items empty', () => {
        render(<PaginationWidget data={ Mapper.TransformLessons([])} />);

        expect(
            container.textContent
        ).toMatch('');
    })
    
    it('shows a single page', () => {
        render(<PaginationWidget data={ Mapper.TransformLessons([lessons[0]])} />);

        expect(
            container.querySelectorAll('ul.pagination li')
        ).toHaveLength(1);
    })

    it('shows multiple pages', () => {
        render(<PaginationWidget data={ Mapper.TransformLessons(lessons)} />);

        expect(
            container.querySelectorAll('ul.pagination li')
        ).toHaveLength(4);
    })

    it.skip('show given number of pages based on page size', () => {
        render(<PaginationWidget data={ Mapper.TransformLessons(lessons)} page={1} pageSize={3} />);

        expect(
            container.querySelectorAll('ul.pagination li')
        ).toHaveLength(2);
    })
})