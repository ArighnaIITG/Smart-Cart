# This file is kind of your project local django-admin for interacting with your project via the command line.
# !/usr/bin/env python

import os
import sys

if _name_ == "_main_":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smart_cart.settings")

    from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)
