import React from 'react';
import { LessonsBoxMenuWidget } from '../widgets/LessonsBoxMenuWidget';
import BannerWidget from '../widgets/BannerWidget';
import FooterWidget from '../widgets/FooterWidget';
import { getSchemeOfWork, getLessons, getSocialMediaLinks, getSiteConfig } from '../services/apiReactServices';

class CoursePage extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            Site: {},
            SchemeOfWork: {},
            Lessons: [],
            Lesson: {
                Markup: "",
            },
            hasError: false,
        }
    
        this.scheme_of_work_id = props.match.params.scheme_of_work_id;
        this.socialmediadata = [];
    }

    componentDidMount() {

        getSiteConfig(this);

        this.socialmediadata = getSocialMediaLinks();
        
        getSchemeOfWork(this, this.scheme_of_work_id);

        getLessons(this, this.scheme_of_work_id);
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
            <CoursePageContainer
                lessons={this.state.Lessons}
                schemeofwork={this.state.SchemeOfWork}
                site={this.state.Site}
                socialmediadata={this.socialmediadata}
            />
        )
    }
};

export const CoursePageContainer = ({lessons, schemeofwork, site, socialmediadata}) => {
    if (lessons === undefined || schemeofwork === undefined || site === undefined) {
        return ( 
            <React.Fragment></React.Fragment>
        )
    } else {

        return (
            <React.Fragment>
                 
                <BannerWidget heading={schemeofwork.name} description={schemeofwork.description} />
                    <div id="main">
                        <div className="inner">
                            <LessonsBoxMenuWidget data={lessons} typeLabelText="Lesson" typeButtonText="View Lesson" />
                        </div>
                    </div>
                <FooterWidget heading={site.name} summary={site.description} socialmedia={socialmediadata} />

            </React.Fragment>
        )
    }
}

export default CoursePage;