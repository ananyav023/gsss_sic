'''# Find Nth term of the series: 1  2  2  3  3  5  5  7  8  11  13  13
series = [1, 2, 2, 3, 3, 5, 5, 7, 8, 11, 13, 13]
n = int(input("Enter Nth term : "))
if 1 <= n <= len(series):
    print("Nth term is :", series[n - 1])
else:
    print("N is out of range.")
'''
def get_nth_term(n):
    series = [1, 2, 2, 3, 3, 5, 5, 7, 8, 11, 13, 13]
    if 1 <= n <= len(series):
        return series[n-1]
    else:
        return "Index out of range"
n = int(input("Enter the value of N: "))
result = get_nth_term(n)
print(f"The {n}th term is: {result}")
