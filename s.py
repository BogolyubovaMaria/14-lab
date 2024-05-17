import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtGui import QIcon
from dost1 import Ui_MainWindow
from PyQt5.QtCore import QUrl

class Travel(QtWidgets.QMainWindow):
    def __init__(self):
        super(Travel,self).__init__()
        self.dost1=Ui_MainWindow()
        self.dost1.setupUi(self)
        self.init__UI()
        self.setPlaceholderText()
        self.Button()

    def init__UI(self):
        self.setWindowTitle('Приложение для путешествий')
        self.setWindowIcon(QIcon('solnce.png'))

    def setPlaceholderText(self):
        self.dost1.verxnee.setPlaceholderText('Здесь должен быть город')
        self.dost1.nizhnee.setPlaceholderText('...')

    def Button(self):
        self.dost1.pushButton.clicked.connect(self.get_landmark)
        self.dost1.commandLinkButton.clicked.connect(self.open_wikipedia)
        self.dost1.commandLinkButton_2.clicked.connect(self.open_wikipedia_cities)


    def get_landmark(self):
        city = self.dost1.verxnee.text()
        # Создаем простой словарь (можно заменить на список или другую структуру данных)
        landmarks = {
            "Moscow": "Kremlin",
            "Paris": "Eiffel Tower",
            "Rome": "Colosseum",
            "Tokyo": "Sensoji Temple",
            "New York": "Statue of Liberty",
            "Cairo": "Pyramids of Giza",
            "Barcelona": "Sagrada Familia",
            "Sydney": "Sydney Opera House",
            "Berlin": "Brandenburg Gate",
            "Dubai": "Burj Khalifa",
            "Amsterdam": "Rijksmuseum",
            "Athens": "Parthenon",
            "Venice": "St. Mark's Basilica",
            "Toronto": "CN Tower",
            "Washington": "White House"
            # и так далее
        }
        # Получаем достопримечательность из словаря
        landmark = landmarks.get(city, "Достопримечательность не найдена")
        # Выводим полученную достопримечательность в поле "nizhnee"
        self.dost1.nizhnee.setText(landmark)

    def open_wikipedia(self):
        city = self.dost1.verxnee.text()
        country = ""

        city_to_country = {
            "Paris": "France",
            "London": "United_Kingdom",
            "Rome": "Italy",
            "New York": "United_States",
            "Moscow": "Russia",
            "Tokyo": "Japan",
            "Barcelona": "Spain",
            "Sydney": "Australia",
            "Berlin": "Germany",
            "Dubai": "United Arab Emirates",
            "Amsterdam": "Netherlands",
            "Athens": "Greece",
            "Venice": "Italy",
            "Toronto": "Canada",
            "Washington": "United_States"
        }
        if city in city_to_country:
            country = city_to_country[city]

        if country:
            url = f"https://en.wikipedia.org/wiki/{country}"
            QtGui.QDesktopServices.openUrl(QUrl(url))
        else:
            self.dost1.nizhnee.setText("Страна не найдена")

    def open_wikipedia_cities(self):
        city = self.dost1.verxnee.text()
        city_url = "https://en.wikipedia.org/wiki/" + city.replace(" ", "_")
        QtGui.QDesktopServices.openUrl(QUrl(city_url))



app =QtWidgets.QApplication([])
application=Travel()
application.show()
sys.exit(app.exec())




