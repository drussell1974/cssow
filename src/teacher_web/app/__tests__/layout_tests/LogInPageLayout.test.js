import React from 'react';

import { createContainer } from '../../helpers/domManipulators';

import LogInPageLayout from '../../pages/LogInPage';

describe("LogInPageLayout", () => {
    let render, container;

    beforeEach(() => (
        { render, container } = createContainer()
    ))

    it("has single column", () => {
        render(<LogInPageLayout />);

        expect(
            container.querySelector(".col-lg-8, .col-md-10, .mx-auto").textContent
        ).not.toBeNull();
    })
    
    it("has register link", () => {
        render(<LogInPageLayout />);

        expect(
            container.querySelector("a#register").textContent
        ).toEqual("Register");
    })
    
    it("has lost password link", () => {
        render(<LogInPageLayout />);

        expect(
            container.querySelector("a#reset").textContent
        ).toEqual("Lost your password?");
    })

    it("has register form", () => {
        render(<LogInPageLayout />);

        expect(
            container.querySelector("form")
        ).not.toBeNull();
    })
})
