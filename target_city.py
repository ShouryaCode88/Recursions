tour_locations = ["India","Wahington D.C","Antarctica","Egypt","Romania","Nepal(Himalayas)","Egypt"]
target_city = "Egypt"

def linear_search(search_list,target_value):
    matches = []
    for idx in range(len(search_list)):
        if (search_list[idx] == target_value):
           matches.append(idx)

    if not matches:
        ValueError("{} is not in the list ".format(target_value))
    else:
        return matches
        
tour_stops = linear_search(tour_locations,target_city)
print("{} is in the following {}".format(target_city,tour_stops))
