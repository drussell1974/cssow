import React from 'react';
import { LessonsBoxMenuWidget } from '../widgets/LessonsBoxMenuWidget';
import BannerWidget from '../widgets/BannerWidget';
import BreadcrumbWidget from '../widgets/BreadcrumbWidget';
import FooterWidget from '../widgets/FooterWidget';
import { SpinnerWidget } from '../widgets/SpinnerWidget';
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
            loading: 0,
            socialmediadata: []
        }
    
        this.scheme_of_work_id = props.match.params.scheme_of_work_id;
    }

    componentDidMount() {

        this.NO_OF_COMPONENTS_TO_LOAD = 4;

        getSiteConfig(this);
                        
        getSchemeOfWork(this, this.scheme_of_work_id);

        getLessons(this, this.scheme_of_work_id);

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
            loading: 50,
        }
      }
      
    render() {
        return (
            <CoursePageContainer
                lessons={this.state.Lessons}
                schemeofwork={this.state.SchemeOfWork}
                site={this.state.Site}
                socialmediadata={this.state.socialmediadata}
                loading={this.state.loading}
            />
        )
    }
};

export const CoursePageContainer = ({lessons, schemeofwork, site, socialmediadata, loading = 0}) => {
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
                            <SpinnerWidget loading={loading} />
                            <BreadcrumbWidget breadcrumbItems={[{text:"Home", url:"/"}]} activePageName={schemeofwork.name} />
                            <LessonsBoxMenuWidget data={lessons} typeLabelText="Lesson" 
                                typeButtonText="View Lesson" 
                                typeButtonClass="button style2 fit"
                                typeDisabledButtonText="Coming soon"
                                typeDisabledButtonClass="button style2 fit disabled"
                            />
                        </div>
                    </div>
                <FooterWidget heading={site.name} summary={site.description} socialmedia={socialmediadata} />

            </React.Fragment>
        )
    }
}

export default CoursePage;