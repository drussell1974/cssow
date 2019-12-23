import React from 'react';
//import { MemoryRouter as Router } from 'react-router-dom';import { createContainer } from '../helpers/domManipulators';
import { createContainer } from '../helpers/domManipulators';
import FakeApiService from '../helpers/FakeApiService';

import TopicGroupHeadingWidget from '../widgets/TopicGroupHeadingWidget';

describe('GroupHeadingWidget', () => {
    let render, container;

    let learningEpisode;

    beforeEach(()=> {
        (
            { render, container} = createContainer()
        ),
        learningEpisode = FakeApiService.getLessonEpisode()
    })
    
    it('renders empty component', () => {
        render(<TopicGroupHeadingWidget />);

        expect(
            container.textContent
        ).toEqual('');
    })

    it('renders empty component when topic same as current topic', () => {
        render(<TopicGroupHeadingWidget row={learningEpisode} current_topic_name='Hardware' />);

        expect(
            container.textContent
        ).toEqual('');
    })

    it('renders empty component when topic same as current topic (ignore casing)', () => {
        render(<TopicGroupHeadingWidget row={learningEpisode} current_topic_name='hardware' />);

        expect(
            container.textContent
        ).toEqual('')
    
    })

    it('shows topic heading if topic changes', () => {
        render(<TopicGroupHeadingWidget row={learningEpisode} current_topic_name='Software' />);

        expect(
            container.querySelector('h1.group-heading').textContent
        ).toMatch('Hardware')    
    })

    it('shows year name in heading if topic changes', () => {
        render(<TopicGroupHeadingWidget row={learningEpisode} current_topic_name='Software' />);

        expect(
            container.querySelector('h1.group-heading').textContent
        ).toEqual('Year 10 Hardware')    
    })
})
