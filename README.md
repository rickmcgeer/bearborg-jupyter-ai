# bearborg_ai

`bearborg_ai` is a Jupyter AI module, a package
that registers additional model providers and slash commands for the Jupyter AI
extension.

## Requirements

- Python 3.9 - 3.12
- JupyterLab 4

## Install

To install the extension, execute:

```bash
pip install bearborg_ai
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall bearborg_ai
```

## Contributing

### Development install

```bash
cd bearborg-ai
pip install -e "."
```

### Development uninstall

```bash
pip uninstall bearborg_ai
```

#### Backend tests

This package uses [Pytest](https://docs.pytest.org/) for Python testing.

Install test dependencies (needed only once):

```sh
cd bearborg-ai
pip install -e ".[test]"
```

To execute them, run:

```sh
pytest -vv -r ap --cov bearborg_ai
```
