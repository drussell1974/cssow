
const onProgress = (reactComponent) => {
    if (reactComponent.NO_OF_COMPONENTS_TO_LOAD == 0 || reactComponent.state.loading == undefined || reactComponent.NO_OF_COMPONENTS_TO_LOAD == undefined){
        return 0;
    }

    let progress = reactComponent.state.loading + 100 / (reactComponent.NO_OF_COMPONENTS_TO_LOAD - 1);
        return progress;
};

const getInstitutes = (reactComponent) => {
    let uri = `${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/institute/?format=json`;
    fetch(uri)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            reactComponent.setState({
                Institutes: data.institutes, 
                hasError: false,
                loading: onProgress(reactComponent),
                isLoaded: true,
            });
        },  
        (error) => {
            reactComponent.setState({
                Institutes: [],
                hasError: true,
                isLoaded: true,
                onerror: onProgress(reactComponent),
            });
        }
    )
}


const getInstitute = (reactComponent, institute_id) => {
    let uri = `${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/institute/${institute_id}?format=json`;
    fetch(uri)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            reactComponent.setState({
                Institute: data.institute,
                hasError: false,
                loading: onProgress(reactComponent),
                isLoaded: true,
            });
        },  
        (error) => {
            reactComponent.setState({
                Institute: {},
                hasError: true,
                isLoaded: true,
                onerror: onProgress(reactComponent),
            });
        }
    )
}


const getDepartments = (reactComponent, institute_id) => {
    let uri = `${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/institute/${institute_id}/department/?format=json`;
    fetch(uri)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            reactComponent.setState({
                Departments: data.departments,
                hasError: false,
                loading: onProgress(reactComponent),
                isLoaded: true,
            });
        },  
        (error) => {
            reactComponent.setState({
                Departments: [],
                hasError: true,
                isLoaded: true,
                onerror: onProgress(reactComponent),
            });
        }
    )
}


const getDepartment = (reactComponent, institute_id, department_id) => {
    let uri = `${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/institute/${institute_id}/department/${department_id}?format=json`;
    fetch(uri)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            reactComponent.setState({
                Department: data.department,
                hasError: false,
                loading: onProgress(reactComponent),
                isLoaded: true,
            });
        },  
        (error) => {
            reactComponent.setState({
                Department: [],
                hasError: true,
                isLoaded: true,
                onerror: onProgress(reactComponent),
            });
        }
    )
}


const getCourses = (reactComponent, institute_id, department_id) => {
    let uri = `${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/institute/${institute_id}/department/${department_id}/schemesofwork/?format=json`;
    fetch(uri)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            reactComponent.setState({
                Courses: data.schemesofwork, 
                hasError: false,
                loading: onProgress(reactComponent),
                isLoaded: true,
            });
        },  
        (error) => {
            reactComponent.setState({
                Courses: [],
                hasError: true,
                isLoaded: true,
                onerror: onProgress(reactComponent),
            });
        }
    )
}


const getCourse = (reactComponent, institute_id, department_id, course_id) => {
    let uri = `${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/institute/${institute_id}/department/${department_id}/schemesofwork/${course_id}?format=json`;
    fetch(uri)
        .then(res => { 
            return res.json();
        })
        .then(
        (data) => {
            reactComponent.setState({
                Course: data.schemeofwork,
                loading: onProgress(reactComponent), 
                hasError: false,
                isLoaded: true,
            });
        },  
        (error) => {
            reactComponent.setState({
                Course: {},
                hasError: true,
                isLoaded: true,
                onerror: onProgress(reactComponent),
            });
        }
    )
}


const getLessons = (reactComponent, institute_id, department_id, course_id) => {
    let uri = `${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/institute/${institute_id}/department/${department_id}/schemesofwork/${course_id}/lessons/?format=json`;
    fetch(uri)
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
                onerror: onProgress(reactComponent),
            });
        }
    )
}


const getLesson = (reactComponent, institute_id, department_id, course_id, lesson_id) => {
    let uri = `${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/institute/${institute_id}/department/${department_id}/schemesofwork/${course_id}/lessons/${lesson_id}?format=json`;
    fetch(uri)
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
                onerror: onProgress(reactComponent),
            });
        }
    )
}


const getResource = (reactComponent, institute_id, department_id, course_id, lesson_id, resource_id) => {
    let uri = `${REACT_APP_STUDENT_WEB__CSSOW_API_URI}/institute/${institute_id}/department/${department_id}/schemesofwork/${course_id}/lessons/${lesson_id}/resources/${resource_id}?format=json`;
    fetch(uri)
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
                onerror: onProgress(reactComponent),
            });
        }
    )
}


const getMarkdown = (reactComponent, institute_id, department_id, course_id, lesson_id, resource_id, md_document_name) => {
    let uri = `${REACT_APP_STUDENT_WEB__CSSOW_API_URI}//institute/${institute_id}/department/${department_id}schemesofwork/${course_id}/lessons/${lesson_id}/resources/${resource_id}/markdown/${md_document_name}?format=json`;
    fetch(uri)
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
            onerror: onProgress(reactComponent),
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


export { getInstitutes, getInstitute, getDepartments, getDepartment, getCourses, getCourse, getLessons, getLesson, getResource, getMarkdown, getSocialMediaLinks, getSiteConfig };