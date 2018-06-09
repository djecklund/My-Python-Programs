from ReadFromFile import ReadFromFile

class Main():

    def main(self):

        # Read the employee file and store it's details in the employees list
        reader = ReadFromFile()
        employees = reader.read()

        total_employee_cost = 0.00
        total_entry_employee_cost = 0.00
        total_associate_employee_cost = 0.00
        total_senior_employee_cost = 0.00
        total_expert_employee_cost = 0.00

        # List out all the employees and calculate the total costs of different categories
        for x in range(0,employees.__len__()):

            print(employees[x].fname + " " + employees[x].lname + " " + employees[x].jobTitle + " " + '${:,.2f}'.format(float(employees[x].salary)))

            if employees[x].jobTitle.startswith("Entry"):
                total_entry_employee_cost += float(employees[x].salary)
                total_employee_cost += float(employees[x].salary)
            elif employees[x].jobTitle.startswith("Associate"):
                total_associate_employee_cost += float(employees[x].salary)
                total_employee_cost += float(employees[x].salary)
            elif employees[x].jobTitle.startswith("Senior"):
                total_senior_employee_cost += float(employees[x].salary)
                total_senior_employee_cost += float(employees[x].salary)
            elif employees[x].jobTitle.startswith("Expert"):
                total_expert_employee_cost += float(employees[x].salary)
                total_expert_employee_cost += float(employees[x].salary)

        # Print the totals out for the user to see, format the salary to have a money format
        print()
        print("Total money spent on entry level employees:", "${:,.2f}".format(float(total_entry_employee_cost)))
        print("Total money spent on Associate level employees:", "${:,.2f}".format(float(total_associate_employee_cost)))
        print("Total money spent on Senior level employees:", "${:,.2f}".format(float(total_senior_employee_cost)))
        print("Total money spent on Expert level employees:", "${:,.2f}".format(float(total_expert_employee_cost)))
        print("Total money spent on All level employees:", "${:,.2f}".format(float(total_employee_cost)))

main = Main()
main.main()
