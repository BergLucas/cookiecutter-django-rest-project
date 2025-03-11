#!/usr/bin/env python
"""{{ cookiecutter.project_slug }} command-line utility for administrative tasks."""

try:
    from {{ cookiecutter.project_slug }} import main
except ImportError as exc:
    raise ImportError(
        "Couldn't import {{ cookiecutter.project_slug }}. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from exc

if __name__ == "__main__":
    main()
