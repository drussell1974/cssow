import React from 'react';
import BannerWidget from '../widgets/BannerWidget';
import BreadcrumbWidget from '../widgets/BreadcrumbWidget';
import FooterWidget from '../widgets/FooterWidget';
import { SpinnerWidget } from '../widgets/SpinnerWidget';
import { getMarkdown, getCourse, getLesson, getSocialMediaLinks, getSiteConfig, getResource, getDepartment, getInstitute } from '../services/apiReactServices';
import { MarkdownWidget } from '../widgets/MarkdownWidget';

class ActivityPage extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            hasError: false,
            loading: 0,
            markdown_html: {},
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

        getResource(this, this.institute_id, this.department_id, this.course_id, this.lesson_id, this.resource_id)

        getMarkdown(this, this.institute_id, this.department_id, this.course_id, this.lesson_id, this.resource_id, this.md_document_name);

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
            hasError: true,
            loading: 50
        }
      }
      
    render() {

        return (
            <React.Fragment>
                <ActivityPageContainer 
                    markdown_html={this.state.markdown_html}
                    resource={this.state.Resource}
                    lesson={this.state.Lesson}
                    course={this.state.Course}
                    institute={this.state.Institute}
                    department={this.state.Department}
                    socialmediadata={this.state.socialmediadata}
                    loading={this.state.loading}
                />
            </React.Fragment>
        )
    }
};

export const ActivityPageContainer = ({markdown_html, resource, lesson, course, department, institute, socialmediadata, loading = 0}) => {
    if (resource === undefined || course === undefined || lesson === undefined || department === undefined || institute === undefined) {
        return (
            <React.Fragment></React.Fragment>
        )
    } else {
        
        let breadcrumbItems = [
            {text:"Home", url:"/"}, 
            {text:course.name, url:`/institute/${institute.id}/department/${department.id}/course/${course.id}/lesson`},
            {text:lesson.title, url:`/institute/${institute.id}/department/${department.id}/course/${course.id}/lesson/${lesson.id}`}
        ]

        return (
            <React.Fragment>

                <BannerWidget heading={resource.title} description={resource.page_note} />
                <SpinnerWidget loading={loading} />
                <div id="main">
                    <div className="inner clearfix">
                        <BreadcrumbWidget breadcrumbItems={breadcrumbItems} activePageName={resource.title} />                
                        <MarkdownWidget markdown_html={markdown_html} />    
                    </div>
                </div>

                <FooterWidget heading={course.name} summary={course.description} socialmedia={socialmediadata} />
            
            </React.Fragment>
        )
    }
}

export default ActivityPage;