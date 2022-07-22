INSERT INTO users (name, email, username, password)
VALUES
  ('test', 'test@test.com', 'test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'other@test.com', 'other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO decks (owner_id, title, category, description, public)
VALUES
  (1, 'Test Title', 'test_category', 'This is a test deck description.', 'TRUE');
  
INSERT INTO cards (deck_id, front, back, notes)
VALUES
  (1, 'test card front', 'test card back', 'test card notes');
