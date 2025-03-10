# jupyter_ai_cborg

`jupyter_ai_cborg` is a Jupyter AI module that registers CBorg models with Jupyter AI as a model provider.

## Requirements

- Python 3.8 - 3.13
- JupyterLab 4

## Install

To install the extension, clone repo and then use pip to install:

```bash
pip install -e .
```

## Setup

Your CBorg API key must be set in the environment variable, CBORG_API_KEY.

After installing, select the CBorg module of choice from the Jupyter AI settings.

## Endpoint Override

The default endpoint is https://api.cborg.lbl.gov.

You can change it by setting the environment variable, CBORG_API_ENDPOINT. For example, use https://api-local.cborg.lbl.gov for direct access on LBLnet (bypassing Cloudflare routing), or use http://localhost:8001 if you are using the CBorg Client-side Proxy to route requests dynamically.

## Bug Reports and Support

Please contact [Science IT Consulting](scienceit@lbl.gov) if you have problems.

## Thanks

Thank you to [Jupyter AI Blablador](https://github.com/FZJ-JSC/jupyter-ai-blablador) for the initial code.


