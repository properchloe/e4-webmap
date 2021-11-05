# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import folium
import csv


FILENAME = 'data/map1.html'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    map1 = folium.Map(location=(35.61, -82.44), zoom_start=10)

    with open("data/volcanoes.tsv", 'r') as fv:
        my_sniffer = csv.Sniffer().sniff(fv.read())
        fv.seek(0)
        my_reader = csv.DictReader(fv, dialect=my_sniffer)
        rows = []
        for row in my_reader:
            if "?" not in row["Type"] and "Historical" not in row['Status'] and "Unnamed" not in row["Volcano Name"]:
                if 'Latitude' in row.keys() and 'Longitude' in row.keys():
                    # print(f"Name: {row['Volcano Name']}\tLatitude: {row['Latitude']}\tLongitude: {row['Longitude']}")
                    rows.append(row)

    for row in rows:
        # print(f"Name: {row['Volcano Name']}\tLatitude: {row['Latitude']}\tLongitude: {row['Longitude']}")
        marker = folium.Marker(location=[row['Latitude'], row['Longitude']], popup=row['Volcano Name'], icon=folium.Icon(color='darkred'))
        marker.add_to(map1)

    map1.save(FILENAME)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
