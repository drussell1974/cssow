import React from 'react';
import BannerWidget from '../widgets/BannerWidget';
import BreadcrumbWidget from '../widgets/BreadcrumbWidget';
import FooterWidget from '../widgets/FooterWidget';
import { SpinnerWidget } from '../widgets/SpinnerWidget';
import { getMarkdown, getCourse, getLesson, getSocialMediaLinks, getSiteConfig, getResource } from '../services/apiReactServices';
import { MarkdownWidget } from '../widgets/MarkdownWidget';
import { LoginWidget } from '../widgets/LoginWidget';

class LoginPage extends React.Component {
    
    onProgress() {
        return this.state.loading + 100 / 3;
    }

    constructor(props){
        super(props);
        this.state = {
            Site: {},
            redirect: {},
            hasError: false,
            loading: 0,
            socialmediadata: []
        }
    }

    componentDidMount() {

        this.NO_OF_COMPONENTS_TO_LOAD = 2;
        
        getSiteConfig(this);

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
            loading: 50
        }
      }
      
    render() {

        return (
            <React.Fragment>
                <LoginPageContainer 
                    site={this.state.Site}
                    socialmediadata={this.state.socialmediadata}
                    loading={this.state.loading}
                />
            </React.Fragment>
        )
    }
};

export const LoginPageContainer = ({site, socialmediadata, loading = 0}) => {
    if (site === undefined) {
        return ( 
            <React.Fragment></React.Fragment>
        )
    } else {
        
        let breadcrumbItems = [
            {text:"Home", url:"/"},
        ]
        
        let redirect = { url: "/" };

        return (
            <React.Fragment>

                <BannerWidget heading={site.name} description={site.description} />
                <SpinnerWidget loading={loading} />
                <div id="main">
                    <div className="inner clearfix">
                        <BreadcrumbWidget breadcrumbItems={breadcrumbItems} activePageName={"Home"} />    
                        <LoginWidget redirect={redirect} />
                    </div>
                </div>
                <FooterWidget heading={site.name} summary={site.description} socialmedia={socialmediadata} />

            </React.Fragment>
        )
    }
}

export default LoginPage;