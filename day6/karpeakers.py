#Take a four digit no where a digit cannot be reapeated twice 
def kaprekar_step(n):
    n_str = f"{n:04d}"
    desc = int(''.join(sorted(n_str, reverse=True)))
    asc = int(''.join(sorted(n_str)))
    result = desc - asc
    print(f"{desc} - {asc} = {result}")
    return result

# Example usage
number = 1100
result = kaprekar_step(number)




