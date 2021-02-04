# input: cleaned wave data
# output: a 2d array containing all of the unique hours of observations that appear in the data and the indices]
# at which they appear
def availableDatetimes(data):
    inds = []
    n = 0
    curr_time = data["datetime"][n]
    while n < data.shape[0]:
        if (data["datetime"][n].hour != curr_time.hour):
            inds += [n]
            curr_time = data["datetime"][n]
            n += 1

        elif (data["datetime"][n].hour == curr_time.hour):
            n += 1

    data = data.iloc[inds]
    l = len(inds)
    data = data.reset_index(drop=True)
    for i in range(0, l):
        data.at[i, "datetime"] = data.at[i, "datetime"].replace(minute=0)

    return data


# input: two datasets containing only the hourly info of the unique observations appearing in the data
# output: a joined array containing only the common observation times
def matchDataByTime2(d1, d2):
    d1 = availableDatetimes(d1)
    d2 = availableDatetimes(d2)
    matched = d1.merge(d2, how='inner', on="datetime")
    return matched


