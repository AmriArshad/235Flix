# CS235FlixSkeleton
The skeleton python project for the 2020 S2 CompSci 235 practical assignment CS235Flix.

## Setup
Install virtual env and dependencies using requirements.txt.

From root run in bash:
```shell
python -m venv venv
. venv/Scripts/activate
pip install -r requirements.txt
```

### A1
Completed the following class objects:
- Actor
- Director
- Genre
- Movie
- Review
- User
- WatchList
- MovieFileCSVReader

Completed testing for these classes under /tests

### Extensions:

Added revenue to Movie class
Added all values to Movie objects in MovieFileCSVReader.dataset_of_movies
Added relevent testing for above

## Testing
From root run (make sure venv is activated):
```shell
py.test -v
```