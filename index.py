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
  socket.run(app, allow_unsafe_werkzeug=True)