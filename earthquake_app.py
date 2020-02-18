import requests
import json
from tkinter import *
from tkinter import ttk

def get_earth_info(*args):
    try:
        #place_list = []
        start_time = str(starttime.get())
        end_time = str(endtime.get())
        lati = str(latitude.get())
        longi = str(longitude.get())
        max_rad = str(maxradiuskm.get())
        min_mag = str(minmagnitude.get())
        url = "https://earthquake.usgs.gov/fdsnws/event/1/query?"
        parameters = {"format": "geojson", "starttime": start_time, "endtime": end_time, "latitude": lati, "longitude": longi, "maxradiuskm": max_rad, "minmagnitude": min_mag}
        response = requests.get(url, headers = {"Accept": "application/json"}, params=parameters)
        data = response.json()
        for item in data["features"]:
            text_box_place.insert("end", item["properties"]["title"])
            text_box_place.insert("end", "\n")
            #place_list.append(item["properties"]["place"])
        #place.set(place_list)
    except ValueError:
        pass


root = Tk()
root.title("Earthquake info")

main_window = ttk.Frame(root)
main_window.grid(column = 0, row = 0)

starttime = StringVar()
endtime = StringVar()
latitude = StringVar()
longitude = StringVar()
maxradiuskm = StringVar()
minmagnitude = StringVar()
place = StringVar()

ttk.Label(main_window, text="Hello! This is earthquake app.").grid(column=0, row=0, columnspan=2)

ttk.Label(main_window, text="Enter start time").grid(column=0, row=1, sticky=(W))
param_starttime = ttk.Entry(main_window, width=10, textvariable=starttime)
param_starttime.grid(column=1, row=1, sticky=(W))

ttk.Label(main_window, text="Enter end time").grid(column=0, row=2, sticky=(W))
param_endtime = ttk.Entry(main_window, width=10, textvariable=endtime)
param_endtime.grid(column=1, row=2, sticky=(W))

ttk.Label(main_window, text="Enter latitude").grid(column=0, row=3, sticky=(W))
param_latitude = ttk.Entry(main_window, width=10, textvariable=latitude)
param_latitude.grid(column=1, row=3, sticky=(W))

ttk.Label(main_window, text="Enter longitude").grid(column=0, row=4, sticky=(W))
param_longitude = ttk.Entry(main_window, width=10, textvariable=longitude)
param_longitude.grid(column=1, row=4, sticky=(W))

ttk.Label(main_window, text="Enter max radius in km").grid(column=0, row=5, sticky=(W))
param_maxradiuskm = ttk.Entry(main_window, width=10, textvariable=maxradiuskm)
param_maxradiuskm.grid(column=1, row=5, sticky=(W))

ttk.Label(main_window, text="Enter min magnitude").grid(column=0, row=6, sticky=(W))
param_minmagnitude = ttk.Entry(main_window, width=10, textvariable=minmagnitude)
param_minmagnitude.grid(column=1, row=6, sticky=(W))

ttk.Label(main_window, text="Earthquake place and magnitude").grid(column=0, row=8, columnspan=2)
text_box_place = Text(main_window, width=50, height=10)
text_box_place.grid(column=0, row=9, columnspan=2)
#list_box_1 = Listbox(main_window, listvariable=place)
#list_box_1.grid(column=0, row=8, columnspan=2, sticky=(W, E))
# ttk.Label(main_window, textvariable=place).grid(column=0, row=8, sticky=(W))

ttk.Button(main_window, text="Get earthquake info", command=get_earth_info).grid(column=0, row=7, columnspan=2)

root.mainloop()
