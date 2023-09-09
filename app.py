from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle image upload
        if "image" in request.files:
            uploaded_image = request.files["image"]
            if uploaded_image.filename != "":
                # Save the uploaded image temporarily
                image_path = "temp_image.png"
                uploaded_image.save(image_path)

                # Call the Python script with the uploaded image
                cmd = ["python", "python_script.py", image_path]
                result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
                output = result.stdout
                return render_template("index.html", output=output)

    return render_template("index.html", output=None)

if __name__ == "__main__":
    app.run(debug=True)
