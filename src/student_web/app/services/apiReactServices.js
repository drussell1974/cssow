
const getSchemeOfWork = (reactComponent) => {
    fetch(`${STUDENT_WEB__CSSOW_API_URI}/schemesofwork/${STUDENT_WEB__DEFAULT_SCHEMEOFWORK}?format=json`)
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

const getLessons = (reactComponent) => {
    fetch(`${STUDENT_WEB__CSSOW_API_URI}/schemesofwork/${STUDENT_WEB__DEFAULT_SCHEMEOFWORK}/lessons/?format=json`)
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

const getLesson = (reactComponent, learning_episode_id, resource_type_id) => {
    fetch(`${STUDENT_WEB__CSSOW_API_URI}/schemesofwork/${STUDENT_WEB__DEFAULT_SCHEMEOFWORK}/lessons/${learning_episode_id}?resource_type_id=${resource_type_id}&format=json`)
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

const getMarkdown = (reactComponent) => {
    reactComponent.setState({
            markdown: {
                "text": "Hello world github/linguist#1 **cool**, and #1!",
                "mode": "gfm",
                "context": "github/gollum"
            }
        })
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



export { getSchemeOfWork, getLessons, getLesson, getSocialMediaLinks, getMarkdown };