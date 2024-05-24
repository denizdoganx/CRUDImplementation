import json
#2018510019 Deniz Doğan-2018510059 Alperen Turhan
#The system is designed according to these query styles.(amount of spaces between words)
#SELECT name,lastname6 FROM STUDENTS WHERE grade !< 40 ORDER BY ASC
#SELECT name FROM STUDENTS WHERE grade > 40 AND name = John ORDER BY DSC(!!The name is set to not be in quotation marks.!!)
#INSERT INTO STUDENT VALUES(15000,Ali,Veli,ali.veli@spacex.com,20)
#DELETE FROM STUDENT WHERE name = John and grade <= 20

def descendingOrder(students):#Sorts the dict by decreasing order
    sortedStudentsDict = {k: v for k, v in sorted(students.items(),reverse = True)}
    return sortedStudentsDict

def sorting(students):
    sortedStudentsDict = {k: v for k, v in sorted(students.items())}
    return sortedStudentsDict

def fileReading():#Here, the file is read and the students are thrown into a dictionary with their information.
    file = open("students.csv", "r")
    file.readline()
    x = file.readline().split(";")
    students = {x[0]: [x[1], x[2], x[3], x[4]]}
    flag = True
    while flag:
        x = file.readline()
        if x != None and x.__len__() != 0:
            y = x.lower().split(";")
            students[y[0]] = y[1], y[2], y[3], y[4]
        else:
            flag = False
    file.close()
    students = sorting(students)
    return students
def writeToJson(students,dictOfselecting):
    #The data in the select query and the result of other queries are written to the json file
    with open("query.json","a") as f:
        json.dump(students, f)
    with open("query.json","a") as f:
        json.dump(dictOfselecting, f)

def deleteOperations(students,query,indx1,indx2,op1,op2):
    #After the delete query is received from the user, this function is called and the student sent by the user is removed from the dictionary.
    if query.__len__() > 7 and (query[7] == 'and' or query[7] == 'or'):
        if op1 == '=' and op2 == '=':
            for student in students:
                if query[7] == 'and':
                    if students[student][indx1] == query[6] and students[student][indx2] == query[10]:
                        students.pop(student)
                        break
                else:
                    if students[student][indx1] == query[6] or students[student][indx2] == query[10]:
                        students.pop(student)
                        break
        elif op1 == '=' and op2 == '!=':
            for student in students:
                if query[7] == 'and':
                    if students[student][indx1] == query[6] and students[student][indx2] != query[10]:
                        students.pop(student)
                        break
                else:
                    if students[student][indx1] == query[6] or students[student][indx2] != query[10]:
                        students.pop(student)
                        break
        elif op1 == '=' and op2 == '<':
            for student in students:
                if query[7] == 'and':
                    if students[student][indx1] == query[6] and int(students[student][indx2]) < int(query[10]):
                        students.pop(student)
                        break
                else:
                    if students[student][indx1] == query[6] or int(students[student][indx2]) < int(query[10]):
                        students.pop(student)
                        break
        elif op1 == '=' and op2 == '>':
            for student in students:
                if query[7] == 'and':
                    if (students[student][indx1] == query[6] and int(students[student][indx2]) > int(query[10])):
                        students.pop(student)
                        break
                else:
                    if (students[student][indx1] == query[6] or int(students[student][indx2]) > int(query[10])):
                        students.pop(student)
                        break
        elif op1 == '=' and op2 == '<=':
            for student in students:
                if query[7] == 'and':
                    if students[student][indx1] == query[6] and int(students[student][indx2]) <= int(query[10]):
                        students.pop(student)
                        break
                else:
                    if students[student][indx1] == query[6] or int(students[student][indx2]) <= int(query[10]):
                        students.pop(student)
                        break
        elif op1 == '=' and op2 == '>=':
            for student in students:
                if query[7] == 'and':
                    if students[student][indx1] == query[6] and int(students[student][indx2]) >= int(query[10]):
                        students.pop(student)
                        break
                else:
                    if students[student][indx1] == query[6] or int(students[student][indx2]) >= int(query[10]):
                        students.pop(student)
                        break
        elif op1 == '!=' and op2 == '=':
            for student in students:
                if query[7] == 'and':
                    if students[student][indx1] != query[6] and students[student][indx2] == query[10]:
                        students.pop(student)
                        break
                else:
                    if students[student][indx1] != query[6] or students[student][indx2] == query[10]:
                        students.pop(student)
                        break
        elif op1 == '!=' and op2 == '!=':
            for student in students:
                if query[7] == 'and':
                    if students[student][indx1] != query[6] and students[student][indx2] != query[10]:
                        students.pop(student)
                        break
                else:
                    if students[student][indx1] != query[6] or students[student][indx2] != query[10]:
                        students.pop(student)
                        break
        elif op1 == '!=' and op2 == '<':
            for student in students:
                if query[7] == 'and':
                    if students[student][indx1] != query[6] and int(students[student][indx2]) < int(query[10]):
                        students.pop(student)
                        break
                else:
                    if students[student][indx1] != query[6] or int(students[student][indx2]) < int(query[10]):
                        students.pop(student)
                        break
        elif op1 == '!=' and op2 == '>':
            for student in students:
                if query[7] == 'and':
                    if students[student][indx1] != query[6] and int(students[student][indx2]) > int(query[10]):
                        students.pop(student)
                        break
                else:
                    if students[student][indx1] != query[6] or int(students[student][indx2]) > int(query[10]):
                        students.pop(student)
                        break
        elif op1 == '!=' and op2 == '<=':
            for student in students:
                if query[7] == 'and':
                    if students[student][indx1] != query[6] and int(students[student][indx2]) <= int(query[10]):
                        students.pop(student)
                        break
                else:
                    if students[student][indx1] != query[6] or int(students[student][indx2]) <= int(query[10]):
                        students.pop(student)
                        break
        elif op1 == '!=' and op2 == '>=':
            for student in students:
                if query[7] == 'and':
                    if students[student][indx1] != query[6] and int(students[student][indx2]) >= int(query[10]):
                        students.pop(student)
                        break
                else:
                    if students[student][indx1] != query[6] or int(students[student][indx2]) >= int(query[10]):
                        students.pop(student)
                        break
        elif op1 == '<' and op2 == '=':
            for student in students:
                if query[7] == 'and':
                    if int(students[student][indx1]) < int(query[6]) and students[student][indx2] == query[10]:
                        students.pop(student)
                        break
                else:
                    if int(students[student][indx1]) < int(query[6]) or students[student][indx2] == query[10]:
                        students.pop(student)
                        break
        elif op1 == '<' and op2 == '!=':
            for student in students:
                if query[7] == 'and':
                    if int(students[student][indx1]) < int(query[6]) and students[student][indx2] != query[10]:
                        students.pop(student)
                        break
                else:
                    if int(students[student][indx1]) < int(query[6]) or students[student][indx2] != query[10]:
                        students.pop(student)
                        break
        elif op1 == '>' and op2 == '=':
            for student in students:
                if query[7] == 'and':
                    if int(students[student][indx1]) > int(query[6]) and students[student][indx2] == query[10]:
                        students.pop(student)
                        break
                else:
                    if int(students[student][indx1]) > int(query[6]) or students[student][indx2] == query[10]:
                        students.pop(student)
                        break
        elif op1 == '>' and op2 == '!=':
            for student in students:
                if query[7] == 'and':
                    if int(students[student][indx1]) > int(query[6]) and students[student][indx2] != query[10]:
                        students.pop(student)
                        break
                else:
                    if int(students[student][indx1]) > int(query[6]) or students[student][indx2] != query[10]:
                        students.pop(student)
                        break
        elif op1 == '<=' and op2 == '=':
            for student in students:
                if query[7] == 'and':
                    if int(students[student][indx1]) <= int(query[6]) and students[student][indx2] == query[10]:
                        students.pop(student)
                        break
                else:
                    if int(students[student][indx1]) <= int(query[6]) or students[student][indx2] == query[10]:
                        students.pop(student)
                        break
        elif op1 == '<=' and op2 == '!=':
            for student in students:
                if query[7] == 'and':
                    if int(students[student][indx1]) <= int(query[6]) and students[student][indx2] != query[10]:
                        students.pop(student)
                        break
                else:
                    if int(students[student][indx1]) <= int(query[6]) or students[student][indx2] != query[10]:
                        students.pop(student)
                        break
        elif op1 == '>=' and op2 == '=':
            for student in students:
                if query[7] == 'and':
                    if int(students[student][indx1]) >= int(query[6]) and students[student][indx2] == query[10]:
                        students.pop(student)
                        break
                else:
                    if int(students[student][indx1]) >= int(query[6]) or students[student][indx2] == query[10]:
                        students.pop(student)
                        break
        elif op1 == '>=' and op2 == '!=':
            for student in students:
                if query[7] == 'and':
                    if int(students[student][indx1]) >= int(query[6]) and students[student][indx2] != query[10]:
                        students.pop(student)
                        break
                else:
                    if int(students[student][indx1]) >= int(query[6]) or students[student][indx2] != query[10]:
                        students.pop(student)
                        break
    else:
        if op1 == '=' and op2 == ' ':
            for student in students:
                if students[student][indx1] == query[6]:
                    students.pop(student)
                    break
        elif op1 == '!=' and op2 == ' ':
            for student in students:
                if students[student][indx1] != query[6]:
                    students.pop(student)
                    break
        elif op1 == '<' and op2 == ' ':
            for student in students:
                if int(students[student][indx1]) < int(query[6]):
                    students.pop(student)
                    break
        elif op1 == '>' and op2 == ' ':
            for student in students:
                if int(students[student][indx1]) > int(query[6]):
                    students.pop(student)
                    break
        elif op1 == '<=' and op2 == ' ':
            for student in students:
                if int(students[student][indx1]) <= int(query[6]):
                    students.pop(student)
                    break
        elif op1 == '>=' and op2 == ' ':
            for student in students:
                if int(students[student][indx1]) >= int(query[6]):
                    students.pop(student)
                    break
