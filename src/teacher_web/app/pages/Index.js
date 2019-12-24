import React, { Fragment } from 'react';
import BannerWidget from '../widgets/BannerWidget';
import { LatestSchemesOfWorkJumbotronWidget } from '../widgets/LatestSchemesOfWorkJumbotronWidget';
import ApiReactService from '../services/ApiReactService';

export const IndexLayout = ({data}) => {
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
                <IndexLayout data={this.state.SchemesOfWork} />
                <hr/>
            </Fragment>
        )
    }
};

export default Index;