import React from 'react';
import { SchemeOfWorkBoxMenuWidget } from '../widgets/SchemeOfWorkBoxMenuWidget';
import BannerWidget from '../widgets/BannerWidget';
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
            Loading: true
        }
    
        this.socialmediadata = [];
    }

    componentDidMount() {

        getSiteConfig(this);

        this.socialmediadata = getSocialMediaLinks();
        
        getSchemesOfWork(this);
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
        }
      }
      
    render() {
        return (

            <SchemeOfWorkPageContainer 
                site={this.state.Site}
                schemesofwork={this.state.SchemesOfWork}
                socialmediadata={this.socialmediadata}
                loading={this.state.Loading}
            />
        )
    }
};

export const SchemeOfWorkPageContainer = ({schemesofwork, site, socialmediadata, loading}) => {
    if (schemesofwork === undefined || site === undefined) {
        return ( 
            <React.Fragment></React.Fragment>
        )
    } else {

        return (
            <React.Fragment>
                    
                <BannerWidget heading={site.name} description={site.description} />
                    <div id="main">
                        <div className="inner">
                            <SchemeOfWorkBoxMenuWidget data={schemesofwork} typeLabelText="Course" typeButtonText="View Course" />
                        </div>
                    </div>
                <FooterWidget heading={site.name} summary={site.description} socialmedia={socialmediadata} />

            </React.Fragment>
        )
    }
}


export default SchemeOfWorkPage;