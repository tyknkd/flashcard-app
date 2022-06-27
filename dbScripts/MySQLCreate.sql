CREATE TABLE `flashcards` (
  `card_id` int PRIMARY KEY AUTO_INCREMENT,
  `category` varchar(255),
  `front` varchar(255),
  `back` varchar(255),
  `notes` varchar(255)
);

CREATE TABLE `decks` (
  `deck_id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `category` varchar(255),
  `owner_id` int,
  `public` bool
);

CREATE TABLE `users` (
  `user_id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `username` varchar(255),
  `email` varchar(255)
);

CREATE TABLE `cards_in_deck` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `card_id` int,
  `deck_id` int
);

CREATE TABLE `cards_created_by_users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `user_id` int,
  `card_id` int
);

ALTER TABLE `decks` ADD FOREIGN KEY (`owner_id`) REFERENCES `users` (`user_id`);
ALTER TABLE `cards_in_deck` ADD FOREIGN KEY (`card_id`) REFERENCES `flashcards` (`card_id`);
ALTER TABLE `cards_in_deck` ADD FOREIGN KEY (`deck_id`) REFERENCES `decks` (`deck_id`);
ALTER TABLE `cards_created_by_users` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);
ALTER TABLE `cards_created_by_users` ADD FOREIGN KEY (`card_id`) REFERENCES `flashcards` (`card_id`);
