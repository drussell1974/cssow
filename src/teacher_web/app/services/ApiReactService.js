const ApiReactService = {
    
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

    getLearningEpisodes(reactComponent, schemeOfWorkId) {
        let uri = `http://127.0.0.1:8000/api/schemeofwork/${schemeOfWorkId}/lessons`

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
    }
}

export default ApiReactService;
