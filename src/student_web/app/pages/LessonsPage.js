import React from 'react';
import { LessonsBoxMenuWidget } from '../widgets/LessonsBoxMenuWidget';
import BannerWidget from '../widgets/BannerWidget';
import BreadcrumbWidget from '../widgets/BreadcrumbWidget';
import FooterWidget from '../widgets/FooterWidget';
import { SpinnerWidget } from '../widgets/SpinnerWidget';
import { getInstitute, getDepartment, getCourse, getLessons, getSocialMediaLinks, getSiteConfig } from '../services/apiReactServices';

class LessonsPage extends React.Component {
   
    onProgress() {
        return this.state.loading + 100 / 3;
    }

    constructor(props){
        super(props);
        this.state = {
            Lessons: [],
            hasError: false,
            loading: 0,
            socialmediadata: []
        }
    
        this.institute_id = props.match.params.institute_id;
        this.department_id = props.match.params.department_id;
        this.course_id = props.match.params.course_id;
    }

    componentDidMount() {

        this.NO_OF_COMPONENTS_TO_LOAD = 6;

        getSiteConfig(this);

        getInstitute(this, this.institute_id);

        getDepartment(this, this.institute_id, this.department_id);

        getCourse(this, this.institute_id, this.department_id, this.course_id);

        getLessons(this, this.institute_id, this.department_id, this.course_id);   

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
            <LessonsPageContainer 
                lessons={this.state.Lessons}
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

export const LessonsPageContainer = ({lessons, course, department, institute, site, socialmediadata, loading = 0}) => {
    if (lessons === undefined || course === undefined || department === undefined || institute === undefined || site === undefined) {
        return ( 
            <React.Fragment></React.Fragment>
        )
    } else {
        
        let breadcrumbItems = [
            {text:"Home", url:"/"}, 
        ]
        
        return (
            <React.Fragment>
                <BannerWidget heading={course.name} description={course.description} />
                <SpinnerWidget loading={loading} />
                <div id="main">
                    <div className="inner clearfix">
                        <BreadcrumbWidget breadcrumbItems={breadcrumbItems} activePageName={course.name} />
                        <LessonsBoxMenuWidget data={lessons} typeLabelText="Lesson" typeButtonText="View Lesson" typeButtonClass="button fit" typeDisabledButtonText="Coming Soon" typeDisabledButtonClass="button fit disabled" />
                    </div>
                </div>
                
                <FooterWidget heading={course.name} summary={course.description} socialmedia={socialmediadata} />

            </React.Fragment>
        )
    }
}

export default LessonsPage;