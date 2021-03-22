import React from 'react';
import { LessonObjectivesWidget } from '../widgets/LessonObjectivesWidget';
import { LessonKeywordsWidget } from '../widgets/LessonKeywordsWidget';
import { LessonBoxMenuWidget } from '../widgets/LessonBoxMenuWidget';
import BannerWidget from '../widgets/BannerWidget';
import BreadcrumbWidget from '../widgets/BreadcrumbWidget';
import FooterWidget from '../widgets/FooterWidget';
import { SpinnerWidget } from '../widgets/SpinnerWidget';
import { getLesson, getCourse, getDepartment, getInstitute, getSiteConfig, getSocialMediaLinks } from '../services/apiReactServices';

class LessonPage extends React.Component {
   
    onProgress() {
        return this.state.loading + 100 / 3;
    }

    constructor(props){
        super(props);
        this.state = {
            hasError: false,
            loading: 0,
            socialmediadata: []
        }
    
        this.institute_id = props.match.params.institute_id;
        this.department_id = props.match.params.department_id;
        this.course_id = props.match.params.course_id;
        this.lesson_id = props.match.params.lesson_id;
        this.resource_id = props.match.params.resource_id;
        this.md_document_name = props.match.params.md_document_name;
    }

    componentDidMount() {

        this.NO_OF_COMPONENTS_TO_LOAD = 6;

        getSiteConfig(this);

        getInstitute(this, this.institute_id);

        getDepartment(this, this.institute_id, this.department_id);

        getCourse(this, this.institute_id, this.department_id, this.course_id);

        getLesson(this, this.institute_id, this.department_id, this.course_id, this.lesson_id);   

        getSocialMediaLinks(this);
    }
    
    static getDerivedStateFromError(error) {
        // Update state so the next render will show the fallback UI.
        return { hasError: true };
      }

    componentDidCatch(error, errorInfo) {
        // You can also log the error to an error reporting service
        
        this.state = {
            hasError: true
        }
      }
      
    render() {
        return (
            <LessonPageContainer 
                lesson={this.state.Lesson}
                course={this.state.Course}
                department={this.state.Department}
                institute={this.state.Institute}
                site={this.state.Site}
                socialmediadata={this.state.socialmediadata}
                loading={this.state.loading}
            />
        )
    }
};

export const LessonPageContainer = ({lesson, course, department, institute, site, socialmediadata, loading = 0}) => {
    if (lesson === undefined || course === undefined || department === undefined || institute === undefined || site === undefined) {
        return ( 
            <React.Fragment></React.Fragment>
        )
    } else {

        let breadcrumbItems = [
            {text:"Home", url:"/"}, 
            {text:course.name, url:`/institute/${institute.id}/department/${department.id}/course/${course.id}/lesson`},
        ]

        return (
            <React.Fragment>
                <BannerWidget heading={lesson.title} description={lesson.summary} />
                <SpinnerWidget loading={loading} />
                <div id="main">
                    <div className="inner clearfix">
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
                
                <FooterWidget heading={course.name} summary={course.description} socialmedia={socialmediadata} />

            </React.Fragment>
        )
    }
}

export default LessonPage;