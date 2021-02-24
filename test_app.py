from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    print("Server recieved request for 'Home' page...")
    return(
        "Welcome to the SQLalchemy Challenge API!"
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs"
        "/api/v1.0/<start>/<end>"
        ) 

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server recieved request for 'precipitation' page...")
    return("precipitation")


if __name__ == "__main__":
    app.run(debug=True)

