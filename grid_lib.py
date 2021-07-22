def normalize(array, qual=True):
    """
    Returns a new version of the given array in which the quantitative values
    have been normalized between 0 and 1.
    WARNING: this function assumes by default there is one qualitative feature
    at the index 0. If this is not the case, please set the qual parameter to
    False.
    :param array : the array containing the values to normalize
    :param qual (default=True) : excludes the first variable from normalization
    if set to True
    :return : a normalized array
    """
    res = []
    if qual:
        res.append(array[0])

    to_norm = []
    # The loop should start index 0 is qual is False and 1 if True
    # Therefore there is no need for another "begin" variable
    for i in range(qual, len(array)):
        to_norm.append(int(array[i]))

    max_norm = max(to_norm)
    min_norm = min(to_norm)
    for intensity in to_norm:
        res.append((intensity - min_norm) / (max_norm - min_norm))

    return res

def uniformize(grid, letter, place, replacement):
    """Finds attributes starting by the designated letter, in the designated
    place (i.e place=0 means first attribute in the rows) and replace them by
    the designated replacement in a new grid.
    Useful to uniformize individuals named separately into a same category.
    Example:
    buffalos = [["B1", "green", 0],
    ["B2", "red", 3],
    ["C4", "blue", 8],
    ["B3", "yellow", 6]]
    buffalos_uni = uniformize(buffalos, 'B', 0, "buffalo")
    buffalos_uni now refers to:
    [["buffalo", "green", 0],
    ["buffalo", "red", 3],
    ["C4", "blue", 8],
    ["buffalo", "yellow", 6]]

    :param grid : the grid you wish to uniformize
    :param letter : the letter to find
    :param place : the index of the attribute to replace
    :param replacement : what to replace the attribute with
    :return : an array of arrays
    """
    res = []
    for line in grid:
        new_line = []
        for i in range(place):
            new_line.append(line[i])
        
        if line[place][0] == letter:
            new_line.append(replacement)
        else:
            new_line.append(line[place])
        
        for i in range(place+1, len(line)):
            new_line.append(line[i])

        res.append(new_line)

    return res


def make_intervals(arrays, nb_intervals):
    """Gives intervals for same-length arrays
    :param arrays : the arrays to be put in the intervals
    :param nb_intervals: the number of desired intervals
    :return : an array of intervals
    """
    
    res = []
    step = len(arrays[0]) // (nb_intervals-1)

    # Ordering the arrays
    ordered = []
    for array in arrays:
        ordered.append(sorted(array))

    # Getting the borders
    borders = []
    for h in range(len(arrays)):
        array_borders = []
        for i in range((step-1), len(arrays[0]), step):
            array_borders.append(float(ordered[h][i]))
        borders.append(array_borders)

    # Getting the average for each border
    borders_mean = []
    for i in range(len(borders[0])):
        border_mean = 0
        for j in range(len(borders)):
            border_mean += borders[j][i]
        border_mean = border_mean / len(borders)
        borders_mean.append(border_mean)

    # Putting the intervals together
    res.append("'(-inf-" + str(borders_mean[0])  + "']")
    for i in range(1, len(borders_mean)):
        res.append("'(" + str(borders_mean[i-1]) + "-" + str(borders_mean[i]) + "]'")

    res.append("'(" + str(borders_mean[-1]) + "-inf)'")
    res = list(dict.fromkeys(res))
    return res


def discretize(arrays, nb_intervals):
    """Discretizes same-length arrays into quantiles
    :param arrays : the array of arrays to discretize
    :param nb_quantiles : the number of desired intervals
    :return : an array of intervals
    """
    res = []
    step = len(arrays[0]) // (nb_intervals-1)

    # Ordering the arrays
    ordered = []
    for array in arrays:
        ordered.append(sorted(array))

    # Getting the borders
    borders = []
    for h in range(len(arrays)):
        array_borders = []
        for i in range((step-1), len(arrays[0]), step):
            array_borders.append(ordered[h][i])
        borders.append(array_borders)

    # Getting the average for each border
    borders_mean = []
    for i in range(len(borders[0])):
        border_mean = 0
        for j in range(len(borders)):
            border_mean += borders[j][i]
        border_mean = border_mean / len(borders)
        borders_mean.append(border_mean)

    # Putting the intensities in the intervals
    for array in arrays:
        res_line = []
        for intensity in array:
            for i in range(len(borders_mean)):
                if intensity <= borders_mean[i]:
                    if i == 0:
                        res_line.append("'(-inf-" + str(borders_mean[0]) + "]'")
                    else:
                        res_line.append("'(" + str(borders_mean[i-1]) + "-" + str(borders_mean[i]) + "]'")
                    break
                elif intensity > borders_mean[-1]:
                    res_line.append("'(" + str(borders_mean[-1]) + "-inf)'")
                    break
        res.append(res_line)
    return res