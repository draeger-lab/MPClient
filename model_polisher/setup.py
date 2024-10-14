from setuptools import setup, find_packages

# Lies den Inhalt der README-Datei für die lange Beschreibung des Pakets
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="model_polisher",  # Name 
    version="2.1.0",  # Versionsnummer 
    author="biodata",  #  Name als Autor
    author_email="biodata@informatik.uni-halle.de",  
    description="A Python package for polishing SBML models using the Model Polisher API",  # Kurze Beschreibung
    long_description=long_description = 
    "ModelPolisher is a simple single-purpose automated curation tool for SBML models. improve the adherence to FAIR data standards as practiced in the SBML modelling community implement non-binding best practices as defined by the SBML specification documents add MIRIAM-style semantic annotations to models, using the BiGG Models knowledgebase and AnnotateDB"
    # Lange Beschreibung des Pakets

    long_description_content_type="text/markdown",  # Format der langen Beschreibung (Markdown)
    url="https://github.com/draeger-lab/MPClient.git",  # URL zum Projekt (GitHub Repository)
    project_urls={
        "Bug Tracker": "https://github.com/draeger-lab/ModelPolisher",  # Bug-Tracker-URL
    },
    classifiers=[  # Metadaten zu deinem Paket
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Lizenz des Pakets 
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},  # Optional, falls dein Code in einem anderen Verzeichnis liegt (z.B. src/)
    packages=find_packages(where="src"),  # Sucht automatisch nach Python-Modulen und Paketen
    python_requires=">=3.6",  # Unterstützte Python-Versionen
    install_requires=[  # Abhängigkeiten, die für dein Paket benötigt werden
        "libsbml>=3.1.0",
       # "model-polisher-api-client",  # Beispiel für den API-Client des Model Polishers
    ],
    entry_points={  # Optionale Skripteinträge für die Kommandozeilenwerkzeuge
        'console_scripts': [
            'polish_model=model_polisher.polish_model:main',  # Beispiel für Skriptaufruf
        ],
    },
)
