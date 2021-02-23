from flask import Flask, jsonify

app = Flask(__name__)

# if jsonify, add dict with "dict = {"": "", ""}"
basic_dict = {"Header": "data", "data1"}


@app.route("/")
def home():
    print(
        "Available Routes:<br>"
        "/api/v1.0/precipitation<br>"
        "/api/v1.0/stations<br>"
        "/api/v1.0/<start><br>"
        "/api/v1.0/<end>") 

@app.route("/api/v1.0/precipitation")
def precipitation():
    """    
    Query the dates and temperature observations of the most active station for the last year of data.
    
    Return a JSON list of temperature observations (TOBS) for the previous year.
    
    """
    return jsonify("precipitation analysis")



@app.route("/api/v1.0/stations")
def stations():
    print("stations")

@app.route("/api/v1.0/<start>")
def <start>():
    print("<start>")


@app.route("/api/v1.0/<end>")
def <end>():
    print("<end>")

if __name__ == "__main__":
    app.run(debug=True)