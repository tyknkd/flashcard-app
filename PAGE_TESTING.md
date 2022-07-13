# Web Pages Design #

### Page 1: Home Page ###
* Page Description (include a mockup or hand drawn image of the page)

    * Header with Links
    * Single Column
    * Description of Service
    * Big Green Link to Deck Viewing Pages
    * Footer with Contact

        <!-- <img src="images/homepage.jpg" alt="Home Page Screenshot" style="float: left; margin-right: 10px;" /> -->

* Parameters needed for the page

    * MVP idea and scope
    * Logo
    * Description excerpt

* Data needed to render the page

    * Home Page HTML
    * Deck Titles and Descriptions

* Link destinations for the page

    * Available
        * Home
        * All decks/Filter Page
        * Individual Decks Interacting Page
    * Available If Logged In
        * Personal Deck Page
        * Personal Deck Creation/Editing Page
    * Available If Not Logged In
        * Log In Page

* List of tests for verifying the rendering of the page

    * Page can be accessed via `/` and `/index.html`
    * Correct page title
    * Correct page contents
    * Appropriate flashcard deck loaded when corresponding deck image clicked
    * All links lead to correct pages
    * Drop down menus display when menu item clicked


=======================================================================


### Page 2: Login Page ###

* Page Description (include a mockup or hand drawn image of the page)

    * Small Logo
    * Simple Middle Box with Login Form
        * Username Box
        * Password Box
    * Small Footer with point of Contact

* Parameters needed for the page

    * Logo
    * Knowledge of HTML Forms

* Data needed to render the page

    * DB with login information and they're assosiated decks

* Link destinations for the page

    * Available
        * Home
        * All decks/Filter Page
        * Individual Decks
    * Not Available (Availible after logged in)
        * Personal Deck Page
        * Personal Deck Creation/Editing Page

* List of tests for verifying the rendering of the page

    * Page can be accessed via `/login/` and `/login`
    * Correct page title
    * Correct page contents
    * All links lead to correct pages
    * Drop down menus display when menu item clicked
    * Correct username and password results in authentication
    * Error displayed for incorrect username/password


=======================================================================


### Page 3: All Deck Viewing Page / Filter Page ###

* Page Description (include a mockup or hand drawn image of the page)

    * !!!May include user created decks OR may have a separate page similar to this to show user created decks

    * Header to other pages
    * Page with all decks creates by World Salad
    * Button to make a new Deck
    * Includes filter to cycle through the decks
    * Footer with Contact

* Parameters needed for the page

    * All decks written out
    * Logo
    * Other pages with corresponding links

* Data needed to render the page

    * Admin created decks

* Link destinations for the page

    * Available
        * Home
        * Individual Decks
    * Available If Logged In
        * Personal Deck Page
        * Personal Deck Creation/Editing Page
    * Available If Not Logged In
        * Log In Page

* List of tests for verifying the rendering of the page

    * Page can be accessed via `/decks/` and `/decks`
    * Correct page title
    * All available decks displayed
    * All links lead to correct pages
    * Drop down menus display when menu item clicked


=======================================================================


### Page 4: Individual Decks Interaction Page - PAGE TO STUDY DECKS ###

* Page Description (include a mockup or hand drawn image of the page)

    * This is a page for interacting with the decks
    * THIS is the interactive USEABLE PAGE - the purpose of our software

* Parameters needed for the page

    * All the created decks

* Data needed to render the page

    * Decks and their corresponding info

* Link destinations for the page

    * Available
        * Home
        * All decks/Filter Page
        * Individual Decks Interacting Page <---- THIS IS THE PAGE
    * Available If Logged In
        * Personal Deck Page
        * Personal Deck Creation/Editing Page
    * Available If Not Logged In
        * Log In Page

* List of tests for verifying the rendering of the page

    * Page can be accessed via `/decks/<deck_name>/` and `/decks/<deck_name>`
    * Correct page title
    * All links lead to correct pages
    * Drop down menus display when menu item clicked
    * Appropriate flashcard deck loaded
    * Clicking flashcard displays back of card
    * Front of flashcard corresponds to correct back of card (i.e., word matches definition)


=======================================================================


### Page 5: Deck Creation/Editing Page ###
* Page Description (include a mockup or hand drawn image of the page)

    * Flash Card Editing in the Center
        * Use text boxes for primary editing software
    * This is the most challenging page

* Parameters needed for the page

    * Direct connection to the DB
    * Preexisting Decks

* Data needed to render the page

    * Direct connection to the DB
    * All decks and potential user login

* Link destinations for the page

    * Available
        * Home
        * All decks/Filter Page
        * Individual Decks Interacting Page
    * Available If Logged In
        * Personal Deck Page
        * Personal Deck Creation/Editing Page
    * Available If Not Logged In
        * Log In Page



* List of tests for verifying the rendering of the page
    * Page can be accessed via `/edit/<deck_name>/` and `/edit/<deck_name>`
    * Correct page title
    * All links lead to correct pages
    * Drop down menus display when clicked
    * Edit Cards displayed
    * Card can be edited and uploaded to DB
    * Verified proper info was stored in the DB
    * Error message displayed when error occured etc.
 
