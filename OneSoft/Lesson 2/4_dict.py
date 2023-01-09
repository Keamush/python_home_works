
head_manager = {
    'full name': 'Bob Smith',
    'salary': '100000',
    'age': '35',
    'position': 'Head manager'
}

QA = {
    'full name': 'Marco Polo',
    'salary': '75000',
    'age': '32',
    'position': 'QA'
}

PM = {
    'full name': 'John Lennon',
    'salary': '90000',
    'age': '36',
    'position': 'Project manager'
}
our_company = [head_manager, QA, PM]

for index, person in enumerate(our_company):
    for key, value in person.items():
        if value == 'Bob Smith':
            our_company[index]['full name'] = 'Mob Smith'

print(our_company)
