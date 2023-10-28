#Task 1.1
print('Task No 1.1')
my_input = input("Enter a string with whitespaces: ")
my_list = list(my_input.lower())

print("Created list is:")
print(my_list)

#Task 1.2
print('\nTask No 1.2')
symbol_freq = {}

for symbol in my_list:
    if symbol in symbol_freq:
        symbol_freq[symbol] += 1
    else:
        symbol_freq[symbol] = 1
# Convert the dictionary to a list of tuples
freq_list = list(symbol_freq.items())

print("Code Output:")
print(freq_list)

#Task1.3
print('\nTask No 1.3')
vowels = {'a', 'e', 'i', 'o', 'u'}
consonants = set("abcdefghijklmnopqrstuvwxyz") - vowels

list_vow = []
list_cons = []
list_sym = []

for symbol, frequency in freq_list:
    if symbol in vowels:
        list_vow.append((symbol, frequency))
    elif symbol in consonants:
        list_cons.append((symbol, frequency))
    else:
        list_sym.append((symbol, frequency))

print("list_vow =", list_vow)
print("list_cons =", list_cons)
print("list_sym =", list_sym)

#Task 1.4
print('\nTask No 1.4')
list_A = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4]

sorted_list = sorted(list_A)

n = len(sorted_list)
quartile_size = n // 4
q1_size = quartile_size
q2_size = quartile_size
q3_size = quartile_size

if n % 4 != 0:
    q1_size += n % 4  

q1 = sorted_list[:q1_size]
q2 = sorted_list[q1_size:q1_size + q2_size]
q3 = sorted_list[q1_size + q2_size:q1_size + q2_size + q3_size]
q4 = sorted_list[q1_size + q2_size + q3_size:]

print("q1 =", q1)
print("q2 =", q2)
print("q3 =", q3)
print("q4 =", q4)


#Task 2.1
print('\nTask No 2.1')
student_name = 'Meirambek'
assignments_scores = [100, 99, 95, 97]
labs_scores = [95.25, 90.75]
tests_scores = [78, 77]

student = {
    'name': student_name,
    'assignment': assignments_scores,
    'test': tests_scores,
    'lab': labs_scores
}
print("student =", student)

#Task 2.2
print('\nTask No 2.2')
submission_check = {student['name']: 0}

if len(student['assignment']) == 4:
    submission_check[student['name']] += 4
if len(student['lab']) == 2:
    submission_check[student['name']] += 2
if len(student['test']) == 2:
    submission_check[student['name']] += 2

print(submission_check)

#Task 2.3
print('\nTask No 2.3')
if submission_check[student['name']] >= 4:
    final_grade = 0.3 * (sum(student['assignment'])*0.25) + 0.5 * (sum(student['lab'])*0.5) + 0.2 * (sum(student['test'])*0.5)
    student['final_grade'] = final_grade
else:
    student['final_grade'] = 0

print(student)

#Task 2.4
print('\nTask No 2.4')
students = {
    student['name']: student
}
print(students)

#Task 3.1
print('\nTask No 3.1')
transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2), (1001, 1)]

stats = {}

for user_id, transaction_type in transactions:
    if user_id not in stats:
        stats[user_id] = {1: 0, 2: 0, 3: 0, 'mft': transaction_type, 'lft': transaction_type}

    stats[user_id][transaction_type] += 1

for user_id, user_stats in stats.items():
    most_frequent = max(user_stats, key=lambda x: user_stats[x] if x != 'mft' and x != 'lft' else 0)
    least_frequent = min(user_stats, key=lambda x: user_stats[x] if x != 'mft' and x != 'lft' else float('inf'))
    user_stats['mft'] = most_frequent
    user_stats['lft'] = least_frequent

print("stats =", stats)