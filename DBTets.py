import sqlite3
from employee import Employee

conn = sqlite3.connect('members.db')

c = conn.cursor()

#Creating table
#c.execute("""CREATE TABLE employees (
#            first text,
#            last text,
#            pay integer
#            )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp.first, emp.last, emp.pay))

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last = :last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""", 
                    {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last", {'first': emp.first, 'last': emp.last})


emp_1 = Employee('Jo', 'Some', 90)
emp_2 = Employee('Ja', 'Some', 80)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Some')
print(emps)


update_pay(emp_1, 92)
remove_emp(emp_2)

emps = get_emps_by_name('Some')
print(emps)


conn.close()
