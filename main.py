import webbrowser
from tracker import Create_Map

if __name__ == '__main__':
    Create_Map()
    webbrowser.open('curr_location.html')