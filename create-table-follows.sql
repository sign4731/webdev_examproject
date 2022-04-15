DROP TABLE IF EXISTS follows;
CREATE TABLE follows(
  user_who_followed_id_fk                      TEXT NOT NULL,
  user_who_got_followed_id_fk                  TEXT NOT NULL
);