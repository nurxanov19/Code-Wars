def multi_table(number):
    my_str = ''
    for i in range(1, 11):
        if not i == 10:
            my_str += f'{i} * {number} = {i*number}\n'
        else: my_str += f'{i} * {number} = {i*number}'

    return my_str

print(multi_table(5))



