import React, { Fragment } from 'react';
import { Link } from 'react-router-dom';

import AdminButtonWidget from '../widgets/AdminButtonWidget';
import CreatedByWidget from '../widgets/CreatedByWidget';
import TopicBadgeWidget from '../widgets/TopicBadgeWidget';
import TopicEditWidget from '../widgets/TopicEditWidget';
import TopicGroupHeadingWidget from '../widgets/TopicGroupHeadingWidget';

export const LessonListingWidgetItem = ({row, current_topic_name, auth}) => {
    if(row === undefined) {
      return (<Fragment></Fragment>);
    } else {
      return (
          <Fragment>
            <TopicGroupHeadingWidget row={row} current_topic_name={current_topic_name} />
            <div className="post-preview">
                <Link to={`/schemeofwork/${row.scheme_of_work_id}/lessons/${row.id}`} name={`lesson${row.id}`}>
                  <h2 className="post-title">
                    {`Lesson ${row.order_of_delivery_id} - ${row.title}`}
                  </h2>
                  <h3 className="post-subtitle">{row.summary}</h3>
                </Link>
                <TopicBadgeWidget list1={row.key_words} list2={row.key_words_from_learning_objectives} />

                <TopicEditWidget auth={auth} />

                <CreatedByWidget row={row} />
            </div>
            <hr />
          </Fragment>
        )
    }
}

export const LessonListingWidget = ({pager, page, auth}) => {

    if(pager === undefined) {
        return (<Fragment></Fragment>);
    } else if (pager.allData.length === 0) {
        return (
            <div className="alert alert-info" role="alert">
                <span className="small">There are no lessons for this scheme of work.</span>
                <AdminButtonWidget buttonText="Click here to get started." auth={auth} to='/lesson/new' />
            </div>
        );
    } else {
      
        let current_topic_name = '';
        let pagedData = pager.GetPagedData(page);
        
        return (
          <Fragment>
            {pagedData.map(item => (
                    <LessonListingWidgetItem key={item.id} row={item} topic_name={current_topic_name} auth={auth} />
                )
              )}
            <p className="paging-info small">{`Showing page ${pager.page} of ${pager.pagerSize} (total records: ${pager.allData.length})`}</p>
          </Fragment>
      )
    };
};