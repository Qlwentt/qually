# Full path and name to your csv file
csv_filepathname="/Users/quaiw/portfolio/kw-scraper/keywords.csv"
# Full path to the directory immediately above your django project directory
your_djangoproject_home="/Users/quaiw/portfolio/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] ='qually.settings'

from qually.jobs.models import Keword

import csv

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    keyword=Keyword()
    keyword.name=row[0]
    keyword.category=row[1]

    keyword.save()