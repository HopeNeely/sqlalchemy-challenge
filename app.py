import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


"""
Database Setup
"""
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station


"""
Flask Setup
"""
app = Flask(__name__)


"""
Flask Routes
"""
@app.route("/")
def home():
    print("Server recieved request for 'Home' page...")
    return(
        "Welcome to the SQLalchemy Challenge API!<br/>"
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "<br/>"
        "Pick a start date after 2016-8-23 and enter date in yyyy-mm-dd form after the following route:<br/>"
        "/api/v1.0/<start>"
        )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """ 
    Create our session (link) from Python to the DB 
    """
    session = Session(engine)

    """    
    Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
    """
    year_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= 2016-8-23).order_by(Measurement.date.desc()).all()

    session.close()

    precip = []
    for date, prcp in year_data:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        precip.append(prcp_dict)


    """
    Return the JSON representation of your dictionary.
    """
    print("Server recieved request for 'precipitation' page...")
    return jsonify(precip)
    

 
@app.route("/api/v1.0/stations")
def stations():
    """
    Create our session (link) from Python to the DB
    """
    session = Session(engine)

    """
    Return a JSON list of stations from the dataset.
    """
    station_counts = session.query(Measurement.station).group_by(Measurement.station).order_by(func.count(Measurement.station)).all()

    session.close()

    stations = list(np.ravel(station_counts))

    print("Server recieved request for 'stations' page...")
    return jsonify(stations)
    
    

@app.route("/api/v1.0/tobs")
def tobs():
    """
    Create our session (link) from Python to the DB
    """
    session = Session(engine)    
    
    """ 
    Query the dates and temperature observations of the most active station for the last year of data.   
    """
    year_temp_data = session.query(Measurement.date, Measurement.station, Measurement.tobs).\
    filter(Measurement.date > 2016-8-23).\
    filter(Measurement.station == 'USC00519523').\
    order_by(Measurement.date).all() 
    
    session.close()
    
    
    temp = []
    for date, station, tobs  in year_temp_data:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["station"] = station
        tobs_dict["tobs"] = tobs
        temp.append(tobs_dict)
    
    """
    Return a JSON list of temperature observations (TOBS) for the previous year.
    """ 
    print("Server recieved request for 'tobs' page...")
    return jsonify(temp)



@app.route("/api/v1.0/<start>")
def temperature(start):
    """
    Create our session (link) from Python to the DB
    """    
    session = Session(engine)  
    
    """
    Return a JSON list of the minimum temperature, the average temperature, and the max temperature for range after start.
    When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
    """
    temperature = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                    filter(Measurement.date >= start).all()
    
    session.close()
    
    t = list(np.ravel(temperature))


    print("Server recieved request for 'temperature' page...")
    return jsonify(t)



if __name__ == "__main__":
    app.run(debug=True)
