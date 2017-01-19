"""
WSGI config for qually_dj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())


# add the hellodjango project path into the sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

# add the conda_env site-packages path to the sys.path
# sys.path.append('/Users/quaiwentt/anaconda/envs/qually_env/lib/python2.7/site-packages')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qually_dj.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
