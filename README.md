## Project Overview
This project provides a backend implemented in Python 
(using pip, FastAPI) and a frontend in Angular (using npm).
It includes configuration management via Pydantic,
a mock GPIO module for testing, and endpoints for handling
coffee machine actions. The idea is, that with the connection of the raspberry pi
board to the specific pins on some caffe machine board there is 
the opportunity to manage the machine remote. 

## Project Goal
Enable automated coffee brewing for some coffe machine (which is still
in the chose) orchestrated through simple API endpoints.
The configuration system allows easy customization of logging
levels and hardware pin usage.  

## Deployment
### Local Setup
 1. Clone the repository.
 2. Navigate to the backend folder and install dependencies:
    1. `cd backend`
    2. `pip install -r requirements.txt`
3. Run the backend:
   1. `python3 main.py`
   
4. Navigate to the frontend folder and install dependencies:
   1. `npm install`
   2. `npm start`
   
Open a browser at your local frontend URL `localhost:4200` and interact with the backend services.

###  Production
Use a docker compose to build frontend with proxy server based on
nginx and backend together:

`docker-compose build -d`


## Tech Stack
- Python, with FastAPI and Pydantic
- Angular (TypeScript, JavaScript)
- pip, npm
