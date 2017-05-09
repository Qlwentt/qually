import sys,os
from os.path import join, dirname
# Full path and name to your csv file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
csv_filepathname= os.path.join(BASE_DIR, "keywords.csv")
# Full path to the directory immediately above your django project directory
sys.path.append(PROJECT_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] ='qually.settings'

from jobs.models import Keword

import csv

def run():
	dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

	for row in dataReader:
	    if row[0] != '' and row[0] != ' ':
		    keyword=Keyword()
		    keyword.name=row[0]
		    keyword.category=row[1]

		    keyword.save()