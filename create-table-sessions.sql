DROP TABLE IF EXISTS sessions;
CREATE TABLE sessions(
  user_session_id            TEXT UNIQUE NOT NULL,
  user_email                 TEXT UNIQUE NOT NULL,
  PRIMARY KEY(user_session_id)
); WITHOUT ROWID