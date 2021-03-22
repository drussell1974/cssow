import 'whatwg-fetch';
import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import ReactTestUtils, { act } from 'react-dom/test-utils';
import { MemoryRouter, useHistory } from 'react-router-dom';
import { createContainer, withEvent } from '../helpers/domManipulators';
import { LoginForm } from '../widgets/LoginWidget';
import  { 
    fetchResponseOK,
    fetchResponseError, 
    requestBodyOf 
} from '../helpers/spyHelpers';

describe("LoginForm", () =>{
    let render, 
        container, 
        form, 
        field, 
        labelFor,
        element, 
        elements, 
        change, 
        submit;
    
    let fetchSpy;

    let socialmediadata = undefined;

    let site = {
        name:"Dave Russell",
        description:"Eu hendrerit felis rhoncus vel. In hac habitasse"
    }

    const validClassCode = {
        class_code: "JKLMNO"
    };
    
    //const originalFetch = window.fetch;
    
    beforeEach(() => {
        ({
            render, 
            container,
            form,
            field,
            labelFor,
            element,
            elements,
            change,
            submit
        } = createContainer(container));
        //fetchSpy = jest.fn(() => fetchResponseOK()) // spy();
        //window.fetch = fetchSpy //.fn;
        //fetchSpy.stubReturnValue(fetchResponseOK());
        jest
            .spyOn(window, 'fetch')
            .mockReturnValue(fetchResponseOK({}));
        
    })
   
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
   
    const expectToBeInputFieldOfTypeText = formElement => {
        expect(formElement).not.toBeNull();
        expect(formElement.tagName).toEqual('INPUT');
        expect(formElement.type).toEqual('text');
    }
        
    const itRendersAsATextBox = (fieldName) => 
        it('renders as a text box', () => {
            render(<LoginForm />);
            expectToBeInputFieldOfTypeText(field('frm-login-form', fieldName));
        });

    const itIncludesTheExistingValue = (fieldName) => 
        it('includes the existing value', () => {
            render(<LoginForm { ...{[fieldName]:'value'} } />);
            expect(field('frm-login-form', fieldName).value).toEqual('value');
        })

    const itRendersAMatchingLabel = (fieldName, id, text) =>
        it('renders a label for the field', () => {
            render(<LoginForm />);
            expect(labelFor(fieldName)).not.toBeNull();
            expect(labelFor(fieldName).textContent).toEqual(text);
            expect(field('frm-login-form', fieldName).id).toEqual(id);
        })

    describe('renders class_code field', () => {

        itRendersAMatchingLabel('class_code', 'class_code', 'Enter your class code');

        itRendersAsATextBox('class_code');
    
        itIncludesTheExistingValue('class_code')
    })

    describe('submit form', () => {

    beforeEach(() => {
        jest
            .spyOn(window, 'fetch')
            .mockReturnValue(fetchResponseOK({}));
    })
    
    afterEach(() => {
        window.fetch.mockRestore(); // = originalFetch;
    })
        it('has a submit button', () => {
            render(<LoginForm />);
            const submitButton = container.querySelector('input[type="submit"]');
            expect(submitButton).not.toBeNull();
        })

        it('calls fetch with the right properties when submitting data', async () => {

            // Mock redirect
            
            // https://medium.com/@chris.marshall/mocking-read-only-functions-which-return-functions-in-jest-enzyme-4d2f2a97c168
            const push = jest.fn();
            
            LoginForm.redirectToLesson = jest.fn(() => {
                push
            });

            const lesson = { id: 123 };
            window.fetch.mockReturnValue(fetchResponseOK(lesson));
            
            render(<LoginForm  
                    { ...validClassCode } 
                    onSave={ window.fetch }
                />);
            
            await act(async () => {
                submit(form('frm-login-form'));
            });
            
            expect(window.fetch).toHaveBeenCalled();
            /*
            expect(fetchSpy).toHaveBeenCalledWith(
                '/lessons/schedule/ABCDEF',
                expect.objectContaining({
                    method:'POST',
                    credentials:'same-origin',
                    headers: { 'Content-Type': 'application/json'}
                }));
            */
        })

        const itSubmitsExistingValue = fieldName =>
            it.skip('saves existing value when submitted', async () => {


                render(
                    <LoginForm { ...{[fieldName]: 'value'} } />);
                  
                submit(form('frm-login-form'));
                
                expect(requestBodyOf(window.fetch)).toMatchObject({
                    [fieldName]: 'value'
                })
            });

        const itFetchesDataWhenSubmitted = fieldName =>
            it.skip('saves new value when submitted', async () => {
                
                render(
                    <LoginForm 
                        {...{ [fieldName]: 'value'}}
                        //onSave={fetchSpy}
                    />);

                await act(async () => {
                    change(
                        field('frm-login-form', fieldName), 
                        withEvent(fieldName, 'newValue')
                        //{target: { value: 'newValue', name: fieldName }}
                    );
                })

                submit(form('frm-login-form'));
                
                expect(requestBodyOf(window.fetch)).toMatchObject({
                    [fieldName]: 'newValue'
                });
            });

        it.skip('does not submit form when there are validation errors', async () => {
            
            render(<LoginForm  
                    { ...{class_code: ""} } 
                    onSave={fetchSpy} 
                />);

            submit(form('frm-login-form'));

            expect(fetchSpy).not.toHaveBeenCalled();
        })

        it('does not submit form when there are validation errors', async () => {
            
            render(<LoginForm  
                    { ...{class_code: ""} } 
                    onSave={window.fetch} 
                />);

            submit(form('frm-login-form'));

            expect(window.fetch).not.toHaveBeenCalled();
        })

        it.skip('notifies onSave when form is submitted', async () => {
            const lesson = { id: 123 };
            window.fetch.mockReturnValue(fetchResponseOK(lesson));
            
            const saveSpy = jest.fn(); //spy();
            
            render(<LoginForm 
                    { ...validClassCode } 
                    onSave={saveSpy} //.fn} 
                />);

            await act(async () => {
                submit(form('frm-login-form'));
            })
            
            expect(window.fetch).toHaveBeenCalled();
            /*expect(saveSpy).toHaveBeenCalledWith(lesson);*/
        })

        it('it does not notify onSave if POST request returns an error', async () => {
            
            window.fetch.mockReturnValue(fetchResponseError());

            const saveSpy = jest.fn(); //spy();

            render(<LoginForm onSave={saveSpy} />);
            await act(async () => {
                submit(form('frm-login-form'));
            })

            expect(saveSpy).not.toHaveBeenCalled();
        })

        it('prevents the default action when submitting the form', async () => {
            const preventDefaultSpy = jest.fn(); //spy();

            render(<LoginForm onSave={window.fetch} />);

            await act(async () => {
                submit(form('frm-login-form'), {
                    preventDefault: preventDefaultSpy //.fn
                })
            })
            expect(preventDefaultSpy).toHaveBeenCalled();
        })

        it('renders error message when fetch call fails', async () => {
            window.fetch.mockReturnValue(fetchResponseError());
            
            render(<LoginForm
                { ...validClassCode } />);

            await act(async () => {
                submit(form('frm-login-form'));
            })

            expect(element('.error')).not.toBeNull();
            expect(element('.error').textContent).toMatch('Class code must be 6 letters and numbers. Please ensure they match correctly.');
        })
  
        itSubmitsExistingValue('class_code');
        
        itFetchesDataWhenSubmitted('class_code');
    })
});