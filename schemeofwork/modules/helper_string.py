def merge_string_list(list1, list2, sep):
    def _check_for_duplicate(list, item_to_check):
        """ return true if found otherwise false """
        found = False
        for item in list:
            if item == item_to_check:
                found = True
                break
        return found


    staging_list = []

    ' check each item from list1 '
    for item in list1.split(sep):
        if item == '':
            continue
        if _check_for_duplicate(list2.split(sep), item) == False:
            ' check if it is in the staging list before adding '
            if _check_for_duplicate(staging_list, item) == False:
                staging_list.append(item)

    ' check each item in list2 '
    for item in list2.split(sep):
        if item == '':
            continue
        ' check if it is in the staging list before adding '
        if _check_for_duplicate(staging_list, item) == False:
            staging_list.append(item)

    # sort
    while True:
        swapped = False
        for i in range(len(staging_list)-1):
            temp1 = staging_list[i]
            temp2 = staging_list[i+1]
            if temp1 > temp2:
                staging_list[i+1] = temp1
                staging_list[i] = temp2
                swapped = True
        if swapped == False:
            break

    return staging_list


def dictionary_to_string(collection, key, filter = None):
    """ show key-value as a comma seperated list """
    return_string = ""
    for item in collection:
        if filter is not None:
            if item[list(filter.keys())[0]] == list(filter.values())[0]:
                return_string = return_string + "{}, ".format(item[key])
        else:
            return_string = return_string + "{}, ".format(item[key])

    return return_string.rstrip(", ")


def string_to_list(string, SEP):
    if string == "" or string is None:
        return []
    else:
        return string.split(SEP)
