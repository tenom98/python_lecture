def sum_nums(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result
def ave_nums(*numbers):
    result = 0
    for n in numbers:
        result += n/3
    return result
print(sum_nums(10,20,30))
print(ave_nums(10,20,30,40,50))