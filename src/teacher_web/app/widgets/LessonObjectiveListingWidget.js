import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

import AdminButtonWidget from '../widgets/AdminButtonWidget';
import CreatedByWidget from '../widgets/CreatedByWidget';
import TopicBadgeWidget from '../widgets/TopicBadgeWidget';
import TopicEditWidget from '../widgets/TopicEditWidget';
import SoloBadgeWidget from '../widgets/SoloBadgeWidget';

export const LessonObjectiveListingWidgetItem = ({row, auth}) => {
    if(row === undefined) {
      return (<Fragment></Fragment>);
    } else {
      return (
          <Fragment>
              <div className="post-preview">
                  <h2 className="post-title">
                    <SoloBadgeWidget solo_taxonomy_level={row.solo_taxonomy_level} /> {row.description}
                  </h2>
                  <h3 className="post-subtitle">{row.topic_name}</h3>
                  <TopicBadgeWidget list1={row.key_words} />
                  <TopicEditWidget auth={auth} />
              </div>
          </Fragment>
        )
    }
}

export const LessonObjectiveListingWidget = ({data, auth}) => {

    if(data === undefined) {
        return (<Fragment></Fragment>);
    } else if (data.length === 0) {
        return (
            <div className="alert alert-info" role="alert">
                <span className="small">There are no learning objectives for this lesson.</span>
                <AdminButtonWidget buttonText="Click here to get started." auth={auth} to='/lesson/new' />
            </div>
        );
    } else {
        return (
            data.learning_objectives.map(item => (
                  <LessonObjectiveListingWidgetItem key={item.id} row={item} auth={auth} />
              )
            )
      )
    };
};
