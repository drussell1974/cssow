const ApiReactService = {
    
    getSchemeOfWork(reactComponent, schemeOfWorkId) {
        var uri = `http://127.0.0.1:8000/api/schemeofwork/${schemeOfWorkId}`;
        fetch(uri)
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

    getSchemesOfWork(reactComponent) {
        fetch("http://127.0.0.1:8000/api/schemeofwork")
            .then(res => { 
                return res.json();
            })
            .then(
            (data) => {
                reactComponent.setState({
                    SchemesOfWork: data.schemesofwork, 
                    hasError: false,
                });
            },  
            (error) => {
                reactComponent.setState({
                    SchemesOfWork: {},
                    hasError: true,
                });
            }
        )
    },

    getLessons(reactComponent, schemeOfWorkId) {
        let uri = `http://127.0.0.1:8000/api/schemeofwork/${schemeOfWorkId}/lessons`;

        fetch(uri)
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
                    Lessons: {},
                    hasError: true,
                });
            }
        )
    },
    
    getLesson(reactComponent, schemeOfWorkId, learningObjectiveId) {
        let uri = `http://127.0.0.1:8000/api/schemeofwork/${schemeOfWorkId}/lessons/${learningObjectiveId}`;
        
        fetch(uri)
            .then(res => { 
                return res.json();
            })
            .then(
            (data) => {
                reactComponent.setState({
                    Lesson: data.lesson, 
                    hasError: false,
                });
            },  
            (error) => {
                reactComponent.setState({
                    Lesson: {},
                    hasError: true,
                });
            }
        )
    }
}

export default ApiReactService;
