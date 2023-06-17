# Word Salad Flashcard App #
## CSPB 3308 Project for Team 0 ##

### Team Name: ###
 Word Salad

### Team Members: ###
 * Thomas Lees, ThomasJHLees
 * Janet Matthews-Derrico, j-derrico
 * Atreyu Sutton, asutton01
 * Tyler Kinkade, tyknkd

### Weekly Meeting: ###
 Mondays, 18:00 MDT, Zoom

### Vision Statement: ###
 Create a web-based dynamic flashcard study app which implements a spaced-repetition algorithm to review user-input content

### Motivation: ###
 Traditional blocked learning (i.e., "cramming") is inefficient compared to spaced interleaved learning (Dunlosky et al., 2013; Kornell & Bjork, 2008; Mondria & Mondria-De Vries, 1994), but very few flashcard apps incorporate spaced-repetition with user content. Therefore, we want to create an easy-to-use app to enable users to study the content they want to study efficiently using spaced-repetition.
 
### Risks to Completion: ###
 * New languages/working environment (e.g., HTML, CSS, SQL, JavaScript, Flask, Heroku)
 * No prior experience working with team members
 * No experience implementing web-based app with user input
 * No experience implementing spaced-repetition algorithms
 * Scope of project (could fail to deliver working project due to high number of desired features)

### Mitigation Strategies: ###
 * Take advantage of documentation--while the languages and working environments are new to us, they aren't *new*, and there is extensive documentation and online resources available
 * Close communication via multiple channels (Email, Google Chat, Zoom, Google Docs, GitHub Projects)
 * Weekly meetings to check in, discuss challenges/obstacles, and make sure everyone is on track
 * Take advantage of team member knowledge on spaced-repetition, research available open source spaced-repetition platforms
 * Focus first and foremost on minimum viable product, then prioritize additional desired, but not required features.  This will ensure ability to deliver a functional project on deadline

### Minimum Viable Product: ###
 * Website interface with a premade English-English vocabulary flashcard set and no user tracking

#### Product Stretch Goals: ####
1. Methods for adding flashcards from the website interface
2. Categorization of flash cards and ability to organize by category from the website
3. A flashcard "deck" concept to organize cards
4. User accounts
5. Saving decks to user profiles
6. Public and Private card decks
7. Searching

### Development Method: ###
We plan to use an Agile framework and borrow pieces of several development idealogies to complete our project.

For our meeting schedule we will largely borrow what Scrum recommends, but condensed into a single weekly meeting. We wil give updates about what we've worked on, what we're going to work on and any blockers that may be in place (standup), host a retrospective of our last sprint period, and complete any required sprint planning. Unfortunately, a daily standup and additional scrum meetings do not make the most sense in a classroom environment.

For our planning and prioritization pieces, we will be using more of a Kanban model. We will define user stories, and organize them in a prioritized backlog. New stories will only be pulled into the board to be worked on when the current work has been completed (within reason). We will also adopt some lean principles in planning where we will only be creating new stories slightly before they are needed instead of trying to map out our entire process. Because of our inexperience in developing programs it makes sense to leave planning to the latest possible second so that we have opportunities to learn pieces that we did not know that we did not know.

The following is a summarized list of the practices we hope to implement on our team: 

Agile 
 * Scrum
   * Practices - combined into a single weekly meeting
     * Release planning
     * Sprint planning
     * Sprint review
     * Sprint retrospective
   * Deliverables
     * Product backlog
     * Sprint backlog
     * Burndown charts
     * Shippable functionality
 * Extreme Programming
   * Team-wide coding standard
   * Collective team ownership
   * Continuous integration via GitHub
   * Test-driven development
   * Simple design/code
   * Small, frequent releases
   * Sustainable work pace
   * Whole team understands whole project
 * Kanban - with our GitHub project board
   * Visualize workflow
   * Limit work in progress
 * Agile Modeling
   * Requirements envisioning
   * Implement in priority order
   * Unified information source (GitHub)
   * Document late as possible
   * Just barely good enough artifacts
 
 (Adapted from Ambler & Holitza, 2012)

