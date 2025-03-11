# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

- **Downloads page:** {{ cookiecutter.downloads_url }}

## Requirements

The application requires:

- [Python](https://www.python.org/) ~= 3.11
- [pip](https://pip.pypa.io/en/stable/)

## Download & Installation

There is only one way to download and install the application:

### Using the GitHub releases

You can download the application on the [downloads page]({{ cookiecutter.downloads_url }}). Then, you can install the application by running the following command:

```bash
pip install {{ cookiecutter.project_slug }}-X.X.X-py3-none-any.whl
```

(Note: The X.X.X must be replaced by the version that you want to install.)

## License

All code is licensed for others under a MIT license (see [LICENSE]({{ cookiecutter.license_url }})).
