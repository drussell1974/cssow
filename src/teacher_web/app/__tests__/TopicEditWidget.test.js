import React from 'react';

import { createContainer } from '../helpers/domManipulators';
import FakeApiService from '../helpers/FakeApiService';

import TopicEditWidget from '../widgets/TopicEditWidget';

describe('TopicEditWidget', () => {
    let render, container;

    let learningEpisode;

    beforeEach(() => {
        (
            {render, container} = createContainer()
        ),
        learningEpisode = FakeApiService.getLessonEpisode()
    })

    it('renders empty component', ()=> {
        render(<TopicEditWidget />);

        expect(
            container.textContent
        ).toEqual('');
    })

    it('renders empty component if NOT authorised', ()=> {
        render(<TopicEditWidget row={learningEpisode} auth={false} />);

        expect(
            container.textContent
        ).toEqual('');
    })
})