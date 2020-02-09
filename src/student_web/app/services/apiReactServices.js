const uri = 'http://api.daverussell.local:8002';

const getSchemeOfWork = (reactComponent) => {
    fetch(uri + "/api/schemesofwork/127?format=json")
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
    fetch(uri + "/api/schemesofwork/127/lessons/?format=json")
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

const getLesson = (reactComponent, learning_episode_id) => {
    fetch(uri + `/api/schemeofwork/127/lessons/${learning_episode_id}?format=json`)
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

export { getSchemeOfWork, getLessons, getLesson, getSocialMediaLinks };