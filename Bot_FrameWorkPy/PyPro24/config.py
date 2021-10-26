#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")

    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "a0a9e61c-c83b-4e76-9a2a-41eef0489e6c")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "b1f05444-59d0-45f2-a37e-30e6436c46f7")
    
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://firstqapy.azurewebsites.net/qnamaker")