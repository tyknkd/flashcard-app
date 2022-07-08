CREATE TABLE `flashcards` (
  `card_id` int PRIMARY KEY,
  `category` varchar(255),
  `front` varchar(255),
  `back` varchar(255),
  `notes` varchar(255)
);

CREATE TABLE `decks` (
  `deck_id` int PRIMARY KEY,
  `name` varchar(255),
  `category` varchar(255),
  `owner_id` int,
  `public` bool
);

CREATE TABLE `users` (
  `user_id` int PRIMARY KEY,
  `name` varchar(255),
  `username` varchar(255),
  `email` varchar(255)
);

CREATE TABLE `cards_in_deck` (
  `id` int PRIMARY KEY,
  `card_id` int,
  `deck_id` int
);

CREATE TABLE `cards_created_by_users` (
  `id` int PRIMARY KEY,
  `user_id` int,
  `card_id` int
);