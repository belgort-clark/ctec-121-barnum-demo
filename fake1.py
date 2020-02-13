# barnum Python library - https://pypi.org/project/barnum/

# import the pandas library
import pandas as pd
# impor the barnum library
from barnum import gen_data

# Create an empty list to store users
users = []

# Create 1000 records
for i in range(1000):
    company = gen_data.create_company_name()
    fname = gen_data.create_name(full_name=False)
    lname = gen_data.create_name(full_name=False)
    title = gen_data.create_job_title()
    email = gen_data.create_email(name=(fname, lname))
    pw = gen_data.create_pw()
    street = gen_data.create_street()
    city_state_zip = gen_data.create_city_state_zip()
    cc = gen_data.create_cc_number()
    # append a new user to the users list
    users.append((company, fname, lname, title, email, pw, street, city_state_zip, cc))

# Create a set of labels for the first row of the excel spreadsheet
labels = ['Company', 'First', 'Last', 'Title', 'Email', 'Password', 'Street', 'City/State/ZIP', 'Credit Card']
# Create a pandas dataframe
df = pd.DataFrame(data=users, columns=labels)
# Sort the data
df.sort_values(['First'], inplace=True)
# Print the first few rows
print(df.head())
# Create an object that can write out data to excel
writer = pd.ExcelWriter('users.xlsx', engine='xlsxwriter')
# write out the user dataframe to the excel writer
df.to_excel(writer, index=False)
# save the excel file
writer.save()
