# AutoDoc Instructions #

AutoDoc is a utility that can be used to automatically document functions in code

### To view the current documentation: ###
 1. Navigate to ./.docs/_build/html
 2. Open index.html in a web browser

### To update the documentation after adding new functions to existing python files: ###
 1. Install Sphinx
 ```
 pip install sphinx
 ```
 2. From the ./docs directory run:
 ```
 make html
 ```
 If on a windows system, ensure you are running the command from cmd instead of powershell
 3. Navigate to ./.docs/_build/html and open index.html in a web browser to see your updated documentation

 ### To update the documentation after adding a new python file: ###
 1. Edit the index.rst file in the ./docs folder and add an entry for the file. Ex:
 ```
 .. automodule:: wordsalad.auth
   :members:
 ```
 2. Repeat instructions for updating documentation for existing python files