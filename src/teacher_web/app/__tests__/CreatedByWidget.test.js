import React from 'react';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import FakeApiService from '../helpers/FakeApiService';

import CreatedByWidget from '../widgets/CreatedByWidget';

describe('CreatedByWidget', () => {

    let render, container;

    let learningEpisode;

    beforeEach(()=> {
        (
            { render, container} = createContainer()
        ),
        learningEpisode = FakeApiService.getLessonEpisode()
    })
        
    it('renders empty component', () => {
        render(<CreatedByWidget />);

        expect(
            container.textContent
        ).toEqual('');
    })
    
    it('shows created by when NOT authorised', () => {
        render(<CreatedByWidget row={learningEpisode} auth={false} />);

        expect(
            container.querySelector('p.post-meta').textContent
        ).toEqual('Created by Dave Russell 2019-12-23T10:17:00 Learning objectives 2');
    })

    it('shows created by when IS authorised and published', () => {
        let request = { url: '/schemeofwork/127'};

        render(<Router>
            <CreatedByWidget row={learningEpisode} auth={true} request={request} />
        </Router>);

        expect(
            container.querySelector('p.post-meta').textContent
        ).not.toEqual('Publish');

        expect(
            container.querySelector('p.post-meta a.delete').textContent
        ).toEqual('Delete');

        expect(
            container.querySelector('p.post-meta a.edit').textContent
        ).toEqual('Edit');
        
        expect(
            container.querySelector('p.post-meta a.copy').textContent
        ).toEqual('Copy');   
    })
})