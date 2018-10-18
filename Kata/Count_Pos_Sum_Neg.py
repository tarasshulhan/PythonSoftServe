def count_positives_sum_negatives(arr):
    Pos_Count = 0
    Neg_Sum = 0

    if arr == [] or arr is False:
        return []
    else:
        for i in arr:
            if i > 0:
                Pos_Count += 1
            else:
                Neg_Sum += i

        return [Pos_Count, Neg_Sum]