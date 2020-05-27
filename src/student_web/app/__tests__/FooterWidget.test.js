import React from 'react';
import ReactDOM from 'react-dom';

import { createContainer } from '../helpers/domManipulators';
import FooterWidget from '../widgets/FooterWidget';

describe('FooterWidget', () => {
    let render, container;

    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(<FooterWidget />);

        expect(
            container.textContent
        ).toMatch('');
    })

    it('has a heading', () => {
        render(<FooterWidget heading='Etiam veroeros lorem' summary='' />);

        expect(
            container.querySelector('footer#footer h2').textContent
        ).toMatch('Etiam veroeros lorem');
    })

    it('has a summary', () => {
        render(<FooterWidget heading='' summary='Pellentesque eleifend malesuada efficitur. Curabitur volutpat dui mi, ac imperdiet dolor tincidunt nec. Ut erat lectus, dictum sit amet lectus a, aliquet rutrum mauris. Etiam nec lectus hendrerit, consectetur risus viverra, iaculis orci. Phasellus eu nibh ut mi luctus auctor. Donec sit amet dolor in diam feugiat venenatis.' />);

        expect(
            container.querySelector('footer#footer p').textContent
        ).toMatch('Pellentesque eleifend malesuada efficitur. Curabitur volutpat dui mi, ac imperdiet dolor tincidunt nec. Ut erat lectus, dictum sit amet lectus a, aliquet rutrum mauris. Etiam nec lectus hendrerit, consectetur risus viverra, iaculis orci. Phasellus eu nibh ut mi luctus auctor. Donec sit amet dolor in diam feugiat venenatis.');
    })

    it('shows no social media links when undefined', () => {
        let socialmediadata = undefined

        render(<FooterWidget heading='' summary='' socialmedia={socialmediadata} />);

        expect(
            container.querySelectorAll('footer#footer .icons li')
        ).toHaveLength(0);
    })

    it('shows social media links', () => {
        let socialmediadata = [
            {
                "name":"Twitter",
                "iconClass":"icon fa-twitter",
                "url":"http://twitter.com",
            },
            {
                "name":"Facebook",
                "iconClass":"icon fa-facebook",
                "url":"http://www.facebook.com",
            },
            {
                "name":"Instagram",
                "iconClass":"icon fa-instagram",
                "url":"http://www.instagram.com",
            },
            {
                "name":"Email",
                "iconClass":"icon fa-envelope",
                "url":"mail://noaddress@example.com",
            },
        ];
        
        render(<FooterWidget heading='' summary='' socialmedia={socialmediadata} />);

        expect(
            container.querySelectorAll('footer#footer .icons li')
        ).toHaveLength(4);
    })
})