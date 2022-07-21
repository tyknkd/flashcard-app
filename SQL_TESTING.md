# SQL Design #

## Tables ##

### Schematic Diagram ###
<img src="https://github.com/ThomasJHLees/Team0Project/blob/main/images/db_schematic.png" width="500px">

### Table 1 ###
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

### Table 2 ###
* Name: `decks`
* Table description: Data describing each deck/set of flashcards: name, category (e.g., SAT vocabulary, GRE vocabulary, elementary Spanish)
* Fields (name and description):
  * `deck_id`: (integer) unique index key
  * `owner_id`: (integer) references `user_id` from `users` table of user which created the deck
  * `title`: (alphanumeric) human-readable title of deck/set of flashcards in title case (e.g., SAT Vocabulary, GRE Vocabulary, Elementary Spanish)
  * `category`: (alphanumeric) category/set descriptive code with no whitespace characters identifying category of flashcard set (e.g., SAT_vocab, GRE_vocab, Spanish_English_elem_vocab) 
  * `description`: (alphanumeric) description of deck
  * `public`: (boolean) indicates whether deck is public (true) or private (false)
* List of tests for verifying each table:
  * Table is empty after initialization 
  * Able to insert multiple rows of test data
  * Query returns expected data for all rows and columns
    
### Table 3 ###
* Name: `flashcards`
* Table description: Data for each flashcard: the clue/question for the "front" of the card, the corresponding answer for the "back" of the card, the category (e.g., SAT vocabulary study set, GRE vocabulary, etc.), and notes (e.g., part-of-speech, frequency, etc.)
* Fields (name and description):
  * `card_id`: (integer) unique index key
  * `deck_id`: (integer) references `deck_id` from `decks` table of deck which contains the card
  * `category`: (alphanumeric) category/set descriptive code with no whitespace characters describing which entry belongs (e.g., SAT_vocab, GRE_vocab, Spanish_English_elem_vocab) 
  * `front`: (alphanumeric) clue/question/prompt for "front" of card
  * `back`: (alphanumeric) answer/response/definition/translation for "back" of card
  * `notes`: (alphanumeric) additional information (e.g., part-of-speech, frequency, etc.)
* List of tests for verifying each table:
  * Table is empty after initialization 
  * Able to insert multiple rows of alphanumeric test data
  * Query returns expected data for all rows and columns


## Data Access Methods
### Table 1 Access Method 1 ### 
* Name: `auth.add_user(name, email, username, password)`
* Description: Add new user to table`
* Parameters: `name`, `email`, `username`, `password`
* Return values: Boolean
* List of tests for verifying each access method:
  * Adding new user with valid user values results in row correctly added to table
  * Duplicate users not permitted
  * Attempting to add invalid user values fails

### Table 1 Access Method 2 ### 
* Name: `auth.get_user(username, password)`
* Description: Get user information for 
* Parameters: `username`, `password`
* Return values: `user_id`, `name`, `email` 
* List of tests for verifying each access method:
  * Return expected values for existent users
  * Nothing returned for incorrect username and/or password

### Table 2 Access Method 1 ### 
* Name: `decks.get_deck(deck_id)`
* Description: Retrieve deck information for specified `deck_id`
* Parameters: `deck_id`
* Return values: `name`, `category`,`owner_id`, `public`, `description`  
* List of tests for verifying each access method:
  * Return expected values for existent decks
  * Attempting to retrieve non-existent deck fails

### Table 2 Access Method 2 ### 
* Name: `decks.add_deck(name, category, owner_id, public, description)`
* Description: Add new deck
* Parameters: `name`, `category`, `owner_id`, `public`, `description`
* Return values: Boolean
* List of tests for verifying each access method:
  * Valid parameters results in row correctly added to table
  * Attempting to add invalid deck values fails

### Table 2 Access Method 3 ### 
* Name: `decks.update(deck_id, name, category, owner_id, public, description)`
* Description: Update existing deck with `deck_id`
* Parameters: `deck_id`, `name`, `category`, `owner_id`, `public`, `description`
* Return values: Boolean
* List of tests for verifying each access method
  * Valid parameters results in update to `deck_id` row
  * Attempting to update with invalid deck values fails

### Table 2 Access Method 4 ### 
* Name: `decks.delete(deck_id)`
* Description: Remove existing deck `deck_id`
* Parameters: `deck_id`
* Return values: Boolean
* List of tests for verifying each access method:
  * Removing existent deck results in deck removed from decks
  * Attempting to remove non-existent deck results in no change

### Table 3 Access Method 1 ### 
* Name: `cards.get_card(card_id)`
* Description: Retrieve card information for specified `card_id`
* Parameters: `card_id`
* Return values: `front`, `category`,`back`, `notes`  
* List of tests for verifying each access method:
  * Return expected values for existent cards
  * Attempting to retrieve non-existent card fails

### Table 3 Access Method 2 ### 
* Name: `cards.add_card(front, category, back, notes)`
* Description: Add new card to table
* Parameters: `front`, `category`,`back`, `notes`
* Return values: Boolean
* List of tests for verifying each access method:
  * Valid parameters results in row correctly added to table
  * Attempting to add invalid card values fails

### Table 3 Access Method 3 ### 
* Name: `cards.update(card_id, front, category, back, notes)`
* Description: Update existing card with `card_id`
* Parameters: `card_id`, `front`, `category`,`back`, `notes`
* Return values: Boolean
* List of tests for verifying each access method
  * Valid parameters results in update to `card_id` row
  * Attempting to update with invalid card values fails

### Table 3 Access Method 4 ### 
* Name: `cards.delete(card_id)`
* Description: Remove existing card with `card_id`
* Parameters: `card_id`
* Return values: Boolean
* List of tests for verifying each access method
  * Removing existent card results in card removed from table
  * Attempting to remove non-existent card results in no change
