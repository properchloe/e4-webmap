# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import folium


FILENAME = 'data/map1.html'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dir(folium)
    help(folium.Map)
    map1 = folium.Map(location=(35.61, -82.44), zoom_start=10)
    map1.save(FILENAME)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
