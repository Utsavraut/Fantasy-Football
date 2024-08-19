from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Get the base directory of the Flask application
        base_dir = os.path.abspath(os.path.dirname(__file__))
        # Adjust path to reach the 'data' folder correctly
        top_15_players_path = os.path.join(base_dir, '..', 'data', 'features', 'top_15_players.csv')
        best_xi_path = os.path.join(base_dir, '..', 'data', 'features', 'best_xi.csv')

        top_15_players = pd.read_csv(top_15_players_path)
        best_xi = pd.read_csv(best_xi_path)
        
        return render_template('index.html', top_15=top_15_players.to_dict(orient='records'), best_xi=best_xi.to_dict(orient='records'))
    except FileNotFoundError as e:
        return str(e)
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
