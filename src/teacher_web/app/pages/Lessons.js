import React, { Fragment } from 'react';

import ApiReactService from '../services/ApiReactService';

import ContentHeadingWidget from '../widgets/ContentHeadingWidget';
import SidebarNavWidget from '../widgets/SidebarNavWidget';
import AdminButtonWidget from '../widgets/AdminButtonWidget';
import AddLearningMaterialsWidget from '../widgets/AddLearningMaterialsWidget';
import PaginationWidget from '../widgets/PaginationWidget';
import { LessonListingWidget } from '../widgets/LessonListingWidget';

const PageMenu = () => {
    
    return (
        <nav className="navbar navbar-expand-lg navbar-light" id="itemNav">
            <div className="container">
                <ul className="navbar-nav ml-auto">
                    <li className="nav-item">
                        <Link className="nav-link" id="lnk-bc-schemes_of_work" href="/">Schemes of Work</Link>
                    </li>
                </ul>
            </div>
        </nav>
    )
}

export const LessonsPageLayout = ({schemesOfWork, lessons}) => {
    return (
        <div className="container">
            <div className="row">
                <div className="col-lg-12 col-md-14 content-heading">
                    <ContentHeadingWidget />
                </div>
            </div>
            <div className="row">
                <div className="col-lg-4 col-md-4">
                    <SidebarNavWidget data={schemesOfWork}/>
                </div>
                <div className="col-lg-8 col-md-10 mx-auto">
                    <div className="clearfix">
                        <PaginationWidget />
                    </div>
                    <AdminButtonWidget />

                    <LessonListingWidget data={lessons}/>
                    
                    <div className="clearfix">
                        <PaginationWidget />    
                    </div>
                    <AddLearningMaterialsWidget />
                    <hr/>
                </div>
            </div>
        </div>
    )
}

class Lessons extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            SchemesOfWork: [],
            Lessons: [],
            hasError: false,
        }
    }

    componentDidMount() {
        ApiReactService.getSchemesOfWork(this);
        ApiReactService.getLessons(this, this.props.match.params.scheme_of_work_id);
    }

    render() {

        return (        
            <Fragment>
                
                <LessonsPageLayout schemesOfWork={this.state.SchemesOfWork} lessons={this.state.Lessons} />

                <hr/>
                <div className="modal fade" id="keywordModal" tabIndex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div className="modal-dialog" role="document">
                    <div className="modal-content">
                    <div className="modal-header">
                        <h5 className="modal-title" id="exampleModalLabel">Key terms</h5>
                        <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div className="modal-body" id="modal-keywords">

                    </div>
                    <div className="modal-footer">
                        <button type="button" className="btn btn-secondary" data-dismiss="modal">Close</button>
                    </div>
                    </div>
                </div>
                </div>
            </Fragment>
        )
    }
};

export default Lessons;