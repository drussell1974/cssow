import React from 'react';
import { LessonBoxMenuWidget } from '../widgets/LessonBoxMenuWidget';
import BannerWidget from '../widgets/BannerWidget';
import FooterWidget from '../widgets/FooterWidget';
import apiReactServices from '../services/apiReactServices';

class Index extends React.Component {
    
    constructor(props){
        super(props);
        this.state = {
            SchemeOfWork: {},
            Lessons: [],
            hasError: false,
        }
    
        this.socialmediadata = [];
    }

    componentDidMount() {

        this.socialmediadata = apiReactServices.getSocialMediaLinks();
        
        apiReactServices.getSchemeOfWork(this);

        apiReactServices.getLessons(this);   
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
            <React.Fragment>
                
                <BannerWidget data={this.state.SchemeOfWork} />
                
                <div id="main">
                    <div className="inner">
                        <LessonBoxMenuWidget data={this.state.Lessons} />
                    </div>
                </div>

                <FooterWidget heading="Computer Science SOW" summary='' socialmedia={this.socialmediadata} />

            </React.Fragment>
        )
    }
};

export default Index;