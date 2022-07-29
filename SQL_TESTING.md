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
  * `email`: (alphanumeric) user email address
  * `username`: (alphanumeric) unique username
  * `password`: (alphanumeric) user password
* List of tests for verifying each table:
  * Table is empty after initialization 
  * Able to insert multiple rows of alphanumeric test data
  * Query returns expected data for all rows and columns
  * Check both access through flask app and table itself

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
  * Check both access through flask and values in table itself
    
### Table 3 ###
* Name: `cards`
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
  * Check access through flask and values in table itself

## Data Access Methods
### Table 1 Access Method 1 ### 
* Name: `auth.add_user(name, email, username, password)`
* Description: Add new user to table
* Parameters: `name`, `email`, `username`, `password`
* Return values: `error` string (None if successful)
* List of tests for verifying each access method:
  * Adding new user with valid user values results in row correctly added to table
  * Duplicate usernames not permitted
  * Attempting to add invalid user values fails

### Table 1 Access Method 2 ### 
* Name: `auth.get_user(username)`
* Description: Get user information
* Parameters: `username`
* Return values: dict of `user_id`, `name`, `email`, `username`, `password` 
* List of tests for verifying each access method:
  * Return expected values for existent users
  * Nothing returned for non-existent user

### Table 1 Access Method 3 ### 
* Name: `auth.get_user_from_id(user_id)`
* Description: Get user information
* Parameters: `user_id`
* Return values: dict of `user_id`, `name`, `email`, `username`, `password` 
* List of tests for verifying each access method:
  * Return expected values for existent users
  * Nothing returned for non-existent user

### Table 2 Access Method 1 ### 
* Name: `decks.get_decks(owner_id)`
* Description: Retrieve deck information for all public decks and decks belonging to `owner_id`. If owner is `None`, then only public decks returned.
* Parameters: None
* Return values: list of dicts of `deck_id`, `owner_id`, `title`, `category`, `description`, `public`  
* List of tests for verifying each access method:
  * Return expected values for all public decks
  * Return expected values for all public decks and decks belonging to `owner_id`

### Table 2 Access Method 2 ### 
* Name: `decks.get_deck(deck_id)`
* Description: Retrieve deck information for specified `deck_id`
* Parameters: `deck_id`
* Return values: dict of `deck_id`, `owner_id`, `title`, `category`, `description`, `public`  
* List of tests for verifying each access method:
  * Return expected values for existent decks
  * Attempting to retrieve non-existent deck fails

### Table 2 Access Method 3 ### 
* Name: `decks.add_deck(owner_id, title, category, description, public)`
* Description: Add new deck
* Parameters: `owner_id`, `title`, `category`, `description`, `public`
* Return values: `error` string (None if successful)
* List of tests for verifying each access method:
  * Valid parameters results in row correctly added to table
  * Attempting to add invalid deck values fails

### Table 2 Access Method 4 ### 
* Name: `decks.update(deck_id, title, category, description, public)`
* Description: Update existing deck with `deck_id`
* Parameters: `deck_id`, `title`, `category`, `description`, `public`
* Return values: `error` string (None if successful)
* List of tests for verifying each access method
  * Valid parameters results in update to `deck_id` row
  * Attempting to update with invalid deck values fails

### Table 2 Access Method 5 ### 
* Name: `decks.remove(deck_id)`
* Description: Remove existing deck `deck_id`
* Parameters: `deck_id`
* Return values: `error` string (None if successful)
* List of tests for verifying each access method:
  * Removing existent deck results in deck removed from decks
  * Attempting to remove non-existent deck results in no change

### Table 3 Access Method 1 ### 
* Name: `cards.get_card(card_id)`
* Description: Retrieve card information for specified `card_id`
* Parameters: `card_id`
* Return values: dict of `deck_id`, `front`, `back`, `notes`  
* List of tests for verifying each access method:
  * Return expected values for existent cards
  * Attempting to retrieve non-existent card fails

### Table 3 Access Method 2 ### 
* Name: `cards.get_cards(deck_id)`
* Description: Retrieve all card information for specified `deck_id`
* Parameters: `deck_id`
* Return values: list of dicts of cards `front`, `back`, `notes`  
* List of tests for verifying each access method:
  * Return expected values for existent deck/cards
  * Attempting to retrieve non-existent deck fails

### Table 3 Access Method 3 ### 
* Name: `cards.add_card(deck_id, front, back, notes)`
* Description: Add new card to table
* Parameters: `deck_id`, `front`, `back`, `notes`
* Return values: `error` string (None if successful)
* List of tests for verifying each access method:
  * Valid parameters results in row correctly added to table
  * Attempting to add invalid card values fails

### Table 3 Access Method 4 ### 
* Name: `cards.update(card_id, front, back, notes)`
* Description: Update existing card with `card_id`
* Parameters: `card_id`, `front`, `back`, `notes`
* Return values: `error` string (None if successful)
* List of tests for verifying each access method
  * Valid parameters results in update to `card_id` row
  * Attempting to update with invalid card values fails

### Table 3 Access Method 5 ### 
* Name: `cards.remove(card_id)`
* Description: Remove existing card with `card_id`
* Parameters: `card_id`
* Return values: `error` string (None if successful)
* List of tests for verifying each access method
  * Removing existent card results in card removed from table
  * Attempting to remove non-existent card results in no change
