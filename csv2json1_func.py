import csv
import json


# Function to convert a CSV to JSON
def csv2json(csvFilePath, jsonFilePath):

    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data with 1~5000
        for rows,i in zip(csvReader,range(1,5001)):
            #1~5000 key ekleyerek siralamis olduk
            data[i] = rows
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

# Driver Code
csvFilePath = r'nl_words_4data.csv'
jsonFilePath = r'nl_words_def.json'

# Call the csv2json function
csv2json(csvFilePath, jsonFilePath)
