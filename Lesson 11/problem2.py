print('_'* 70)
print('Narrative Bot: ')

name = input('Student Name: ')
grade = input('Grade: ')

print('Narrative: ')
print(name +', your grade in AP Computer Science is ' + grade + '%.')
grade = int(grade)
if grade > 65:
	print('You have excelled in all components in the class!')
	print('I wish you continued success in the next semester of AP Computer Science!')
else:
	print('This largely a result of missing projects and homework assignments.')
	print('Unfortunately, because this grade is less than a 65, you will have to complete an MBA assignment next semester.')
print('_'* 70)