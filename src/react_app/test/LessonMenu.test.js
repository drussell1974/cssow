import LessonMenu from '../pages/LessonMenu';

import React from 'react';
import ReactDOM from 'react-dom';

describe('lessons', () => {
    let container;

    beforeEach(() => {
        container = document.createElement('div');
    })
    it('renders empty model', () => {    
        ReactDOM.render(<LessonMenu />, container);
        
        expect(container.textContent).toMatch('')
    })
});