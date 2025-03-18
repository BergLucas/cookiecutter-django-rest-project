# {{ cookiecutter.project_name }} Documentation

- **Developer documentation:** {{cookiecutter.devdoc_url}}

## Cloning the project

You can clone the repository using the following command:

```bash
git clone {{cookiecutter.repo_url}}.git
```

## Building the documentation

### Requirements

The application requires:

- [Python](https://www.python.org/) ~= 3.11
- [Poetry](https://python-poetry.org/) ~= 2.0

### SysAdmin documentation

You can build the SysAdmin documentation by running the following commands in the project root:

```bash
poetry install --only=docs
poetry poe build-docs -p sysadmin html
```

The SysAdmin documentation will be generated in the folder `docs/_build/sysadmin/html`.

### Developer documentation

You can build the developer documentation by running the following commands in the project root:

```bash
poetry install --only=docs
poetry poe build-docs -p dev html
```

The developer documentation will be generated in the folder `docs/_build/dev/html`.

## Setting up a development environment

### Requirements

The application requires:

- [Python](https://www.python.org/) ~= 3.11
- [Poetry](https://python-poetry.org/) ~= 2.0

### Python environment setup

You can setup the Python development environment by running the following command in the project root:

```bash
poetry install
```

### Code verification

You can use several commands to verify the quality of the code:

#### Running the tests

```bash
poetry poe test
```

#### Running the tests with coverage

```bash
poetry poe coverage  # only generate coverage data
# or
poetry poe coverage-report  # generate and display coverage data
# or
poetry poe coverage-html  # generate coverage data and create an HTML report
```

#### Formatting the code

```bash
poetry poe format
```

#### Checking code for errors

```bash
poetry poe check  # check the code and fix errors
# or
poetry poe check-nofix  # check the code but do not fix errors
# or
poetry poe check-unsafe  # check the code and do unsafe errors fix
```

#### Typechecking the code

```bash
poetry poe typecheck
```

#### Linting the code

```bash
poetry poe lint  # format, check and typecheck the code
```

#### Verify the code

```bash
poetry poe verify  # format, check, typecheck and test the code
```

### Database setup

You can setup a sqlite development database by running the following command in the project root:

```bash
poetry poe migrate
```

### Execution

You can execute the application in development mode by running the following command in the project root:

```bash
poetry poe dev
```

### Creation of a super user

You can create a super user by running the following command in the project root:

```bash
poetry poe createsuperuser
```

## Setting up a docker development environment

### Requirements

The application requires:

- [Python](https://www.python.org/) ~= 3.11
- [Poetry](https://python-poetry.org/) ~= 2.0
- [Docker](https://www.docker.com/) ~= 28.0
- [Docker Compose](https://docs.docker.com/compose/) ~= 2.33

### Python environment setup

You can setup the Python development environment by running the following command in the project root:

```bash
poetry install
```

### Code verification

You can use the same commands as in the classic Python environment to verify the quality of the code.

### Execution

You can execute the application in development mode on docker by running the following command in the project root:

```bash
poetry poe dev-docker
```

### Execution of commands in the development container

You can open the development container terminal by running the following command in the project root:

```bash
poetry poe bash-docker
```

This will allow you to run the same commands as in the classic Python environment but inside the container. This may be necessary if the command requires access to the database.
