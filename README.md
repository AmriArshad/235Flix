# CS235Flix
2020 S2 CompSci 235 practical assignment CS235Flix.

### A1
Built a domain model for a simple movie review site. Testing completed using pytest.

### A2
Built a web application that relies on a repository pattern and other architectural design patterns such as Dependency Inversion and Single Responsibility. The app utilises the Flask framework and uses Jinja templating and WTForms. Flask Blueprints have also been used to maintain some level of seperation between the apps functions. All testing has been done using pytest and includes unit and end-to-end integration testing.

## Setup
Install virtual env and dependencies using requirements.txt.

From root run in terminal:
```shell
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

If using windows run the following in root:
```shell
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

## Testing
From root run (make sure venv is activated):
```shell
$ python -m pytest
```

## Running the web app
from root (also making sure venv is activated):
```shell
$ flask run
```
now open http://127.0.0.1:5000/

## Screenshots

![Home](screenshots/1.png)
![Register](screenshots/2.png)
![Login](screenshots/3.png)
![Browse](screenshots/4.png)
![BrowseActor](screenshots/5.png)
![BrowseDirector](screenshots/6.png)
![BrowseGenre](screenshots/7.png)
![ReviewEmpty](screenshots/8.png)
![Review](screenshots/9.png)
