from typing import List


def correlate_arrays(arr1: List, arr2: List) -> List:

    corr = []
    for x_idx, x in enumerate(arr1):
        for y_idx, y in enumerate(arr2):
            if x_idx == y_idx:
                continue
            corr.append([x, y])

    corr_without_repetitions = []
    for i, elem in enumerate(corr):
        temp_arr = [elem[1], elem[0]]
        if corr.index(temp_arr) < i:
            continue
        corr_without_repetitions.append(elem)
    return corr_without_repetitions
