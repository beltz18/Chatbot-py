import json
import time
import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/get-data')
def get_data():
  output = request.get_json()
  print(output)
  print(type(output))
  result = json.loads(output)
  print(result)
  print(type(result))
  return result

# from Data.main import ChatBotAssistant

# assistant = ChatBotAssistant('data-bot.json', model_name="test_model")
# assistant.train_model()
# assistant.save_model()

print("¡Bienvenido a ChuckBot, el Chatbot informativo que te ofrece datos interesantes sobre el Maravilloso actor Chuck Norris!\n")
print("Recuerda que puedes finalizar el programa con el comando 'stop'")

# while True:
#   message = input("Escribe algo: ")
#   if message == "stop":
#     break
#   else:
#     assistant.request(message)