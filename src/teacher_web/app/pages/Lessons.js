import React, { Fragment } from 'react';

import ApiReactService from '../services/ApiReactService';
import pager from '../services/Pager';

import ContentHeadingWidget from '../widgets/ContentHeadingWidget';
import SidebarNavWidget, { Mapper } from '../widgets/SidebarNavWidget';
import AdminButtonWidget from '../widgets/AdminButtonWidget';
import AddLearningMaterialsWidget from '../widgets/AddLearningMaterialsWidget';
import PaginationWidget from '../widgets/PaginationWidget';
import { LessonListingWidget } from '../widgets/LessonListingWidget';

export const LessonsPageLayout = ({onBookmarkClicked, onSidebarNavItemClicked, page = 1, lessons = [],  schemeofwork = {}, schemesOfWork = []}) => {
    
    pager.init(lessons, 10, page);

    return (
        <div className="container">
            <div className="row">
                <div className="col-lg-12 col-md-14 content-heading">
                    <ContentHeadingWidget main_heading={schemeofwork.name} />
                </div>
            </div>
            <div className="row">
                <div className="col-lg-4 col-md-4">
                    <SidebarNavWidget data={Mapper.TransformSchemesOfWork(schemesOfWork, schemeofwork.id)} onItemClicked={onSidebarNavItemClicked} />
                </div>
                <div className="col-lg-8 col-md-10 mx-auto">
                    <div className="clearfix pagination-top">
                        <PaginationWidget pager={pager} uri={`/schemeofwork/${schemeofwork.id}/lessons`} onBookmarkClicked={onBookmarkClicked} />
                    </div>
                    <AdminButtonWidget />

                    <LessonListingWidget pager={pager} page={page} />
                    
                    <div className="clearfix pagination-bottom">
                        <PaginationWidget pager={pager} uri={`/schemeofwork/${schemeofwork.id}/lessons`} onBookmarkClicked={onBookmarkClicked} />
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
            SchemeOfWorkId: this.props.match.params.scheme_of_work_id,
            SchemesOfWork: [],
            Lessons: [],
            hasError: false,
        };
        this.handleBookmarkClicked = this.handleBookmarkClicked.bind(this);
        this.handleSidebarNavItemClicked = this.handleSidebarNavItemClicked.bind(this);
    }

    componentDidMount() {
        ApiReactService.getSchemesOfWork(this);
        ApiReactService.getSchemeOfWork(this, this.props.match.params.scheme_of_work_id);
        ApiReactService.getLessons(this, this.props.match.params.scheme_of_work_id);
    }

    handleBookmarkClicked(pageNumber) {
        this.setState({
            Page: pageNumber,
        })
    }

    handleSidebarNavItemClicked(scheme_of_work_id) {
        this.setState({
            SchemeOfWorkId: scheme_of_work_id,
        })
    }

    render() {

        return (        
            <Fragment>
                <LessonsPageLayout onBookmarkClicked={this.handleBookmarkClicked} onSidebarNavItemClicked={this.handleSidebarNavItemClicked} page={this.state.Page} lessons={this.state.Lessons} schemeofwork={this.state.SchemeOfWork} schemesOfWork={this.state.SchemesOfWork} />

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