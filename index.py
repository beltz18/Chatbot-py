import json
import asyncio

from flask          import Flask, render_template
from flask_socketio import SocketIO, send
from Data.main      import ChatBotAssistant

app = Flask(__name__)
app.config['SECRET'] = "BossGymAdmin1234"
socket = SocketIO(app, cors_allowed_origins="*")

assistant = ChatBotAssistant('Data/data-bot.json', model_name="test_model")
assistant.train_model()
assistant.save_model()

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/get-data/<string:data>', methods=['POST'])
async def get_data(data):
  message = json.loads(data)
  dataBot = await assistant.request(message)
  await asyncio.sleep(10)
  print(dataBot)
  return await render_template('index.html')

if __name__ == '__main__':
  asyncio.run(app.run(debug=True))