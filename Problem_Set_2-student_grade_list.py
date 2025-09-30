#list of students
studentlist = ['Alex', 'Adam', 'Kris', 'Steve', 'Eve', 'Sally', 'Sarah', 'Polly', 'Luna', 'Penny']

#list of grades that correspond to order of students
grades = [88, 90, 77, 76, 82, 79, 95, 86, 93, 100]


#Questions 2
#creates a for loop that takes each name and each grade in the lists above and will give name, actual grade, and letter grade
#online help for zip: https://stackoverflow.com/questions/1663807/how-do-i-iterate-through-two-lists-in-parallel
for name, grade in zip(studentlist, grades):
    if grade >= 90:                                     #if grade is larger or equal to 90 prints name, actual grade and letter grade (A+)
        print(name + " " + str(grade) + ' A+')
    elif grade >= 85 and grade < 90:                   #if grade is between 85 and 89 prints, name, actual grade, and letter grade (A)
        print(name + " " + str(grade) + ' A')
    elif grade >= 80 and grade < 85:                  #if grade is between 80 and 84 prints, name, actual grade and letter grade (A-)
        print(name + " " + str(grade) + ' A-')
    else:                                              #all else prints name, grade and letter grade (B+)
        print(name + " " + str(grade) + ' B+')

#creates a definition version of code above except removing the for loop to use in next step
def gradecalculator(name, grade):
    if grade >= 90:
        average = print(name + " " + str(grade) + ' A+')
    elif grade >= 85 and grade < 90:
        average = print(name + " " + str(grade) + ' A')
    elif grade >= 80 and grade < 85:
        average = print(name + " " + str(grade) + ' A-')
    else:
        average = print(name + " " + str(grade) + ' B+')
    return average

#students input their name and if student is in list will retrieve the name, number grade, and letter grade for student
#if not in list will return: student not in list
def gradeLookup(name_list, grade_list):
    name_input = input('Enter student name: ')            #user inputs name
    if name_input in name_list:                             #if name is in name list will do the following actions
        if name_input == 'Alex':         #if name Alex retrieves the name from name list and correspondent grade from grade list (in index position 0) and uses gradecalculator to give back grades for student
            grades = gradecalculator(name_list[0], grade_list[0])        #done for rest of students
        if name_input == 'Adam':
            grades = gradecalculator(name_list[1], grade_list[1])
        elif name_input == "Kris":
            grades = gradecalculator(name_input[2], grade_list[2])
        elif name_input == "Steve":
            grades = gradecalculator(name_list[3], grade_list[3])
        elif name_input == "Eve":
            grades = gradecalculator(name_list[4], grade_list[4])
        elif name_input == "Sally":
            grades = gradecalculator(name_list[5], grade_list[5])
        elif name_input == "Sarah":
            grades = gradecalculator(name_list[6], grade_list[6])
        elif name_input == "Polly":
            grades = gradecalculator(name_list[7], grade_list[7])
        elif name_input == "Luna":
            grades = gradecalculator(name_list[8], grade_list[8])
        elif name_input == "Penny":
            grades = gradecalculator(name_list[9], grade_list[9])
    else:                                     #if student not in list will print student not in list
        grades = print("Student not in list")
    return grades

#activates function
gradeLookup(studentlist, grades)

