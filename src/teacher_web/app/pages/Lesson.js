import React, { Fragment } from 'react';
import ApiReactService from '../services/ApiReactService';

import BannerWidget from '../widgets/BannerWidget';
import BlackboardDisplayButton from '../widgets/BlackboardDisplayButton';
import ContentHeadingWidget from '../widgets/ContentHeadingWidget';
import SidebarNavWidget, { Mapper }from '../widgets/SidebarNavWidget';
import { LessonObjectiveListingWidget } from '../widgets/LessonObjectiveListingWidget';

export const LessonPageLayout = ({onSidebarNavItemClicked, lessons = [], lesson = {}}) => {
    return (
        <div className="container">
            <div className="row">
                <div className="col-lg-12 col-md-14 content-heading">
                    <ContentHeadingWidget main_heading={lesson.title} sub_heading={lesson.scheme_of_work_name} strap_line={lesson.strap_line} />
                </div>
            </div>
            <div className="row">
                <div className="col-lg-4 col-md-4">
                    <BlackboardDisplayButton lesson={lesson} />
                    <SidebarNavWidget data={Mapper.TransformLessons(lessons, lesson.id)} onItemClicked={onSidebarNavItemClicked} />
                </div>
                <div className="col-lg-8 col-md-10 mx-auto">
                    
                    <LessonObjectiveListingWidget data={lesson.learning_objectives} />
                    
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

        this.handleSidebarNavItemClicked = this.handleSidebarNavItemClicked.bind(this)
    }

    componentWillMount() {
        ApiReactService.getLessons(this, this.props.match.params.scheme_of_work_id);
        ApiReactService.getLesson(this, this.props.match.params.scheme_of_work_id, this.props.match.params.learning_episode_id);
    }

    handleSidebarNavItemClicked(learningEpisodeId) {
        console.log(`executing: handleSidebarNavItemClicked(learningEpisodeId)`);
        ApiReactService.getLesson(this, this.props.match.params.scheme_of_work_id, learningEpisodeId);
    }   

    render() {

        return (        
            <Fragment>
                <LessonPageLayout lessons={this.state.Lessons} lesson={this.state.Lesson} onSidebarNavItemClicked={this.handleSidebarNavItemClicked} />
            </Fragment>
        )
    }
};

export default Lesson;