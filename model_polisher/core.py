from __future__ import print_function
from model_polisher.configuration import Configuration
from model_polisher import FullRunApi, ApiClient            
import base64
import libsbml
import tempfile
import json
import logging

# Set up basic configuration for the logging system
logging.basicConfig(level=logging.DEBUG)

def polish_model_document(config, document):
    """
    Polish a libsbml.SBMLDocument object using the Model Polisher API.

    Parameters:
    config_dict (dict): Configuration dictionary for the Model Polisher.
    document (libsbml.SBMLDocument): The SBML document to be polished.

    Returns:
    dict: Result dictionary containing run_id, diff, and polished model.
    """
    logging.debug("Preparing request.")
    client_configuration = Configuration()
    client_configuration.host = "https://biodata.informatik.uni-halle.de/modelling/api/v2.1"
    #client_configuration.host = "http://localhost:3000"
    api_instance = FullRunApi(ApiClient(client_configuration))

    # Convert the configuration dictionary to a Config object
    # config = model_polisher_config_dict_to_obj(config_dict)

    tmp_file = tempfile.NamedTemporaryFile()
    # Convert SBML document to string
    libsbml.writeSBMLToFile(document, tmp_file.name)

    logging.debug("Sending request.")
    # Upload a model fil    e and parameters for the Model Polisher.
    api_response = api_instance.submit_file_post(model_file=tmp_file.name,
                                                 config=json.dumps(config))

    logging.debug("Decoding response.")
    # Decode the polished SBML string from Base64
    polished_sbml_str = base64.b64decode(api_response.model_file).decode('utf-8')
    logging.debug("Reading SBML from decoded response.")
    polished_document = libsbml.readSBMLFromString(polished_sbml_str)

    result = {
        "run_id": api_response.run_id,
        "diff": api_response.diff,
        "polished_document": polished_document,
        "pre_validation": api_response.pre_validation,
        "post_validation": api_response.post_validation
    }
    return result


def polish_model_file(config, file_path):
    """
    Polish an SBML file using the Model Polisher API.

    Parameters:
    config_dict (dict): Configuration dictionary for the Model Polisher.
    file_path (str): Path to the SBML file to be polished.

    Returns:
    dict: Result dictionary containing run_id, diff, and path to the polished model.
    """
    logging.debug("Preparing request.")
    client_configuration = Configuration()
    client_configuration.host = "https://biodata.informatik.uni-halle.de/modelling/api/v2.1"
    #client_configuration.host = "http://localhost:3000"
    api_instance = FullRunApi(ApiClient(client_configuration))

    logging.debug("Sending request.")
    # Upload a model file and parameters for the Model Polisher.
    api_response = api_instance.submit_file_post(model_file=file_path,
                                                 config=json.dumps(config))

    # Decode the polished SBML string from Base64
    logging.debug("Decoding response.")
    polished_sbml_str = base64.b64decode(api_response.model_file).decode('utf-8')
    logging.debug("Reading SBML from decoded response.")
    polished_document = libsbml.readSBMLFromString(polished_sbml_str)

    result = {
        "run_id": api_response.run_id,
        "diff": api_response.diff,
        "polished_document": polished_document,
        "pre_validation": api_response.pre_validation,
        "post_validation": api_response.post_validation
    }
    return result
