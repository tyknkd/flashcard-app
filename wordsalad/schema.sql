CREATE TABLE users (
  user_id INTEGER PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255),
  username VARCHAR(255),
  password VARCHAR(255)
);

CREATE TABLE decks (
  deck_id INTEGER PRIMARY KEY,
  owner_id INTEGER, 
  title VARCHAR(255),
  category VARCHAR(255),
  description VARCHAR(255),
  public BOOLEAN, 
  FOREIGN KEY (owner_id) 
    REFERENCES users (user_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

CREATE TABLE cards (
  card_id INTEGER PRIMARY KEY,
  deck_id INTEGER, 
  front VARCHAR(255),
  back VARCHAR(255),
  notes VARCHAR(255),
  FOREIGN KEY (deck_id) 
    REFERENCES decks (deck_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
); 
