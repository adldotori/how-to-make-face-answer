subject = ['audio&speech', 'nlp', 'vision', 'recommend']
all_subject_name = ''
# ----------------------------------------
# TODO : Concatenate all subject name.
# >>> audio&speech nlp vision recommend 
for i in subject:
    all_subject_name+= i+' '
print(all_subject_name)
# ----------------------------------------

if all_subject_name == 'audio&speech nlp vision recommend ':
    print('[+] Stage1 Success!\n')
else:
    print('[-] Stage1 Fail...\n')


grade = [4.5, 3.5, 4.0, 4.0]
avg = 0
# ----------------------------------------
# TODO : Compute average of grade. Use len() function.
for i in grade:
    avg += i
avg /= len(grade)
print(avg)
# ----------------------------------------

if avg == 4:
    print('[+] Stage2 Success!\n')
else:
    print('[-] Stage2 Fail...\n')


grade = [4.5, 3.5, 4.0, 4.0]

# ----------------------------------------
# TODO : Change all grade to 4.5. Use range(), len() function.
for i in range(len(grade)):
    grade[i] = 4.5
print(grade)
# ----------------------------------------

if grade == [4.5, 4.5, 4.5, 4.5]:
    print('[+] Stage3 Success!\n')
else:
    print('[-] Stage3 Fail...\n')


subject = ['audio&speech', 'nlp', 'vision', 'recommend']
grade = [4.5, 3.5, 4.0, 4.0]

# ----------------------------------------
# TODO : Print like this. Use zip() function.
# >>> audio&speech : 4.5/nlp : 3.5/vision : 4.0/recommend : 4.0/
string = ''
for i, j in zip(subject, grade):
    string+= i+' : '+str(j) + '/'
print(string)
# ----------------------------------------

if string == 'audio&speech : 4.5/nlp : 3.5/vision : 4.0/recommend : 4.0/':
    print('[+] Stage4 Success!\n')
else:
    print('[-] Stage4 Fail...\n')


grade = {'audio&speech': 4.5, 'nlp': 3.5, 'vision': 4.0, 'recommend': 4.0}
avg = 0

# ----------------------------------------
# TODO : Compute average of grade. Use values(), len() function.
for i in grade.values():
    avg += i
avg /= len(grade)
print(avg)
# ----------------------------------------

if  avg == 4:
    print('[+] Stage5 Success!\n')
else:
    print('[-] Stage5 Fail...\n')


# all_grade is grade of two students.
all_grade = [{'audio&speech': 4.5, 'nlp': 3.5, 'vision': 4.0, 'recommend': 4.0}, {'audio&speech': 2.5, 'nlp': 3.0, 'vision': 4.5, 'recommend': 4.5}]
avg_grade = {'audio&speech': 0, 'nlp': 0, 'vision': 0, 'recommend': 0}

# ----------------------------------------
# TODO : Compute average of each subject.
# {'audio&speech':3.5, 'nlp':3.25, 'vision':4.25, 'recommend':4.25}
for student in all_grade:
    for grade in student.items():
        avg_grade[grade[0]] += grade[1]/len(all_grade)
print(avg_grade)
# ----------------------------------------

if str(avg_grade) == '{\'audio&speech\': 3.5, \'nlp\': 3.25, \'vision\': 4.25, \'recommend\': 4.25}':
    print('[+] Stage6 Success!\n')
else:
    print('[-] Stage6 Fail...\n')