from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data (replace with actual data from your analysis)
    group_growth = [100, 150, 200, 250, 300]  # Example: Daily new members
    active_members = [80, 75, 85, 90, 88]  # Example: Percentage of active members

    return render_template('index.html', 
                           group_growth=group_growth, 
                           active_members=active_members)

if __name__ == '__main__':
    app.run(debug=True)