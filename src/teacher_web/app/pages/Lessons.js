import React, { Fragment } from 'react';
import BannerWidget from '../widgets/BannerWidget';
import { LatestSchemesOfWorkJumbotronWidget } from '../widgets/LatestSchemesOfWorkJumbotronWidget';
import  getSchemesOfWork  from '../services/ApiReactService';

class Lessons extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            SchemesOfWork: [],
            hasError: false,
        }
    }

    componentDidMount() {
        getSchemesOfWork(this);
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

export default Lessons;