from typing import List
from pprint import pprint

def find_max_val(weights: List[int], vals: List[int], targeted_weight: int):

    max_val_sum = 0
    max_val_weight = 0

    for row in range(len(vals)):
        row_weight = weights[row]
        row_val = vals[row]

        for col in range(len(vals)):
            
            if row == col:
                continue

            if (row_weight + weights[col]) <= targeted_weight:
                row_weight = row_weight + weights[col]
                row_val = row_val + vals[col]

                if row_val > max_val_sum:
                    max_val_sum = row_val
                    max_val_weight = row_weight
           

    return (max_val_weight, max_val_sum)        

            



print(find_max_val([5, 10, 4, 20, 1], [2, 8, 10, 1, 12], 20))



