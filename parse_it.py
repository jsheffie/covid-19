#!/usr/bin/env python3
import csv
import io
import json

# https://stackoverflow.com/a/6048203/1184492
def write_csv_file(filename, data):

    with io.open(filename, 'w', encoding="utf-8") as outfile:
        outfile.write(data)
        print("Wrote to file {}".format(filename))

# with open('covid_19.csv', newline='') as csvfile:
#     datareader = csv.reader(csvfile, delimiter=' ', quotechar='|')

#     # Use for exploring the data
#     cnt = 0
#     for row in datareader:
#         if cnt == 0:
#             print(', '.join(row))
#             print('-'*100)
#         data_array = row[0].split(',')
#         try:
#             if data_array[1].lower() == 'us':
#                 print(', '.join(row))
#         except IndexError:
#             pass
#         cnt+=1


charts = [ 'washington', 'new york', 'california', 'texas' ]
for chart_name in charts:
    with open('covid_19.csv', newline='') as csvfile:
        datareader = csv.reader(csvfile, delimiter='+', quotechar='|')

        # Print out Texas Covid Data
        cnt = 0
        final_csv_data=""
        header_row=""
        filename='{}.csv'.format(chart_name)
        for row in datareader:
            if cnt == 0:
                final_csv_data="date,close\n"
                header_row = row[0].split(',')
            else:
                try:
                    data_array = row[0].split(',')
                    # print(data_array[0].lower())
                    # print(data_array)
                    if data_array[0].lower() == chart_name and data_array[1].lower() == 'us':
                        index_range = [i for i in range(90) if i > 50  ]
                        for index in index_range:
                            final_csv_data+="{}-{:02d}-{:02d},{}\n".format("2020", int(header_row[index].split('/')[0]),int(header_row[index].split('/')[1]), data_array[index])
                except IndexError:
                    pass
            cnt+=1
        write_csv_file(filename, final_csv_data)

