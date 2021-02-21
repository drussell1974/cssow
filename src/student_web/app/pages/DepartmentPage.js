import React from 'react';
import { DepartmentBoxMenuWidget } from '../widgets/DepartmentBoxMenuWidget';
import BannerWidget from '../widgets/BannerWidget';
import BreadcrumbWidget from '../widgets/BreadcrumbWidget';
import FooterWidget from '../widgets/FooterWidget';
import { SpinnerWidget } from '../widgets/SpinnerWidget';
import { getDepartments, getInstitute, getCourses, getSiteConfig, getSocialMediaLinks } from '../services/apiReactServices';

class DepartmentPage extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            // Site: {}, TODO: Check if this needs resetting here 
            // Institute: {}, TODO: Check if this needs resetting here
            Departments: [],
            hasError: false,
            loading: 0,
            socialmediadata: []
        }

        this.institute_id = props.match.params.institute_id;
        this.department_id = props.match.params.department_id;
    }

    componentDidMount() {

        this.NO_OF_COMPONENTS_TO_LOAD = 4;

        getSiteConfig(this);

        getInstitute(this, this.institute_id);

        getDepartments(this, this.institute_id);

        getSocialMediaLinks(this);
    }
    
    static getDerivedStateFromError(error) {
        // Update state so the next render will show the fallback UI.
        return { hasError: true };
      }

    componentDidCatch(error, errorInfo) {
        // You can also log the error to an error reporting service
        console.log(`error:${error} ${errorInfo}`);
        
        this.state = {
            hasError: true,
            loading: 50
        }
      }
      
    render() {
        return (

            <DepartmentPageContainer 
                departments={this.state.Departments}
                institute={this.state.Institute}
                site={this.state.Site}
                socialmediadata={this.state.socialmediadata}
                loading={this.state.loading}
            />
        )
    }
};

export const DepartmentPageContainer = ({departments, institute, site, socialmediadata, loading = 0}) => {
    if (departments === undefined || institute === undefined || site === undefined) {
        return ( 
            <React.Fragment></React.Fragment>
        )
    } else {
        let breadcrumbItems = [
            {text:"Home", url:"/"}, 
            {text:institute.name, url:`/institute/`},
        ]

        return (
            <React.Fragment>
                <BannerWidget heading={institute.name} description={institute.description} />
                <SpinnerWidget loading={loading} />
                <div id="main">
                    <div className="inner clearfix">
                        <BreadcrumbWidget breadcrumbItems={breadcrumbItems} activePageName={institute.name} />    
                        <DepartmentBoxMenuWidget data={departments} typeLabelText="Department" typeButtonText="View Department" typeButtonClass="button fit" typeDisabledButtonText="Coming Soon" typeDisabledButtonClass="button fit disabled" />
                    </div>
                </div>
                <FooterWidget heading={site.name} summary={site.description} socialmedia={socialmediadata} />
            </React.Fragment>
        )
    }
}


export default DepartmentPage;