# import json
# from flask          import Flask, render_template
# from flask_socketio import SocketIO, send
# # from Data.main      import ChatBotAssistant

# app = Flask(__name__)
# app.config["SECRET_KEY"] = "secret"
# socketio = SocketIO(app)

# # assistant = ChatBotAssistant('Data/data-bot.json', model_name="test_model")
# # assistant.train_model()
# # assistant.save_model()

# @app.route('/')
# def index():
#   return render_template('index.html')

# @socketio.on("message")
# def handle_message(value):
#   print(value)

# # @app.route('/get-data/<string:data>', methods=['POST'])
# # def get_data(data):
# #   message = json.loads(data)
# #   dataBot = assistant.request(message)
# #   return render_template('index.html')

# if __name__ == '__main__':
#   socketio.run(app)

import json
from flask          import Flask, render_template
from flask_socketio import SocketIO, send, emit
from Data.main      import ChatBotAssistant

assistant = ChatBotAssistant('Data/data-bot.json', model_name="test_model")
assistant.train_model()
assistant.save_model()

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
socket = SocketIO(app)

@app.route("/")
def index():
  return render_template("index.html")

@socket.on("message")
def handle_message(data):
  dataBot = assistant.request(data['value'])
  emit("res", dataBot)

if __name__ == "__main__":
  socket.run(app)