vision = 4.0
nlp = 3.5
speech = 4.5

# ----------------------------------------
# TODO : Compute average of grade
# avg = Sum of grade / N (N : count of grade)
avg = (vision + nlp + speech) / 3
print(avg)
# ----------------------------------------

if avg == 4.0:
    print('[+] Stage1 Success!\n')
else:
    print('[-] Stage1 Fail...')


# ----------------------------------------
# TODO : Compute variance of grade
# var = Sum of (grade - avg)^2 / N (grade : vision, nlp ,speech)
# Use 'avg'.
var = ((vision - avg)**2 + (nlp - avg)**2 + (speech - avg)**2) / 3
print(var)
# ----------------------------------------

if var == 1/6:
    print('[+] Stage2 Success!\n')
else:
    print('[-] Stage2 Fail...')


grade = 'A'
subject = 'vision'

# ----------------------------------------
# TODO : Print subject's 5th character and print like this.
# >>> vision's grade is A
b = subject[4]
string_grade = subject+'\'s grade is '+grade
print(string_grade)
# ----------------------------------------

if b == 'o' and string_grade == 'vision\'s grade is A':
    print('[+] Stage3 Success!\n')
else:
    print('[-] Stage3 Fail...')


subject = 'vision'

# ----------------------------------------
# TODO : Print 2nd to 5th characters of subject.
#        Print reverse of subject.
#        Print last character of subject.
slice_subject = subject[1:5]
reverse_subject = subject[::-1]
last_subject = subject[-1]
print(slice_subject, reverse_subject, last_subject)
# ----------------------------------------

if slice_subject == 'isio' and reverse_subject == 'noisiv' and last_subject == 'n':
    print('[+] Stage4 Success!\n')
else:
    print('[-] Stage4 Fail...')


first_subject = 'vision'
second_subject = 'nlp'

# ----------------------------------------
# TODO : Concatenate two subject's name.
# >>> vision nlp
concat = first_subject + ' ' + second_subject
print(concat)
# ----------------------------------------

if concat == 'vision nlp':
    print('[+] Stage5 Success!\n')
else:
    print('[-] Stage5 Fail...')


subject = ['vision', 'nlp', 'speech']

# ----------------------------------------
# TODO : Append 'recommend' subject to subject list.
subject.append('recommend')
print(subject)
# ----------------------------------------

if subject == ['vision', 'nlp', 'speech', 'recommend']:
    print('[+] Stage6 Success!\n')
else:
    print('[-] Stage6 Fail...')


subject == ['vision', 'nlp', 'speech', 'recommend']

# ----------------------------------------
# TODO : Reverse the order of subject.
subject = subject[::-1]
print(subject)
# ----------------------------------------

if subject == ['recommend', 'speech', 'nlp', 'vision']:
    print('[+] Stage7 Success!\n')
else:
    print('[-] Stage7 Fail...')


subject = ['recommend', 'speech', 'nlp', 'vision']

# ----------------------------------------
# TODO : Change second element to 'audio&speech'.
subject[1] = 'audio&speech'
print(subject)
# ----------------------------------------

if subject == ['recommend', 'audio&speech', 'nlp', 'vision']:
    print('[+] Stage8 Success!\n')
else:
    print('[-] Stage8 Fail...')


grade = {'audio&speech': 4.5,
        'nlp': 3.5,
        'vision': 4.0}

# ----------------------------------------
# TODO : Add 'recommend's grade 4.0.
grade['recommend'] = 4.0
print(grade)
# ----------------------------------------

if grade['recommend'] == 4.0:
    print('[+] Stage9 Success!\n')
else:
    print('[-] Stage9 Fail...')


grade = {'audio&speech': 4.5, 'nlp': 3.5, 'vision': 4.0, 'recommend': 4.0}

# ----------------------------------------
# TODO : Print key of grade.
#        Print items of grade.
keys = grade.keys()
items = grade.items()
print(keys)
print(items)
# ----------------------------------------

if list(keys) == ['audio&speech', 'nlp', 'vision', 'recommend'] and list(items) == [('audio&speech', 4.5), ('nlp', 3.5), ('vision', 4.0), ('recommend', 4.0)]:
    print('[+] Stage10 Success!\n')
else:
    print('[-] Stage10 Fail...')