# Web Pages Design #

### Page 1: Home Page ###
* Page Description (include a mockup or hand drawn image of the page)

    * Header with logo
    * Navigation menu
    * Single column
    * Flashcard deck preview
    * Description of service
    * Prominent button to deck viewing page
    * Login and register links or user name and logout link if logged in
    * Footer with contact

* Parameters needed for the page

    * MVP idea and scope
    * Logo
    * Description excerpt

* Data needed to render the page

    * Home page HTML
    * Deck IDs, titles, descriptions, categories, owner, and public status
    * User login status

* Link destinations for the page

    * Available
        * Home `/`
        * About page `/about/`
        * Decks page `/decks/`
    * Available If Logged In
        * Log out `/auth/logout/`
    * Available If Not Logged In
        * Log in `/auth/login/`
        * Register `/auth/register/`

* List of tests for verifying the rendering of the page

    * Page can be accessed via `/` and `/index.html`
    * Correct page title
    * Correct page contents
    * Appropriate flashcard deck loaded when corresponding deck image clicked
    * All links lead to correct pages
    * Drop down menus display when menu item clicked

<img src="https://github.com/ThomasJHLees/Team0Project/blob/main/images/mockups/home.png?raw=true" width="1000">

=======================================================================


### Page 2: About Page ###
* Page Description (include a mockup or hand drawn image of the page)

    * Header with logo
    * Navigation menu
    * Single column
    * Description of service
    * Tips on best usage
    * Footer with contact

* Parameters needed for the page

    * Tips on best usage
    * Logo
    * Description excerpt

* Data needed to render the page

    * About page HTML
    * User login status

* Link destinations for the page

    * Available
        * Home `/`
        * Decks page `/decks/`
    * Available If Logged In
        * Log out `/auth/logout/`
    * Available If Not Logged In
        * Log in `/auth/login/`
        * Register `/auth/register/`

* List of tests for verifying the rendering of the page

    * Page can be accessed via `/about` and `/about/`
    * Correct page title
    * Correct page contents
    * Appropriate flashcard deck loaded when corresponding deck image clicked
    * All links lead to correct pages
    * Drop down menus display when menu item clicked

<img src="https://github.com/ThomasJHLees/Team0Project/blob/main/images/mockups/about.png?raw=true" width="1000">

=======================================================================


### Page 3: Registration Page ###

* Page Description (include a mockup or hand drawn image of the page)

    * New user registration page
    * Header with small logo
    * Simple middle box with registration form
        * Name field
        * Email field
        * Username field
        * Password field
        * Register button
    * Small Footer with point of contact

* Parameters needed for the page

    * Logo
    * Knowledge of HTML Forms

* Data needed to render the page

    * DB with login information and they're assosiated decks

* Link destinations for the page

    * Available
        * Home `/`
        * About page `/about/`
        * Decks page `/decks/`
    * Available If Logged In
        * Log out `/auth/logout/`
    * Available If Not Logged In
        * Log in `/auth/login/`
        * Register `/auth/register/`


* List of tests for verifying the rendering of the page

    * Page can be accessed via `/auth/register/` and `/auth/register`
    * Correct page title
    * Correct page contents
    * All links lead to correct pages
    * Drop down menus display when menu item clicked
    * Valid user input results in redirect to login page
    * Error displayed for invalid input


### Page 4: Login Page ###

* Page Description (include a mockup or hand drawn image of the page)

    * Registered user login page
    * Header with small logo
    * Simple middle box with login form
        * Username field
        * Password field
        * Log in button
    * Small footer with point of contact

* Parameters needed for the page

    * Logo
    * Knowledge of HTML Forms

* Data needed to render the page

    * DB with login information and they're assosiated decks

* Link destinations for the page

    * Available
        * Home `/`
        * About page `/about/`
        * Decks page `/decks/`
    * Available If Logged In
        * Log out `/auth/logout/`
    * Available If Not Logged In
        * Log in `/auth/login`
        * Register `/auth/register/`


* List of tests for verifying the rendering of the page

    * Page can be accessed via `/auth/login/` and `/auth/login`
    * Correct page title
    * Correct page contents
    * All links lead to correct pages
    * Drop down menus display when menu item clicked
    * Correct username and password results in authentication and redirects to decks page
    * Error displayed for invalid username/password

<img src="https://github.com/ThomasJHLees/Team0Project/blob/main/images/mockups/login.png?raw=true" width="1000">

=======================================================================


### Page 5: Decks Viewing Page ###

* Page Description (include a mockup or hand drawn image of the page)

    * Displays public and user-created decks
    * Header with logo
    * Navigation menu to other pages
    * If logged in, button/link to create a new deck
    * If logged in, button/link to edit only decks owned by user
    * Includes means to filter decks
    * Footer with contact

* Parameters needed for the page

    * All decks' details (deck_id, title, description, category, owner, public status)
    * Logo
    * Other pages with corresponding links

* Data needed to render the page

    * Admin created decks

