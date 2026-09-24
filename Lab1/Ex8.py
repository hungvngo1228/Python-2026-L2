def extract_even(l):
    result = []
    for x in l:
        if x % 2 == 0:
            result.append(x)

    return result
numbers = [1, 4, 5, -1, 10]
print(extract_even(numbers))