import React from 'react';

import { createContainer } from '../helpers/domManipulators';

import TopicBadgeWidget from '../widgets/TopicBadgeWidget';

describe('TopicBadgeWidget', () => {
    let render, container;

    beforeEach(() => (
        { render, container} = createContainer()
    ))  

    it('renders empty component', () => {
        render(<TopicBadgeWidget />);

        expect(
            container.textContent
        ).toEqual('');
    })

    it('renders empty component if list empty', () => {
        render(<TopicBadgeWidget list1={[]} />);

        expect(
            container.textContent
        ).toEqual('');
    })
})