import numpy as np

name = input("Enter student name:")
subjects = input("Enter subjects seperated with comma:")

#for changing the string into list
subjects = subjects.split(",")
print(subjects)

# convert marks into list
marks = input("Enter marks seperated by comma:")
marks = marks.split(",")

# convert marks to integer
int_marks = []
for mark in marks:
    int_marks.append( int(mark))
print(int_marks)
marks_array = np.array(int_marks)
print(marks_array)

# to show combined subjects and marks
for subject , int_mark in zip(subjects ,int_marks):
    print(subject , int_mark)

average_marks = np.mean(marks_array)
print("The average marks are:" , average_marks)

# to check the performance category we will use if elif and else
def check_performance(average_marks):
    if average_marks >= 90:
        performance = "Excellent performance"
    elif average_marks >= 80:
        performance =" very good performance"
    elif average_marks >= 70:
        performance = "good performance"
    elif average_marks >= 60:
        performance = "average performance"
    else:
        performance = "needs improvement"
    return performance

performance = check_performance(average_marks)
print("student performance is:" , performance)

# finding maximum marks in the list int_marks
print("The maximum marks:" , max(int_marks))

# finding minimum marks in the list int_marks
print("The minimum marks:" ,min(int_marks))

#taking different values for expences
food = int(input("Enter food expenses:"))
transport = int(input("Enter transport expenses:"))
study = int(input("Enter study expenses:"))
others = int(input("Enter other expenses:"))

# using dictionary for expenses
expenses = {
    "Food" : food,
    "Transport" : transport,
    "Study" : study,
    "Other" : others
}

#total expenses
print(expenses)
total_expenses = sum(expenses.values())
print( "Total expenses:" , total_expenses)

# highest expenses
highest_expenses = max(expenses.values())
print("Highest expenses are:" ,highest_expenses)

# displaying key and value both together
for category , amount in expenses.items():
    if amount == highest_expenses:
        print("The highest amount category is:" , category)

age = int(input("Enter age:"))
semester = int(input("Enter semester:"))

# adding a proper student record in dictionary

student_record = {
    "Name":name,
    "Age":age,
    "Semester":semester,
    "subject_marks":dict(zip(subjects , int_marks)),
    "Average":average_marks,
    "Expenses":expenses,
    "Performance":performance
    }
print(student_record)