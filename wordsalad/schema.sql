CREATE TABLE `flashcards` (
  `card_id` INTEGER PRIMARY KEY,
  `category` varchar(255),
  `front` varchar(255), 
  `back` varchar(255), 
  `notes` varchar(255)
);

CREATE TABLE `decks` (
  `deck_id` INTEGER PRIMARY KEY,
  `name` varchar(255),
  `category` varchar(255),
  `owner_id` int,
  `public` bool
);

CREATE TABLE `users` (
  `user_id` INTEGER PRIMARY KEY,
  `name` varchar(255),
  `username` varchar(255),
  `email` varchar(255),
  `password` varchar(255)
);

CREATE TABLE `cards_in_deck` (
  `id` INTEGER PRIMARY KEY,
  `card_id` int,
  `deck_id` int
);

CREATE TABLE `cards_created_by_users` (
  `id` INTEGER PRIMARY KEY,
  `user_id` int,
  `card_id` int
);
