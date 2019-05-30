from flask import Flask, jsonify

app = Flask(__name__)

work_note = [
    {
        'id': 1,
        'text': 'Забрать кроссовки из химчистки',

    },
    {
        'id': 2,
        'text': 'Купить бумагу для принтера'
    }
]

private_note = [
    {
        'id': 1,
        'text': 'Встретиться с менеджером по продажам',

    },
    {
        'id': 2,
        'text': 'Забрать машину из автосервиса'
    }
]

archive_note = [
    {
        'id': 1,
        'text': 'Отдать телефон в мастерскую',

    },
    {
        'id': 2,
        'text': 'Снять деньги с карты'
    }
]


@app.route("/", methods=['GET'])
def get_main():
    return jsonify({'work_notes': work_note, 'private_notes': private_note, 'archive_notes': archive_note})


@app.route('/work', methods=['GET'])
def get_work_notes():
    return jsonify({'work_notes': work_note})


@app.route('/private', methods=['GET'])
def get_private_notes():
    return jsonify({'private_notes': private_note})


@app.route('/archive', methods=['GET'])
def get_archive_notes():
    return jsonify({'archive_notes': archive_note})


app.run(debug=True)
