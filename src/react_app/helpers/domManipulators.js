import React from 'react';
import ReactDOM from 'react-dom';
import { MemoryRouter } from 'react-router-dom';

export const createContainer = () => {
    const container = document.createElement('div');

    return {
        render: component => ReactDOM.render(
                component
            , container),
        container
    };
};