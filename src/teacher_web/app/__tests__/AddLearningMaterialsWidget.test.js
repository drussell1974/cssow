import React from 'react';
import { MemoryRouter as Router } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import AddLearningMaterialsWidget from '../widgets/AddLearningMaterialsWidget';

describe('AddLearningMaterialsWidget', () => {
    let render, container;

    beforeEach(() => {
        (
            {render, container} = createContainer()
        )
    })

    it('renders empty component', () => {
        render(
            <Router>
                <AddLearningMaterialsWidget />
            </Router>);
        
        expect(
            container.textContent
        ).toMatch('');
    })

    it.skip('has content', () => {
        render(
            <Router>
                <AddLearningMaterialsWidget scheme_of_work_id={12} />
            </Router>);

        expect(
            container.querySelector('section.alert div#div-references').textContent
        ).not.toMatch('TODO: get references for editing');
    })

    it('has link to add learning materials', () => {
        render(
            <Router>
                <AddLearningMaterialsWidget scheme_of_work_id={12} return_url='/learningepisode' />
            </Router>);

        expect(
            container.querySelector('section.alert a#add-reference').textContent
        ).toMatch('Add learning materials');

        expect(
            container.querySelector('section.alert a#add-reference').getAttribute('href')
        ).toMatch('/reference:/12?_next=/learningepisode');

    })
})