import React, { Fragment } from 'react';
import ApiReactService from '../services/ApiReactService';

import BannerWidget from '../widgets/BannerWidget';
import BlackboardDisplayButton from '../widgets/BlackboardDisplayButton';
import ContentHeadingWidget from '../widgets/ContentHeadingWidget';
import SidebarNavWidget, { Mapper }from '../widgets/SidebarNavWidget';
import PaginationWidget, { Mapper as PaginationMapper } from '../widgets/PaginationWidget';

export const LessonPageLayout = ({lessons = [], lesson = []}) => {
    return (
        <div className="container">
            <div className="row">
                <div className="col-lg-12 col-md-14 content-heading">
                    <ContentHeadingWidget />
                </div>
            </div>
            <div className="row">
                <div className="col-lg-4 col-md-4">
                    <BlackboardDisplayButton lesson={lesson} />
                    <SidebarNavWidget data={Mapper.TransformLessons(lessons)} />
                </div>
                <div className="col-lg-8 col-md-10 mx-auto">
                    <PaginationWidget data={PaginationMapper.TransformLessons(lessons)} />
                    <PaginationWidget data={PaginationMapper.TransformLessons(lessons)} />
                </div>
            </div>
        </div>
    )
}

class Lesson extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            Lesson: [],
            Lessons: [],
            hasError: false,
        }
    }

    componentDidMount() {
        ApiReactService.getLessons(this, this.props.match.params.scheme_of_work_id);
        ApiReactService.getLesson(this, this.props.match.params.scheme_of_work_id, this.props.match.params.learning_objective_id);
    }

    render() {

        return (        
            <Fragment>
                <LessonPageLayout lesson={this.state.Lesson} />
            </Fragment>
        )
    }
};

export default Lesson;