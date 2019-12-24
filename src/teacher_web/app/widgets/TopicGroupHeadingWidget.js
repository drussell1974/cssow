import React, { Fragment } from 'react';

const TopicGroupHeadingWidget = ({row, current_topic_name}) => {
    if(row === undefined || current_topic_name === undefined || (row.topic_name.toLowerCase() === current_topic_name.toLowerCase()) ) {
        return (<Fragment></Fragment>);
    } else {
        return (
          <h1 className="group-heading">{row.year_name} {row.topic_name}</h1>
        )
    }
};

export default TopicGroupHeadingWidget;