import React from 'react';
import { InstituteBoxMenuWidget } from '../widgets/InstituteBoxMenuWidget';
import BannerWidget from '../widgets/BannerWidget';
import BreadcrumbWidget from '../widgets/BreadcrumbWidget';
import FooterWidget from '../widgets/FooterWidget';
import { SpinnerWidget } from '../widgets/SpinnerWidget';
import { getInstitutes, getSiteConfig, getSocialMediaLinks } from '../services/apiReactServices';

class InstitutePage extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            Site: {},
            Institutes: [],
            loading: 0,
            socialmediadata: [],
            hasError: false,
            error: {}
        }

        this.institute_id = 2; //props.match.params.institute_id;
    }

    componentDidMount() {

        this.NO_OF_COMPONENTS_TO_LOAD = 3;

        getSiteConfig(this);
        
        getInstitutes(this);

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

            <InstitutePageContainer 
                site={this.state.Site}
                institutes={this.state.Institutes}
                socialmediadata={this.state.socialmediadata}
                loading={this.state.loading}
            />
        )
    }
};

export const InstitutePageContainer = ({institutes, site, socialmediadata, loading = 0}) => {
    if (institutes === undefined || site === undefined) {
        return ( 
            <React.Fragment><center>institute could not be loaded</center></React.Fragment>
        )
    } else {

        let breadcrumbItems = [
            {text:"Home", url:"/"},
        ]

        return (
            <React.Fragment>
                    
                <BannerWidget heading={site.name} description={site.description} />
                <SpinnerWidget loading={loading} />
                <div id="main">
                    <div className="inner clearfix">
                        <BreadcrumbWidget activePageName={"Institutes"} breadcrumbItems={breadcrumbItems} />   
                        <InstituteBoxMenuWidget data={institutes} typeLabelText="Institutes" typeButtonText="View Institute" typeButtonClass="button fit" typeDisabledButtonText="Coming Soon" typeDisabledButtonClass="button fit disabled" />
                    </div>
                </div>
                <FooterWidget heading={site.name} summary={site.description} socialmedia={socialmediadata} />

            </React.Fragment>
        )
    }
}


export default InstitutePage;