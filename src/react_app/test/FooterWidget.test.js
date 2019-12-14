import React from 'react';
import ReactDOM from 'react-dom';

import FooterWidget from '../widgets/FooterWidget';

describe('', () => {
    let container;

    beforeEach(() => {
        container = document.createElement('div');
    })

    it('renders empty model', () => {
        ReactDOM.render(<FooterWidget />, container);

        expect(
            container.textContent
        ).toMatch('');
    })

    it('has a heading', () => {
        ReactDOM.render(<FooterWidget heading='Etiam veroeros lorem' summary='' />, container);

        expect(
            container.querySelector('footer#footer h2').textContent
        ).toMatch('Etiam veroeros lorem');
    })

    it('has a summary', () => {
        ReactDOM.render(<FooterWidget heading='' summary='Pellentesque eleifend malesuada efficitur. Curabitur volutpat dui mi, ac imperdiet dolor tincidunt nec. Ut erat lectus, dictum sit amet lectus a, aliquet rutrum mauris. Etiam nec lectus hendrerit, consectetur risus viverra, iaculis orci. Phasellus eu nibh ut mi luctus auctor. Donec sit amet dolor in diam feugiat venenatis.' />, container);

        expect(
            container.querySelector('footer#footer p').textContent
        ).toMatch('Pellentesque eleifend malesuada efficitur. Curabitur volutpat dui mi, ac imperdiet dolor tincidunt nec. Ut erat lectus, dictum sit amet lectus a, aliquet rutrum mauris. Etiam nec lectus hendrerit, consectetur risus viverra, iaculis orci. Phasellus eu nibh ut mi luctus auctor. Donec sit amet dolor in diam feugiat venenatis.');
    })

    it('shows no social media links when undefined', () => {
        let socialmediadata = undefined

        ReactDOM.render(<FooterWidget heading='' summary='' socialmedia={socialmediadata} />, container);

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
        
        ReactDOM.render(<FooterWidget heading='' summary='' socialmedia={socialmediadata} />, container);

        expect(
            container.querySelectorAll('footer#footer .icons li')
        ).toHaveLength(4);
    })
})