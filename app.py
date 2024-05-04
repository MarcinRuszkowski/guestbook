from flask import request, jsonify

from config import app, db
from models import Entry


@app.route('/entries', methods=['GET'])
def get_all_entries():
    entries = Entry.query.all()
    json_entries = list(map(lambda x: x.to_json(), entries))
    return jsonify({
        "entries": json_entries
            })


@app.route('/create_enter', method=['POST'])
def create_enter():
    name = request.json.get('name')
    content = request.json.get('content')

    if not name or not content:
        return jsonify({
            "message": "You must include a name and content"
                }), 400
    
    new_enter = Entry(name=name, content=content)




if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)