def printStudent(query,students,student):#After the select query, the selected students are printed on the screen with their given features.
    if query[1] == 'name':
        print(students[student][0])
    elif query[1] == 'name,lastname':
        print(students[student][0] + " " + students[student][1])
    elif query[1 == 'name,lastname,email']:
        print(students[student][0] + " " + students[student][1] + " " + students[student][2])
    elif query[1] == 'lastname':
        print(students[student][1])
    elif query[1] == 'lastname,email':
        print(students[student][1] + " " + students[student][2])
    elif query[1 == 'lastname,email,grade']:
        print(students[student][1] + " " + students[student][2] + " " + students[student][3])
    elif query[1] == 'email':
        print(students[student][2])
    elif query[1] == 'email,grade':
        print(students[student][2] + " " + students[student][3])
    elif query[1] == 'grade':
        print(students[student][3])
    elif query[1 == '*']:
        print(students[student][0] + " " + students[student][1] + " " + students[student][2]+ " " + students[student][3])

def selectOperations(students,query,indx1,indx2,op1,op2):
    #This function is called after checking that the query from the user is a select query.
    #Here, the students called by the user are assigned to a different dictionary and the print function is called to print them on the screen.
    if query[10] == 'dsc' or (query.__len__() > 12 and query[14] == 'dsc'):
        students = descendingOrder(students)
    if query.__len__() > 10 and (query[8] == 'and' or query[8] == 'or'):
        if op1 == '=' and op2 == '=':
            for student in students:
                if query[8] == 'and':
                    if students[student][indx1] == query[7] and students[student][indx2] == query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if students[student][indx1] == query[7] or students[student][indx2] == query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '=' and op2 == '!=':
            for student in students:
                if query[8] == 'and':
                    if (students[student][indx1] == query[7] and students[student][indx2] != query[11]):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if (students[student][indx1] == query[7] or students[student][indx2] != query[11]):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '=' and op2 == '<':
            for student in students:
                if query[8] == 'and':
                    if students[student][indx1] == query[7] and int(students[student][indx2]) < int(query[11]):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if students[student][indx1] == query[7] or int(students[student][indx2]) < int(query[11]):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '=' and op2 == '>':
            for student in students:
                if query[8] == 'and':
                    if (students[student][indx1] == query[7] and int(students[student][indx2]) > int(query[11])):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if (students[student][indx1] == query[7] or int(students[student][indx2]) > int(query[11])):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '=' and op2 == '<=':
            for student in students:
                if query[8] == 'and':
                    if students[student][indx1] == query[7] and int(students[student][indx2]) <= int(query[11]):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if students[student][indx1] == query[7] or int(students[student][indx2]) <= int(query[11]):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '=' and op2 == '>=':
            for student in students:
                if query[8] == 'and':
                    if students[student][indx1] == query[7] and int(students[student][indx2]) >= int(query[11]):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if students[student][indx1] == query[7] or int(students[student][indx2] >= query[11]):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '!=' and op2 == '=':
            for student in students:
                if query[8] == 'and':
                    if students[student][indx1] != query[7] and students[student][indx2] == query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if students[student][indx1] != query[7] or students[student][indx2] == query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '!=' and op2 == '!=':
            for student in students:
                if query[7] == 'and':
                    if students[student][indx1] != query[7] and students[student][indx2] != query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if students[student][indx1] != query[7] or students[student][indx2] != query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '!=' and op2 == '<':
            for student in students:
                if query[8] == 'and':
                    if students[student][indx1] != query[7] and int(students[student][indx2]) < int(query[11]):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if students[student][indx1] != query[7] or int(students[student][indx2]) < int(query[11]):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '!=' and op2 == '>':
            for student in students:
                if query[8] == 'and':
                    if students[student][indx1] != query[7] and int(students[student][indx2]) > int(query[11]):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if students[student][indx1] != query[7] or int(students[student][indx2]) > int(query[11]):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '!=' and op2 == '<=':
            for student in students:
                if query[8] == 'and':
                    if students[student][indx1] != query[7] and int(students[student][indx2]) <= int(query[11]):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if students[student][indx1] != query[7] or int(students[student][indx2]) <= int(query[11]):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '!=' and op2 == '>=':
            for student in students:
                if query[8] == 'and':
                    if students[student][indx1] != query[7] and int(students[student][indx2]) >= int(query[11]):
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if students[student][indx1] != query[7] or int(students[student][indx2]) >= int(query[11]):
                        printStudent(query, student)
                        dictOfselecting[student] = students[student]
        elif op1 == '<' and op2 == '=':
            for student in students:
                if query[8] == 'and':
                    if int(students[student][indx1]) < int(query[7]) and students[student][indx2] == query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if int(students[student][indx1]) < int(query[7]) or students[student][indx2] == query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '<' and op2 == '!=':
            for student in students:
                if query[8] == 'and':
                    if int(students[student][indx1]) < int(query[7]) and students[student][indx2] != query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if int(students[student][indx1]) < int(query[7]) or students[student][indx2] != query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '>' and op2 == '=':
            for student in students:
                if query[8] == 'and':
                    if int(students[student][indx1]) > int(query[7]) and students[student][indx2] == query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if int(students[student][indx1]) > int(query[7]) or students[student][indx2] == query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '>' and op2 == '!=':
            for student in students:
                if query[8] == 'and':
                    if int(students[student][indx1]) > int(query[7]) and students[student][indx2] != query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if int(students[student][indx1]) > int(query[7]) or students[student][indx2] != query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '<=' and op2 == '=':
            for student in students:
                if query[8] == 'and':
                    if int(students[student][indx1]) <= int(query[7]) and students[student][indx2] == query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if int(students[student][indx1]) <= int(query[7]) or students[student][indx2] == query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '<=' and op2 == '!=':
            for student in students:
                if query[8] == 'and':
                    if int(students[student][indx1]) <= int(query[7]) and students[student][indx2] != query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if int(students[student][indx1]) <= int(query[7]) or students[student][indx2] != query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '>=' and op2 == '=':
            for student in students:
                if query[8] == 'and':
                    if int(students[student][indx1]) >= int(query[7]) and students[student][indx2] == query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if int(students[student][indx1]) >= int(query[7]) or students[student][indx2] == query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
        elif op1 == '>=' and op2 == '!=':
            for student in students:
                if query[8] == 'and':
                    if int(students[student][indx1]) >= int(query[7]) and students[student][indx2] != query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
                else:
                    if int(students[student][indx1]) >= int(query[7]) or students[student][indx2] != query[11]:
                        printStudent(query,students,student)
                        dictOfselecting[student] = students[student]
    else:
        if op1 == '=' and op2 == ' ':
            for student in students:
                if students[student][indx1] == query[7]:
                    printStudent(query,students,student)
                    dictOfselecting[student] = students[student]
        elif op1 == '!=' and op2 == ' ':
            for student in students:
                if students[student][indx1] != query[7]:
                    printStudent(query,students,student)
                    dictOfselecting[student] = students[student]
        elif op1 == '<' and op2 == ' ':
            for student in students:
                if int(students[student][indx1]) < int(query[7]):
                    printStudent(query,students,student)
                    dictOfselecting[student] = students[student]
        elif op1 == '>' and op2 == ' ':
            for student in students:
                if int(students[student][indx1]) > int(query[7]):
                    printStudent(query,students,student)
                    dictOfselecting[student] = students[student]
        elif op1 == '<=' and op2 == ' ':
            for student in students:
                if int(students[student][indx1]) <= int(query[7]):
                    printStudent(query,students,student)
                    dictOfselecting[student] = students[student]
        elif op1 == '>=' and op2 == ' ':
            for student in students:
                if int(students[student][indx1]) >= int(query[7]):
                    printStudent(query,students,student)
                    dictOfselecting[student] = students[student]

