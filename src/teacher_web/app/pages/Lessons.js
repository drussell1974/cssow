import React, { Fragment } from 'react';

import ApiReactService from '../services/ApiReactService';

import ContentHeadingWidget from '../widgets/ContentHeadingWidget';
import SidebarNavWidget from '../widgets/SidebarNavWidget';
import AdminButtonWidget from '../widgets/AdminButtonWidget';
import AddLearningMaterialsWidget from '../widgets/AddLearningMaterialsWidget';
import PaginationWidget from '../widgets/PaginationWidget';

const PageMenu = () => {
    
    return (
        <nav class="navbar navbar-expand-lg navbar-light" id="itemNav">
            <div class="container">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <Link class="nav-link" id="lnk-bc-schemes_of_work" href="/">Schemes of Work</Link>
                    </li>
                </ul>
            </div>
        </nav>
    )
}

class Lessons extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            Lessons: [],
            hasError: false,
        }
    }

    componentDidMount() {
        ApiReactService.getLessons(this);
    }

    render() {

        return (        
            <Fragment>
                
                <div class="container">
                    <div class="row">
                        <div class="col-lg-12 col-md-14 content-heading">
                            <ContentHeadingWidget />
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-lg-4 col-md-4">
                            <SidebarNavWidget />
                        </div>
                        <div class="col-lg-8 col-md-10 mx-auto">
                        <div class="clearfix">
                            <PaginationWidget />
                        </div>
                        <AdminButtonWidget />

                        <LessonListingWidget data={this.state.Lessons}/>
                         
                        <div class="clearfix">
                            <PaginationWidget />    
                        </div>
                        <AddLearningMaterialsWidget />
                        <hr/>
                    </div>
                </div>
                </div>

                <hr/>
                <div class="modal fade" id="keywordModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Key terms</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body" id="modal-keywords">

                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    </div>
                    </div>
                </div>
                </div>
            </Fragment>
        )
    }
};

export default Lessons;