import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import ReactTestUtils from 'react-dom/test-utils';
import { MemoryRouter } from 'react-router-dom';

import { createContainer } from '../helpers/domManipulators';
import { LoginForm } from '../widgets/LoginWidget';

describe("LoginForm", () =>{
    let render, container;

    let socialmediadata = undefined;

    let site = {
        name:"Dave Russell",
        description:"Eu hendrerit felis rhoncus vel. In hac habitasse"
    }

    const validClassCode = {
        class_code: "JKLMNO"
    };
    
    // TODO: read from query string
    // let redirect = { url:"http://localhost/institute/2/department/5/course/11" };

    beforeEach(() => {
        ({render, container} = createContainer(container))
        //fetchSpy = spy();
        //window.fetch = fetchSpy.fn;
    })

    const spy = () => { 
        let receivedArguments;
        //let returnValue;
        //stubReturnValue: value => returnValue = value;

        return {
            fn: (...args) => {
                receivedArguments = args;
                //return returnValue;
            },
            receivedArguments: () => receivedArguments,
            receivedArgument: n => receivedArguments[n]
        };
    };

    it('renders empty model', () => {
        render(
            <MemoryRouter>
                <LoginForm />
            </MemoryRouter>);
        
        expect(container.textContent).toMatch('');
    });


    it('renders a form', () => {
        render(<LoginForm />);
        expect(
            container.querySelector('form[id="frm-login-form"]')
        ).not.toBeNull();
    });

    it('render the heading', () => {
        render(<LoginForm />);
        expect(
            container.querySelector('form[id="frm-login-form"] h2').textContent
        ).toMatch('Enter your class code');
    })

    describe('render link', () => {
        it('with text', () => {
            render(<LoginForm />);
            expect(
                container.querySelector('form[id="frm-login-form"] p a').textContent
            ).toMatch('I am a teacher');
        })

        it.skip('with url', () => {
            render(<LoginForm />);
            expect(
                container.querySelector('form[id="frm-login-form"] p a[href=]').textContent
            ).toMatch('x');
        })
    })

    const form = id => container.querySelector('form[id="frm-login-form"]');
    const field = (name) => form('frm-login-form').elements[name];
    const labelFor = formElement => 
        container.querySelector(`h2[for="${formElement}"]`);
   
    const expectToBeInputFieldOfTypeText = formElement => {
        expect(formElement).not.toBeNull();
        expect(formElement.tagName).toEqual('INPUT');
        expect(formElement.type).toEqual('text');
    }
        
    const itRendersAsATextBox = (fieldName) => 
        it('renders as a text box', () => {
            render(<LoginForm />);
            expectToBeInputFieldOfTypeText(field(fieldName));
        });

    const itIncludesTheExistingValue = (fieldName) => 
        it('includes the existing value', () => {
            render(<LoginForm { ...{[fieldName]:'value'} } />);
            expect(field(fieldName).value).toEqual('value');
        })

    const itRendersAMatchingLabel = (fieldName, id, text) =>
        it('renders a label for the field', () => {
            render(<LoginForm />);
            expect(labelFor(fieldName)).not.toBeNull();
            expect(labelFor(fieldName).textContent).toEqual(text);
            expect(field(fieldName).id).toEqual(id);
        })

    describe('renders class_code field', () => {

        itRendersAMatchingLabel('class_code', 'class_code', 'Enter your class code');

        itRendersAsATextBox('class_code');
    
        itIncludesTheExistingValue('class_code')
    })

    describe('render submit form', () => {

        const originalFetch = window.fetch;
        let fetchSpy;

        it('has a submit button', () => {
            render(<LoginForm />);
            const submitButton = container.querySelector('input[type="submit"]');
            expect(submitButton).not.toBeNull();
        })

        it('calls fetch with the right properties when submitting data', async () => {
            // expect.hasAssertions();

            const fetchSpy = spy();
            render(
                <LoginForm fetch={fetchSpy.fn} />
            );
            
            ReactTestUtils.Simulate.submit(form('frm-login-form'));

            //expect(fetchSpy).toHaveBeenCalled();
            expect(fetchSpy.receivedArgument(0)).toEqual('/customers');
            
            const fetchOpts = fetchSpy.receivedArgument(1);
            expect(fetchOpts.method).toEqual('POST');
            expect(fetchOpts.credentials).toEqual('same-origin');
            expect(fetchOpts.headers).toEqual({
                'Content-Type': 'application/json'
            });
        })

        const itSubmitsExistingValue = fieldName =>
            it.skip('saves existing value when submitted', async () => {
                let submitSpy = spy();

                render(
                    <LoginForm { ...validClassCode } 
                        onSubmit={ submitSpy.fn }
                    />);
                    
                await ReactTestUtils.Simulate.submit(form('frm-login-form'));

                expect(submitSpy).toHaveBeenCalled();
            });

        const itFetchesDataWhenSubmitted = fieldName =>
            it('fetches data when submitted', async () => {
                let fetchSpy = spy();

                render(
                    <LoginForm { ...validClassCode } 
                        fetch={fetchSpy.fn}
                        //onSubmit={() => {}}
                    />);
                    
                await ReactTestUtils.Simulate.submit(form('frm-login-form'));

                const fetchOpts = fetchSpy.receivedArgument(1);
                expect(JSON.parse(fetchOpts.body)[fieldName]).toEqual('JKLMNO');
                //expect(submitSpy).toHaveBeenCalled();
            });

        it.skip('does not submit form when there are validation errors', async () => {
            expect.hasAssertions();
            render(<LoginForm { ...validClassCode }
                // class_code="BCDEFG"
                onSubmit={ ({class_code}) =>
                    expect(class_code).toEqual('JKLMNO')
                }/>);
            await ReactTestUtils.Simulate.submit(form('frm-login-form'));

            expect(window.fetch).not.toHaveBeenCalled();
        })

        itSubmitsExistingValue('class_code');
        
        itFetchesDataWhenSubmitted('class_code');
    })

    expect.extend({
        toHaveBeenCalled(received) {
            if (received.receivedArguments() === undefined) {
                return {
                    pass: false,
                    message: () => 'Spy was not called'
                }
            }
            return { pass: true, message: () => 'Spy was called'};
        }
    });
});


