import React from 'react';
import { LessonObjectivesWidget } from '../widgets/LessonObjectivesWidget';
import { LessonKeywordsWidget } from '../widgets/LessonKeywordsWidget';
import { LessonBoxMenuWidget } from '../widgets/LessonBoxMenuWidget';
import BannerWidget from '../widgets/BannerWidget';
import BreadcrumbWidget from '../widgets/BreadcrumbWidget';
import FooterWidget from '../widgets/FooterWidget';
import { SpinnerWidget } from '../widgets/SpinnerWidget';
import { getSchemeOfWork, getLesson, getSocialMediaLinks } from '../services/apiReactServices';

class LessonPage extends React.Component {
   
    onProgress() {
        return this.state.loading + 100 / 3;
    }

    constructor(props){
        super(props);
        this.state = {
            SchemeOfWork: {},
            Lesson: {},
            hasError: false,
            loading: 0,
            socialmediadata: []
        }
    
        this.scheme_of_work_id = props.match.params.scheme_of_work_id;
        this.lesson_id = props.match.params.lesson_id;
        this.resource_id = props.match.params.resource_id;
        this.md_document_name = props.match.params.md_document_name;
    }

    componentDidMount() {

        this.NO_OF_COMPONENTS_TO_LOAD = 3;

        getSchemeOfWork(this, this.scheme_of_work_id);

        getLesson(this, this.scheme_of_work_id, this.lesson_id);   

        getSocialMediaLinks(this);
    }
    
    static getDerivedStateFromError(error) {
        // Update state so the next render will show the fallback UI.
        return { hasError: true };
      }

    componentDidCatch(error, errorInfo) {
        // You can also log the error to an error reporting service
        console.log(error, errorInfo);
        
        this.state = {
            hasError: true
        }
      }
      
    render() {
        return (
            <LessonPageContainer 
                lesson={this.state.Lesson}
                keywords={this.state.Lesson.keywords}
                schemeofwork={this.state.SchemeOfWork}
                socialmediadata={this.state.socialmediadata}
            />
        )
    }
};

export const LessonPageContainer = ({schemeofwork, lesson, socialmediadata, loading = 0}) => {
    if (lesson === undefined || schemeofwork === undefined) {
        return ( 
            <React.Fragment></React.Fragment>
        )
    } else {

        let breadcrumbItems = [
            {text:"Home", url:"/"}, 
            {text:schemeofwork.name, url:`/Course/${schemeofwork.id}`},
        ]

        return (
            <React.Fragment>
                
                <BannerWidget heading={lesson.title} description={lesson.summary} />
                <SpinnerWidget loading={loading} />
                <div id="main">
                    <div className="inner">
                        <BreadcrumbWidget breadcrumbItems={breadcrumbItems} activePageName={lesson.title} />
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