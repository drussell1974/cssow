import React from 'react';
import BannerWidget from '../widgets/BannerWidget';
import FooterWidget from '../widgets/FooterWidget';
import { getMarkdown, getSchemeOfWork, getResource, getSocialMediaLinks } from '../services/apiReactServices';
import { MarkdownWidget } from '../widgets/MarkdownWidget';

class Activity extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            SchemeOfWork: {},
            Resource: {},
            hasError: false,
            markdown_html: {},
        }
    
        this.socialmediadata = [];

        this.scheme_of_work_id = REACT_APP_STUDENT_WEB__DEFAULT_SCHEMEOFWORK;
        this.lesson_id = props.match.params.lesson_id;
        this.resource_id = props.match.params.resource_id;
        this.md_document_name = props.match.params.md_document_name;
    }

    componentDidMount() {

        this.socialmediadata = getSocialMediaLinks();
        
        getSchemeOfWork(this);

        getResource(this, this.scheme_of_work_id, this.lesson_id, this.resource_id);

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
                <ActivityPageContainer 
                    resource={this.state.Resource}
                    schemeofwork={this.state.SchemeOfWork}
                    markdown_html={this.state.markdown_html}
                    socialmediadata={this.socialmediadata}
                />
            </React.Fragment>
        )
    }
};

export const ActivityPageContainer = ({resource, schemeofwork, markdown_html, socialmediadata}) => {
    console.log(`resource:${resource}, schemeofwork:${schemeofwork}`);
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