students = fileReading()
dictOfselecting = {}
while True:#The system waits for a query from the user until the user presses 1.
    #The controls here are to find out which query the user entered.
    print("Enter a query or press 1 to exit")
    query = input()
    query = query.lower().split(" ")
    if query[0] == '1':#If the user presses 1, the necessary functions are called to write the final dictionaries to the json file.
        writeToJson(students,dictOfselecting)
        break
    elif query[0] == 'select' and (query[1] == 'name' or query[1] == 'name,lastname' or query[1] == '*') and query[2] == 'from' and query[3] == 'students' and query[4] == 'where' and (query[8] == 'order' or query[12] == 'order') and (query[9] == 'by' or query[13] == 'by'):
        if query.__len__() > 12:
            if query[5] == 'name' and query[6] == '=':
                if query[9] == 'lastname' and query[10] == '=':
                    selectOperations(students, query, 0, 1, '=', '=')
                elif query[9] == 'lastname' and query[10] == '!=':
                    selectOperations(students, query, 0, 1, '=', '!=')
                elif query[9] == 'email' and query[10] == '=':
                    selectOperations(students, query, 0, 2, '=', '=')
                elif query[9] == 'email' and query[10] == '!=':
                    selectOperations(students, query, 0, 2, '=', '!=')
                elif query[9] == 'grade' and query[10] == '=':
                    selectOperations(students, query, 0, 3, '=', '=')
                elif query[9] == 'grade' and query[10] == '!=':
                    selectOperations(students, query, 0, 3, '=', '!=')
                elif query[9] == 'grade' and (query[10] == '<=' or query[10] == '!>'):
                    selectOperations(students, query, 0, 3, '=', '<=')
                elif query[9] == 'grade' and (query[10] == '>=' or query[10] == '!<'):
                    selectOperations(students, query, 0, 3, '=', '>=')
                elif query[9] == 'grade' and query[10] == '<':
                    selectOperations(students, query, 0, 3, '=', '<')
                elif query[9] == 'grade' and query[10] == '>':
                    selectOperations(students, query, 0, 3, '=', '>')

            elif query[5] == 'name' and query[6] == '!=':
                if query[9] == 'lastname' and query[10] == '=':
                    selectOperations(students, query, 0, 1, '!=', '=')
                elif query[9] == 'lastname' and query[10] == '!=':
                    selectOperations(students, query, 0, 1, '!=', '!=')
                elif query[9] == 'email' and query[10] == '=':
                    selectOperations(students, query, 0, 2, '!=', '=')
                elif query[9] == 'email' and query[10] == '!=':
                    selectOperations(students, query, 0, 2, '!=', '!=')
                elif query[9] == 'grade' and query[10] == '=':
                    selectOperations(students, query, 0, 3, '!=', '=')
                elif query[9] == 'grade' and query[10] == '!=':
                    selectOperations(students, query, 0, 3, '!=', '!=')
                elif query[9] == 'grade' and (query[10] == '<=' or query[10] == '!>'):
                    selectOperations(students, query, 0, 3, '!=', '<=')
                elif query[9] == 'grade' and (query[10] == '>=' or query[10] == '!<'):
                    selectOperations(students, query, 0, 3, '!=', '>=')
                elif query[9] == 'grade' and query[10] == '<':
                    selectOperations(students, query, 0, 3, '!=', '<')
                elif query[9] == 'grade' and query[10] == '>':
                    selectOperations(students, query, 0, 3, '!=', '>')

            elif query[5] == 'lastname' and query[6] == '=':
                if query[9] == 'name' and query[10] == '=':
                    selectOperations(students, query, 1, 0, '=', '=')
                elif query[9] == 'name' and query[10] == '!=':
                    selectOperations(students, query, 1, 0, '=', '!=')
                elif query[9] == 'email' and query[10] == '=':
                    selectOperations(students, query, 1, 2, '=', '=')
                elif query[9] == 'email' and query[10] == '!=':
                    selectOperations(students, query, 1, 2, '=', '!=')
                elif query[9] == 'grade' and query[10] == '=':
                    selectOperations(students, query, 1, 3, '=', '=')
                elif query[9] == 'grade' and query[10] == '!=':
                    selectOperations(students, query, 1, 3, '=', '!=')
                elif query[9] == 'grade' and (query[10] == '<=' or query[10] == '!>'):
                    selectOperations(students, query, 1, 3, '=', '<=')
                elif query[9] == 'grade' and (query[10] == '>=' or query[10] == '!<'):
                    selectOperations(students, query, 1, 3, '=', '>=')
                elif query[9] == 'grade' and query[10] == '<':
                    selectOperations(students, query, 1, 3, '=', '<')
                elif query[9] == 'grade' and query[10] == '>':
                    selectOperations(students, query, 1, 3, '=', '>')

            elif query[5] == 'lastname' and query[6] == '!=':
                if query[9] == 'name' and query[10] == '=':
                    selectOperations(students, query, 1, 0, '!=', '=')
                elif query[9] == 'name' and query[10] == '!=':
                    selectOperations(students, query, 1, 0, '!=', '!=')
                elif query[9] == 'email' and query[10] == '=':
                    selectOperations(students, query, 1, 2, '!=', '=')
                elif query[9] == 'email' and query[10] == '!=':
                    selectOperations(students, query, 1, 2, '!=', '!=')
                elif query[9] == 'grade' and query[10] == '=':
                    selectOperations(students, query, 1, 3, '!=', '=')
                elif query[9] == 'grade' and query[10] == '!=':
                    selectOperations(students, query, 1, 3, '!=', '!=')
                elif query[9] == 'grade' and (query[10] == '<=' or query[10] == '!>'):
                    selectOperations(students, query, 1, 3, '!=', '<=')
                elif query[9] == 'grade' and (query[10] == '>=' or query[10] == '!<'):
                    selectOperations(students, query, 1, 3, '!=', '>=')
                elif query[9] == 'grade' and query[10] == '<':
                    selectOperations(students, query, 1, 3, '!=', '<')
                elif query[9] == 'grade' and query[10] == '>':
                    selectOperations(students, query, 1, 3, '!=', '>')

            elif query[5] == 'email' and query[6] == '=':
                if query[9] == 'name' and query[10] == '=':
                    selectOperations(students, query, 2, 0, '=', '=')
                elif query[9] == 'name' and query[10] == '!=':
                    selectOperations(students, query, 2, 0, '=', '!=')
                elif query[9] == 'lastname' and query[10] == '=':
                    selectOperations(students, query, 2, 1, '=', '=')
                elif query[9] == 'lastname' and query[10] == '!=':
                    selectOperations(students, query, 2, 1, '=', '!=')
                elif query[9] == 'grade' and query[10] == '=':
                    selectOperations(students, query, 2, 3, '=', '=')
                elif query[9] == 'grade' and query[10] == '!=':
                    selectOperations(students, query, 2, 3, '=', '!=')
                elif query[9] == 'grade' and (query[10] == '<=' or query[10] == '!>'):
                    selectOperations(students, query, 2, 3, '=', '<=')
                elif query[9] == 'grade' and (query[10] == '>=' or query[10] == '!<'):
                    selectOperations(students, query, 2, 3, '=', '>=')
                elif query[9] == 'grade' and query[10] == '<':
                    selectOperations(students, query, 2, 3, '=', '<')
                elif query[9] == 'grade' and query[10] == '>':
                    selectOperations(students, query, 2, 3, '=', '>')

            elif query[5] == 'email' and query[6] == '!=':
                if query[9] == 'name' and query[10] == '=':
                    selectOperations(students, query, 2, 0, '!=', '=')
                elif query[9] == 'name' and query[10] == '!=':
                    selectOperations(students, query, 2, 0, '!=', '!=')
                elif query[9] == 'lastname' and query[10] == '=':
                    selectOperations(students, query, 2, 1, '!=', '=')
                elif query[9] == 'lastname' and query[10] == '!=':
                    selectOperations(students, query, 2, 1, '!=', '!=')
                elif query[9] == 'grade' and query[10] == '=':
                    selectOperations(students, query, 2, 3, '!=', '=')
                elif query[9] == 'grade' and query[10] == '!=':
                    selectOperations(students, query, 2, 3, '!=', '!=')
                elif query[9] == 'grade' and (query[10] == '<=' or query[10] == '!>'):
                    selectOperations(students, query, 2, 3, '!=', '<=')
                elif query[9] == 'grade' and (query[10] == '>=' or query[10] == '!<'):
                    selectOperations(students, query, 2, 3, '!=', '>=')
                elif query[9] == 'grade' and query[10] == '<':
                    selectOperations(students, query, 2, 3, '!=', '<')
                elif query[9] == 'grade' and query[10] == '>':
                    selectOperations(students, query, 2, 3, '!=', '>')

            elif query[5] == 'grade' and query[6] == '=':
                if query[9] == 'name' and query[10] == '=':
                    selectOperations(students, query, 3, 0, '=', '=')
                elif query[9] == 'name' and query[10] == '!=':
                    selectOperations(students, query, 3, 0, '=', '!=')
                elif query[9] == 'lastname' and query[10] == '=':
                    selectOperations(students, query, 3, 1, '=', '=')
                elif query[9] == 'lastname' and query[10] == '!=':
                    selectOperations(students, query, 3, 1, '=', '!=')
                elif query[9] == 'email' and query[10] == '=':
                    selectOperations(students, query, 3, 2, '=', '=')
                elif query[9] == 'email' and query[10] == '!=':
                    selectOperations(students, query, 3, 2, '=', '!=')

            elif query[5] == 'grade' and query[6] == '!=':
                if query[9] == 'name' and query[10] == '=':
                    selectOperations(students, query, 3, 0, '!=', '=')
                elif query[9] == 'name' and query[10] == '!=':
                    selectOperations(students, query, 3, 0, '!=', '!=')
                elif query[9] == 'lastname' and query[10] == '=':
                    selectOperations(students, query, 3, 1, '!=', '=')
                elif query[9] == 'lastname' and query[10] == '!=':
                    selectOperations(students, query, 3, 1, '!=', '!=')
                elif query[9] == 'email' and query[10] == '=':
                    selectOperations(students, query, 3, 2, '!=', '=')
                elif query[9] == 'email' and query[10] == '!=':
                    selectOperations(students, query, 3, 2, '!=', '!=')

            elif query[5] == 'grade' and (query[6] == '<=' or query[6] == '!>'):
                if query[9] == 'name' and query[10] == '=':
                    selectOperations(students, query, 3, 0, '<=', '=')
                elif query[9] == 'name' and query[10] == '!=':
                    selectOperations(students, query, 3, 0, '<=', '!=')
                elif query[9] == 'lastname' and query[10] == '=':
                    selectOperations(students, query, 3, 1, '<=', '=')
                elif query[9] == 'lastname' and query[10] == '!=':
                    selectOperations(students, query, 3, 1, '<=', '!=')
                elif query[9] == 'email' and query[10] == '=':
                    selectOperations(students, query, 3, 2, '<=', '=')
                elif query[9] == 'email' and query[10] == '!=':
                    selectOperations(students, query, 3, 2, '<=', '!=')

            elif query[5] == 'grade' and (query[6] == '>=' or query[6] == '!<'):
                if query[9] == 'name' and query[10] == '=':
                    selectOperations(students, query, 3, 0, '>=', '=')
                elif query[9] == 'name' and query[10] == '!=':
                    selectOperations(students, query, 3, 0, '>=', '!=')
                elif query[9] == 'lastname' and query[10] == '=':
                    selectOperations(students, query, 3, 1, '>=', '=')
                elif query[9] == 'lastname' and query[10] == '!=':
                    selectOperations(students, query, 3, 1, '>=', '!=')
                elif query[9] == 'email' and query[10] == '=':
                    selectOperations(students, query, 3, 2, '>=', '=')
                elif query[9] == 'email' and query[10] == '!=':
                    selectOperations(students, query, 3, 2, '>=', '!=')

            elif query[5] == 'grade' and query[6] == '<':
                if query[9] == 'name' and query[10] == '=':
                    selectOperations(students, query, 3, 0, '<', '=')
                elif query[9] == 'name' and query[10] == '!=':
                    selectOperations(students, query, 3, 0, '<', '!=')
                elif query[9] == 'lastname' and query[10] == '=':
                    selectOperations(students, query, 3, 1, '<', '=')
                elif query[9] == 'lastname' and query[10] == '!=':
                    selectOperations(students, query, 3, 1, '<', '!=')
                elif query[9] == 'email' and query[10] == '=':
                    selectOperations(students, query, 3, 2, '<', '=')
                elif query[9] == 'email' and query[10] == '!=':
                    selectOperations(students, query, 3, 2, '<', '!=')

            elif query[5] == 'grade' and query[6] == '>':
                if query[9] == 'name' and query[10] == '=':
                    selectOperations(students, query, 3, 0, '>', '=')
                elif query[9] == 'name' and query[10] == '!=':
                    selectOperations(students, query, 3, 0, '>', '!=')
                elif query[9] == 'lastname' and query[10] == '=':
                    selectOperations(students, query, 3, 1, '>', '=')
                elif query[9] == 'lastname' and query[10] == '!=':
                    selectOperations(students, query, 3, 1, '>', '!=')
                elif query[9] == 'email' and query[10] == '=':
                    selectOperations(students, query, 3, 2, '>', '=')
                elif query[9] == 'email' and query[10] == '!=':
                    selectOperations(students, query, 3, 2, '>', '!=')

        else:
            if query[5] == 'name' and query[6] == '=':
                selectOperations(students, query, 0, 0, '=', ' ')
            elif query[5] == 'name' and query[6] == '!=':
                selectOperations(students, query, 0, 0, '!=', ' ')
            elif query[5] == 'lastname' and query[6] == '=':
                selectOperations(students, query, 1, 0, '=', ' ')
            elif query[5] == 'lastname' and query[6] == '!=':
                selectOperations(students, query, 1, 0, '!=', ' ')
            elif query[5] == 'email' and query[6] == '=':
                selectOperations(students, query, 2, 0, '=', ' ')
            elif query[5] == 'email' and query[6] == '!=':
                selectOperations(students, query, 2, 0, '!=', ' ')
            elif query[5] == 'grade' and query[6] == '=':
                selectOperations(students, query, 3, 0, '=', ' ')
            elif query[5] == 'grade' and query[6] == '!=':
                selectOperations(students, query, 3, 0, '!=', ' ')
            elif query[5] == 'grade' and (query[6] == '<=' or query[6] == '!>'):
                selectOperations(students, query, 3, 0, '<=', ' ')
            elif query[5] == 'grade' and (query[6] == '>=' or query[6] == '!<'):
                selectOperations(students, query, 3, 0, '>=', ' ')
            elif query[5] == 'grade' and query[6] == '<':
                selectOperations(students, query, 3, 0, '<', ' ')
            elif query[5] == 'grade' and query[6] == '>':
                selectOperations(students, query, 3, 0, '>', ' ')



    elif query[0] == 'insert' and query[1] == 'into' and query[2] == 'student' and query[3] == 'values':
        x = query[3].split(",")
        x[0] = x[0].split("(")
        x[4] = x[4].split(")")
        students[x[0][1]] = x[1], x[2], x[3], x[4][0]
        students = sorting(students)
    elif query[0] == 'delete' and query[1] == 'from' and query[2] == 'student' and query[3] == 'where':
        if query.__len__() > 7:
            if query[4] == 'name' and query[5] == '=':
                if query[8] == 'lastname' and query[9] == '=':
                    deleteOperations(students, query, 0, 1, '=', '=')
                elif query[8] == 'lastname' and query[9] == '!=':
                    deleteOperations(students, query, 0, 1, '=', '!=')
                elif query[8] == 'email' and query[9] == '=':
                    deleteOperations(students, query, 0, 2, '=', '=')
                elif query[8] == 'email' and query[9] == '!=':
                    deleteOperations(students, query, 0, 2, '=', '!=')
                elif query[8] == 'grade' and query[9] == '=':
                    deleteOperations(students, query, 0, 3, '=', '=')
                elif query[8] == 'grade' and query[9] == '!=':
                    deleteOperations(students, query, 0, 3, '=', '!=')
                elif query[8] == 'grade' and (query[9] == '<=' or query[9] == '!>'):
                    deleteOperations(students, query, 0, 3, '=', '<=')
                elif query[8] == 'grade' and (query[9] == '>=' or query[9] == '!<'):
                    deleteOperations(students, query, 0, 3, '=', '>=')
                elif query[8] == 'grade' and query[9] == '<':
                    deleteOperations(students, query, 0, 3, '=', '<')
                elif query[8] == 'grade' and query[9] == '>':
                    deleteOperations(students, query, 0, 3, '=', '>')

            elif query[4] == 'name' and query[5] == '!=':
                if query[8] == 'lastname' and query[9] == '=':
                    deleteOperations(students, query, 0, 1, '!=', '=')
                elif query[8] == 'lastname' and query[9] == '!=':
                    deleteOperations(students, query, 0, 1, '!=', '!=')
                elif query[8] == 'email' and query[9] == '=':
                    deleteOperations(students, query, 0, 2, '!=', '=')
                elif query[8] == 'email' and query[9] == '!=':
                    deleteOperations(students, query, 0, 2, '!=', '!=')
                elif query[8] == 'grade' and query[9] == '=':
                    deleteOperations(students, query, 0, 3, '!=', '=')
                elif query[8] == 'grade' and query[9] == '!=':
                    deleteOperations(students, query, 0, 3, '!=', '!=')
                elif query[8] == 'grade' and (query[9] == '<=' or query[9] == '!>'):
                    deleteOperations(students, query, 0, 3, '!=', '<=')
                elif query[8] == 'grade' and (query[9] == '>=' or query[9] == '!<'):
                    deleteOperations(students, query, 0, 3, '!=', '>=')
                elif query[8] == 'grade' and query[9] == '<':
                    deleteOperations(students, query, 0, 3, '!=', '<')
                elif query[8] == 'grade' and query[9] == '>':
                    deleteOperations(students, query, 0, 3, '!=', '>')

            elif query[4] == 'lastname' and query[5] == '=':
                if query[8] == 'name' and query[9] == '=':
                    deleteOperations(students, query, 1, 0, '=', '=')
                elif query[8] == 'name' and query[9] == '!=':
                    deleteOperations(students, query, 1, 0, '=', '!=')
                elif query[8] == 'email' and query[9] == '=':
                    deleteOperations(students, query, 1, 2, '=', '=')
                elif query[8] == 'email' and query[9] == '!=':
                    deleteOperations(students, query, 1, 2, '=', '!=')
                elif query[8] == 'grade' and query[9] == '=':
                    deleteOperations(students, query, 1, 3, '=', '=')
                elif query[8] == 'grade' and query[9] == '!=':
                    deleteOperations(students, query, 1, 3, '=', '!=')
                elif query[8] == 'grade' and (query[9] == '<=' or query[9] == '!>'):
                    deleteOperations(students, query, 1, 3, '=', '<=')
                elif query[8] == 'grade' and (query[9] == '>=' or query[9] == '!<'):
                    deleteOperations(students, query, 1, 3, '=', '>=')
                elif query[8] == 'grade' and query[9] == '<':
                    deleteOperations(students, query, 1, 3, '=', '<')
                elif query[8] == 'grade' and query[9] == '>':
                    deleteOperations(students, query, 1, 3, '=', '>')

            elif query[4] == 'lastname' and query[5] == '!=':
                if query[8] == 'name' and query[9] == '=':
                    deleteOperations(students, query, 1, 0, '!=', '=')
                elif query[8] == 'name' and query[9] == '!=':
                    deleteOperations(students, query, 1, 0, '!=', '!=')
                elif query[8] == 'email' and query[9] == '=':
                    deleteOperations(students, query, 1, 2, '!=', '=')
                elif query[8] == 'email' and query[9] == '!=':
                    deleteOperations(students, query, 1, 2, '!=', '!=')
                elif query[8] == 'grade' and query[9] == '=':
                    deleteOperations(students, query, 1, 3, '!=', '=')
                elif query[8] == 'grade' and query[9] == '!=':
                    deleteOperations(students, query, 1, 3, '!=', '!=')
                elif query[8] == 'grade' and (query[9] == '<=' or query[9] == '!>'):
                    deleteOperations(students, query, 1, 3, '!=', '<=')
                elif query[8] == 'grade' and (query[9] == '>=' or query[9] == '!<'):
                    deleteOperations(students, query, 1, 3, '!=', '>=')
                elif query[8] == 'grade' and query[9] == '<':
                    deleteOperations(students, query, 1, 3, '!=', '<')
                elif query[8] == 'grade' and query[9] == '>':
                    deleteOperations(students, query, 1, 3, '!=', '>')

            elif query[4] == 'email' and query[5] == '=':
                if query[8] == 'name' and query[9] == '=':
                    deleteOperations(students, query, 2, 0, '=', '=')
                elif query[8] == 'name' and query[9] == '!=':
                    deleteOperations(students, query, 2, 0, '=', '!=')
                elif query[8] == 'lastname' and query[9] == '=':
                    deleteOperations(students, query, 2, 1, '=', '=')
                elif query[8] == 'lastname' and query[9] == '!=':
                    deleteOperations(students, query, 2, 1, '=', '!=')
                elif query[8] == 'grade' and query[9] == '=':
                    deleteOperations(students, query, 2, 3, '=', '=')
                elif query[8] == 'grade' and query[9] == '!=':
                    deleteOperations(students, query, 2, 3, '=', '!=')
                elif query[8] == 'grade' and (query[9] == '<=' or query[9] == '!>'):
                    deleteOperations(students, query, 2, 3, '=', '<=')
                elif query[8] == 'grade' and (query[9] == '>=' or query[9] == '!<'):
                    deleteOperations(students, query, 2, 3, '=', '>=')
                elif query[8] == 'grade' and query[9] == '<':
                    deleteOperations(students, query, 2, 3, '=', '<')
                elif query[8] == 'grade' and query[9] == '>':
                    deleteOperations(students, query, 2, 3, '=', '>')

            elif query[4] == 'email' and query[5] == '!=':
                if query[8] == 'name' and query[9] == '=':
                    deleteOperations(students, query, 2, 0, '!=', '=')
                elif query[8] == 'name' and query[9] == '!=':
                    deleteOperations(students, query, 2, 0, '!=', '!=')
                elif query[8] == 'lastname' and query[9] == '=':
                    deleteOperations(students, query, 2, 1, '!=', '=')
                elif query[8] == 'lastname' and query[9] == '!=':
                    deleteOperations(students, query, 2, 1, '!=', '!=')
                elif query[8] == 'grade' and query[9] == '=':
                    deleteOperations(students, query, 2, 3, '!=', '=')
                elif query[8] == 'grade' and query[9] == '!=':
                    deleteOperations(students, query, 2, 3, '!=', '!=')
                elif query[8] == 'grade' and (query[9] == '<=' or query[9] == '!>'):
                    deleteOperations(students, query, 2, 3, '!=', '<=')
                elif query[8] == 'grade' and (query[9] == '>=' or query[9] == '!<'):
                    deleteOperations(students, query, 2, 3, '!=', '>=')
                elif query[8] == 'grade' and query[9] == '<':
                    deleteOperations(students, query, 2, 3, '!=', '<')
                elif query[8] == 'grade' and query[9] == '>':
                    deleteOperations(students, query, 2, 3, '!=', '>')

            elif query[4] == 'grade' and query[5] == '=':
                if query[8] == 'name' and query[9] == '=':
                    deleteOperations(students, query, 3, 0, '=', '=')
                elif query[8] == 'name' and query[9] == '!=':
                    deleteOperations(students, query, 3, 0, '=', '!=')
                elif query[8] == 'lastname' and query[9] == '=':
                    deleteOperations(students, query, 3, 1, '=', '=')
                elif query[8] == 'lastname' and query[9] == '!=':
                    deleteOperations(students, query, 3, 1, '=', '!=')
                elif query[8] == 'email' and query[9] == '=':
                    deleteOperations(students, query, 3, 2, '=', '=')
                elif query[8] == 'email' and query[9] == '!=':
                    deleteOperations(students, query, 3, 2, '=', '!=')

            elif query[4] == 'grade' and query[5] == '!=':
                if query[8] == 'name' and query[9] == '=':
                    deleteOperations(students, query, 3, 0, '!=', '=')
                elif query[8] == 'name' and query[9] == '!=':
                    deleteOperations(students, query, 3, 0, '!=', '!=')
                elif query[8] == 'lastname' and query[9] == '=':
                    deleteOperations(students, query, 3, 1, '!=', '=')
                elif query[8] == 'lastname' and query[9] == '!=':
                    deleteOperations(students, query, 3, 1, '!=', '!=')
                elif query[8] == 'email' and query[9] == '=':
                    deleteOperations(students, query, 3, 2, '!=', '=')
                elif query[8] == 'email' and query[9] == '!=':
                    deleteOperations(students, query, 3, 2, '!=', '!=')

            elif query[4] == 'grade' and (query[5] == '<=' or query[5] == '!>'):
                if query[8] == 'name' and query[9] == '=':
                    deleteOperations(students, query, 3, 0, '<=', '=')
                elif query[8] == 'name' and query[9] == '!=':
                    deleteOperations(students, query, 3, 0, '<=', '!=')
                elif query[8] == 'lastname' and query[9] == '=':
                    deleteOperations(students, query, 3, 1, '<=', '=')
                elif query[8] == 'lastname' and query[9] == '!=':
                    deleteOperations(students, query, 3, 1, '<=', '!=')
                elif query[8] == 'email' and query[9] == '=':
                    deleteOperations(students, query, 3, 2, '<=', '=')
                elif query[8] == 'email' and query[9] == '!=':
                    deleteOperations(students, query, 3, 2, '<=', '!=')

            elif query[4] == 'grade' and (query[5] == '>=' or query[5] == '!<'):
                if query[8] == 'name' and query[9] == '=':
                    deleteOperations(students, query, 3, 0, '>=', '=')
                elif query[8] == 'name' and query[9] == '!=':
                    deleteOperations(students, query, 3, 0, '>=', '!=')
                elif query[8] == 'lastname' and query[9] == '=':
                    deleteOperations(students, query, 3, 1, '>=', '=')
                elif query[8] == 'lastname' and query[9] == '!=':
                    deleteOperations(students, query, 3, 1, '>=', '!=')
                elif query[8] == 'email' and query[9] == '=':
                    deleteOperations(students, query, 3, 2, '>=', '=')
                elif query[8] == 'email' and query[9] == '!=':
                    deleteOperations(students, query, 3, 2, '>=', '!=')

            elif query[4] == 'grade' and query[5] == '<':
                if query[8] == 'name' and query[9] == '=':
                    deleteOperations(students, query, 3, 0, '<', '=')
                elif query[8] == 'name' and query[9] == '!=':
                    deleteOperations(students, query, 3, 0, '<', '!=')
                elif query[8] == 'lastname' and query[9] == '=':
                    deleteOperations(students, query, 3, 1, '<', '=')
                elif query[8] == 'lastname' and query[9] == '!=':
                    deleteOperations(students, query, 3, 1, '<', '!=')
                elif query[8] == 'email' and query[9] == '=':
                    deleteOperations(students, query, 3, 2, '<', '=')
                elif query[8] == 'email' and query[9] == '!=':
                    deleteOperations(students, query, 3, 2, '<', '!=')

            elif query[4] == 'grade' and query[5] == '>':
                if query[8] == 'name' and query[9] == '=':
                    deleteOperations(students, query, 3, 0, '>', '=')
                elif query[8] == 'name' and query[9] == '!=':
                    deleteOperations(students, query, 3, 0, '>', '!=')
                elif query[8] == 'lastname' and query[9] == '=':
                    deleteOperations(students, query, 3, 1, '>', '=')
                elif query[8] == 'lastname' and query[9] == '!=':
                    deleteOperations(students, query, 3, 1, '>', '!=')
                elif query[8] == 'email' and query[9] == '=':
                    deleteOperations(students, query, 3, 2, '>', '=')
                elif query[8] == 'email' and query[9] == '!=':
                    deleteOperations(students, query, 3, 2, '>', '!=')

        else:
            if query[4] == 'name' and query[5] == '=':
                deleteOperations(students, query, 0, 0, '=', ' ')
            elif query[4] == 'name' and query[5] == '!=':
                deleteOperations(students, query, 0, 0, '!=', ' ')
            elif query[4] == 'lastname' and query[5] == '=':
                deleteOperations(students, query, 1, 0, '=', ' ')
            elif query[4] == 'lastname' and query[5] == '!=':
                deleteOperations(students, query, 1, 0, '!=', ' ')
            elif query[4] == 'email' and query[5] == '=':
                deleteOperations(students, query, 2, 0, '=', ' ')
            elif query[4] == 'email' and query[5] == '!=':
                deleteOperations(students, query, 2, 0, '!=', ' ')
            elif query[4] == 'grade' and query[5] == '=':
                deleteOperations(students, query, 3, 0, '=', ' ')
            elif query[4] == 'grade' and query[5] == '!=':
                deleteOperations(students, query, 3, 0, '!=', ' ')
            elif query[4] == 'grade' and (query[5] == '<=' or query[5] == '!>'):
                deleteOperations(students, query, 3, 0, '<=', ' ')
            elif query[4] == 'grade' and (query[5] == '>=' or query[5] == '!<'):
                deleteOperations(students, query, 3, 0, '>=', ' ')
            elif query[4] == 'grade' and query[5] == '<':
                deleteOperations(students, query, 3, 0, '<', ' ')
            elif query[4] == 'grade' and query[5] == '>':
                deleteOperations(students, query, 3, 0, '>', ' ')

    else:
        print("Please enter a query in the appropriate form")

