# Doug's Cookiecutter Data Science Project Template

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### [Original project homepage](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/douglasdaly/cookiecutter-data-science



### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── scripts            <- Folder for scripts used in this project for various tasks
│   └── build_features.py
│   └── get_data.py
│   └── predict_model.py
│   └── process_data.py
│   └── train_model.py
│
├── src                <- Source code for library used in this project and installed as a
│   │                     development library for use within this projects virtualenv.
│   │
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Functions/Classes related to acquiring the data
│   │   └── __init__.py
│   │   └── file_functions.py
│   │   └── get_data_functions.py
│   │   └── parse.py
│   │   └── process.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── __init__.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   └── __init__.py
│   │   └── base.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── __init__.py
│
├── setup.py           <- Setup python config for installing library from src folder
│
└── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
```

### Setting up the project virtualenv
------------

    make create_environment


### Installing dependencies
------------

    make requirements


### Running the tests
------------

    py.test tests

