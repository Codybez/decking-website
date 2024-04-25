from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
      return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/submit-project', methods=['POST'])
def submit_project():
    name = request.form['name']
    email = request.form['email']
    details = request.form['details']
    images = request.files.getlist('image')  # Handles multiple images

    for image in images:
        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # You can now store the filename along with the project details in your database

    # After saving the details and images, redirect the user or show a success message
    flash('Project submitted successfully!')
    return redirect(url_for('index'))  # Redirect to homepag