import requests

question_data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean&category=18").json()["results"]
