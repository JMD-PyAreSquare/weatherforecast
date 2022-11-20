# weather station project
This is a simple weather station project which uses an API token/key to acess openweathermap.org and requests information on the given city.

## how to get an API key
I've already provided instructions on how to get an API key for openweathermap.org in the 
`
weather api.py
`
file, but here are the instructions in case you didn't know:
- go to https://www.openweathermap.org
- sign up for an account (It's 100% free!)
- confirm your email address
- go to the `My API keys` section under your name (Top right)
- copy and pase the API key in the `weather api.py` project when asked

## how it works
once given an API key and a city, the file will send a request to the openweathermap servers and then decode the response into a way that the user can understand. This information will then be hosted on a local webpage that is hosted on the users machine at `localhost:9999`. After that the program makes a way for the browser to send a get request to the webpage without crashing.
