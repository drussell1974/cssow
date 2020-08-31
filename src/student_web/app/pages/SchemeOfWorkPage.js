import React from 'react';
import { SchemeOfWorkBoxMenuWidget } from '../widgets/SchemeOfWorkBoxMenuWidget';
import BannerWidget from '../widgets/BannerWidget';
import BreadcrumbWidget from '../widgets/BreadcrumbWidget';
import FooterWidget from '../widgets/FooterWidget';
import { SpinnerWidget } from '../widgets/SpinnerWidget';
import { getSchemesOfWork, getSiteConfig, getSocialMediaLinks } from '../services/apiReactServices';

class SchemeOfWorkPage extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            Site: {},
            SchemesOfWork: [],
            hasError: false,
            loading: 0,
            socialmediadata: []
        }
    }

    componentDidMount() {

        this.NO_OF_COMPONENTS_TO_LOAD = 3;

        getSiteConfig(this);
        
        getSchemesOfWork(this);

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

            <SchemeOfWorkPageContainer 
                site={this.state.Site}
                schemesofwork={this.state.SchemesOfWork}
                socialmediadata={this.state.socialmediadata}
                loading={this.state.loading}
            />
        )
    }
};

export const SchemeOfWorkPageContainer = ({schemesofwork, site, socialmediadata, loading = 0}) => {
    if (schemesofwork === undefined || site === undefined) {
        return ( 
            <React.Fragment></React.Fragment>
        )
    } else {

        return (
            <React.Fragment>
                    
                <BannerWidget heading={site.name} description={site.description} />
                <SpinnerWidget loading={loading} />
                <div id="main">
                    <div className="inner clearfix">
                        <BreadcrumbWidget activePageName={"Home"} />    
                        <SchemeOfWorkBoxMenuWidget data={schemesofwork} typeLabelText="Course" typeButtonText="View Course" typeButtonClass="button fit" typeDisabledButtonText="Coming Soon" typeDisabledButtonClass="button fit disabled" />
                    </div>
                </div>
                <FooterWidget heading={site.name} summary={site.description} socialmedia={socialmediadata} />

            </React.Fragment>
        )
    }
}


export default SchemeOfWorkPage;