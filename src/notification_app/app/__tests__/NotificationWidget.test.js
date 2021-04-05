import React from 'react';
import ReactDOM from 'react-dom';

import { createContainer } from '../helpers/domManipulators';
import NotificationWidget from '../widgets/NotificationWidget';

describe('NotificationWidget', () => {
    let render, container;

    beforeEach(() => {
        ({render, container} = createContainer());
    })

    it('renders empty model', () => {
        render(<NotificationWidget />);

        expect(
            container.textContent
        ).toMatch('');
    })

    it('renders single message', () => {
        let messages=[{"id": 1, "message":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce nec elit quis lorem semper rutrum quis sed turpis.", "action":"http://localhost/dosomething/1" }]
        render(<NotificationWidget messages={messages} />);

        expect(
            container.querySelector('#dropdownNotificationsMenuButton').textContent
        ).toMatch('1');
        
        expect(
            container.querySelector('.alert .dropdown-menu .dropdown-item').textContent
        ).toMatch('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce nec elit quis lorem semper rutrum quis sed turpis.');
    
        expect(
            container.querySelector('.alert .dropdown-menu .dropdown-item').getAttribute('href')
        ).toMatch('http://localhost/dosomething/1');
    })

    it('renders multiple messages', () => {
        let messages=[
            {"id": 1, "message":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce nec elit quis lorem semper rutrum quis sed turpis.", "action":"http://localhost/dosomething/1" },
            {"id": 2, "message":"Suspendisse semper neque diam, posuere facilisis quam vulputate eu. In et lorem mi.", "action":"http://localhost/dosomething/2" },
            {"id": 3, "message":"Nulla vulputate nisi at ipsum porttitor, sit amet sagittis ipsum convallis. Donec lacinia diam vel euismod aliquam. Nulla molestie iaculis augue ut ultricies. Maecenas in finibus lorem.", "action":"http://localhost/dosomething/3" }
        ]
        render(<NotificationWidget messages={messages} />);

        expect(
            container.querySelector('#dropdownNotificationsMenuButton').textContent
        ).toMatch('3');
        
        expect(
            container.querySelector('.alert .dropdown-menu .dropdown-item:first-child').textContent
        ).toMatch('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce nec elit quis lorem semper rutrum quis sed turpis.');

        expect(
            container.querySelector('.alert .dropdown-menu .dropdown-item:last-child').textContent
        ).toMatch('Nulla vulputate nisi at ipsum porttitor, sit amet sagittis ipsum convallis. Donec lacinia diam vel euismod aliquam. Nulla molestie iaculis augue ut ultricies. Maecenas in finibus lorem.');
    
        expect(
            container.querySelector('.alert .dropdown-menu .dropdown-item:first-child').getAttribute('href')
        ).toMatch('http://localhost/dosomething/1');

        expect(
            container.querySelector('.alert .dropdown-menu .dropdown-item:last-child').getAttribute('href')
        ).toMatch('http://localhost/dosomething/3');
    })
})