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


@app.route('/create_enter', methods=['POST'])
def create_enter():
    name = request.json.get('name')
    content = request.json.get('content')

    if not name or not content:
        return jsonify({
            "message": "You must include a name and content."
                }), 400
    
    new_enter = Entry(name=name, content=content)
    try:
        db.session.add(new_enter)
        db.session.commit()
    except Exception as exc:
        return jsonify({"message": str(exc)}), 400

    return jsonify({
        "message": "Enter Created!"
    }), 201


@app.route('/update_entry/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id: int):
    entry = Entry.query.get_or_404(entry_id, description='Entry does not exist.')
    
    data = request.json
    entry.name = data.get('name', entry.name)
    entry.content = data.get('content', entry.content)

    db.session.commit()

    return jsonify({
        "message": "Entry updated."
    }), 200


@app.route('/delete_entry/<int:entry_id', methods=['DELETE'])
def delete_entry(entry_id: int):
    entry = Entry.query.get_or_404(entry_id, description='Entry does not exist.')

    db.session.delete(entry)
    db.session.commit()

    return jsonify({
        "message": "Entry deleted."
    }), 200





if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)