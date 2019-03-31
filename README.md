# Doug's Cookiecutter Data Science Project Template

*A logical, reasonably standardized, but flexible project structure for doing 
and sharing data science work.*


**[Original project homepage](http://drivendata.github.io/cookiecutter-data-science/)**


### Requirements

[Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: 
This can be installed with pip by or conda depending on how you manage your 
Python packages:

```bash
$ pip install cookiecutter
```
or

```bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

To start a new project simply run:

```bash
$ cookiecutter gh:douglasdaly/cookiecutter-data-science
```



### Project Layout

The directory structure of your new project looks like this: 

```
├── data
│   ├── cooked         <- Derived/fully-cooked data.
│   ├── external       <- Additional data from external sources.
│   ├── interim        <- Temporary store for any interim data.
│   ├── processed      <- The (lightly) processed raw data.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project
│
├── media              <- Any media files used by or generated from the project.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for 
│                         ordering), the creator's initials, and a short `-` 
│                         delimited description, e.g. `1-dd-initial-data-exploration.ipynb`.
│
├── references         <- Helpful reference information for the project/data.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│
├── requirements.txt   <- The requirements file for reproducing the analysis 
│                         environment, e.g. generated with `pip freeze > 
│                         requirements.txt`.
│
├── scripts            <- Folder for scripts used in this project.
│   ├── data.py        <- Script tools for working with the data.
│   └── media.py       <- Script tools for generating media files.
│
├── src                <- Source code used in this project.
│   │
│   ├── data           <- Code related to acquiring and processing the data
│   │   ├── file_functions.py
│   │   ├── get_data_functions.py
│   │   ├── parse.py
│   │   └── process.py
│   │
│   ├── models         <- Code for models.
│   │
│   └── visualization  <- Code for visualizations
│
├── LICENSE            <- License file for the new project.
├── Makefile           <- Makefile with helpful commands
├── README.md          <- The top-level README for using this project.
└── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
```


### Running the Tests

```bash
py.test tests
```

### License

This project is licensed under the MIT license.  See the ```LICENSE``` file
for more details.