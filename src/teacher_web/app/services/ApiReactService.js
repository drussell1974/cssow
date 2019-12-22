const getSchemesOfWork = (reactComponent) => {
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
}

export default getSchemesOfWork;
