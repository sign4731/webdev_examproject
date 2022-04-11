DROP TABLE IF EXISTS tweets_liked_by;
CREATE TABLE tweets_liked_by(
  tweet_id_fk                 TEXT NOT NULL,
  user_id_fk                  TEXT NOT NULL
); WITHOUT ROWID