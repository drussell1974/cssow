import React, { Fragment } from 'react';

import ApiReactService from '../services/ApiReactService';

import ContentHeadingWidget from '../widgets/ContentHeadingWidget';
import SidebarNavWidget, { Mapper } from '../widgets/SidebarNavWidget';
import AdminButtonWidget from '../widgets/AdminButtonWidget';
import AddLearningMaterialsWidget from '../widgets/AddLearningMaterialsWidget';
import PaginationWidget from '../widgets/PaginationWidget';
import { LessonListingWidget } from '../widgets/LessonListingWidget';

export const LessonsPageLayout = ({pager, page = 1, schemeofwork = {}, schemesOfWork = []}) => {
    
    return (
        <div className="container">
            <div className="row">
                <div className="col-lg-12 col-md-14 content-heading">
                    <ContentHeadingWidget main_heading={schemeofwork.name} />
                </div>
            </div>
            <div className="row">
                <div className="col-lg-4 col-md-4">
                    <SidebarNavWidget data={Mapper.TransformSchemesOfWork(schemesOfWork)}/>
                </div>
                <div className="col-lg-8 col-md-10 mx-auto">
                    <div className="clearfix pagination-top">
                        <PaginationWidget pager={pager} uri={`/schemeofwork/${schemeofwork.id}/lessons`} />
                    </div>
                    <AdminButtonWidget />

                    <LessonListingWidget pager={pager} page={page} />
                    
                    <div className="clearfix pagination-bottom">
                        <PaginationWidget pager={pager} uri={`/schemeofwork/${schemeofwork.id}/lessons`} />
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
            Page: 1,
            SchemeOfWork: {},
            SchemesOfWork: [],
            Lessons: [],
            hasError: false,
        }
    }

    componentDidMount() {
        ApiReactService.getSchemesOfWork(this);
        ApiReactService.getSchemeOfWork(this, this.props.match.params.scheme_of_work_id);
        ApiReactService.getLessons(this, this.props.match.params.scheme_of_work_id);
        
        var Pager = require('../services/Pager.js');
        this.pager = new Pager(this.state.Lessons);
    }

    render() {
        return (        
            <Fragment>
                <LessonsPageLayout pager={this.pager} page={this.state.Page} schemeofwork={this.state.SchemeOfWork} schemesOfWork={this.state.SchemesOfWork} />

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