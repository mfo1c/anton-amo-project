import time

from app import amo, sender
import secret_info
from flask import Flask, request


flask_app = Flask(__name__)


@flask_app.route('/', methods=["POST"])
def hello():
    d = request.form.to_dict()
    if int(d['message[add][0][created_at]']) + 10 < int(time.time()):
        return 'ok'  # избавление от дублей от амо
    receiver_id = d['message[add][0][chat_id]']
    chat_history = amo.get_chat_history(receiver_id)
    answer_from_api = sender.get_answer(chat_history)
    amo.send_message(answer_from_api)


flask_app.run(host='0.0.0.0', debug=True)