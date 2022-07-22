CREATE TABLE users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE decks (
  deck_id INTEGER PRIMARY KEY AUTOINCREMENT,
  owner_id INTEGER NOT NULL, 
  title TEXT NOT NULL,
  category TEXT NOT NULL,
  description TEXT,
  public BOOLEAN NOT NULL, 
  FOREIGN KEY (owner_id) 
    REFERENCES users (user_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

CREATE TABLE cards (
  card_id INTEGER PRIMARY KEY AUTOINCREMENT,
  deck_id INTEGER NOT NULL, 
  front TEXT NOT NULL,
  back TEXT NOT NULL,
  notes TEXT,
  FOREIGN KEY (deck_id) 
    REFERENCES decks (deck_id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
); 
