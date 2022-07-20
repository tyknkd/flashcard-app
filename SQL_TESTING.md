# SQL Design #

## Tables ##

### Schematic Diagram ###
<img src="https://github.com/ThomasJHLees/Team0Project/blob/main/images/db_schematic.png" width="500px">

### Table 1 ###
* Name: `flashcards`
* Table description: Data for each flashcard: the clue/question for the "front" of the card, the corresponding answer for the "back" of the card, the category (e.g., SAT vocabulary study set, GRE vocabulary, etc.), and notes (e.g., part-of-speech, frequency, etc.)
* Fields (name and description):
  * `card_id`: (integer) unique index key
  * `category`: (alphanumeric) category/set descriptive code with no whitespace characters describing which entry belongs (e.g., SAT_vocab, GRE_vocab, Spanish_English_elem_vocab) 
  * `front`: (alphanumeric) clue/question/prompt for "front" of card
  * `back`: (alphanumeric) answer/response/definition/translation for "back" of card
  * `notes`: (alphanumeric) additional information (e.g., part-of-speech, frequency, etc.)
* List of tests for verifying each table:
  * Table is empty after initialization 
  * Able to insert multiple rows of alphanumeric test data
  * Query returns expected data for all rows and columns

### Table 2 ###
* Name: `users`
* Table description: User information, including name, username, email address, and password
* Fields (name and description):
  * `user_id`: (integer) unique index key
  * `name`: (alphanumeric) user's name
  * `username`: (alphanumeric) username
  * `email`: (alphanumeric) user email address
  * `password`: (alphanumeric) user password
* List of tests for verifying each table:
  * Table is empty after initialization 
  * Able to insert multiple rows of alphanumeric test data
  * Query returns expected data for all rows and columns

### Table 3 ###
* Name: `decks`
* Table description: Data describing each deck/set of flashcards: name, category (e.g., SAT vocabulary, GRE vocabulary, elementary Spanish)
* Fields (name and description):
  * `deck_id`: (integer) unique index key
  * `name`: (alphanumeric) human-readable name of deck/set of flashcards in title case (e.g., SAT Vocabulary, GRE Vocabulary, Elementary Spanish)
  * `category`: (alphanumeric) category/set descriptive code with no whitespace characters identifying category of flashcard set (e.g., SAT_vocab, GRE_vocab, Spanish_English_elem_vocab) 
  * `owner_id`: (integer) references `user_id` from `users` table of user which created the deck
  * `public`: (boolean) indicates whether deck is public (true) or private (false)
  * `description`: (alphanumeric) description of deck
* List of tests for verifying each table:
  * Table is empty after initialization 
  * Able to insert multiple rows of test data
  * Query returns expected data for all rows and columns
    
### Table 4 ###
* Name: `cards_in_deck`
* Table description: Contains `card_id` for each flashcard and its corresponding `deck_id` based on the card's category
* Fields (name and description):
  * `id`: (integer) unique index key
  * `card_id`: (integer) references unique `card_id` in `flashcards` table
  * `deck_id`: (integer) references `deck_id` in `decks` table
* List of tests for verifying each table:
  * Table is empty after initialization 
  * After inserting multiple rows of test data in `flashcards` and `decks`, query returns expected data for all rows and columns

### Table 5 ###
* Name: `cards_created_by_users`
* Table description: Contains `card_id` for each flashcard created by a user and its corresponding `user_id` and `category`
* Fields (name and description):
  * `id`: (integer) unique index key
  * `user_id`: (integer) references unique `user_id` in `users` table
  * `card_id`: (integer) references unique `card_id` in `flashcards` table
  * `category`: (alphanumeric) references `category` in `flashcards` table
* List of tests for verifying each table:
  * Table is empty after initialization 
  * After inserting multiple rows of test data in `flashcards` and `users`, query returns expected data for all rows and columns

## Data Access Methods
### Table 1 Access Method 1 ### 
* Name: Add flashcard
* Description: Add new flashcard via post to `/decks/<deck_id>/add` 
* Parameters: 
* Return values: 
* List of tests for verifying each access method:
  * Able to add multiple flashcards of test data
  * Unable to add incomplete/invalid data
  * Query returns expected data for all rows and columns

### Table 1 Access Method 2 ### 
* Name: View flashcard
* Description: View flashcards via request to `/decks/<deck_id>`
* Parameters:
* Return values:
* List of tests for verifying each access method:
  * Retrieved data for all rows and columns as expected 
  * Attempting to retrieve non-existent card results in error message

### Table 1 Access Method 3 ### 
* Name: Edit flashcard
* Description: Edit flashcard via request to `/decks/<deck_id>/edit`
* Parameters:
* Return values:
* List of tests for verifying each access method:
  * Retrieved data for all edited rows as expected
  * Attempting to edit non-existent card results in error message

### Table 1 Access Method 4 ### 
* Name: Remove flashcard
* Description: Remove flashcard via request to `/decks/<deck_id>/edit`
* Parameters:
* Return values:
* List of tests for verifying each access method:
  * Removed flashcard no longer exists
  * Attempting to remove non-existent card results in error message

### Table 2 Access Method 1 ### 
* Name: Register user
* Description: Create new user account via `/auth/register`
* Parameters:
* Return values:
* List of tests for verifying each access method:
  * Able to add multiple users with valid parameters
  * Registering with invalid arguments fails
  * Query returns expected data for all rows and columns

### Table 2 Access Method 2 ### 
* Name: Authenticate user
* Description: Log in via `/auth/login`
* Parameters:
* Return values:
* List of tests for verifying each access method:
  * Able to login with valid credentials
  * Username returned after valid login
  * Unable to login with invalid credentials

### Table 3 Access Method 1 ### 
* Name: `decks.get_deck(deck_id, check_owner=True)`
* Description: Retrieve deck information for specified `deck_id` and optionally check if requesting user is owner of deck
* Parameters: `deck_id`, `check_owner`
* Return values: `name`, `category`,`owner_id`, `public`, `description`  
* List of tests for verifying each access method:
  * Return expected values for existent decks
  * Attempting to retrieve non-existent deck fails

### Table 3 Access Method 2 ### 
* Name: `decks.create()`
* Description: Add new deck via `/decks/create` form
* Parameters: None
* Return values: Added deck posts to `/decks`
* List of tests for verifying each access method:
  * Adding valid deck information results in deck displaying
  * Attempting to add invalid deck values fails

### Table 3 Access Method 3 ### 
* Name: `decks.edit(deck_id)`
* Description: Edit existing deck via `/decks/edit`
* Parameters: `deck_id`
* Return values: Edited deck posts to `/decks`
* List of tests for verifying each access method
  * Valid deck information results in edited deck displaying
  * Attempting to updated with invalid deck values fails

### Table 3 Access Method 4 ### 
* Name: `decks.delete(deck_id)`
* Description: Remove existing deck via `/decks/edit`
* Parameters: `deck_id`
* Return values: Deck no longer posted to `/decks`
* List of tests for verifying each access method
  * Removing existent deck results in deck removed from decks
  * Attempting to remove non-existent deck results in no change

### Table 4 Access Method 1 ### 
* Name: 
* Description: View cards for a particular deck via `/decks/<deck_id>`
* Parameters
* Return values
* List of tests for verifying each access method

### Table 5 Access Method 1 ### 
* Name: 
* Description: View cards for particular user via `/decks/<deck_id>`
* Parameters
* Return values
* List of tests for verifying each access method

## Test Descriptions ##
### Test 1 ###
* Use case name
* Description
* Pre-conditions
* Test steps
   1. 
   2. 
   3. 
   4. 
* Expected result
* Post-conditions
