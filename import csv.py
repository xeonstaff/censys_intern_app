import csv

my_dict = {'64c070222c8370d19c4530c1f1f32c4025247c05dfce699f180ca826952680cd': 
{'validity_start': '2022-02-22T14:40:39Z', 'validity_end': '2022-05-23T14:40:38Z'}, 
'd9e8a91e02b05baf6f59359a9df54484b7ee49308a62a1155995bced587127a6': 
{'validity_start': '2022-01-27T18:24:25Z', 'validity_end': '2022-04-27T18:24:24Z'}, 
'685896cbf3a19b913337d5a4b75c626a154630504e116efa65ec4a03b7555b5d': 
{'validity_start': '2022-01-27T18:24:25Z', 'validity_end': '2022-04-27T18:24:24Z'}}

headers= ['SHA','start_date','end_date']

with open('info.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for item in my_dict:
        entry=[item,my_dict[item]['validity_start'][0:10],my_dict[item]['validity_end'][0:10]]
        writer.writerow(entry)
    


# with open('info.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(my_dict.keys())
    