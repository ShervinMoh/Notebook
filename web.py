from flask import Flask, render_template, request, jsonify
from main import Note, Repository

app = Flask(__name__)

# Initialize repository
repository = Repository()

@app.route('/')
def home():
    return render_template('main_page.html')

@app.route('/add_note', methods=['POST'])
def add_note():
    data = request.json
    title = data.get('title')
    user_text = data.get('text')
    
    if not title or not user_text:
        return jsonify({'success': False, 'message': 'Title and text are required'})
    
    new_note = Note(title, user_text)
    repository.add_note(new_note)
    return jsonify({'success': True, 'message': 'Note added successfully', 'id': new_note.user_id})

@app.route('/get_notes', methods=['GET'])
def get_notes():
    notes = repository.get_all_notes()
    # Convert the notes to a more frontend-friendly format
    formatted_notes = []
    for note_dict in notes:
        for note_id, note_data in note_dict.items():
            formatted_notes.append({
                'id': note_id,
                'title': note_data['title'],
                'text': note_data['user_text'],
                'date': note_data['date']
            })
    return jsonify({'notes': formatted_notes})

@app.route('/edit_note', methods=['POST'])
def edit_note():
    data = request.json
    note_id = data.get('id')
    title = data.get('title')
    user_text = data.get('text')
    
    if not note_id:
        return jsonify({'success': False, 'message': 'Note ID is required'})
    
    if repository.edit_entry(note_id, title, user_text):
        return jsonify({'success': True, 'message': 'Note updated successfully'})
    else:
        return jsonify({'success': False, 'message': 'Note not found'})

@app.route('/remove_note', methods=['POST'])
def remove_note():
    data = request.json
    note_id = data.get('id')
    
    if not note_id:
        return jsonify({'success': False, 'message': 'Note ID is required'})
    
    if repository.remove_entry(note_id):
        return jsonify({'success': True, 'message': 'Note removed successfully'})
    else:
        return jsonify({'success': False, 'message': 'Note not found'})

if __name__ == '__main__':
    app.run(debug=True)