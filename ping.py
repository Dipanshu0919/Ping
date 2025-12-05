import os, requests, json, sqlitecloud, datetime

allsecrets = os.environ.get("ALL_SECRETS")
allsecrets = json.loads(allsecrets)

def sqlitecloud():
  try:
    keys = allsecrets.get("SQLITECLOUD", "")
    if keys == "":
      print("No key found")
      return
      
    key_list = list(keys)
    for key in key_list:
      db = sqlitecloud.connect(key)
      db.row_factory = sqlitecloud.Row
      c = db.cursor()
      create = "CREATE TABLE IF NOT EXISTS PINGER(LAST_PING TEXT)"
      c.execute(create)
      fetch = c.execute("SELECT * FROM PINGER").fetchone()
      if fetch:
        c.execute("UPDATE PINGER SET LAST_PING=(?)", (datetime.datetime.now(), ))
        print(f"PING FROM {key} DONE.")
      else:
        c.execute("INSERT INTO PINGER(LAST_PING) VALUES=(?)", (datetime.datetime.now(), ))
  except Exception as e:
    print(e)
    
if __name__ == "__main__":
  sqlitecloud()
