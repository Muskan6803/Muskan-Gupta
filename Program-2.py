# Problem-2: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
 
#   Output: (examples)
    # 1) input a = 1, then output : 1
    # 2) input a = 2, then output : 1, 3
    # 3) input a = 3, then output : 1, 3, 5
    # 4) input a = 4, then output : 1, 3, 5, 7
    # .
    # .
    # 5) input a = x, then output : 1, 3, 5, 7, .......

def generate_odd_series(a: int):
    series = []
    for i in range(a):
        series.append(2 * i + 1)
    return series

# Example usage
print("Input: 1 -> Output:", generate_odd_series(1))  # [1]
print("Input: 2 -> Output:", generate_odd_series(2))  # [1, 3]
print("Input: 4 -> Output:", generate_odd_series(4))  # [1, 3, 5, 7]
print("Input: 6 -> Output:", generate_odd_series(6))  # [1, 3, 5, 7, 9, 11]
