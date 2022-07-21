CREATE TABLE users (
  user_id INT PRIMARY KEY,
  name VARCHAR,
  email VARCHAR,
  username VARCHAR,
  password VARCHAR
);

CREATE TABLE decks (
  deck_id INT PRIMARY KEY,
  owner_id INT, 
  title VARCHAR,
  category VARCHAR,
  description VARCHAR,
  'public' BOOL, 
  FOREIGN KEY (owner_id) 
    REFERENCES users (user_id)
);

CREATE TABLE cards (
  card_id INT PRIMARY KEY,
  deck_id INT, 
  front VARCHAR,
  back VARCHAR,
  notes VARCHAR,
  FOREIGN KEY (deck_id) 
    REFERENCES decks (deck_id)
); 
