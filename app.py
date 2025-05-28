from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# In-memory list to store tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'POST':
        task = request.json.get('task')
        tasks.append({'id': len(tasks) + 1, 'task': task, 'completed': False})
        return jsonify({'message': 'Task added successfully!'}), 201

    return jsonify(tasks)

@app.route('/api/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if request.method == 'PUT':
        if task:
            task['completed'] = request.json.get('completed', task['completed'])
            return jsonify({'message': 'Task updated successfully!'}), 200
        return jsonify({'error': 'Task not found!'}), 404

    if request.method == 'DELETE':
        if task:
            tasks.remove(task)
            return jsonify({'message': 'Task deleted successfully!'}), 200
        return jsonify({'error': 'Task not found!'}), 404

if __name__ == '__main__':
    app.run(debug=True)
