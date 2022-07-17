# SQL Design #

## Tables ##

### Schematic Diagram ###
<img src="https://github.com/ThomasJHLees/Team0Project/blob/main/images/db_schematic.png" width="500px">

###  Table 1 ###
* Name: flashcards
* Table description: Data for each flashcard: the clue for the "front" of the card, the corresponding answer for the "back" of the card, the category (e.g., SAT vocabulary study set, GRE vocabulary, etc.), and notes (e.g., part-of-speech, frequency, etc.)
* Fields (name and description):
  * card_id: integer, unique index key
  * category: alphanumeric string, group(s) to which entry belongs (e.g., SAT vocabulary set, GRE vocabulary set, elementary-level Spanish-English vocabulary set, etc.) 
  * front: alphanumeric string, clue/question/prompt for "front" of card
  * back: alphanumeric string, answer/response/definition/translation for "back" of card
  * notes: alphanumeric string, additional information (e.g., part-of-speech, frequency, etc.)
* List of tests for verifying each table
  * After initial populate, data for each row and column in flashcard source CSVs is in table
  * After initial populate, only rows in source data are in table (i.e., no extra data points)

###  Table 2 ###
* Name
* Table description
* Fields (name and description)
* List of tests for verifying each table

###  Table 3 ###
* Name
* Table description
* Fields (name and description)
* List of tests for verifying each table

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
