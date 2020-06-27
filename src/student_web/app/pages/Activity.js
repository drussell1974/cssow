import React from 'react';
import BannerWidget from '../widgets/BannerWidget';
import FooterWidget from '../widgets/FooterWidget';
import { getSchemeOfWork, getLesson, getSocialMediaLinks } from '../services/apiReactServices';
import { LessonActivityWidget } from '../widgets/LessonActivityWidget';

class Activity extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            SchemeOfWork: {},
            Lesson: {},
            hasError: false,
        }
    
        this.socialmediadata = [];

        this.learning_episode_id = props.match.params.learning_episode_id;
    }

    componentDidMount() {

        this.socialmediadata = getSocialMediaLinks();
        
        getSchemeOfWork(this);

        getLesson(this, this.learning_episode_id, 7);   
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
                        <LessonActivityWidget data={this.state.Lesson} />    
                    </div>
                </div>
                
                <FooterWidget heading="Computer Science SOW" summary='' socialmedia={this.socialmediadata} />

            </React.Fragment>
        )
    }
};

export default Activity;