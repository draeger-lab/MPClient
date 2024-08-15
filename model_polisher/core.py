from __future__ import print_function
from model_polisher.configuration import Configuration
from model_polisher import FullRunApi, ApiClient            
import base64
import libsbml
import tempfile
import json

def polish_model_document(config, document):
    """
    Polish a libsbml.SBMLDocument object using the Model Polisher API.

    Parameters:
    config_dict (dict): Configuration dictionary for the Model Polisher.
    document (libsbml.SBMLDocument): The SBML document to be polished.

    Returns:
    dict: Result dictionary containing run_id, diff, and polished model.
    """
    client_configuration = Configuration()
    client_configuration.host = "https://biodata.informatik.uni-halle.de/modelling/api/development"
    api_instance = FullRunApi(ApiClient(client_configuration))

    # Convert the configuration dictionary to a Config object
    # config = model_polisher_config_dict_to_obj(config_dict)

    tmp_file = tempfile.NamedTemporaryFile()
    # Convert SBML document to string
    libsbml.writeSBMLToFile(document, tmp_file.name)

    # Upload a model fil    e and parameters for the Model Polisher.
    api_response = api_instance.submit_file_post(model_file=tmp_file.name,
                                                 config=json.dumps(config))

    # Decode the polished SBML string from Base64
    polished_sbml_str = base64.b64decode(api_response.model_file).decode('utf-8')
    polished_document = libsbml.readSBMLFromString(polished_sbml_str)

    result = {
        "run_id": api_response.run_id,
        "diff": api_response.diff,
        "polished_document": polished_document
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
    client_configuration = Configuration()
    client_configuration.host = "https://biodata.informatik.uni-halle.de/modelling/api/development"
    api_instance = FullRunApi(ApiClient(client_configuration))

    # Upload a model file and parameters for the Model Polisher.
    api_response = api_instance.submit_file_post(model_file=file_path,
                                                 config=json.dumps(config))

    # Decode the polished SBML string from Base64
    polished_sbml_str = base64.b64decode(api_response.model_file).decode('utf-8')
    polished_document = libsbml.readSBMLFromString(polished_sbml_str)

    result = {
        "run_id": api_response.run_id,
        "diff": api_response.diff,
        "polished_document": polished_document
    }
    return result
