INSERT INTO users (name, email, username, password)
VALUES
  ('test', 'test@test.com', 'test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'other@test.com', 'other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO decks (name, category, owner_id, public, description)
VALUES
  ('test title', 'test_category', 1, 'TRUE', 'test description');
  
INSERT INTO flashcards (category, front, back, notes)
VALUES
  ('test_category', 'test front', 'test back', 'test notes');
