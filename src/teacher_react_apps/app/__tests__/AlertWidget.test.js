import React from 'react';
import ReactDOM from 'react-dom';

import { createContainer } from '../helpers/domManipulators';
import AlertWidget from '../widgets/AlertWidget';

describe('AlertWidget', () => {
    let render, container;

    beforeEach(() => {
        ({render, container} = createContainer());
    })

    let deleteMessageCallback = () => {
        
    }

    it('renders empty model', () => {
        render(<AlertWidget />);

        expect(
            container.textContent
        ).toMatch('');
    })

    it('renders single message', () => {
        
        let messages={
            1: {"id": 1, "notify_message":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce nec elit quis lorem semper rutrum quis sed turpis.", "action":"http://localhost/dosomething/1" }
        }
        
        render(<AlertWidget messages={messages} deleteMessageCallback={deleteMessageCallback} />);
        
        expect(
            container.querySelector('.alert strong').textContent
        ).toMatch('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce nec elit quis lorem semper rutrum quis sed turpis.');
    
        expect(
            container.querySelector('.alert .alert-link').getAttribute('href')
        ).toMatch('http://localhost/dosomething/1');

        expect(
            container.querySelector('.alert .alert-link').textContent
        ).toMatch('action now');
    })

    it('renders multiple messages', () => {
        

        let messages={
            1: {"id": 1, "notify_message":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce nec elit quis lorem semper rutrum quis sed turpis.", "action":"http://localhost/dosomething/1" },
            2: {"id": 2, "notify_message":"Suspendisse semper neque diam, posuere facilisis quam vulputate eu. In et lorem mi.", "action":"http://localhost/dosomething/2" },
            3: {"id": 3, "notify_message":"Nulla vulputate nisi at ipsum porttitor, sit amet sagittis ipsum convallis. Donec lacinia diam vel euismod aliquam. Nulla molestie iaculis augue ut ultricies. Maecenas in finibus lorem.", "action":"http://localhost/dosomething/3" }
        }

        render(<AlertWidget messages={messages} deleteMessageCallback={deleteMessageCallback} />);

        expect(
            container.querySelector('.alert:first-child strong').textContent
        ).toMatch('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce nec elit quis lorem semper rutrum quis sed turpis.');

        expect(
            container.querySelector('.alert:first-child .alert-link').textContent
        ).toMatch('action now');
    
        expect(
            container.querySelector('.alert:first-child .alert-link').getAttribute('href')
        ).toMatch('http://localhost/dosomething/1');

        expect(
            container.querySelector('.alert:last-child strong').textContent
        ).toMatch('Nulla vulputate nisi at ipsum porttitor, sit amet sagittis ipsum convallis. Donec lacinia diam vel euismod aliquam. Nulla molestie iaculis augue ut ultricies. Maecenas in finibus lorem.');
    
        expect(
            container.querySelector('.alert:last-child .alert-link').textContent
        ).toMatch('action now');

        expect(
            container.querySelector('.alert:last-child .alert-link').getAttribute('href')
        ).toMatch('http://localhost/dosomething/3');
    })
})