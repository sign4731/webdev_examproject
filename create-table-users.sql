DROP TABLE IF EXISTS users;
CREATE TABLE users(
  user_id                 TEXT UNIQUE NOT NULL,
  user_tag                TEXT UNIQUE NOT NULL,
  user_first_name         TEXT NOT NULL,
  user_last_name          TEXT NOT NULL,
  user_email              TEXT UNIQUE NOT NULL,
  user_password           TEXT NOT NULL,
  user_image              TEXT NOT NULL,
  user_iat                TEXT NOT NULL,
  PRIMARY KEY(user_id)
); WITHOUT ROWID