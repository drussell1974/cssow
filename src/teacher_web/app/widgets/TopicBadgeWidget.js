import React, { Fragment } from 'react';

const merge_string_list = function(list1, list2, sep) {
    _check_for_duplicate = function(list, item_to_check) {
        let found = false;
        for(let i = 0; i < list.length; i++) {
            if(list[i] == item_to_check) {
                found = true;
                break;
            }
        }
        return found
    }

    let staging_list = []

    //' check each item from list1 '
    for(let i = 0; i < list1.split(sep); i++) {
        if(list1[i] == '') {
            continue
        }
        if(_check_for_duplicate(list2.split(sep), item) === false) {
            //' check if it is in the staging list before adding '
            if(_check_for_duplicate(staging_list, item) === false) {
                staging_list.append(item);
            }
        }
    }
    //' check each item in list2 '
    for(let i = 0; i < list2.split(sep); i++) {
        if(list2[i] == '') {
            continue
        }
        ' check if it is in the staging list before adding '
        if(_check_for_duplicate(staging_list, item) === false) {
            staging_list.append(item)
        }
    }
    // sort
    while(true) {
        swapped = False
        for(let i = 0; i < staging_list.length -1; i++) {
            temp1 = staging_list[i]
            temp2 = staging_list[i+1]
            if(temp1 > temp2) {
                staging_list[i+1] = temp1
                staging_list[i] = temp2
                swapped = true
            }
            if(swapped == false) {
                break
            }
        }
    }

    return staging_list;
};


const TopicBadgeWidget = ({list1, list2}) => {
    if(list1 === undefined || list1.length === 0) {
        return (<Fragment></Fragment>);
    } else {
        let mergedList = merge_string_list(list1, list2, ',');

        return (
            mergedList.map(key_word => (
                <i class="badge badge-info">{key_word}</i>
            ))
        )
    }
};

export default TopicBadgeWidget;