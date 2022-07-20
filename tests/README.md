# Unit Testing
References: 
[https://flask.palletsprojects.com/en/2.1.x/tutorial/install/](https://flask.palletsprojects.com/en/2.1.x/tutorial/install/)
[https://flask.palletsprojects.com/en/2.1.x/tutorial/tests/](https://flask.palletsprojects.com/en/2.1.x/tutorial/tests/)


1. Install `wordsalad` project in the virtual environment (venv):
```
$ pip install -e .
```

2. Install pytest and coverage in the virtual environment:
```
$ pip install pytest coverage
```

3. Run tests:
```
$ pytest
```

4. Measure code coverage:
```
$ coverage run -m pytest
```

5. View coverage report in terminal:
```
$ coverage report
```

Or view coverage report in htmlcov/index.html
```
$ coverage html
```
