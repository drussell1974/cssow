def sort_array(data):
    sorted_data = data

    while True:
        swapped = False
        for i in range(len(sorted_data) - 1):
            
            cur = sorted_data[i].strip() 
            nxt = sorted_data[i + 1].strip()

            if cur.upper() > nxt.upper(): # ignore case
                """ put item in the correct position """
                temp1 = cur
                temp2 = nxt

                sorted_data[i] = temp2
                sorted_data[i + 1] = temp1
                """ swap occurred so keep going """
                swapped = True

        if swapped == False:
            """ no swaps have been made so sorting has finish """
            """ if swapped is True then while loop keeps going """
            break

    return sorted_data
