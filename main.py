# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import folium
import csv


FILENAME = 'data/map1.html'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dir(folium)
    help(folium.Map)
    map1 = folium.Map(location=(35.61, -82.44), zoom_start=10)
    map1.save(FILENAME)

    with open("data/volcanoes.tsv", 'r') as fv:
        my_sniffer = csv.Sniffer().sniff(fv.read())
        fv.seek(0)
        my_reader = csv.DictReader(fv, dialect=my_sniffer)
        rows = []
        for row in my_reader:
            rows.append(row)
        print(rows[0])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
