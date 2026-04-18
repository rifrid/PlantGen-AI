from flask import Flask, request, render_template_string

app = Flask(__name__)

def generate_plant_info(plant_name):
    return {
        "description": f"{plant_name} is a beautiful plant ideal for indoor and outdoor decoration.",
        "water": "Water once every 1-2 weeks",
        "light": "Indirect sunlight",
        "soil": "Well-draining soil"
    }

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>PlantGen AI</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">
    <h1>🌱 PlantGen AI</h1>
    <form method="POST">
        <input type="text" name="plant" placeholder="Enter plant name" required>
        <button type="submit">Generate</button>
    </form>

    {% if result %}
        <h2>Result</h2>
        <p><strong>Description:</strong> {{result.description}}</p>
        <p><strong>Water:</strong> {{result.water}}</p>
        <p><strong>Light:</strong> {{result.light}}</p>
        <p><strong>Soil:</strong> {{result.soil}}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        plant = request.form["plant"]
        result = generate_plant_info(plant)
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
