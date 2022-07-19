# Flask Instructions #

Flask is a lightweight local web development server.

To view the project website locally:
 1. Install Flask: [https://flask.palletsprojects.com/en/2.1.x/installation/](https://flask.palletsprojects.com/en/2.1.x/installation/)
 2. Clone `wordsalad` to your machine.
 3. In a Bash terminal, from the directory containing `wordsalad`, enter:
    ```
    $ export FLASK_APP=wordsalad
    $ export FLASK_ENV=development
    $ flask init-db
    $ flask run
    ```
 4. Open `http://127.0.0.1:5000/` in a web browser.

See [https://flask.palletsprojects.com/en/2.1.x/tutorial/factory/](https://flask.palletsprojects.com/en/2.1.x/tutorial/factory/) for more information. 
