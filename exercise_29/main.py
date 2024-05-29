worker_salary = float(input("Write the worker's salary: "))
new_worker_salary = 0
increase_per = 0
CENT = 100



if worker_salary <= 280:
    increase_per = 20
    new_worker_salary = worker_salary + (worker_salary * (increase_per / CENT))



elif 280 < worker_salary <= 700:
    increase_per = 15
    new_worker_salary = worker_salary + (worker_salary * (increase_per / CENT))




elif 700 < worker_salary <= 1500:
    increase_per = 10
    new_worker_salary = worker_salary + (worker_salary * (increase_per / CENT))

else:
    increase_per = 5
    new_worker_salary = worker_salary + (worker_salary * (increase_per / CENT))

print(f"The worker's salary was R$ {worker_salary:.2f}")
print(f"The salary will be incresead by {increase_per:.2f} percent")
print(f"The incresead value is R$ {new_worker_salary - worker_salary:.2f}")
print(f"The new worker's salary is R$ {new_worker_salary:.2f}")