import sys,os
from os.path import join, dirname
# Full path and name to your csv file
csv_filepathname= os.path.join(BASE_DIR, "keywords.csv")
# Full path to the directory immediately above your django project directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PROJECT_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] ='qually.settings'

from qually.jobs.models import Keword

import csv

def run():
	dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

	for row in dataReader:
	    if row[0] != '' and row[0] != " "
		    keyword=Keyword()
		    keyword.name=row[0]
		    keyword.category=row[1]

		    keyword.save()