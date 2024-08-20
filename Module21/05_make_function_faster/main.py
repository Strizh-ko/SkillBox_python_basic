def calculating_math_func(data, fact_dct):
    result = 0

    if data in fact_dct:
        result = fact_dct[data]
    else:
        for index in range(max(fact_dct.keys()) + 1, data + 1):
            fact_dct[index] = index * fact_dct[index - 1]
            result = fact_dct[index]

    result /= data ** 3
    result = result ** 10
    return result



fact_dct = {1:1}
print(calculating_math_func(9, fact_dct))
print(calculating_math_func(6, fact_dct))
print(calculating_math_func(10, fact_dct))