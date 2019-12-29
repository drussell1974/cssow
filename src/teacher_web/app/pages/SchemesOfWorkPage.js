import React, { Fragment } from 'react';
import BannerWidget from '../widgets/BannerWidget';
import { LatestSchemesOfWorkJumbotronWidget } from '../widgets/LatestSchemesOfWorkJumbotronWidget';
import ApiReactService from '../services/ApiReactService';


export const SchemesOWorkPageLayout = ({data}) => {
    
    //document.title += " - Scheme of work";
    var siteH1Elem = document.querySelector(".site-heading h1");
    if(siteH1Elem !== null) {
        siteH1Elem.innerText = "Schemes of Work";
    }
    var siteSubElem = document.querySelector('.site-heading .subheading');
    if(siteSubElem !== null) {
        siteSubElem.innerText = "Our shared schemes of work by key stage";
    }
    
    return (
        <div className="container">
            <div className="row">
                <div className="col-lg-8 col-md-8 mx-auto">
                    <LatestSchemesOfWorkJumbotronWidget data={data} />
                </div>
            </div>
        </div>
    )
}

class SchemesOfWorkPage extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            SchemesOfWork: [],
            hasError: false,
        }
    }

    componentDidMount() {
        ApiReactService.getSchemesOfWork(this);
    }

    render() {

        return (        
            <Fragment>
                <SchemesOWorkPageLayout data={this.state.SchemesOfWork} />
                <hr/>
            </Fragment>
        )
    }
};

export default SchemesOfWorkPage;