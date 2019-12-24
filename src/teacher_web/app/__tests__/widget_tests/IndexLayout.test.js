import React from 'react';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../../helpers/domManipulators';
import FakeApiService from '../../helpers/FakeApiService';

import { IndexLayout } from '../../pages/Index';

describe('IndexLayout', () => {
    let render, container;

    let contentRow;
    let schemesofwork;

    beforeEach(() => {
        (
            { render, container } = createContainer()
        )
    })

    it('has single column', () => {
        render(<IndexLayout data={[]} />);

        expect(
            container.querySelector('.container .row > .col-lg-8, .col-md-8, .mx-auto')
        ).not.toBeNull();
    })

    it('has latest schemes of work', () => {
        
        schemesofwork = FakeApiService.getSchemesOfWork();
        
        render(
            <Router>
                <IndexLayout data={schemesofwork} />
            </Router>);

        expect(
            container.querySelectorAll('.post-preview')
        ).toHaveLength(3);
    })
})