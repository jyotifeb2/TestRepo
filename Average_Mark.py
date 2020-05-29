
n = int(input('How many numbers: '))
print(n)
student_marks = {}

for _ in range(n):
    name, *line = input('Enter number : ').split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input('Enter number : ')

print("{0:.2f}".format(round(sum(student_marks[query_name]) / len(student_marks[query_name]), 2)))