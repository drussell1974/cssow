
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
            });
        },  
        (error) => {
            reactComponent.setState({
                SchemesOfWork: [],
                hasError: true,
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


const getResource = (reactComponent, scheme_of_work_id, lesson_id, resource_id) => {
    fetch(`${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/schemesofwork/${scheme_of_work_id}/lessons/${lesson_id}/resources/${resource_id}?format=json`)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            reactComponent.setState({
                Resource: data.resource, 
                hasError: false,
            });
        },  
        (error) => {
            reactComponent.setState({
                Resource: {},
                hasError: true,
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
            markdown_html: result.markdown
          });
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
            reactComponent.setState({
            isLoaded: true,
            markdown_html: error,
            error
          });
        }
      )
} 


const getSocialMediaLinks = () => {
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


const getSiteConfig = (reactComponent) => {
    reactComponent.setState({
        Site: {
            name:"Dave Russell",
            description:""
        }, 
        hasError: false,
    });
}


export { getSchemesOfWork, getSchemeOfWork, getLessons, getLesson, getResource, getMarkdown, getSocialMediaLinks, getSiteConfig };