employee_file = open("dealing with files/employees.txt", "a")

employee_file.write("\nToby - Human Resources")

employee_file.close()


index_pg = open("dealing with files/index.html", "w")
index_pg.write("<p>This is a HTML page.</p>")