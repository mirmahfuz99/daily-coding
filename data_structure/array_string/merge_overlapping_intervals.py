def merge(intervals):
    intervals.sort


    n = len(intervals)
    new_intervals = []
    new_intervals.append(intervals[0])

    for i in range(1,n):
        start, end = new_intervals[-1]

        if intervals[i][0] > end:              #Not overlapping
            new_intervals.append[intervals[i]]
        elif intervals[i][1] > end:            #Overlapping, end update required
            end = intervals[i][1]
            new_intervals[-1] = (start,end)    

        return new_intervals    
            

        

print(merge([(1, 3), (2, 6)]))        