### Project Tracking Software: ### 
  [GitHub Projects](https://github.com/users/ThomasJHLees/projects/1)
  
### Directory Tree ###

This project has the following directory tree:
```
.  
├── wordsalad/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── home.py
│   ├── decks.py
│   ├── cards.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── about.html
│   │   ├── decks/
│   │   │   ├── index.html
│   │   │   ├── create.html
│   │   │   ├── edit.html
│   │   │   └── cards/
|   │   │       ├── index.html
|   │   │       ├── add.html
│   |   │       └── edit.html
│   │   └── auth/
│   │       ├── login.html
│   │       └── register.html
│   ├── static/
│   |   ├── style.css
│   |   ├── js/
|   │   |   └── cards.js
|   │   └── images/
|   │       ├── logo.jpg
|   │       ├── salad.png
|   │       ├── GRE.png
|   │       ├── LSAT.png
|   │       └── SAT.png
├── instance/  
│   └── wordsalad.sqlite  
├── tests/  
│   ├── data.sql  
│   ├── conftest.py  
│   ├── setup.cfg  
│   ├── test_factory.py  
│   ├── test_db.py  
│   ├── test_auth.py  
│   ├── test_home.py  
│   ├── test_decks.py  
│   └── test_cards.py  
├── .docs/
|   ├── _build/
|   |   ├── doctrees/
|   |   └── html/
|   ├── Makefile
|   ├── README.md
|   ├── conf.py
|   ├── index.rst
│   └── make.bat
├── csv/
|   ├── source_info.csv
|   ├── SAT_vocab.csv
|   ├── GRE_vocab.csv
│   └── LSAT_vocab.csv
├── images/  
│   ├── db_schematic.png  
│   ├── kanban/  
│   │    └── kanban20220*.png
│   └── mockups/  
│        ├── about.png
│        ├── createcard.png
│        ├── decks.png
│        ├── flashcard.png
│        ├── home.png
│        ├── homepage.jpg
│        └── login.png
├── Procfile 
├── requirements.txt 
├── run.py 
├── setup.py 
├── MANIFEST.in 
├── README.md 
├── WEEKLY_STATUS.md 
├── PAGE_TESTING.md 
├── SQL_TESTING.md 
└── FINAL_REPORT.md 
```

| File                                                                              | Description                                            |
| --------------------------------------------------------------------------------- | ------------------------------------------------------ |
| wordsalad/                                                                        | Application directory                                  |
| &nbsp;&nbsp;&nbsp;`__init__.py`                                                   | Flask application factory                              |
| &nbsp;&nbsp;&nbsp;db.py                                                           | Database initialization script                         |
| &nbsp;&nbsp;&nbsp;schema.sql                                                      | SQL database schema                                    |
| &nbsp;&nbsp;&nbsp;auth.py                                                         | Blueprint to handle authorization requests             |
| &nbsp;&nbsp;&nbsp;home.py                                                         | Blueprint to handle home/about page requests           |
| &nbsp;&nbsp;&nbsp;decks.py                                                        | Blueprint to handle view/add/edit/delete deck requests |
| &nbsp;&nbsp;&nbsp;cards.py                                                        | Blueprint to handle view/add/edit/delete card requests |
| &nbsp;&nbsp;&nbsp;templates/                                                      | Web app templates directory                            |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;base.html                                     | Base web app page template                             |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index.html                                    | Main web app page                                      |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;about.html                                    | About web app page                                     |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decks/                                        | Web app flashcard decks directory                      |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index.html                  | Web app flashcard decks main page                      |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;create.html                 | Web app page to add new deck                           |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;edit.html                   | Web app page to edit existing deck                     |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cards/                      | Web app flashcard deck directory                       |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index.html| Web app flashcard deck cards page                      |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;add.html  | Web app page to add flashcards to deck (incl. via CSV) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;edit.html | Web app page to edit flashcard in deck                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth/                                         | Web app user authentication directory                  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;login.html                  | Web app user authentication login page                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;register.html               | Web app user registration page                         |
| &nbsp;&nbsp;&nbsp;static/                                                         | Web app static files directory                         |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;style.css                                     | Cascading style sheet                                  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;js/                                           | JavaScript directory                                   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cards.js                    | Card flipping JavaScript                               |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;images/                                       | Web app images directory                               |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*.png                       | Web app images files                                   |
| instance/                                                                         | Database directory                                     |
| &nbsp;&nbsp;&nbsp;wordsalad.sqlite                                                | SQLite sample database for Heroku deployment           |
| tests/                                                                            | Unit tests directory                                   |
| &nbsp;&nbsp;&nbsp;data.sql                                                        | Unit test SQL data                                     |
| &nbsp;&nbsp;&nbsp;conftest.py                                                     | Unit test configuration script (runs for every test)   |
| &nbsp;&nbsp;&nbsp;setup.cfg                                                       | Unit test setup configuration file                     |
| &nbsp;&nbsp;&nbsp;test_factory.py                                                 | App factory unit tests                                 |
| &nbsp;&nbsp;&nbsp;test_db.py                                                      | Database unit tests                                    |
| &nbsp;&nbsp;&nbsp;test_auth.py                                                    | Authentication unit tests                              |
| &nbsp;&nbsp;&nbsp;test_home.py                                                    | Home page unit tests                                   |
| &nbsp;&nbsp;&nbsp;test_decks.py                                                   | Decks pages unit tests                                 |
| &nbsp;&nbsp;&nbsp;test_cards.py                                                   | Cards pages unit tests                                 |
| .docs/                                                                            | Autodocumenter directory                               |
| &nbsp;&nbsp;&nbsp;_build/                                                         | Build files directory                                  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;doctrees/                                     | Document trees directory                               |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;html/                                         | HTML files directory                                   |
| &nbsp;&nbsp;&nbsp;Makefile                                                        | Make file                                              |
| &nbsp;&nbsp;&nbsp;README.md                                                       | Instructions for installing autodocumenter             |
| &nbsp;&nbsp;&nbsp;conf.py                                                         | Configuration script                                   |
| &nbsp;&nbsp;&nbsp;index.rst                                                       | Documentation index page                               |
| &nbsp;&nbsp;&nbsp;make.bat                                                        | Make batch file                                        |
| csv/                                                                              | Flashcard CSV files directory                          |
| &nbsp;&nbsp;&nbsp;source_info.csv                                                 | Source data information                                |
| &nbsp;&nbsp;&nbsp;SAT_vocab.csv                                                   | SAT vocabulary source data                             |
| &nbsp;&nbsp;&nbsp;GRE_vocab.csv                                                   | GRE vocabulary source data                             |
| &nbsp;&nbsp;&nbsp;LSAT_vocab.csv                                                  | LSAT vocabulary source data                            |
| images/                                                                           | Documentation images directory                         |
| &nbsp;&nbsp;&nbsp;db_schematic.png                                                | Database schematic diagram                             |
| &nbsp;&nbsp;&nbsp;kanban/                                                         | Kanban screenshots directory                           |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;kanban2022\*.png                              | Weekly Kanban screenshots                              |
| &nbsp;&nbsp;&nbsp;mockups/                                                        | Web page mockup directory                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\*.png                                        | Web page mockups                                       |
| Procfile                                                                          | Heroku procfile                                        |
| requirements.txt                                                                  | Dependencies for deploying to Heroku                   |
| run.py                                                                            | Script for Heroku deployment                           |
| setup.py                                                                          | Script to install app                                  |
| MANIFEST.in                                                                       | List of other files to include at installation         |
| README.md                                                                         | Summary of project                                     |
| WEEKLY_STATUS.md                                                                  | Summary of weekly meeting, progress, tasks             |
| PAGE_TESTING.md                                                                   | Summary of web pages, testing to implement             |
| SQL_TESTING.md                                                                    | Summary of database schema, methods, testing           |
| FINAL_REPORT.md                                                                   | Final project report                                   |

### References: ###
Ambler, S. W., & Holitza, M. (2012). _Agile for dummies, IBM limited edition._ Wiley.

Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students’ learning with effective learning techniques: Promising directions from cognitive and educational psychology. _Psychological Science in the Public Interest, 14_(1), 4-58. [https://doi.org/10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)

Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the “enemy of induction”? _Psychological Science, 19_(6), 585-592. [https://doi.org/10.1111/j.1467-9280.2008.02127.x](https://doi.org/10.1111/j.1467-9280.2008.02127.x)

Mondria, J-A., & Mondria-De Vries, S. (1994). Efficiently memorizing words with the help of word
cards and “hand computer”: Theory and applications. _System, 22_(1), 47–57. [https://doi.org/10.1016/0346-251X(94)90039-6](https://doi.org/10.1016/0346-251X\(94\)90039-6)
