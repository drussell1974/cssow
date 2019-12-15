const apiReactServices = {
    getSchemeOfWork: (reactComponent) => {
        fetch("http://127.0.0.1:8000/api/schemeofwork/127?format=json")
            .then(res => { 
                return res.json();
            })
            .then(
            (data) => {
                reactComponent.setState({
                    SchemeOfWork: data.schemeofwork, 
                    hasError: false,
                });
            },  
            (error) => {
                reactComponent.setState({
                    SchemeOfWork: {},
                    hasError: true,
                });
            }
        )
    },

    getLessons: (reactComponent) => {
        fetch("http://127.0.0.1:8000/api/schemeofwork/127/lessons?format=json")
            .then(res => { 
                return res.json();
            })
            .then(
            (data) => {
                reactComponent.setState({
                    Lessons: data.lessons, 
                    hasError: false,
                });
            },  
            (error) => {
                reactComponent.setState({
                    Lessons: [],
                    hasError: true,
                });
            }
        )
    },

    getSocialMediaLinks: () => {
        return [
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
    }
}

export default apiReactServices;