import csv
import sys

for row in csv.reader(iter(sys.stdin.readline, '')):
    try:
        int(row[0])
        col1 = row[0]
    except:
        col1 = f'"{row[0]}"'

    try:
        int(row[1])
        col2 = row[1]
    except:
        col2 = f'"{row[1]}"'

    try:
        int(row[2])
        col3 = row[2]
    except:
        col3 = f'"{row[2]}"'

    print(f'{col2},{col1},{col3}')
