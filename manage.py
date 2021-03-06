#!/usr/bin/env python
import os
import sys

import dotenv


# dotenv.read_dotenv() #take this line out for production

print "sys args: {}".format(sys.argv)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qually_dj.settings")
    # if you need to run collect staticfiles again, comment out the try block with sys.argv[1]
    try:
        if sys.argv[1] == 'runserver':
            # print "in dev: {}".format(sys.argv)
            dotenv.read_dotenv()
    except IndexError:
        print "production mode"
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
            execute_from_command_line(sys.argv)

        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
