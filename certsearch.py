#application for censys
import csv
from censys.search import CensysCertificates

#query certificate database
c = CensysCertificates()

#fields required by search
#other available fields are:
# "parsed.subject_dn",
# "parsed.names",
# "parsed.subject.common_name",

fields = [
    "parsed.fingerprint_sha256",
    "parsed.validity.start",
    "parsed.validity.end",
]

data_dict={}

#filter results by 'censys.io' domains, and trusted certificates
for page in c.search(
    "parsed.names: censys.io  and tags: trusted",
    fields,
):
#save results to the data_dict dictionary with 
#SHA acting as key and validity_start and validity_end as values
#in a sub-dictionary 
    data_dict[page['parsed.fingerprint_sha256']] = {'validity_start':page['parsed.validity.start'],
    'validity_end':page['parsed.validity.end']}

#headers to add to the first row of CSV file
headers= ['SHA','start_date','end_date']

#open info.csv file and write search contents to file 
with open('info.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for item in data_dict:
        entry=[item,data_dict[item]['validity_start'][0:10],data_dict[item]['validity_end'][0:10]]
        writer.writerow(entry)
    
    
    