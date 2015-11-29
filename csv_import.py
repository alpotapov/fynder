

# Full path and name to your csv file
csv_filepathname="/Users/alexander/Documents/Hackathons/appatnight/fynder_backend/csv_categories_v2.csv"
# Full path to your django project directory
your_djangoproject_home="/Users/alexander/Documents/Hackathons/appatnight/fynder_backend/"

# import sys,os
# sys.path.append(your_djangoproject_home)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from data.models import Venue, Category
import csv

dataReader = csv.reader(open(csv_filepathname), delimiter=';', quotechar='"')

for row in dataReader:
    print(row)
    if row[0] != 'Category': # Ignore the header row, import everything else
        cat = Category()
        cat.name = row[0]
        cat.woman = int(row[1])
        cat.man = int(row[2])
        # cat.kids = row[3]
        cat.morning = int(row[4])
        cat.noon = int(row[5])
        cat.evening = int(row[6])
        cat.culture = int(row[7])
        cat.leisure = int(row[8])
        cat.shopping = int(row[9])
        cat.restaurant = int(row[10])

        cat.save()