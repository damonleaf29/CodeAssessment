# CodeAssessment
Code Assessment for BrightSign

Using Python 3.6.7

Required installs: 
python -m pip install requests

Run using command:
python3 CoordinatesAPI.py desiredIP  
EX: python3 CoordinatesAPI.py 66.45.44.0  // A random Colorado IP

Output:
The output of the getCoordinates function is a tuple of Floats. (latitude, longitude)
As for security, there are currently no checks for kinds of IP addresses we're recieving and if they're harmful or not. We could enable the security module in our get request by appending '&security = {1}', as recommended by https://ipstack.com/documentation.