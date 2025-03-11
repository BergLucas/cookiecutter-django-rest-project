import os
import sys

from django.core.management import execute_from_command_line


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ cookiecutter.project_slug }}.settings")
    execute_from_command_line(sys.argv)
