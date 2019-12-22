import React from 'react';
import ReactDOM from 'react-dom';

import { createContainer } from '../helpers/domManipulators';
import SignInWidget from '../widgets/SignInWidget';

describe('SignInWidget', () => {
    
    let render, container;

    beforeEach(() => {
     (
        { render, container } = createContainer()
     )
    })

    it('renders empty component', () => {
        render(<SignInWidget />);

        expect(
            container.textContent
        ).not.toMatch('LoginSign upLost password');
    })

    it('log in options when explicitly NOT authenticated', () => {
        render(<SignInWidget auth={false} />);

        expect(
            container.querySelector('.login').textContent
        ).toMatch('Login');

        expect(
            container.querySelector('.register').textContent
        ).toMatch('Sign up');
        
        expect(
            container.querySelector('.retrieve-password').textContent
        ).toMatch('Lost password');
    })

    it('log in options when explicitly authenticated', () => {
        
        // TODO: Find best way to authenticate with react (api callback)
        
        render(<SignInWidget auth={true} />);

        expect(
            container.querySelector('.profile').textContent
        ).toMatch('Profile');

        expect(
            container.querySelector('.change-password').textContent
        ).toMatch('Change password');
        
        expect(
            container.querySelector('.logout').textContent
        ).toMatch('Logout');
    })
})