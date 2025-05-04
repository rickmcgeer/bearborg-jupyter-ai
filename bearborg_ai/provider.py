from os import getenv

from typing import ClassVar, List, Dict, Any, Optional, AsyncIterator

from langchain_openai import ChatOpenAI, OpenAI, OpenAIEmbeddings
from langchain_core.outputs import Generation, GenerationChunk, LLMResult

from langchain_core.callbacks import (
    AsyncCallbackManagerForLLMRun,
    CallbackManagerForLLMRun,
)


from jupyter_ai import EnvAuthStrategy, Field
from jupyter_ai_magics import BaseProvider, BaseEmbeddingsProvider, Persona
# from jupyter_ai.models.providers import provider

# Difference between OpenAI and ChatOpenAI:
#   https://stackoverflow.com/questions/76950609/what-is-the-difference-between-openai-and-chatopenai-in-langchain

def _stream_response_to_generation_chunk(
    stream_response: Dict[str, Any],
) -> GenerationChunk:
    """Convert a stream response to a generation chunk."""
    if not stream_response["choices"]:
        return GenerationChunk(text="")
    return GenerationChunk(
        text=stream_response["choices"][0]["text"] if stream_response["choices"][0]["text"] is not None else "", # this appears to return None at end of generation, triggering pydandic error
        generation_info=dict(
            finish_reason=stream_response["choices"][0].get("finish_reason", None),
            logprobs=stream_response["choices"][0].get("logprobs", None),
        ),
    )

import langchain_openai.llms.base

# bug fix maybe CBorg specific not sure!
langchain_openai.llms.base._stream_response_to_generation_chunk = _stream_response_to_generation_chunk


class BearBorgAPIKey:

    key = getenv('LITELLM_API_KEY')

    def get_secret_value(self):
        return self.key
    

class BearBorgProvider(BaseProvider, OpenAI):
# class BearBorgProvider(BaseCompletionModel, OpenAI):
    model_config = {"ignored_types": (str,bool,float,Persona,EnvAuthStrategy,BearBorgAPIKey)}
    id = "bearborg-completions"
    name = "BearBorg"
    models = [
        "azure/gpt-4o",
        "azure/gpt-4o-mini",
        "gemini/gemini-1.5-pro",
        "gemini/gemini-1.5-flash"    ,
        "gemini/gemini-2.0-flash-lite-001",
        "gemini/gemini-2.0-flash-001"
    ]

    streaming = False
    temperature = 0.5
    help: str = "Click here for more details on [CBorg](https://cborg.lbl.gov)"
    model_id_key = "model_name"
    model_id_label = "Model ID"
    # registry = False
    pypi_package_deps = ["langchain_openai"]
    #auth_strategy = EnvAuthStrategy(
    #    name="LITELLM_API_KEY", keyword_param="openai_api_key",
    #)
    openai_api_key = BearBorgAPIKey()
    openai_api_base = getenv("LITELLM_SERVER", 'https://bearborg.berkeley.edu:4433') + '/v1'
    openai_organization = "Research IT"
    persona = Persona(name="BearBorg", avatar_route="api/ai/static/jupyternaut.svg")

    @classmethod
    def is_api_key_exc(cls, e: Exception):
        """
        Determine if the exception is an BearBorg API key error.
        """
        import openai

        if isinstance(e, openai.AuthenticationError):
            error_details = e.json_body.get("error", {})
            return error_details.get("code") == "invalid_api_key"
        return False

# @provider(id="bearborg-chat")
class BearBorgChatProvider(BaseProvider, ChatOpenAI):
# class BearBorgChatProvider(BaseChatModel, ChatOpenAI):
    model_config = {"ignored_types": (str,bool,float,Persona,EnvAuthStrategy,BearBorgAPIKey)}
    id = "bearborg-chat"
    name = "BearBorg"
    models = [
        "azure/gpt-4o",
        "azure/gpt-4o-mini",
        "gemini/gemini-1.5-pro",
        "gemini/gemini-1.5-flash"    ,
        "gemini/gemini-2.0-flash-lite-001",
        "gemini/gemini-2.0-flash-001"
    ]
    streaming = False
    temperature = 0.5
    help: str = "Click here for more details on [CBorg](https://cborg.lbl.gov)"
    model_id_key = "model_name"
    model_id_label = "Model ID"
    # registry = False
    pypi_package_deps = ["langchain_openai"]
    #auth_strategy =  EnvAuthStrategy(
    #    name="LITELLM_API_KEY", keyword_param="openai_api_key",
    #)
    openai_api_key = BearBorgAPIKey()
    openai_api_base = getenv("LITELLM_SERVER", 'https://bearborg.berkeley.edu:4433') + '/v1'
    openai_organization = "Berkeley Lab"
    persona = Persona(name="BearBorg", avatar_route="api/ai/static/jupyternaut.svg")

    @classmethod
    def is_api_key_exc(cls, e: Exception):
        """
        Determine if the exception is an CBorg API key error.
        """
        import openai

        if isinstance(e, openai.AuthenticationError):
            error_details = e.json_body.get("error", {})
            return error_details.get("code") == "invalid_api_key"
        return False

# @provider(id="bearborg-embeddings")
class BearBorgEmbeddingsProvider(BaseEmbeddingsProvider, OpenAIEmbeddings):
# class BearBorgEmbeddingsProvider(BaseEmbeddingsModel, OpenAIEmbeddings):
    model_config = {"ignored_types": (str,Persona,EnvAuthStrategy,BearBorgAPIKey)}
    id = "bearborg-embeddings"
    name = "BearBorg"
    models = [
        "azure/gpt-4o",
        "azure/gpt-4o-mini",
        "gemini/gemini-1.5-pro",
        "gemini/gemini-1.5-flash"    ,
        "gemini/gemini-2.0-flash-lite-001",
        "gemini/gemini-2.0-flash-001"
    ]
    help: str = "Click here for more details on [CBorg](https://cborg.lbl.gov)"
    model_id_key = "model"
    model_id_label = "Model ID"
    # registry = False
    pypi_package_deps = ["langchain_openai"]
    #auth_strategy =  EnvAuthStrategy(
    #    name="LITELLM_API_KEY", keyword_param="openai_api_key",
    #)
    openai_api_key = BearBorgAPIKey()
    openai_api_base = getenv("LITELLM_SERVER", 'https://bearborg.berkeley.edu:4433')
    openai_organization = "RIT"
    persona = Persona(name="BearBorg", avatar_route="api/ai/static/jupyternaut.svg")
