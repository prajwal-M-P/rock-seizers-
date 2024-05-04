student= {
    'name':'prajwal',
    'sub': {
        'physics':89,
        'mathematics':90,
        'biolagy':91,
        'chemistry':90
    }
}
print(len(list(student.items())))
print(list(student.keys()))
print(student['sub']['physics'])
student.update({'sum':400})
print(student)
print(student.get('age','Invalid key you pressed'))
print(student['sum'])
print(student.__subclasshook__)