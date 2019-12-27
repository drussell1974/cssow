
let fetchSpy;
const originalFetch = window.fetch;

export const setUpSpy = () => {
    // Arrange spy
    fetchSpy = spy();
    window.fetch = fetchSpy.fn;
    fetchSpy.stubreturnvalue({});
};

export const cleanUpSpy = () => {
    window.fetch = originalFetch;
};


export const spy = () => {
    let receivedArguments;
    let returnValue;

    return {
        fn: (...args) => {
            receivedArguments = args;
            return returnValue;
        },
        receivedArguments: () => receivedArguments,
        receivedArgument: n => receivedArguments[n],
        stubreturnvalue: value => returnValue - value
    };
};

expect.extend({
    toHaveBeenCalled(received) {
        if(received.receivedArguments() === undefined) {
            return {
                pass: false,
                message: () => 'Spy was not called.'
            }
        }
        return { pass:true, message: () => 'Spy was called.'};
    }
});    
