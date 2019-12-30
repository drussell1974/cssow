import React from "react";
import ReactTestUtils, { act } from "react-dom/test-utils";

import { createContainer } from "../helpers/domManipulators";
import { spy, setUpSpy, cleanUpSpy } from "../helpers/jest.extend.spy";

import LogInFormWidget from "../widgets/LogInFormWidget";

describe("LoginFormWidget", () => {
    let render, container;

    beforeEach(() => {
        (
            {  render, container } = createContainer()
        );
        setUpSpy();
    });

    afterEach(() => {
        cleanUpSpy();
    })

    it("renders empty component", () => {
        render(<LogInFormWidget />);

        expect(
            container.textContent
        ).toEqual("");
    })

    it("notify when submitted", async () => {

        let formSubmitSpy = spy();

        render(<LogInFormWidget auth={false} onSubmit={formSubmitSpy.fn} />);

        let form = container.querySelector("form");

        await act(async () => {
            ReactTestUtils.Simulate.submit(form);
        });
        
        expect(
            formSubmitSpy
        ).toHaveBeenCalled();

        // ... and returned from values
        expect(formSubmitSpy.receivedArgument(0)).toEqual('/customers');

        const fetchOpts = formSubmitSpy.receivedArgument(1);
        expect(fetchOpts.method).toEqual('POST');
        expect(fetchOpts.credentials).toEqual('same-origin');
        expect(fetchOpts.headers).toEqual({
            'Content-Type': 'application/json'
        });
    })

    describe("email field", () => {
        it("has label", () => {
            render(<LogInFormWidget auth={false} />);

            let elem = container.querySelector("#auth_user_email__row label");

            expect(
                elem.textContent
            ).toEqual("email");

            expect(
                elem.getAttribute("class")
            ).toEqual("form-control-label col-sm-3");
        });

        it("has input", () => {
            render(<LogInFormWidget auth={false} />);

            let elem = container.querySelector("#auth_user_email__row input");
            
            expect(
                elem.getAttribute("name")
            ).toEqual("email");

            expect(
                elem.getAttribute("type")
            ).toEqual("text");

            expect(
                elem.getAttribute("class")
            ).toEqual("form-control string");
        })

        it("has helpblock", () => {
            render(<LogInFormWidget auth={false} />);

            let elem = container.querySelector("#auth_user_email__row span");

            expect(
                elem.getAttribute("class")
            ).toEqual("help-block");

            expect(
                elem.textContent
            ).toEqual("");
        })
    })
    
    describe("password field", () => {
        it("has label", () => {
            render(<LogInFormWidget auth={false} />);

            let elem = container.querySelector("#auth_user_password__row label");

            expect(
                elem.textContent
            ).toEqual("Password");

            expect(
                elem.getAttribute("class")
            ).toEqual("form-control-label col-sm-3");
        });

        it("has input", () => {
            render(<LogInFormWidget auth={false} />);

            let elem = container.querySelector("#auth_user_password__row input");
            
            expect(
                elem.getAttribute("name")
            ).toEqual("password");

            expect(
                elem.getAttribute("type")
            ).toEqual("password");

            expect(
                elem.getAttribute("class")
            ).toEqual("form-control password");
        })

        it("has helpblock", () => {
            render(<LogInFormWidget auth={false} />);

            let elem = container.querySelector("#auth_user_password__row span");

            expect(
                elem.getAttribute("class")
            ).toEqual("help-block");

            expect(
                elem.textContent
            ).toEqual("");
        })
    })

    describe("remember me field", () => {
        it("has label", () => {
            render(<LogInFormWidget auth={false} />);

            let elem = container.querySelector("#auth_user_remember_me__row label");

            expect(
                elem.textContent
            ).toEqual("Remember me (for 30 days)");

            expect(
                elem.getAttribute("class")
            ).toEqual("form-check-label");
        });

        it("has input", () => {
            render(<LogInFormWidget auth={false} />);

            let elem = container.querySelector("#auth_user_remember_me__row input");
            
            expect(
                elem.getAttribute("name")
            ).toEqual("remember_me");

            expect(
                elem.getAttribute("type")
            ).toEqual("checkbox");

            expect(
                elem.getAttribute("class")
            ).toEqual("boolean form-check-input");
        })

        it("has helpblock", () => {
            render(<LogInFormWidget auth={false} />);

            let elem = container.querySelector("#auth_user_remember_me__row span");

            expect(
                elem.getAttribute("class")
            ).toEqual("help-block");

            expect(
                elem.textContent
            ).toEqual("");
        })
    })

    describe("submit button", () => {
        it("has input", () => {
            render(<LogInFormWidget auth={false} />);

            let elem = container.querySelector('#submit_record__row input');

            expect(
                elem.getAttribute("type")
            ).toEqual("submit")

            expect(
                elem.getAttribute("value")
            ).toEqual("Log In")

            expect(
                elem.getAttribute("class")
            ).toEqual("btn btn-primary")
        })
    })
})
