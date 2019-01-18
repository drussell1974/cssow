def merge_string_list(list1, list2, sep):
    staging_list = ""
    for item1 in list1.split(sep):
        found = False
        for item2 in list2.split(sep):
            if item1 == item2:
                found = True
                break
        if found == False:
            staging_list = staging_list + item1 + ","


    for item1 in list2.split(sep):
        found = False
        for item2 in staging_list.split(sep):
            if item1 == item2:
                found = True
                break
        if found == False:
            staging_list = staging_list + item1 + ","

    return staging_list.rstrip(",").lstrip(",")
