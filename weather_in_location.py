import scrollphathd as sphd
import tkinter
import tkintermapview
import requests
import time
import api_key

location = tkinter.Tk()
location.title("Select location")
location.geometry("800x600")
location.resizable(False, False)

def select_location(coordinates):
    global latitude
    global longitude
    coordinates_simple = tuple([float("{0:.2f}".format(n)) for n in coordinates])
    latitude = coordinates_simple[0]
    longitude = coordinates_simple[1]
    parameters = {"lat": latitude, "lon": longitude}
    location.destroy()
    while True:
        appid = api_key.API_KEY_SERVICE
        address = "https://api.openweathermap.org/data/2.5/weather?appid="+appid
        response = requests.get(address, params=parameters)
        weather_data = ((response.json().get("main")))
        temperature_celsius = (weather_data.get("temp") - 273.15)
        temperature_display = str(round(temperature_celsius, 1))+" C"
        sphd.clear()
        sphd.set_brightness(0.5)
        sphd.write_string(temperature_display)
        sphd.show()
        sphd.scroll(1)
        time.sleep(10)

map_widget = tkintermapview.TkinterMapView(location, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
map_widget.set_position(51.77674, 19.45469)
map_widget.set_zoom(50)
map_widget.add_right_click_menu_command(label="Set location", command=select_location, pass_coords=True)

location.mainloop()
