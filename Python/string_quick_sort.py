from load import strings

def quicksort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)

    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


sorted_names = quicksort(strings)

# EXPLANATION
"""
                                values = [1,4,2,7,3,0]
                                        ||
                                        \/
                        less: [0] pivot: [1] more: [4,2,7,3]
                                        ||
                                        \/
return quicksort(less)          + pivot: [1] +                          quicksort(more)
        ||                                                                     ||                                                                    
        \/                                                                     \/
    values = [0]                                                        values = [4,2,7,3]
return values: [0]                                               less=[2,3] pivot: [4] more=[7]
                                                                                ||    
                                                                                \/
                                        return quicksort(less)            + pivot: [4] +          quicksort[more]
                                                ||                                                      ||    
                                                \/                                                      \/                                     
                                            values = [2,3]                                         values = [7]
                                        less: [] pivot: [2] more: [3]                            return values: [7]

                    return quicksort(less)     + pivot: [2] +       quicksort[more]
                                ||                                       ||                       
                                \/                                       \/                                                                                                                                               
                            values = []                             values = [3]
                        return values: []                        return values: [3]


result = [0] + [1] + (([] + [2] + [3]) + [4] + ([7]))
result = [0,1,2,3,4,7]
"""                         
