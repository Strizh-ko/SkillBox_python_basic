students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def func(students):
    lst = []
    count = 0
    for i in students.values():
        lst.extend(i['interests'])
        count += len(i['surname'])
    return lst, count

lst, count = func(students)
print('Общий список интересов:', lst)
print('Кол-во символов во всех фамилиях:', count)

pairs = {id: info["age"] for id, info in students.items()}
for id, age in pairs.items():
    print(f'id : {id}, age : {age}')