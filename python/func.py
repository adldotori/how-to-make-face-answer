def sum_salary(a, b):
    '''
        두 개의 월급 합을 더함
    '''
    print(f'Total salary is {a + b}')

def diff_salary(a, b=300):
    print(f'Salary\'s difference is {a - b}')


def return_salary_info(a, b):
    return a, b

if __name__ == '__main__':
    sum_salary(300, 400)
    diff_salary(500, 400)
    print(return_salary_info(100, 200))