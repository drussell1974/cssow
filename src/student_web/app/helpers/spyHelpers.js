
export const fetchResponseOK = body => 
    Promise.resolve({
        ok: true,
        json: () => Promise.resolve(body)
    })


export const fetchResponseNotOK = body => 
    Promise.resolve({
        ok: false,
        json: () => Promise.resolve(body)
    })

    
export const fetchResponseError = () => 
    Promise.resolve({ ok: false });


export const requestBodyOf = (fetchSpy) => 
    JSON.parse(fetchSpy.mock.calls[0][1].body);
