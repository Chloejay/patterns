# a template for setting up a Python open source project 

ref. http://michal.karzynski.pl/blog/2019/05/26/python-project-maturity-checklist/

#### create setup.py 
using https://packaging.python.org/tutorials/packaging-projects/ 

```
$ pip install setuptools wheel
$ python setup.py sdist
$ python setup.py bdist_wheel
```
#### Create a requirements.txt file
```
#add the required packages here on setup.py 
setup(
    install_requires=["colorful", "docopt"],
) 
```
###### on requirements.txt to generate the detailed version of each dependency. 

#### Set up a Git repo
```
curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore > .gitignore

$ git init
$ git add --all
$ git commit -m 'Initial commit'
```
#### Use Black to format the code 
```
$ pip install black 
$ black my_module 
```
#### Set up pre-commit hooks
```
$ pip install pre-commit
$ touch .pre-commit-config.yaml
$ pre-commit sample-config
$ pre-commit install
#see more details on https://pre-commit.com/ 
```
Black will be called to check your style when running `git commit`.

#### Pylint or Flake8 

#### Create a tox.ini config

#### Refactor your code to be unit-testable and add tests
<small>Tip: Using unit tests is one of the best practices. Writing good unit tests is an art and it takes time, but it’s an investment which pays off many times over, especially on a large project which you maintain over a long period.</small>

```
$ pip install pytest
$ pytest 
```
Make sure to add the pytest command to your tox.ini file. 
```
$ pip install pytest pytest-cov 
#to use pytest-cov to generate the pytest testing report 
$ pytest --cov=my_module --cov-report=html tests/
```
#### Add docstrings and documentation

#### Add type annotations and a MyPy verification step
Python 3.5 added the option to annotate your code with type information. This is a very useful and clean type of documentation and you should use. And use Mypy for the static type checking. 
```
$ mypy --config-file=tox.ini module_name
```

#### Requirement.txt updater 
The best way to deal with changing dependencies it to use a service, which periodically bumps versions in your requirements.txt files and creates a pull request with each version change. using Pyup https://pyup.io/ or Dependabot, which is automated offered by GitHub. 
