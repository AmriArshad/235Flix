# CS235Flix
2020 S2 CompSci 235 practical assignment CS235Flix.

### A1
Built domain model

### A2
Built web app that relies on a repository pattern

## Setup
Install virtual env and dependencies using requirements.txt.

From root run in bash:
```shell
$ python -m venv venv
$ . venv/Scripts/activate
$ pip install -r requirements.txt
```

If using windows run the following in root:
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt

## Testing
From root run (make sure venv is activated):
```shell
$ python -m pytest
```

## Running the web app
```shell
$ flask run
```
now open localhost:5000 or http://127.0.0.1:5000/