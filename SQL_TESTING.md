# SQL Design #

## Tables ##

### Schematic Diagram ###
<img src="https://github.com/ThomasJHLees/Team0Project/blob/main/images/db_schematic.png" width="500px">

### Table 1 ###
* Name: `flashcards`
* Table description: Data for each flashcard: the clue/question for the "front" of the card, the corresponding answer for the "back" of the card, the category (e.g., SAT vocabulary study set, GRE vocabulary, etc.), and notes (e.g., part-of-speech, frequency, etc.)
* Fields (name and description):
  * `card_id`: integer, unique index key
  * `category`: alphanumeric, category/set descriptive code with no whitespace characters describing which entry belongs (e.g., SAT_vocab, GRE_vocab, Spanish_English_elem_vocab) 
  * `front`: alphanumeric, clue/question/prompt for "front" of card
  * `back`: alphanumeric, answer/response/definition/translation for "back" of card
  * `notes`: alphanumeric, additional information (e.g., part-of-speech, frequency, etc.)
* List of tests for verifying each table:
  * After initial populate, data for each row and column in flashcard source CSVs is in table and category matches source data category:
    * `category` matches source data category
    * `front` matches source data prompt/word
    * `back` matches source data answer/definition
    * `notes` matches source data notes
  * After initial populate, only rows in source data are in table (i.e., no extra data points from unknown sources)

### Table 2 ###
* Name: `users`
* Table description: User information, including name, username, email address, and password
* Fields (name and description):
  * `user_id`: integer, unique index key
  * `name`: alphanumeric, user's name
  * `username`: alphanumeric, username
  * `email`: alphanumeric, user email address
  * `password`: alphanumeric, user password
* List of tests for verifying each table:
  * Administrative super user account details are correct
  * After initial populate, only super user account exists
  * After adding new user, user account details are as expected

### Table 3 ###
* Name: `decks`
* Table description: Data describing each deck/set of flashcards: name, category (e.g., SAT vocabulary, GRE vocabulary, elementary Spanish)
* Fields (name and description):
  * `deck_id`: integer, unique index key
  * `name`: alphanumeric, human-readable name of deck/set of flashcards in title case (e.g., SAT Vocabulary, GRE Vocabulary, Elementary Spanish)
  * `category`: alphanumeric, category/set descriptive code with no whitespace characters identifying category of flashcard set (e.g., SAT_vocab, GRE_vocab, Spanish_English_elem_vocab) 
  * `owner_id`: integer, references `user_id` from `users` table of user which created the deck
  * `public`: boolean, indicates whether deck is public (true) or private (false)
  * `description`: alphanumeric, description of deck
* List of tests for verifying each table:
  * After initial populate, a deck exists for each flashcard source data CSV
  * After initial populate, each row and column as expected:
    * `name` matches human-readable source data name in `/Decks/source_info.csv`
    * `category` matches source data category code in `/Decks/source_info.csv`
    * `owner_id` matches `user_id` of administrative superuser
    * `public` set to true
    * `description` matches brief description in `/Decks/source_info.csv`

### Table 4 ###
* Name: `cards_in_deck`
* Table description: Contains `card_id` for each flashcard and its corresponding `deck_id` based on the card's category
* Fields (name and description):
  * `id`: integer, unique index key
  * `card_id`: integer, references unique `card_id` in `flashcards` table
  * `deck_id`: integer, references `deck_id` in `decks` table
* List of tests for verifying each table:
  * After initial populate, the number of entries matches the number of entries in `flashcards`
  * After initial populate, for each `card_id`, `deck_id` matches `deck_id` in `decks` with same `category` as the corresponding `card_id` in `flashcards`   

## Data Access Methods
### Table 1 Access Method 1 ### 
* Name
* Description
* Parameters
* Return values
* List of tests for verifying each access method

### Table 2 Access Method 1 ### 
* Name
* Description
* Parameters
* Return values
* List of tests for verifying each access method

### Table 3 Access Method 1 ### 
* Name
* Description
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
* Actual result
* Status (Pass/Fail)
* Notes
* Post-conditions
