DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets(
  tweet_id                 TEXT UNIQUE NOT NULL,
  tweet_text               TEXT NOT NULL,
  tweet_image              TEXT NOT NULL,
  tweet_created_by         TEXT NOT NULL,
  tweet_iat                TEXT NOT NULL,
  tweet_iat_date           TEXT NOT NULL,
  tweet_updated_at         TEXT NOT NULL,
  PRIMARY KEY(tweet_id)
) WITHOUT ROWID;