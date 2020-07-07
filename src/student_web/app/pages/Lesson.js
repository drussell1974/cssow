import React from 'react';
import { LessonObjectivesWidget } from '../widgets/LessonObjectivesWidget';
import { LessonBoxMenuWidget } from '../widgets/LessonBoxMenuWidget';
import { LessonActivityWidget } from '../widgets/LessonActivityWidget';
import BannerWidget from '../widgets/BannerWidget';
import FooterWidget from '../widgets/FooterWidget';
import { getSchemeOfWork, getLesson, getSocialMediaLinks, getMarkdown } from '../services/apiReactServices';

class Index extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            SchemeOfWork: {},
            Lesson: {},
            hasError: false,
        }
    
        this.socialmediadata = [];

        this.learning_episode_id = props.match.params.learning_episode_id;
        this.scheme_of_work_id = "openldap";
        this.lesson_id = "lesson3";
        this.resource_id = "activity1"
        this.md_document_name = "configuring-a-client-with-autofs-ldap-and-nfs.md";
    }

    componentDidMount() {

        this.socialmediadata = getSocialMediaLinks();
        
        getSchemeOfWork(this);

        getLesson(this, this.learning_episode_id, 7);   

        // TODO: Get activity name (/openldap/lesson3/activity1/configuring-a-client-with-autofs-ldap-and-nfs)
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
                        <LessonObjectivesWidget data={this.state.Lesson} />

                        <LessonBoxMenuWidget data={this.state.Lesson} typeButtonText="View" />
                        
                        <LessonActivityWidget data={this.state.Lesson} markdown_html={this.state.markdown_html} />
                    </div>
                </div>
                
                <FooterWidget heading="Computer Science SOW" summary='' socialmedia={this.socialmediadata} />

            </React.Fragment>
        )
    }
};

export default Index;