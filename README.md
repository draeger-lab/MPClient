# model-polisher
API for the [Model Polisher](https://github.com/draeger-lab/MPServer).

- API version: 2.1
- Package version: 0.0.1

## Getting Started

```python
import libsbml
import model_polisher as mp

model_file = "path/to/iAF1260 .xml"
sbml = libsbml.readSBMLFromFile(model_file)

# you can pass a file
result = mp.polish_model_file(model_file)

# or you can pass a libsbml.SBMLDocument object
result2 = mp.polish_model_document(sbml)

# result is a dictionary with three keys:
# result["run_id"]
# result["diff"]
# result["polished_document"]
```

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

Right now, the package is only hosted on GitHub. You can install it like this:

```sh
pip install git+https://github.com/draeger-lab/MPClient.git
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
