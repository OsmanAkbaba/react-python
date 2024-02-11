from flask import Flask, jsonify
from flask_cors import CORS
#app instance eli sovelluksen esiintymä

app = Flask(__name__)
CORS(app)

@app.route("/api/home", methods=['GET'])
def  return_home():
    return jsonify({
        'message': "TOIMII ",
        'people': ['jussi', 'mikko', 'pekka']
    })
    

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    
    #debug=True, jotta nähdään virheet ja jos julkaistaan, poistetaan tämä
    
    
#Käynnistetään serveri komennolla python server.py