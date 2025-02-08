from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for prompts
prompts = {}

@app.route('/api/prompts', methods=['POST'])
def create_prompt():
    """
    Create a new prompt.
    """
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "Invalid input. 'text' field is required."}), 400
    prompt_id = len(prompts) + 1
    prompts[prompt_id] = data
    return jsonify({"message": "Prompt created", "id": prompt_id}), 201

@app.route('/api/prompts', methods=['GET'])
def get_prompts():
    """
    Retrieve all prompts.
    """
    return jsonify(prompts), 200

@app.route('/api/prompts/<int:prompt_id>', methods=['PUT'])
def update_prompt(prompt_id):
    """
    Update an existing prompt by ID.
    """
    if prompt_id not in prompts:
        return jsonify({"error": "Prompt not found"}), 404
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "Invalid input. 'text' field is required."}), 400
    prompts[prompt_id] = data
    return jsonify({"message": "Prompt updated"}), 200

@app.route('/api/prompts/<int:prompt_id>', methods=['DELETE'])
def delete_prompt(prompt_id):
    """
    Delete a prompt by ID.
    """
    if prompt_id not in prompts:
        return jsonify({"error": "Prompt not found"}), 404
    del prompts[prompt_id]
    return jsonify({"message": "Prompt deleted"}), 200

@app.route('/api/scripts/preview', methods=['POST'])
def generate_script_preview():
    """
    Generate and return a script preview based on the provided topic.
    """
    data = request.json
    if not data or 'topic' not in data:
        return jsonify({"error": "Invalid input. 'topic' field is required."}), 400
    topic = data['topic']

    # Simulate script generation using FilmCrafter
    try:
        from main import FilmCrafter  # Assuming FilmCrafter is defined in main.py
        crafter = FilmCrafter(topic=topic)
        crafter.casting()
        crafter.scenes_plan()
        crafter.lines_generate()
        crafter.position_mark()
        crafter.action_mark()
        crafter.stage1_verify()
        crafter.stage2_verify()
        crafter.move_mark()
        crafter.stage3_verify()
        crafter.clean_script()
        script_path = crafter.script_path
        script = read_json(script_path)  # Assuming read_json is defined in util.py
        return jsonify(script), 200
    except Exception as e:
        return jsonify({"error": f"Failed to generate script preview: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
