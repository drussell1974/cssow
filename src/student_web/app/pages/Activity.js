import React from 'react';
import BannerWidget from '../widgets/BannerWidget';
import FooterWidget from '../widgets/FooterWidget';
import { getMarkdown, getSchemeOfWork, getLesson, getSocialMediaLinks } from '../services/apiReactServices';
import { LessonActivityWidget } from '../widgets/LessonActivityWidget';

class Activity extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            SchemeOfWork: {},
            Lesson: {},
            hasError: false,
            markdown_html: {},
        }
    
        this.socialmediadata = [];

        this.learning_episode_id = props.match.params.learning_episode_id;

        this.scheme_of_work_id = props.match.params.scheme_of_work_id; 
        this.lesson_id = props.match.params.lesson_id;
        this.resource_id = props.match.params.resource_id;
        this.md_document_name = props.match.params.md_document_name;
    }

    componentDidMount() {

        this.socialmediadata = getSocialMediaLinks();
        
        getSchemeOfWork(this);

        getLesson(this, this.learning_episode_id, 7);   

        getMarkdown(this, this.scheme_of_work_id, this.lesson_id, this.resource_id, this.md_document_name);
    }
    
    static getDerivedStateFromError(error) {
        // Update state so the next render will show the fallback UI.
        return { hasError: true };
      }

    componentDidCatch(error, errorInfo) {
        // You can also log the error to an error reporting service
        console.log(error, errorInfo);
        
        this.state = {
            hasError: true,
        }
      }
      
    render() {
        return (
            <React.Fragment>
                
                <BannerWidget heading={this.state.Lesson.title} description={this.state.Lesson.summary} />

                <div id="main">
                    <div className="inner">
                        <LessonActivityWidget data={this.state.Lesson} markdown_html={this.state.markdown_html} />    
                    </div>
                </div>
                
                <FooterWidget heading="Computer Science SOW" summary='' socialmedia={this.socialmediadata} />

            </React.Fragment>
        )
    }
};

export default Activity;