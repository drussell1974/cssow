import React from 'react';
import BannerWidget from '../widgets/BannerWidget';
import FooterWidget from '../widgets/FooterWidget';
import { getMarkdown, getSchemeOfWork, getLesson, getSocialMediaLinks } from '../services/apiReactServices';
import { MarkdownWidget } from '../widgets/MarkdownWidget';

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

        this.lesson_id = props.match.params.lesson_id;
        this.resource_id = props.match.params.resource_id;
        this.md_document_name = props.match.params.md_document_name;
    }

    componentDidMount() {

        this.socialmediadata = getSocialMediaLinks();
        
        getSchemeOfWork(this);

        getLesson(this, this.lesson_id);   

        getMarkdown(this, REACT_APP_STUDENT_WEB__DEFAULT_SCHEMEOFWORK, this.lesson_id, this.resource_id, this.md_document_name);
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
                <ActivityPageContainer 
                    resource={this.state.Lesson}
                    schemeofwork={this.state.SchemeOfWork}
                    markdown_html={this.state.markdown_html}
                    socialmediadata={this.socialmediadata}
                />
            </React.Fragment>
        )
    }
};

export const ActivityPageContainer = ({resource, schemeofwork, markdown_html, socialmediadata}) => {
    if (resource === undefined || schemeofwork === undefined) {
        return ( 
            <React.Fragment></React.Fragment>
        )
    } else {
        return (
            <React.Fragment>

                <BannerWidget heading={resource.title} description={resource.page_note} />

                <div id="main">
                    <div className="inner">
                        <MarkdownWidget markdown_html={markdown_html} />    
                    </div>
                </div>

                <FooterWidget heading={schemeofwork.name} summary={schemeofwork.description} socialmedia={socialmediadata} />
            
            </React.Fragment>
        )
    }
}

export default Activity;