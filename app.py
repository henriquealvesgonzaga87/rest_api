from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [
    {"id": "0", "name": "Henrique", "skills": ["Python", "Flask"]},
    {"id": "1", "name": "Gisa", "Skills": ["Pyhton", "Django"]}
]


@app.route("/dev/<int:id>/", methods=["GET", "PUT", "DELETE"])
def developer(id):
    if request.method == "GET":
        try:
            response = developers[id]
        except IndexError:
            message = f"developer with ID {id} doesn't exist"
            response = {"status": "error", "message": message}
        except Exception:
            message = "Unknowed error"
            response = {"status": "error", "message": message}
        return jsonify(response)
    elif request.method == "PUT":
        datas = json.loads(request.data)
        developers[id] = datas
        return jsonify(datas)
    elif request.method == "DELETE":
        developers.pop(id)
        return jsonify({"status": "deleted", "message": "the item was deleted"})


@app.route("/dev/", methods=["GET", "POST"])
def list_developers():
    if request.method == "POST":
        datas = json.loads(request.data)
        position = len(developers)
        datas["id"] = position
        developers.append(datas)
        return jsonify(developers[position])
    elif request.method == "GET":
        return jsonify(developers)


if __name__ == "__main__":
    app.run(debug=True)
