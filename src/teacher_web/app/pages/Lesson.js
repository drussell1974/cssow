import React, { Fragment } from 'react';
import BannerWidget from '../widgets/BannerWidget';
import { LatestSchemesOfWorkJumbotronWidget } from '../widgets/LatestSchemesOfWorkJumbotronWidget';
import ApiReactService from '../services/ApiReactService';

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
                <h1>Lesson</h1>
                <p>{this.state.Lesson.title}</p>
            </Fragment>
        )
    }
};

export default Lesson;