# jupyter_ai_cborg

`jupyter_ai_cborg` is a Python module that registers CBorg as a model provider for Jupyter AI.

## Requirements

- Python 3.8 - 3.13
- JupyterLab 4

## Installation

To install the extension, clone this repo and then use pip to install from the local directory:

```bash
git clone https://github.com/lbnl-science-it/cborg-jupyter-ai.git
cd cborg-jupyter-ai
pip install -e .
```

If you use a virtual environment, be sure to activate the venv prior to installation.

## Setup

Authentication for CBorg is provided via your API key, which must be defined as an environment variable CBORG_API_KEY:

```bash
export CBORG_API_KEY="sk-..."
jupyter-lab
```

## Model Selection

Within Jupyter Lab, select the Jupyter AI icon on the left. Select the CBorg model of choice from the drop down menuse.

## Budget Checking via /spend

A custom slash command "/spend" is available, which returns your current API key spend and budget reset date.

## Changing the API Endpoint

The default endpoint is https://api.cborg.lbl.gov.

To change the endpoint, set the environment variable CBORG_API_ENDPOINT, e.g. for usage internal to LBLnet:

```bash
export CBORG_API_ENDPOINT="https://api-local.cborg.lbl.gov"
```

For CBorg Client Proxy users, you can use http://localhost:8001 to route requests dynamically to the best endpoint (advanced use case).

## Bug Reports and Support

Please contact [Science IT Consulting](scienceit@lbl.gov) if you have problems.

## TODO Items

- Inline completion support
- Add more models to chat and embeddings 

## Thanks

Thank you to [Jupyter AI Blablador](https://github.com/FZJ-JSC/jupyter-ai-blablador) for the initial code.


