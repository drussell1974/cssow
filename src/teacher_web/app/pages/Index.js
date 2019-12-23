import React, { Fragment } from 'react';
import BannerWidget from '../widgets/BannerWidget';
import { LatestSchemesOfWorkJumbotronWidget } from '../widgets/LatestSchemesOfWorkJumbotronWidget';
import ApiReactService from '../services/ApiReactService';

class Index extends React.Component {
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
                <div className="container">
                    <div className="row">
                        <div className="col-lg-8 col-md-8 mx-auto">
                            <LatestSchemesOfWorkJumbotronWidget data={this.state.SchemesOfWork} />
                        </div>
                    </div>
                </div>
                <hr/>
            </Fragment>
        )
    }
};

export default Index;