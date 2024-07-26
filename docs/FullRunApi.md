# model_polisher.FullRunApi

All URIs are relative to *https://BioDatA.informatik.uni-halle.de/modeling/polisher/v2.1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_file_post**](FullRunApi.md#submit_file_post) | **POST** /submit/file | Upload a model file and parameters for the ModelPolisher.

# **submit_file_post**
> InlineResponse200 submit_file_post(body)

Upload a model file and parameters for the ModelPolisher.

### Example
```python
from __future__ import print_function
import time
import model_polisher
from model_polisher.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = model_polisher.FullRunApi()
body = model_polisher.SubmitFileBody() # SubmitFileBody | 

try:
    # Upload a model file and parameters for the ModelPolisher.
    api_response = api_instance.submit_file_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FullRunApi->submit_file_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmitFileBody**](SubmitFileBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/mixed
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

