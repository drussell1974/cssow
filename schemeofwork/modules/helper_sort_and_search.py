def sort_array(data):
    sorted_data = data

    while True:
        swapped = False
        for i in range(len(sorted_data) - 1):
            if sorted_data[i] > sorted_data[i + 1]:
                """ put item in the correct position """
                temp1 = sorted_data[i]
                temp2 = sorted_data[i + 1]

                sorted_data[i] = temp2
                sorted_data[i + 1] = temp1
                swapped = True

        if swapped == False:
            """ no more sorting required so finish """
            break

    return sorted_data


def _sort_by_solo_and_group(data):
    sorted_data = data

    while True:
        swapped = False
        for i in range(len(sorted_data) - 1):
            if sorted_data[i].solo_taxonomy_level > sorted_data[i + 1].solo_taxonomy_level:
                """ put item in the correct position """
                temp1 = sorted_data[i]
                temp2 = sorted_data[i + 1]

                sorted_data[i] = temp2
                sorted_data[i + 1] = temp1
                swapped = True

        if swapped == False:
            """ no more sorting required so finish """
            break
    # bubble sort by group_name
    while True:
        swapped = False
        for i in range(len(sorted_data) - 1):
            if sorted_data[i].group_name > sorted_data[i + 1].group_name:
                """ put item in the correct position """
                temp1 = sorted_data[i]
                temp2 = sorted_data[i + 1]

                sorted_data[i] = temp2
                sorted_data[i + 1] = temp1
                swapped = True

        if swapped == False:
            """ no more sorting required so finish """
            break

    return sorted_data
