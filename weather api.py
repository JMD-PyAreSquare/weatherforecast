import requests
import datetime as dt
from time import strftime
from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
api_url = "http://api.openweathermap.org/data/2.5/weather?"
yn = input('Do you have an API key for openweathermap.org? [Yes/No]')
if yn == 'Yes':
    api_key = input("Type the API key here. Don't include quotation marks.")
    city = input('What city do you want to know about?')

    def kelvin_to_celsius_fahrenheit(kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) + 32
        return celsius, fahrenheit

    def webpage(a, b, c, d, e, f, g, x, r, z):
        html = """
                <!DOCTYPE html>
                <html>
                <head>
                <style>
                div {
                    background-color: lightblue;
                    width: 300px;
                    border: 15px solid skyblue;
                    padding: 50px;
                    }

                h1 {
                    text-align: center;
                    font-family: "Source Sans Pro", sans-serif;
                    font-weight: normal;
                }

                p {
                    text-align: center;
                    font-family: "Source Sans Pro", sans-serif;
                    font-weight: normal;
                }
                </style>
                <title>Weather Station</title>
                <meta http-equiv="refresh" content="10">
                </head>
                <body>
                <center>
                """ + f"""
                <h1>Weather Forecast For {city} on {strftime('%x')}</h1>
                <p>This website should auto-refresh/update once every 10 seconds</p>
                <div>
                <p style="font-family:arial">{a}</p>
                <p style="font-family:arial">{b}</p>
                <p style="font-family:arial">{c}</p>
                <p style="font-family:arial">{d}</p>
                <p style="font-family:arial">{e}</p>
                <p style="font-family:arial">{f}</p>
                <p style="font-family:arial">{g}</p>
                <p style="font-family:arial"> The current time in <i>your</i> area is {x}</p>
                </div>
                <!--{r}-->
                </center>
                </body>
                </html>
                """
        return str(html)

    class PyHTTP(BaseHTTPRequestHandler):
        def do_GET(self):
            url = api_url + 'appid=' + api_key + '&q=' + city
            response = requests.get(url).json()
            debugtime = response
            temp_kelvin = response['main']['temp']
            temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
            feels_like_kelvin = response['main']['feels_like']
            feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
            wind_speed = response['wind']['speed']
            humidity = response['main']['humidity']
            description = response['weather'][0]['description']
            sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
            sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
            act = dt.datetime.utcfromtimestamp(response['sys']['id']+response['timezone'])
            reading_a = f'Temperature in {city}: {temp_celsius:.2f}*C or {temp_fahrenheit:.2f}*F'
            reading_b = f'Temperature in {city} feels like: {feels_like_celsius:.2f}*C or {feels_like_fahrenheit:.2f}*F'
            reading_c = f'Humidity in {city}: {humidity:}%'
            reading_d = f'Wind Speed in {city}: {wind_speed:}m/s'
            reading_e = f'General Weather in {city}: {description}'
            reading_f = f'Sun rises in {city} at {sunrise_time} local time'
            reading_g = f'Sun sets in {city} at {sunset_time} local time'
            rand_x = strftime('%I:%M:%S %p')
            html = webpage(a=reading_a,b=reading_b,c=reading_c,d=reading_d,e=reading_e,f=reading_f,g=reading_g,x=rand_x,r=debugtime,z=act)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(html,'utf-8'))

        def do_POST(self):
            url = api_url + 'appid=' + api_key + '&q=' + city
            response = requests.get(url).json()
            temp_kelvin = response['main']['temp']
            temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
            feels_like_kelvin = response['main']['feels_like']
            feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
            wind_speed = response['wind']['speed']
            humidity = response['main']['humidity']
            description = response['weather'][0]['description']
            sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
            sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
            reading_a = f'Temperature in {city}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F'
            reading_b = f'Temperature in {city} feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F'
            reading_c = f'Humidity in {city}: {humidity:}%'
            reading_d = f'Wind Speed in {city}: {wind_speed:}m/s'
            reading_e = f'General Weather in {city}: {description}'
            reading_f = f'Sun rises in {city} at {sunrise_time} local time'
            reading_g = f'Sun sets in {city} at {sunset_time} local time'
            rand_x = strftime('%I:%M:%S %p')
            html = webpage(a=reading_a,b=reading_b,c=reading_c,d=reading_d,e=reading_e,f=reading_f,g=reading_g,x=rand_x)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers
            self.wfile.write(bytes(html,'utf-8'))

    server = HTTPServer((HOST, PORT), PyHTTP)
    print('server started!')
    server.serve_forever()
    for i in range(2):
        print(i)
    server.server_close()
    print('server stopped.')      

elif yn == 'No':
    print('Go to openweathermap.org.')
    print('Create a free account and verify the email.')
    print('Go to the dropdown menu that is under your name.')
    print('Click on the My Api Keys section')
