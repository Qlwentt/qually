"""
WSGI config for qually_dj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
import dotenv
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())


# add the hellodjango project path into the sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# print "sys.path: {}".format(sys.path)
# print "DJango settings mod: {}".format(os.environ.get("DJANGO_SETTINGS_MODULE"))

# import qually_dj.settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qually_dj.settings")

# print "settings mod after set default: {}".format(os.environ.get("DJANGO_SETTINGS_MODULE"))



from django.core.wsgi import get_wsgi_application

try:
    if sys.argv[1] == 'runserver':
    	# print "helooooooooooooooooooooooooooooooo"
    	# print "in dev: {}".format(sys.argv)
    	dotenv.read_dotenv()
except IndexError: 
	print "production mode"
application = get_wsgi_application()





