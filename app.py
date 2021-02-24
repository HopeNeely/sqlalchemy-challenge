from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    print("Server recieved request for 'Home' page...")
    return(
        "Welcome to the SQLalchemy Challenge API!<br/>"
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/<start>/<end>"
        )

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server recieved request for 'precipitation' page...")
    return("precipitation")
    """    
    Query the dates and temperature observations of the most active station for the last year of data.
    
    Return a JSON list of temperature observations (TOBS) for the previous year.
    """
    """
    Note: for specific routes: 
    return jsonify("precipitation analysis")
    """
 
@app.route("/api/v1.0/stations")
def stations():
    print("Server recieved request for 'stations' page...")
    return("stations")
    """ 
    Return a JSON list of stations from the dataset.
    
    """


@app.route("/api/v1.0/tobs")
def tobs():
    print("Server recieved request for 'tobs' page...")
    return("tobs")
    """ 
    Query the dates and temperature observations of the most active station for the last year of data.

    Return a JSON list of temperature observations (TOBS) for the previous year.
    
    """
"""
@app.route("/api/v1.0/<start>/<end>")
def temperature(start, end):
    print("start/end")
"""

"""
Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
    
"""

"""
This is an example from class:
Fetch the Justice League character whose real_name matches
the path variable supplied by the user, or a 404 if not."""

"""
    canonicalized = real_name.replace(" ", "").lower()
    for character in justice_league_members:
        search_term = character["real_name"].replace(" ", "").lower()

        if search_term == canonicalized:
            return jsonify(character)

    return jsonify({"error": f"Character with real_name {real_name} not found."}), 404
"""

"""
I don't think I need this. 
@app.route("/api/v1.0/<end>")
def <end>():
    print("<end>")
"""


if __name__ == "__main__":
    app.run(debug=True)
