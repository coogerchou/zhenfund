#!/usr/bin/env python
import os

import importlib,sys
importlib.reload(sys)

import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trydjango18.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
