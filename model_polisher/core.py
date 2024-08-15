from __future__ import print_function
import tempfile
from model_polisher.rest import ApiException
from model_polisher.configuration import Configuration
from model_polisher.parameters.config import Config
from model_polisher import FullRunApi, ApiClient, SubmitFileBody
import base64
import libsbml
import model_polisher

def polish_model_document(config_dict, document):
    """
    Polish a libsbml.SBMLDocument object using the Model Polisher API.

    Parameters:
    config_dict (dict): Configuration dictionary for the Model Polisher.
    document (libsbml.SBMLDocument): The SBML document to be polished.

    Returns:
    dict: Result dictionary containing run_id, diff, and polished model.
    """
    client_configuration = Configuration()
    client_configuration.host = "https://biodata.informatik.uni-halle.de/modelling/api/development/"
    api_instance = FullRunApi(ApiClient(client_configuration))

    # Convert the configuration dictionary to a Config object
    config = model_polisher_config_dict_to_obj(config_dict)

    if config is None:
        print("Error: Configuration object is None")
        return None

    # Convert SBML document to string
    sbml_str = libsbml.writeSBMLToString(document)

    # Create the SubmitFileBody with correct parameters
    body = SubmitFileBody(model_file=sbml_str, config=config)

    try:
        # Upload a model file and parameters for the Model Polisher.
        api_response = api_instance.submit_file_post(body)

        # Decode the polished SBML string from Base64
        polished_sbml_str = base64.b64decode(api_response.model_file).decode('utf-8')
        polished_document = libsbml.readSBMLFromString(polished_sbml_str)

        result = {
            "run_id": api_response.run_id,
            "diff": api_response.diff,
            "polished_document": polished_document
        }
        return result
    except ApiException as e:
        print(f"Exception when calling FullRunApi->submit_file_post: {e}")
        return None

def model_polisher_config_dict_to_obj(config_dict):
    """
    Convert a configuration dictionary to a Config object.
    """
    config = Config()
    for key, value in config_dict.items():
        if hasattr(config, key):
            setattr(config, key, value)
        else:
            print(f"Warning: {key} is not a valid attribute of Config")
    return config

def polish_model_file(config_dict, file_path):
    """
    Polish an SBML file using the Model Polisher API.

    Parameters:
    config_dict (dict): Configuration dictionary for the Model Polisher.
    file_path (str): Path to the SBML file to be polished.

    Returns:
    dict: Result dictionary containing run_id, diff, and path to the polished model.
    """
    document = libsbml.readSBML(file_path)
    result = polish_model_document(config_dict, document)

    if result:
        polished_sbml_str = libsbml.writeSBMLToString(result["polished_document"])
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xml')
        with open(temp_file.name, 'w') as f:
            f.write(polished_sbml_str)

        result["polished_file_path"] = temp_file.name
        del result["polished_document"]  # Remove the document to avoid confusion
        return result
    return None
