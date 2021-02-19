# Greensteam - How to start the project
1. Download repo to local storage
2. Go to repo directory then run command _docker build -t [name-of-the-image] ._
3. Once image is built run _docker run -d --name [name-of-the-container] -p 80:80 [name-of-the-image]_

Once container is running open web browser and go to _http://127.0.0.1/docs_ <- you can try and execute rest commands from GUI

Under _http://127.0.0.1/docs _**schemas:passenger**_ you will find structure of json request. Required fields are marked with red star.

In order to send passenger data _**post** http://127.0.0.1/passenger_

In order to retrive last posted passenger risk _**get** http://127.0.0.1/passenger/risk_

In order to retrive list of posted passengers _**get** http://127.0.0.1/passengers_ Passengers also contains information about their risk once it was assessed. 


**Further improvements**
1. Check whatever values are in range (range definition) [age, class number]
2. Autofill required values 
3. Implementation of list import (more than one passenger at a time)
4. Improved error handling
5. Lightweight DB for passengers
6. Depending on nubmer of input data use another ML method
