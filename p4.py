# 4. Arithmetic Operation on list element

employee = ['kumar', 'sekar', 'arul', 'moorthy']
salary = [1000,5000,3000,2000]

name = input("Enter the name: ");


# add all employee salary +500
for x in range(len(salary)):
    salary[x] = salary[x] + 500

print(salary)


findKumerIndex = employee.index(name)
salary[findKumerIndex] = salary[findKumerIndex] + 1000

print(name, "bonus :", salary[findKumerIndex]);
