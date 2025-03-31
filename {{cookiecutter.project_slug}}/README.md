# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

- **Documentation:** {{ cookiecutter.sysadmindoc_url }}
- **Downloads page:** {{ cookiecutter.downloads_url }}

## Requirements

The application requires:

- [Python](https://www.python.org/) ~= 3.11
- [pip](https://pip.pypa.io/en/stable/)

## Download & Installation

There are two ways to download and install the application:

### Using Git

You can install the application using Git by running the following command:

```bash
pip install git+{{cookiecutter.repo_url}}.git
```

### Using the GitHub releases

You can download the application on the [downloads page]({{ cookiecutter.downloads_url }}). Then, you can install the application by running the following command:

```bash
pip install {{ cookiecutter.project_slug }}-X.X.X-py3-none-any.whl
```

(Note: The X.X.X must be replaced by the version that you want to install.)

## Database setup

You can setup the database by running the following command:

```bash
{{ cookiecutter.project_slug }} migrate # or "python -m {{ cookiecutter.project_slug }} migrate"
```

## Execution

You can quickly execute the application by running the following command:

```bash
{{ cookiecutter.project_slug }} runserver # or "python -m {{ cookiecutter.project_slug }} runserver"
```

## Creation of a super user

You can create a super user by running the following command:

```bash
{{ cookiecutter.project_slug }} createsuperuser # or "python -m {{ cookiecutter.project_slug }} createsuperuser"
```

## License

All code is licensed for others under a MIT license (see [LICENSE]({{ cookiecutter.license_url }})).
