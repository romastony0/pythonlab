import pandas as pd;

data = {
    'Regno': ['21csea33','21csea34','21csea35'],
    'Name': ['tamil','venkat','vishwanath'],
    'Course': ['MCA','MCA','MSc']
}

# load csv file
# pf = pd.DataFrame(data)
# pf.to_csv('C:/Users/91944/Desktop/vishwanath.csv')

#display records
r = pd.read_csv('C:/Users/91944/Desktop/vishwanath.csv')
print(r)
print('-----------------------------------------')

#display one row
n = r['Name']
print(n)
print('-------------------------------------------')

#insert new column
mobile = [7876556674,8764678376,7354748362]
r['mobile']=mobile
print(r)
print('---------------------------------------------')

#delete a particular name
delete = r[r.Name != 'venkat']
print(delete)
print('---------------------------------------------')

#add new records
r.loc[len(r.index)] = ['','21csea36','yellappan','MCA',4875847584]
print(r)
print('-------------------------------------------------------')

#scholarschip
scholar = 1000;
r['scholarship'] = scholar
print(r)
print('-------------------------------------------------')

#add particular scholarship add 2000
v = r.Course == 'MSc'
r.loc[v, 'scholarship'] = r['scholarship'] + 2000
print(r)
print('--------------------------------------------------')

#display second record
second = r[r.index == 1]
print(second)

print('-------------------------------------------------')

# display mobile no in msc
m = r['Course'] == 'MSc'
g = r.loc[m, 'mobile']
print(g)
print('-------------------------------------------------')


# display course mca records
course = r[r['Course'] == 'MCA']
print(course)