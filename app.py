from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret123"

#Home Page
@app.route('/')
def home():
    return render_template('index.html')

#Mood Selection Page
@app.route('/mood')
def mood():
    return render_template('mood.html')

#Result Page
@app.route('/result', methods=['POST'])
def result():
    selected_mood = request.form.get('mood')

    #Define sample music and quotes
    mood_data = {
        "Happy": {
            "quote": "Happiness is not out there,it's within you. Collect moments, not things!","music":"https://youtu.be/oLgzs8nut3A?si=fvtyW_z9urvzqsSi"
        },
        "Sad": {
            "quote": "One day you'll look back and realize,this strength was born from sadness","music":"https://youtu.be/ZWuzH0fW8l0?si=tGxp-xRoUCa9mriT"
        },
        "Stressed": {
            "quote": "Breathe. You're doing better than you think. Slow down-not everything needs an immediate reaction. Peace begins when expectations end. ","music":"https://youtu.be/6LD30ChPsSs?si=S08SjEfP2VbyyvrR"
        },
        "Motivated": {
            "quote":"Start where you are. Use what you have. Do what you can. One day or day one-you decide. Dreams don't work unless you do","music":"https://youtu.be/OW_S_t5fxZA?si=B1iL2SlOzKlRgxfZ"
        }
    }

    data = mood_data.get(selected_mood, {})
    return render_template('result.html',mood=selected_mood, data=data)

#About Page
@app.route('/about')
def about():
    return render_template('about.html')

#Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # later you can save to DB or send email
        print(name, email, message)

        flash("Thank you for your feedback 🎵", "success")
        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run()

