from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []

@app.get("/todos")
def get_todos():
    return jsonify(todos)

@app.post("/todos")
def create_todo():
    data = request.json
    item = {"id": len(todos)+1, "title": data.get("title"), "done": False}
    todos.append(item)
    return jsonify(item), 201

@app.put("/todos/<int:todo_id>")
def update_todo(todo_id):
    data = request.json
    for t in todos:
        if t["id"] == todo_id:
            t.update(data)
            return jsonify(t)
    return jsonify({"error": "not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0")
