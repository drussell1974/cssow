import React, { Fragment } from 'react';

// MODAL SCRIPT HERE

const TopicEditWidget = ({row, auth}) => {
    if(row === undefined || auth === false ) {
        return (<Fragment></Fragment>);
    } else {
        let keywordsData = `${row.key_words}, ${row.key_words_from_learning_objectives}`; 
        return (
            <a href={`#${row.id}`} class="btn-keyword-modal small" data-keywords={keywordsData}>
                Edit definitions
            </a>
        )
    }
};

export default TopicEditWidget;