name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

#for loop to find data, and to write the data in a list format
emailst = list()
for line in handle:
    #Searching for a line that starts with "From"
    if not line.startswith("From "):
        continue
    #Split the line and create a list
    else:
        lines = line.split()
    emailst.append(lines[1])

#for loop to convert list into dictionary where the key is email and the value is its sum
email_dict = dict()
for email in emailst:
    email_dict[email] = email_dict.get(email, 0) + 1

#for loop to find the most common data
data_value = None
data_key = None
for email,count in email_dict.items():
    if data_value is None or count > data_value:
        data_value = count
        data_key = email
print(data_key,data_value)
