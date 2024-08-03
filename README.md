# model-polisher
API for the Model Polisher.

- API version: 2.1
- Package version: 0.0.1

## Getting Started

```python
from __future__ import print_function
import time
import model_polisher
from model_polisher.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = model_polisher.FullRunApi(model_polisher.ApiClient(configuration))
body = model_polisher.SubmitFileBody() # SubmitFileBody | 

try:
    # Upload a model file and parameters for the ModelPolisher.
    api_response = api_instance.submit_file_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FullRunApi->submit_file_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://BioDatA.informatik.uni-halle.de/modeling/polisher/v2.1/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FullRunApi* | [**submit_file_post**](docs/FullRunApi.md#submit_file_post) | **POST** /submit/file | Upload a model file and parameters for the ModelPolisher.

## Requirements.

Python 2.7 and 3.4+