* Link destinations for the page

    * Available
        * Home `/`
        * About page `/about/`
        * Individual deck pages `/decks/<deck_id>/`
    * Available If Logged In
        * Log out `/auth/logout/`
     * Available If Logged In and Owner of Deck
        * Create deck `/decks/create/`
        * Edit deck `/decks/<deck_id>/edit/`
        * Log out `/auth/logout/`
    * Available If Not Logged In
        * Log in `/auth/login/`
        * Register `/auth/register/`

* List of tests for verifying the rendering of the page

    * Page can be accessed via `/decks/` and `/decks`
    * Correct page title
    * All available decks displayed
    * All links lead to correct pages
    * Drop down menus display when menu item clicked

    <img src="https://github.com/ThomasJHLees/Team0Project/blob/main/images/mockups/decks.png?raw=true" width="1000">


=======================================================================


### Page 6: Individual Deck Page - PAGE TO STUDY DECKS ###

* Page Description (include a mockup or hand drawn image of the page)

    * Displays flashcards for currently selected deck
    * THIS is the interactive USEABLE PAGE - the purpose of our software
    * Header with logo
    * Navigation menu
    * User can toggle between front and back of flashcards
    * User can create/edit cards and change deck information of user-owned decks
    * User can bulk upload cards from CSV file
    * This is the most challenging page

* Parameters needed for the page

    * Logo
    * Deck details for selected deck  (deck_id, title, description, category, owner, public status)

* Data needed to render the page

    * Deck details for selected deck  (deck_id, title, description, category, owner, public status)
    * Details for cards in deck (card_id, front, back, notes)

* Link destinations for the page
 
    * Available
        * Home `/`
        * Decks page `/decks/`
        * About page `/about/`
    * Available If Logged In
        * Log out `/auth/logout/`
    * Available If Logged In and Owner of Current Deck
        * Add card `/decks/<deck_id>/add/`
        * Edit card `/decks/<deck_id>/<card_id>/edit/`
        * Edit deck `/decks/<deck_id>/edit/`
        * Log out `/auth/logout/`
    * Available If Not Logged In
        * Log in `/auth/login/`
        * Register `/auth/register/`

* List of tests for verifying the rendering of the page

    * Page can be accessed via `/decks/<deck_id>/` and `/decks/<deck_id>`
    * Correct page title
    * All links lead to correct pages
    * Drop down menus display when menu item clicked
    * Appropriate flashcard deck loaded
    * Clicking flashcard displays back of card
    * Front of flashcard corresponds to correct back of card (i.e., word matches definition)

<img src="https://github.com/ThomasJHLees/Team0Project/blob/main/images/mockups/flashcard.png?raw=true" width="1000">

=======================================================================

### Page 7: Deck Creation Page ###
* Page Description (include a mockup or hand drawn image of the page)

    * Page to create new deck (login required)
    * Header with log
    * Navigation menu
    * Deck creation form in center
        * Title field
        * Category field
        * Description field
        * Public checkbox/toggle
        * Save button

* Parameters needed for the page

    * Logo
    * User ID

* Data needed to render the page

    * User ID

* Link destinations for the page

    * Available
        * Home `/`
        * Decks page `/decks/`
        * About page `/about/`
        * Log out `/auth/logout/`

* List of tests for verifying the rendering of the page
    * Page can be accessed via `/decks/<deck_id>/edit/` and `/decks/<deck_id>/edit`
    * Correct page title
    * All links lead to correct pages
    * Drop down menus display when clicked
    * Edit Cards displayed
    * Card can be edited and uploaded to DB
    * Verified proper info was stored in the DB
    * Error message displayed when error occured etc.



### Page 8: Card Creation/Editing Pages ###
* Page Description (include a mockup or hand drawn image of the page)

    * Page to add/edit cards in deck owned by user
    * Flash card editing/creation form in the center
        * Card front field
        * Card back field
        * Notes field
        * Save button
        
* Parameters needed for the page

    * Logo
    * Existing deck

* Data needed to render the page

    * User ID
    * Deck ID
    * Card ID (if editing)

* Link destinations for the page

    * Available
        * Home `/`
        * Decks page `/decks/`
        * About page `/about/`
    * Available If Logged In and Owner of Current Deck
        * Deck `/decks/<deck_id>`
        * Log out `/auth/logout/`
    
* List of tests for verifying the rendering of the page
    * Creation page can be accessed via `/decks/<deck_id>/add/` and `/decks/<deck_id>/add`
    * Edit page can be accessed via `/decks/<deck_id>/<card_id>/edit/` and `/decks/<deck_id>/<card_id>/edit`
    * Correct page title
    * All links lead to correct pages
    * Drop down menus display when clicked
    * Valid input results in card inserted correctly for current deck into DB
    * Error message displayed for invalid input
 
<img src="https://github.com/ThomasJHLees/Team0Project/blob/main/images/mockups/createcard.png?raw=true" width="1000">



