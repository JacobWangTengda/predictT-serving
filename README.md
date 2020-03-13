# predictT-serving


### Description
This repository hosts the code for a local flask server written in python, which turns a trained time series prediction model into a microservice. This microservice will eventually be integrated into the predictT platform and consumed by other parts of the projects.

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
    ├── pics                                # pictures used in the report
    |   ├── Dockerfile.png     
    |   ├── Postman.png 
    |   ├── .....
    ├── app.py                              # Flask Server Code
    ├── Dockerfile                          # Docker File
    └── README.md
    
### Prediction File Format
* Must be in csv format
* Dates should be in the first column
* Values should be in the second column

<br/>Please check the files in the data folder for more details
### Usage
1. Download [Docker](https://www.docker.com/products/docker-desktop) if necessary
2. Clone the repository to your local system
3. Go to terminal and Build a docker image based on the Dockerfile included in this repository
    ```bash
    sudo docker build --tag flask-docker-app .
    ```
4. Run the docker image in terminal using the following command:
    ```bash
    sudo docker run --name flask-docker-app -p 5001:5001 flask-docker-app
    ```
5. Open [Postman](https://www.getpostman.com/downloads/) and type ```http://0.0.0.0:5001``` in the url field
6. Send a post request to the above mentioned URL with the following json object, where the key is called 'file' and the value is the relative path of your prediction file
    ```json
    {"file": "data/file_name.csv"}
    ```
    
------------------------------------------------------------------------------------------------------------------------------

# STAT359 Final Report

### Summary of Work
Throughout the quarter, I’ve been working on the model deployment part of the project. Listed below are the individual components of my project and they will be illustrated in more detail in the next section.
-	Train prediction model and write the flask predicT application
-	Containerize the application using docker and run the container locally
-	Deploy the docker container to the cloud providers.

Model deployment is usually one of the last parts of a data science lifecycle, which is also the case in this predicT project. In order to get the most value out of a machine learning model, it is important to deploy them into production so that a business can start to utilize the model and make predictions. Meanwhile, model deployment is one of the most difficult process of gaining value from machine learning as it requires knowledge from multiple fields, including data science, IT infrastructure, software engineering as well as business domain knowledge. 

Lack of portability used to be a huge issue where the software cannot be migrated easily from one computing environment to another. A recently developed product called docker and the concept of containerization has come into place to address this issue. As I have no prior exposure to this product and its relevant terminology, it took me quite some time to understand what it is and how it works. Intuitively at a higher level, I would like to describe each software as a parcel that needs to be carried around and the computing devices as cargo ships. Docker is then a crane which uses the containers to move the parcels across different cargo ships. It ensures that containers are safely isolated so that they can be placed properly regardless of the type of the cargo ship. 

In a word, it is truly an enriching experience to learn to use docker as well as other necessary tools and concepts in the field of model deployment. I believe they are of great value to my future career.


### Reproduction of Work
#### Model Training
- Dataset: [Energy Consumption Data](https://www.kaggle.com/robikscube/hourly-energy-consumption/version/3)
- Generated Features:
    * Hour
    * Day
    * Month
    * Quarter
    * Year
    * Day of Month
    * Week of Year
- Model: [XGboost](https://xgboost.readthedocs.io/en/latest/)
- Validation Metods:
    * K-fold cross validation
    * Train-test split

<br/> The trained model is saved as a pickle file so that it could be imported by the flask application later.
#### Flask Application with the prediction function
The code for the predicT flask app is modified from a sample flask file provide by the teaching assistant. You can access the file [here](https://drive.google.com/open?id=1sSt_ZzjufZLqpMCqmg6xFxXuK9GRR2n0).  

#### Build and Run Docker Image
I followed an online [tutorial](https://www.geeksforgeeks.org/dockerize-your-flask-app/) to write docker files and create docker images. A screenshot of the docker file is shown below:
![picture](https://github.com/JacobWangTengda/predictT-serving/blob/master/pics/Dockerfile.png)
<br/>This docker file will first pull python images from the docker registry and copy all the files in the application folder, where the flask code is stored. It is required to create a requirement.txt file with all the necessary packages and its version so that the docker file can ‘pip’ install all the dependencies of the application. The docker file then exposes port 5001, which the application sits on, and executes the ```python app.py``` command.

After the docker file is written, you can build a docker image from this file. This docker image will create a docker container during runtime where the application is encapsulated inside. For more detail, please see the Usage section of the readme file.
#### Make a request to the predict function
You can make a HTTP request to the flask application once it is up and running. The input of the request is a csv file with the raw data and the output contains the predicted value. To make the POST request, you need to download Postman beforehand. Since the application is running locally and listens to port 5001, specify the host URL as ```http://0.0.0.0:5001```. The body of the request is a json object as shown in the screenshot below. The value of the entry is the path to the prediction file in the repository. Please refer to the screenshot below for more details.

<br/>![](https://github.com/JacobWangTengda/predictT-serving/blob/master/pics/postman.png)

#### Deploy Docker image to the cloud
The previous steps only run the application locally. With the increasing popularity of cloud computing, we would also like to explore the possibility to utilize the services from major cloud provides and deploy the application to the cloud. In the second half of this quarter, I’ve tried to deploy docker images to Google Cloud Platform (GCP) and the Amazon Web Services (AWS). 
##### Cloud Provider 1: Google Cloud Platform (GCP)
GCP is nice enough to provide a comprehensive tutorial on how to deploy a containerized application, which can be found [here](https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app). It is straightforward to follow and includes all the step needed including how to package a web application in a docker image, and run that container on a Google Kubernetes Engine (GKE) cluster as a load-balanced set of replicas that can scale to the needs of users. GCP also provides a cloud shell/terminal that I find to be rather user-friendly. 

<br>![](https://github.com/JacobWangTengda/predictT-serving/blob/master/pics/GCP.png)
##### Cloud Provider 2: AWS ECR
I’ve been researching on the Amazon Elastic Container Service (ECR), which is a highly scalable, high performance container management service that supports Docker containers and allows you to easily run application on a managed cluster of Amazon EC2 instances. I followed this [tutorial](https://towardsdatascience.com/how-to-deploy-a-docker-container-python-on-amazon-ecs-using-amazon-ecr-9c52922b738f) and created a containerized static webpage. Given more time, the same procedure can be replicated on the flask predicT application. 


### Future Insights
