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
                  <a href={`#${row.id}`}>
                    <h4 className="post-title">
                        <SoloBadgeWidget solo_taxonomy_level={row.solo_taxonomy_level} /> {row.description}
                    </h4>
                    <h5 className="post-subtitle">{row.topic_name}</h5>
                  </a>
                  <TopicBadgeWidget list1={row.key_words} />
                  <TopicEditWidget auth={auth} />
              </div>
              <hr/>
          </Fragment>
        )
    }
}

export const LessonObjectiveListingWidget = ({data, auth}) => {

    if(data === undefined || data.length === 0) {
        return (
            <div className="alert alert-info" role="alert">
                <span className="small">There are no learning objectives for this lesson.</span>
                <AdminButtonWidget buttonText="Click here to get started." auth={auth} to='/lesson/new' />
            </div>
        );
    } else {
        return (
            data.map(item => (
                  <LessonObjectiveListingWidgetItem key={item.id} row={item} auth={auth} />
              )
            )
      )
    };
};
