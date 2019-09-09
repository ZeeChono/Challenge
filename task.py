import csv
from beautifultable import BeautifulTable
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

MOR = []
REN = []
OWN = []
with open('home_ownership_data.csv') as file:
    reader = csv.DictReader(file)
    # allocate id into different categories for further use
    for elements in reader:
        if elements['home_ownership'] == "MORTGAGE":
            MOR.append(elements['member_id'])
        if elements['home_ownership'] == "RENT":
            REN.append(elements['member_id'])
        if elements['home_ownership'] == "OWN":
            OWN.append(elements['member_id'])

with open('loan_data.csv') as file:
    reader = csv.DictReader(file)
    tot_MOR = 0
    tot_REN = 0
    tot_OWN = 0
    # sum up their loan_amnt
    for elements in reader:
        if elements['member_id'] in MOR:
            tot_MOR += int(elements['loan_amnt'])
        if elements['member_id'] in REN:
            tot_REN += int(elements['loan_amnt'])
        if elements['member_id'] in OWN:
            tot_OWN += int(elements['loan_amnt'])
# here's my table
# first compute the average
ave_MOR = float("{:.6f}".format(tot_MOR / len(MOR)))
ave_REN = float("{:.6f}".format(tot_REN / len(REN)))
ave_OWN = float("{:.6f}".format(tot_OWN / len(OWN)))
h0 = ["", "home_ownership", "    loan_amnt    "]
h1 = [0, "MORTGAGE", ave_MOR]
h2 = [1, "OWN", ave_OWN]
h3 = [2, "RENT", ave_REN]
table = BeautifulTable()
table.column_headers = h0
table.append_row(h1)
table.append_row(h2)
table.append_row(h3)
print(table)
# here's my graph
plt.figure(figsize=(8, 6), dpi=80)
N = 3
index = np.arange(N)
values = (ave_MOR, ave_OWN, ave_REN)
width = 0.4
p2 = plt.bar(index, values, width, label="loan_amnt", color="#87CEFA")
plt.xlabel('Home ownership')
plt.ylabel('Average loan amount ($)')
plt.title('Average loan amounts per home ownership')
plt.xticks(index, ('MORTGAGE', 'OWN', 'RENT'))
plt.legend(loc="upper right")
plt.show()


