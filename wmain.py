from wlogic import *

def main():
    """"
    Create the application, open the main window, and run's the program. 
    """""
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == '__main__':
    main()