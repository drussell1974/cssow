import React from 'react';
import { CourseBoxMenuWidget } from '../widgets/CourseBoxMenuWidget';
import BannerWidget from '../widgets/BannerWidget';
import BreadcrumbWidget from '../widgets/BreadcrumbWidget';
import FooterWidget from '../widgets/FooterWidget';
import { SpinnerWidget } from '../widgets/SpinnerWidget';
import { getCourses, getSocialMediaLinks, getSiteConfig, getInstitute, getDepartment } from '../services/apiReactServices';


class CoursePage extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            Courses: [],
            hasError: false,
            loading: 0,
            socialmediadata: []
        }

        this.institute_id = props.match.params.institute_id;
        this.department_id = props.match.params.department_id;
    }

    componentDidMount() {

        this.NO_OF_COMPONENTS_TO_LOAD = 5;

        getSiteConfig(this);

        getInstitute(this, this.institute_id);

        getDepartment(this, this.institute_id, this.department_id);

        getCourses(this, this.institute_id, this.department_id);

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
                courses={this.state.Courses}
                department={this.state.Department}
                institute={this.state.Institute}
                site={this.state.Site}
                socialmediadata={this.state.socialmediadata}
                loading={this.state.loading}
            />
        )
    }
};

export const CoursePageContainer = ({courses, department, institute, site, socialmediadata, loading = 0}) => {
    if (courses === undefined || department === undefined || institute === undefined || site === undefined) {
        return ( 
            <React.Fragment></React.Fragment>
        )
    } else {
        
        let breadcrumbItems = [
            {text:"Home", url:"/"}, 
            {text:institute.name, url:`/institute/`},
            {text:department.name, url:`/institute/${institute.id}/department/`},
        ]

        return (
            <React.Fragment>
                 
                <BannerWidget heading={department.name} description={department.description} />
                <SpinnerWidget loading={loading} />
                <div id="main">
                    <div className="inner clearfix">
                        <BreadcrumbWidget breadcrumbItems={breadcrumbItems} activePageName={department.name} />   
                        <CourseBoxMenuWidget data={courses} typeLabelText="Course" 
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