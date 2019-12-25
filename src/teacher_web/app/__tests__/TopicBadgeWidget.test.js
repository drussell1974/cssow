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

    it('renders empty component list1 empty', () => {
        render(<TopicBadgeWidget list1="" />);

        expect(
            container.textContent
        ).toEqual('');
    })

    it('renders empty component if both list1 and list2 are empty', () => {
        render(<TopicBadgeWidget list1="" list2="" />);

        expect(
            container.textContent
        ).toEqual('');
    })
    
    it('has single badge from list1', () => {
        render(<TopicBadgeWidget list1={"Topic1"} />);

        expect(
            container.textContent
        ).toEqual('Topic1');

        expect(
            container.querySelectorAll('.badge-info')
        ).toHaveLength(1);
    })

    it('has single badge from list1 and list2 (ignore duplicate)', () => {
        render(<TopicBadgeWidget list1="Topic1" list2="Topic1" />);

        expect(
            container.textContent
        ).toEqual('Topic1');

        expect(
            container.querySelectorAll('.badge-info')
        ).toHaveLength(1);
    })

    it('has multiple badges from list1', () => {
        render(<TopicBadgeWidget list1="Topic1,Topic2" />);

        expect(
            container.textContent
        ).toEqual('Topic1Topic2');

        expect(
            container.querySelectorAll('.badge-info')
        ).toHaveLength(2);
    })

    it('has multiple badges from list1 when list2 empty', () => {
        render(<TopicBadgeWidget list1="Topic1,Topic2" list2="" />);

        expect(
            container.textContent
        ).toEqual('Topic1Topic2');

        expect(
            container.querySelectorAll('.badge-info')
        ).toHaveLength(2);
    })

    it('has multiple badges from list2 when list1 empty', () => {
        render(<TopicBadgeWidget list1={""} list2={"Topic1,Topic2"} />);

        expect(
            container.textContent
        ).toEqual('Topic1Topic2');

        expect(
            container.querySelectorAll('.badge-info')
        ).toHaveLength(2);
    })

    it('has multiple badges from list1 and list2', () => {
        render(<TopicBadgeWidget list1={"Topic1"} list2={"Topic2"} />);

        expect(
            container.textContent
        ).toEqual('Topic1Topic2');

        expect(
            container.querySelectorAll('.badge-info')
        ).toHaveLength(2);
    })
    
    it('has multiple badges for list1 and list2', () => {
        render(<TopicBadgeWidget list1={"Topic1,Topic2"} list2={"Topic3,Topic4"} />);

        expect(
            container.textContent
        ).toEqual('Topic1Topic2Topic3Topic4');

        expect(
            container.querySelectorAll('.badge-info')
        ).toHaveLength(4);
    })

    it('sort badges for list1 and list2', () => {
        render(<TopicBadgeWidget list1={"Topic4,Topic2"} list2={"Topic3,Topic1"} />);

        expect(
            container.textContent
        ).toEqual('Topic1Topic2Topic3Topic4');

        expect(
            container.querySelectorAll('.badge-info')
        ).toHaveLength(4);
    })

    it('ignore duplicates from different lists', () => {
        render(<TopicBadgeWidget list1={"Topic1,Topic2"} list2={"Topic3,Topic1"} />);

        expect(
            container.textContent
        ).toEqual('Topic1Topic2Topic3');

        expect(
            container.querySelectorAll('.badge-info')
        ).toHaveLength(3);
    })

    it('ignore duplicates from same list', () => {
        render(<TopicBadgeWidget list1={"Topic1,Topic1,Topic2"} list2={"Topic3,Topic2,Topic1,Topic2"} />);

        expect(
            container.textContent
        ).toEqual('Topic1Topic2Topic3');

        expect(
            container.querySelectorAll('.badge-info')
        ).toHaveLength(3);
    })
})