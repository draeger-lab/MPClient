import pprint
import libsbml
import core

absolute_path_to_some_file = "/home/rick/Software/SystemsBiology/MPClient/resources/iAF1260small.xml"

result = core.polish_model_file(absolute_path_to_some_file)

sbml = libsbml.readSBMLFromFile(absolute_path_to_some_file)

result2 = core.polish_model_document(sbml)

pprint.pprint(result)
