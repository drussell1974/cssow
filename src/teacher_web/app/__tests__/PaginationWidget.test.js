import React from 'react';
import { createContainer } from '../helpers/domManipulators';

import PaginationWidget from '../widgets/PaginationWidget';

describe('PaginationWidget', () => {
    let render, container;

    beforeEach(() => (
        { render, container} = createContainer()
    ))

    it('renders empty container', () => {
        render(<PaginationWidget />);

        expect(
            container.textContent
        ).toMatch('');
    })

    it('renders empty container when pager items empty', () => {
        render(<PaginationWidget pager={[]} />);

        expect(
            container.textContent
        ).toMatch('');
    })
    
    it('shows a single page', () => {
        render(<PaginationWidget pager={[0]} />);

        expect(
            container.querySelectorAll('ul.pagination li')
        ).toHaveLength(1);

        expect(
            container.querySelector('ul.pagination').textContent
        ).toMatch('1');
    })

    it('shows multiple pages', () => {
        render(<PaginationWidget pager={[0]} />);

        expect(
            container.querySelectorAll('ul.pagination li')
        ).toHaveLength(1);

        expect(
            container.querySelector('ul.pagination').textContent
        ).toMatch('1');
    })
    
})