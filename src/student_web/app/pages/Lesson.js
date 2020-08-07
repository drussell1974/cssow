import React from 'react';
import { LessonObjectivesWidget } from '../widgets/LessonObjectivesWidget';
import { LessonKeywordsWidget } from '../widgets/LessonKeywordsWidget';
import { LessonBoxMenuWidget } from '../widgets/LessonBoxMenuWidget';
import BannerWidget from '../widgets/BannerWidget';
import FooterWidget from '../widgets/FooterWidget';
import { getSchemeOfWork, getLesson, getSocialMediaLinks } from '../services/apiReactServices';

class LessonPage extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            SchemeOfWork: {},
            Lesson: {},
            hasError: false,
        }
    
        this.socialmediadata = [];

        this.scheme_of_work_id = props.match.params.scheme_of_work_id;
        this.lesson_id = props.match.params.lesson_id;
        this.resource_id = props.match.params.resource_id;
        this.md_document_name = props.match.params.md_document_name;
    }

    componentDidMount() {

        this.socialmediadata = getSocialMediaLinks();
        
        getSchemeOfWork(this);

        getLesson(this, this.lesson_id, 7);   
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
            <LessonPageContainer 
                lesson={this.state.Lesson}
                keywords={this.state.Lesson.keywords}
                schemeofwork={this.state.SchemeOfWork}
                socialmediadata={this.socialmediadata}
            />
        )
    }
};

export const LessonPageContainer = ({schemeofwork, lesson, socialmediadata}) => {
    if (lesson === undefined || schemeofwork === undefined) {
        return ( 
            <React.Fragment></React.Fragment>
        )
    } else {

        return (
            <React.Fragment>
                
                <BannerWidget heading={lesson.title} description={lesson.summary} />

                <div id="main">
                    <div className="inner">
                        <section className="objectives">
                            <LessonObjectivesWidget data={lesson} />
                        </section>
                        <section className="keywords">
                            <LessonKeywordsWidget keywords={lesson.key_words} />
                        </section>
                        <section className="resources">
                            <LessonBoxMenuWidget data={lesson} typeButtonText="View" />                        
                        </section>
                    </div>
                </div>
                
                <FooterWidget heading={schemeofwork.name} summary={schemeofwork.description} socialmedia={socialmediadata} />

            </React.Fragment>
        )
    }
}

export default LessonPage;