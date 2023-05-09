from flask import Flask, render_template, request, redirect, url_for, flash, session
from communication import Communication

app = Flask(__name__)
com = Communication()

@app.route('/')
def index():
    return render_template('index.html', title='Accueil')

@app.route('/emotion', methods=['GET'])
def emotion():
    if request.args.get("nb_personnes") is not None and request.args.get("nb_personnes") != "0":
        com.start(request.args.get("nb_personnes"))
        data = com.get_data()
        return render_template('analyse.html', title='Analyse des émotions', nb_personnes=request.args.get("nb_personnes"), data=data)
    
    if request.args == [] or request.args.get("nb_personnes") == "0" or request.args.get("nb_personnes") is None or request.args.get("nb_personnes") == "None" or request.args.get("nb_personnes") == "" or request.args == None:
        com.stop()
      
    
    return render_template('emotion.html', title='Détection d\'émotions')


if __name__ == "__main__":
    app.run(debug=True)