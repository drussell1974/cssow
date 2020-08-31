
const onProgress = (reactComponent) => {
    if (reactComponent.NO_OF_COMPONENTS_TO_LOAD == 0 || reactComponent.state.loading == undefined || reactComponent.NO_OF_COMPONENTS_TO_LOAD == undefined){
        return 0;
    }

    let progress = reactComponent.state.loading + 100 / (reactComponent.NO_OF_COMPONENTS_TO_LOAD - 1);
        return progress;
};

const getSchemesOfWork = (reactComponent) => {
    fetch(`${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/schemesofwork/?format=json`)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            reactComponent.setState({
                SchemesOfWork: data.schemesofwork, 
                hasError: false,
                loading: onProgress(reactComponent),
                isLoaded: true,
            });
        },  
        (error) => {
            reactComponent.setState({
                SchemesOfWork: [],
                hasError: true,
                isLoaded: true,
                onerror: onProgress(reactComponent),
            });
        }
    )
}


const getSchemeOfWork = (reactComponent, scheme_of_work_id) => {
    fetch(`${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/schemesofwork/${scheme_of_work_id}?format=json`)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            reactComponent.setState({
                SchemeOfWork: data.schemeofwork,
                loading: onProgress(reactComponent), 
                hasError: false,
                isLoaded: true,
            });
        },  
        (error) => {
            reactComponent.setState({
                SchemeOfWork: {},
                hasError: true,
                isLoaded: true,
                onerror: reactComponent.onError(error),
            });
        }
    )
}


const getLessons = (reactComponent, scheme_of_work_id) => {
    fetch(`${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/schemesofwork/${scheme_of_work_id}/lessons/?format=json`)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            reactComponent.setState({
                Lessons: data.lessons, 
                loading: onProgress(reactComponent),
                hasError: false,
                isLoaded: true,
            });
        },  
        (error) => {
            reactComponent.setState({
                Lessons: [],
                hasError: true,
                isLoaded: true,
                onerror: reactComponent.onError(error),
            });
        }
    )
}


const getLesson = (reactComponent, scheme_of_work_id, lesson_id) => {
    fetch(`${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/schemesofwork/${scheme_of_work_id}/lessons/${lesson_id}?format=json`)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            reactComponent.setState({
                Lesson: data.lesson, 
                loading: onProgress(reactComponent),
                hasError: false,
                isLoaded: true,
            });
        },  
        (error) => {
            reactComponent.setState({
                Lesson: {},
                hasError: true,
                isLoaded: true,
                onerror: reactComponent.onError(error),
            });
        }
    )
}


const getResource = (reactComponent, scheme_of_work_id, lesson_id, resource_id) => {
    fetch(`${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/schemesofwork/${scheme_of_work_id}/lessons/${lesson_id}/resources/${resource_id}?format=json`)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            reactComponent.setState({
                Resource: data.resource,
                loading: onProgress(reactComponent), 
                hasError: false,
                isLoaded: true,
            });
        },  
        (error) => {
            reactComponent.setState({
                Resource: {},
                hasError: true,
                isLoaded: true,
                onerror: reactComponent.onError(error),
            });
        }
    )
}


const getMarkdown = (reactComponent, scheme_of_work_id, lesson_id, resource_id, md_document_name) => {
    fetch(`${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/schemesofwork/${scheme_of_work_id}/lessons/${lesson_id}/resources/${resource_id}/markdown/${md_document_name}?format=json`)
      .then(res => res.json())
      .then(
        (result) => {
            reactComponent.setState({
            isLoaded: true,
            loading: onProgress(reactComponent),
            markdown_html: result.markdown,
          });
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
            reactComponent.setState({
            hasError: true,
            isLoaded: true,
            markdown_html: error,
            error,
            onerror: reactComponent.onError(error),
          });
        }
      )
} 


const getSocialMediaLinks = (reactComponent) => {
    reactComponent.setState({
        socialmediadata: [
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
        ],
        loading: onProgress(reactComponent),
        hasError: false,
        isLoaded: true,
    });
}


const getSiteConfig = (reactComponent) => {
    reactComponent.setState({
        Site: {
            name:"Dave Russell",
            description:""
        }, 
        loading: onProgress(reactComponent),
        hasError: false,
        isLoaded: true,
    });
}


export { getSchemesOfWork, getSchemeOfWork, getLessons, getLesson, getResource, getMarkdown, getSocialMediaLinks, getSiteConfig };