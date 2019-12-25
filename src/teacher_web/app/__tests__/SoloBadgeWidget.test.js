import React from 'react';

import { createContainer } from '../helpers/domManipulators';

import SoloBadgeWidget from '../widgets/SoloBadgeWidget';

describe('SoloBadgeWidget', () => {
    let render, container;

    beforeEach(() => (
        {render, container} = createContainer()
    ))

    it('renders empty component', () => {
        render(<SoloBadgeWidget />);

        expect(
            container.querySelector('i')
        ).toBeNull();
    })

    it('renders empty component for invalid solo_taxonomy_level', () => {
        render(<SoloBadgeWidget solo_taxonomy_level='x' />);

        expect(
            container.querySelector('i')
        ).toBeNull();
    })

    it('renders xxx for solo_taxonomy_level A', () => {
        render(<SoloBadgeWidget solo_taxonomy_level='A' />);

        expect(
            container.querySelector('i')
        ).toBeNull();
    })

    it('renders star icon for solo_taxonomy_level B', () => {
        render(<SoloBadgeWidget solo_taxonomy_level='B' />);

        expect(
            container.querySelector('i').getAttribute('class')
        ).toEqual('far fa-star');
    })

    
    it('renders star icon for solo_taxonomy_level C', () => {
        render(<SoloBadgeWidget solo_taxonomy_level='C' />);

        expect(
            container.querySelector('i').getAttribute('class')
        ).toEqual('fas fa-star');
    })
    
    it('renders trophy icon for solo_taxonomy_level D', () => {
        render(<SoloBadgeWidget solo_taxonomy_level='D' />);

        expect(
            container.querySelector('i').getAttribute('class')
        ).toEqual('fas fa-trophy');
    })
})