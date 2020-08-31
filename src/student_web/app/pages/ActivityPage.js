import React from 'react';
import BannerWidget from '../widgets/BannerWidget';
import BreadcrumbWidget from '../widgets/BreadcrumbWidget';
import FooterWidget from '../widgets/FooterWidget';
import { SpinnerWidget } from '../widgets/SpinnerWidget';
import { getMarkdown, getSchemeOfWork, getLesson, getSocialMediaLinks, getSiteConfig } from '../services/apiReactServices';
import { MarkdownWidget } from '../widgets/MarkdownWidget';

class ActivityPage extends React.Component {
    
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
            markdown_html: {},
            socialmediadata: []
        }

        this.scheme_of_work_id = props.match.params.scheme_of_work_id;
        this.lesson_id = props.match.params.lesson_id;
        this.resource_id = props.match.params.resource_id;
        this.md_document_name = props.match.params.md_document_name;
    }

    componentDidMount() {

        this.NO_OF_COMPONENTS_TO_LOAD = 5;

        getSiteConfig(this);

        getSchemeOfWork(this, this.scheme_of_work_id);

        getLesson(this, this.scheme_of_work_id, this.lesson_id);

        getMarkdown(this, this.scheme_of_work_id, this.lesson_id, this.resource_id, this.md_document_name);

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
                    resource={this.state.Lesson}
                    schemeofwork={this.state.SchemeOfWork}
                    lesson={this.state.Lesson}
                    markdown_html={this.state.markdown_html}
                    socialmediadata={this.state.socialmediadata}
                    loading={this.state.loading}
                />
            </React.Fragment>
        )
    }
};

export const ActivityPageContainer = ({resource, schemeofwork, lesson, markdown_html, socialmediadata, loading = 0}) => {
    if (resource === undefined || schemeofwork === undefined || lesson === undefined) {
        return ( 
            <React.Fragment></React.Fragment>
        )
    } else {
        
        let breadcrumbItems = [
            {text:"Home", url:"/"}, 
            {text:schemeofwork.name, url:`/Course/${schemeofwork.id}`},
            {text:lesson.title, url:`/Course/${schemeofwork.id}/Lesson/${lesson.id}`}
        ]

        return (
            <React.Fragment>

                <BannerWidget heading={resource.title} description={resource.page_note} />

                <div id="main">
                    <div className="inner">
                        <SpinnerWidget loading={loading} />
                        <BreadcrumbWidget breadcrumbItems={breadcrumbItems} activePageName={resource.title} />
                        <MarkdownWidget markdown_html={markdown_html} />    
                    </div>
                </div>

                <FooterWidget heading={schemeofwork.name} summary={schemeofwork.description} socialmedia={socialmediadata} />
            
            </React.Fragment>
        )
    }
}

export default ActivityPage;