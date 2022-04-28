import re

##############################
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
##############################
def _is_text(text=None):
  if not text: return None
  text = re.sub("[\n\t]*", "", text)
  text = re.sub(" +", " ", text)
  text = text.strip()
  print(text)
  return text

##############################

REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

GMAIL_PASSWORD = "Kpjq09r#"
