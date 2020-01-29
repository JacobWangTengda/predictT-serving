# predictT-serving


### Description
This repository hosts the code for a local flask server written in python, which turns a trained time series prediction model into a microservice. This microservice will be integrated into the predictT platform and consumed by other parts of the projects.

### Folder Structure

    ├── data                                # Data files used in prediction
    |   ├── AEP_hourly.csv
    |   ├── COMED_hourly.csv
    |   ├── EKPC_hourly.csv
    |   ├── .....
    ├── model                               # Model related files
    │   ├── model.pickle.dat                # XGboost model saved using pickle library
    │   ├── Train Prediction Model.ipynb    # Model Training Code
    ├── src                                 # Source files folder
    |   ├── util.py                         # Utility Function
    ├── app.py                              # Flask Server Code
    ├── Dockerfile                          # Docker File
    └── README.md
    
### Prediction File Format
* Must be in csv format
* Dates should be in the first column
* Values should be in the second column
### Usage
1. Run the docker containerin in terminal using the following command:
```bash
sudo docker run --name flask-docker-app -p 5001:5001 flask-docker-app
```
2. Open [Postman](https://www.getpostman.com/downloads/) and type [http://0.0.0.0:5001](http://0.0.0.0:5001)</b> in the url field
3. Send a post request to the above mentioned URL with the following json object, where the key is called 'file' and the value is the relative path of your prediction file
    ```json
    {"file": "../data/file_name.csv"}
    ```
