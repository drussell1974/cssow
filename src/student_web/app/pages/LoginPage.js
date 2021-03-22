import React from 'react';
import { useHistory } from 'react-router-dom';
import BannerWidget from '../widgets/BannerWidget';
import BreadcrumbWidget from '../widgets/BreadcrumbWidget';
import FooterWidget from '../widgets/FooterWidget';
import { SpinnerWidget } from '../widgets/SpinnerWidget';
import { getMarkdown, getCourse, getLesson, getSocialMediaLinks, getSiteConfig, getResource, getLessonFromClassCode } from '../services/apiReactServices';
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
            //redirect: {},
            hasError: false,
            loading: 0,
            socialmediadata: [],
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

    handleSubmit(e, onFetch){
        // #205 call api to get scheduled lesson getLessonFromClassCode(this)
        getLessonFromClassCode(this, e.class_code, onFetch);
    }
      
    render() {

        return (
            <React.Fragment>
                <LoginPageContainer 
                    site={this.state.Site}
                    socialmediadata={this.state.socialmediadata}
                    onSubmit={ this.handleSubmit.bind(this) }
                    onFetch= { this.handleSubmit.bind(this) }
                    class_code={ this.state.class_code }
                    loading={this.state.loading}
                />
            </React.Fragment>
        )
    }
};

export const LoginPageContainer = ({site, socialmediadata, onSubmit, onFetch, class_code, loading = 0}) => {
    if (site === undefined) {
        return ( 
            <React.Fragment></React.Fragment>
        )
    } else {
        
        let breadcrumbItems = [
            {text:"Home", url:"/"},
        ]
        
        //let redirect = { url: "/" };

        return (
            <React.Fragment>

                <BannerWidget heading={site.name} description={site.description} />
                <SpinnerWidget loading={loading} />
                <div id="main">
                    <div className="inner clearfix">
                        <BreadcrumbWidget breadcrumbItems={breadcrumbItems} activePageName={"Home"} />    
                        <LoginWidget class_code={class_code} onSave={ onSubmit } onFetch={ onFetch } />
                    </div>
                </div>
                <FooterWidget heading={site.name} summary={site.description} socialmedia={socialmediadata} />

            </React.Fragment>
        )
    }
}

export default LoginPage;