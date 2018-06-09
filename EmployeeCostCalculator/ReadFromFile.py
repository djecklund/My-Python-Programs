from Employee import *

class ReadFromFile():

    def read(self):
        # open the file to read
        fr = open("Input File/employeeInfo.txt")

        employees = []

        # store the employee information in a list of Employee objects
        for line in fr:
            employees.append(Employee(line.split("|")[0], line.split("|")[1], line.split("|")[2], line.split("|")[3]))

        return employees
