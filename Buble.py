import time
from typing import List

def bubble_sort_recursive(arr: List[int], n: int) -> None:
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubble_sort_recursive(arr, n - 1)

data = [5, 2, 9, 1, 5, 6]
print("Sebelum:", data)
bubble_sort_recursive(data, len(data))
print("Sesudah:", data)

start_total_time = time.time()
end_total_time = time.time()
execution_total_time = end_total_time - start_total_time
print(execution_total_time)