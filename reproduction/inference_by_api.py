import os
from urllib.parse import urljoin
import requests
from datetime import datetime
import copy
import re
import json
import os
import pickle
import platform
import random
import subprocess
import uuid
import sys
import io
from typing import List
import inspect
from functools import wraps
from typing import get_type_hints, Union, _GenericAlias
from urllib.parse import urlparse
from contextlib import contextmanager
import difflib
import demjson3 as demjson
import pytz
import tiktoken

from settings.settings import get_completions_settings
# from memgpt.local_llm.settings.settings import get_completions_settings
# from memgpt.local_llm.utils import count_tokens, post_json_auth_request

WEBUI_API_SUFFIX = "/v1/completions"

def count_tokens(s: str, model: str = "gpt-4") -> int:
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(s))

def post_json_auth_request(uri, json_payload, auth_type, auth_key):
    """Send a POST request with a JSON payload and optional authentication"""

    # By default most local LLM inference servers do not have authorization enabled
    if auth_type is None:
        response = requests.post(uri, json=json_payload)

    # Used by OpenAI, together.ai, Mistral AI
    elif auth_type == "bearer_token":
        if auth_key is None:
            raise ValueError(f"auth_type is {auth_type}, but auth_key is null")
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {auth_key}"}
        response = requests.post(uri, json=json_payload, headers=headers)

    # Used by OpenAI Azure
    elif auth_type == "api_key":
        if auth_key is None:
            raise ValueError(f"auth_type is {auth_type}, but auth_key is null")
        headers = {"Content-Type": "application/json", "api-key": f"{auth_key}"}
        response = requests.post(uri, json=json_payload, headers=headers)

    else:
        raise ValueError(f"Unsupport authentication type: {auth_type}")

    return response




def get_vllm_completion(endpoint, auth_type, auth_key, model, prompt, context_window, user, grammar=None):

    """https://github.com/vllm-project/vllm/blob/main/examples/api_client.py"""
    from utils import printd

    prompt_tokens = count_tokens(prompt)
    if prompt_tokens > context_window:
        raise Exception(f"Request exceeds maximum context length ({prompt_tokens} > {context_window} tokens)")

    # Settings for the generation, includes the prompt + stop tokens, max length, etc
    settings = get_completions_settings()
    request = settings
    request["prompt"] = prompt
    request["max_tokens"] = 3000  # int(context_window - prompt_tokens)
    request["stream"] = False
    request["user"] = user

    # currently hardcoded, since we are only supporting one model with the hosted endpoint
    request["model"] = model

    # Set grammar
    if grammar is not None:
        raise NotImplementedError

    if not endpoint.startswith(("http://", "https://")):
        raise ValueError(f"Endpoint ({endpoint}) must begin with http:// or https://")

    try:
        URI = urljoin(endpoint.strip("/") + "/", WEBUI_API_SUFFIX.strip("/"))
        printd(URI)
        response = post_json_auth_request(uri=URI, json_payload=request, auth_type=auth_type, auth_key=auth_key)
        if response.status_code == 200:
            result_full = response.json()
            printd(f"JSON API response:\n{result_full}")
            result = result_full["choices"][0]["text"]
            usage = result_full.get("usage", None)
        else:
            raise Exception(
                f"API call got non-200 response code (code={response.status_code}, msg={response.text}) for address: {URI}."
                + f" Make sure that the vLLM server is running and reachable at {URI}."
            )

    except:
        # TODO handle gracefully
        raise

    # Pass usage statistics back to main thread
    # These are used to compute memory warning messages
    completion_tokens = usage.get("completion_tokens", None) if usage is not None else None
    total_tokens = prompt_tokens + completion_tokens if completion_tokens is not None else None
    usage = {
        "prompt_tokens": prompt_tokens,  # can grab from usage dict, but it's usually wrong (set to 0)
        "completion_tokens": completion_tokens,
        "total_tokens": total_tokens,
    }

    return result, usage
