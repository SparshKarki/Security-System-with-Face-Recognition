from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget,QApplication,QWidget,QMainWindow,QPushButton,QLineEdit,QLabel,QVBoxLayout,QHBoxLayout,QFrame,QGridLayout,QComboBox,QTableWidget,QTableWidgetItem, QSplashScreen, QFileDialog
from PyQt5.QtWidgets import QHeaderView,qApp
import PyQt5.QtGui
from PyQt5.QtGui import *
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from recognize_faces_video import recognition
from encode_faces import TrainData
from video_recog import pushButton_handler

# QMainWIndow creates a main window who's class name is HomeScreen 
class HomeScreen(QMainWindow): 
    def __init__(self): # init is a constructor that allows the class to initialize the attributes, self shows that the work is been done in QMainWindow
        super().__init__()
        self.setWindowTitle("Criminal Detection System") #Window TitleBar
        self.setWindowIcon(QtGui.QIcon('c.png')) #Window Icon, imported from QTGUI
        self.center() #calls center function
        widget=QWidget() # Creates a widget area on the main window
        self.setFixedSize(640,480) #area size
        widget.setStyleSheet("background:grey")
        layout_horizontal=QHBoxLayout()
        menu_vertical_layout=QVBoxLayout()

        self.dataset=QPushButton("Dataset")
        self.recognize = QPushButton("Recognize")
        self.train = QPushButton("Train")
        self.about = QPushButton("About")

        menu_vertical_layout.setContentsMargins(0,0,0,0)
        menu_vertical_layout.setSpacing(0)
        self.dataset.setStyleSheet("width:200px;height:160px;font-size:20px;background:silver;color:black;font-weight:bold;border:1px solid white")
        self.recognize.setStyleSheet("width:200px;height:160px;font-size:20px;background:silver;color:black;font-weight:bold;border:1px solid white")
        self.train.setStyleSheet("width:200px;height:160px;font-size:20px;background:silver;color:black;font-weight:bold;border:1px solid white")
        self.about.setStyleSheet("width:200px;height:160px;font-size:20px;background:silver;color:black;font-weight:bold;border:1px solid white")


        self.dataset.clicked.connect(self.showDataset)
        self.recognize.clicked.connect(self.showRecognize)
        self.train.clicked.connect(self.showTrain)
        self.about.clicked.connect(self.showAbout)

        menu_frame=QFrame() #Add menu widgets on the left side of the horizontal box
        menu_vertical_layout.addWidget(self.dataset)
        menu_vertical_layout.addWidget(self.recognize)
        menu_vertical_layout.addWidget(self.train)
        menu_vertical_layout.addWidget(self.about)
        menu_vertical_layout.addStretch()
        menu_frame.setLayout(menu_vertical_layout)
        #menu_frame.setMinimumWidth(200)
        #menu_frame.setMaximumHeight(200)




        parent_vertical=QVBoxLayout() # Generate a vertical layout on right side of the main window
        parent_vertical.setContentsMargins(0,0,0,0)
        self.vertical_1=QVBoxLayout() #overlay a vertical box when the button is clicked
        self.addDataset()


        self.vertical_2=QVBoxLayout()
        self.addRecognize()

        self.vertical_3=QVBoxLayout()
        self.addtraining()

        self.vertical_4=QVBoxLayout()
        self.addAbout()

        self.vertical_5=QVBoxLayout()
        self.addIntro()


        self.frame_1=QFrame()
        self.frame_1.setMinimumWidth(420)
        self.frame_1.setMaximumWidth(420)
        self.frame_1.setMaximumHeight(480)
        self.frame_1.setMaximumHeight(480)
        self.frame_1.setLayout(self.vertical_1) # Set vertical_1 layout inside the frame_1

        self.frame_2=QFrame()
        self.frame_2.setMinimumWidth(420)
        self.frame_2.setMaximumWidth(420)
        self.frame_2.setMaximumHeight(480)
        self.frame_2.setMaximumHeight(480)
        self.frame_2.setLayout(self.vertical_2)

        self.frame_3=QFrame()
        self.frame_3.setMinimumWidth(420)
        self.frame_3.setMaximumWidth(420)
        self.frame_3.setMaximumHeight(480)
        self.frame_3.setMaximumHeight(480)
        self.frame_3.setLayout(self.vertical_3)


        self.frame_4=QFrame()
        self.frame_4.setMinimumWidth(420)
        self.frame_4.setMaximumWidth(420)
        self.frame_4.setMaximumHeight(480)
        self.frame_4.setMaximumHeight(480)
        self.frame_4.setLayout(self.vertical_4)

        self.frame_5=QFrame()
        self.frame_5.setMinimumWidth(420)
        self.frame_5.setMaximumWidth(420)
        self.frame_5.setMaximumHeight(480)
        self.frame_5.setMaximumHeight(480)
        self.frame_5.setLayout(self.vertical_5)

        parent_vertical.addWidget(self.frame_1)
        parent_vertical.addWidget(self.frame_2)
        parent_vertical.addWidget(self.frame_3)
        parent_vertical.addWidget(self.frame_4)
        parent_vertical.addWidget(self.frame_5)



        layout_horizontal.addWidget(menu_frame) # Add menu frame on the main window layout
        layout_horizontal.addLayout(parent_vertical) # Add parent vertical on the main window layout
        layout_horizontal.setContentsMargins(0,0,0,0)
        parent_vertical.setContentsMargins(0,0,0,0)
        parent_vertical.addStretch() # stretch the widget to adjust on the main window 
        #menu_vertical_layout.addStretch()
        layout_horizontal.addStretch()
        widget.setLayout(layout_horizontal) # set the layout of layout_horizontal on the main window

        # hide the windows which are not in use
        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_5.show()


        self.setCentralWidget(widget)

    def showAbout(self):
        self.dataset.setStyleSheet("width:200px;height:160px;font-size:20px;background:silver;color:black;font-weight:bold;border:1px solid white")
        self.recognize.setStyleSheet("width:200px;height:160px;font-size:20px;background:silver;color:black;font-weight:bold;border:1px solid white")
        self.train.setStyleSheet("width:200px;height:160px;font-size:20px;background:silver;color:black;font-weight:bold;border:1px solid white")
        self.about.setStyleSheet("width:200px;height:160px;font-size:20px;background:#6fbbd3;color:#fff;font-weight:bold;border:1px solid white")


        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.show()
        self.frame_5.hide()


    def showTrain(self):
        self.dataset.setStyleSheet("width:200px;height:160px;font-size:20px;background:silver;color:black;font-weight:bold;border:1px solid white")
        self.recognize.setStyleSheet("width:200px;height:160px;font-size:20px;background:silver;color:black;font-weight:bold;border:1px solid white")
        self.train.setStyleSheet("width:200px;height:160px;font-size:20px;background:#6fbbd3;color:#fff;font-weight:bold;border:1px solid white")
        self.about.setStyleSheet("width:200px;height:160px;font-size:20px;background:silver;color:black;font-weight:bold;border:1px solid white")


        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_4.hide()
        self.frame_3.show()
        self.frame_5.hide()


    def showRecognize(self):
        self.dataset.setStyleSheet("width:200px;height:160px;font-size:20px;background:silver;color:balck;font-weight:bold;border:1px solid white")
        self.recognize.setStyleSheet("width:200px;height:160px;font-size:20px;background:#6fbbd3;color:#fff;font-weight:bold;border:1px solid white")
        self.train.setStyleSheet("width:200px;height:160px;font-size:20px;background:silver;color:black;font-weight:bold;border:1px solid white")
        self.about.setStyleSheet("width:200px;height:160px;font-size:20px;background:silver;color:black;font-weight:bold;border:1px solid white")

        self.frame_1.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_2.show()
        self.frame_5.hide()


    def showDataset(self):
        self.dataset.setStyleSheet("width:200px;height:160px;font-size:20px;background:#6fbbd3;color:#fff;font-weight:bold;border:1px solid white")
        self.recognize.setStyleSheet("width:200px;height:160px;font-size:20px;background:silver;color:black;font-weight:bold;border:1px solid white")
        self.train.setStyleSheet("width:200px;height:160px;font-size:20px;background:silver;color:black;font-weight:bold;border:1px solid white")
        self.about.setStyleSheet("width:200px;height:160px;font-size:20px;background:silver;color:black;font-weight:bold;border:1px solid white")

        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_1.show()
        self.frame_5.hide()


    def addDataset(self): # Function to add dataset to the frame
        vertical_layout = QVBoxLayout()
        frame = QFrame()
        frame.setStyleSheet("background-color:white;")


        horizontal = QHBoxLayout()
        label = QLabel("Dataset")
        label.setStyleSheet("background-color:#6fbbd3;color:#fff;font-size:40px;text-align:center;border: 1px solid black;")
        label.setAlignment(Qt.AlignCenter)
        horizontal.addWidget(label)
        vertical_layout.addLayout(horizontal)
        self.vertical_1.addWidget(frame)
        self.vertical_1.addStretch()
        frame.setLayout(vertical_layout)

        horizontalframe = QHBoxLayout()
        vertical_layout.addLayout(horizontalframe)

        def getText():
            text, okPressed = QInputDialog.getText(self, "Get text","Your name:", QLineEdit.Normal, "")
            if okPressed and text != '':
                path = 'dataset/' + text 
                try:
                    os.mkdir(path)
                except OSError:
                    print ("Creation of the directory %s failed" % path)
                    self.close_application()
                else:
                    print ("Successfully created the directory %s " % path)
                    import cv2
                    size = 4
                    webcam = cv2.VideoCapture(0) #Use camera 0

                    classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                    while True:
                        (rval, im) = webcam.read()
                        im=cv2.flip(im,1,0)
                        mini = cv2.resize(im,(int(im.shape[1] / size), int(im.shape[0] / size)))

                        faces = classifier.detectMultiScale(mini)
                        for f in faces:
                            (x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
                            cv2.rectangle(im, (x, y), (x + w, y + h),(0,255,0),thickness=4)
                            sub_face = im[y:y+h, x:x+w]
                            FaceFileName = "dataset/" + text +"/face_" + str(y) + ".jpg"
                            cv2.imwrite(FaceFileName, sub_face)

                        cv2.imshow('click picture: Press Escape key to exit',   im)
                        key = cv2.waitKey(10)
                        if key == 27:
                            break
                    cv2.destroyAllWindows()

        def close_application():
            choice = QtWidgets.QMessageBox.question(self, 'Extract!',
                                                "Name Already Exists. Try again? ",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                self.getText()
            else:
                pass

        def folder():
            dirname = os.path.dirname(os.path.abspath(__file__))
            filename = QFileDialog.getOpenFileName(None, 'Dataset', os.path.join(dirname, 'dataset/'), 'All Files(*.*)')

        horizontal1 = QHBoxLayout()
        add = QPushButton("create dataset")
        add.clicked.connect(getText)
        openfile = QPushButton("Open Folder")
        openfile.clicked.connect(folder)
        horizontal1.addWidget(add)
        horizontal1.addWidget(openfile)
        vertical_layout.addLayout(horizontal1)

    def addRecognize (self):
        vertical_layout = QVBoxLayout()
        frame = QFrame()
        frame.setStyleSheet("background-color:white;")


        horizontal = QHBoxLayout()
        label = QLabel("Recognize")
        label.setStyleSheet("background-color:#6fbbd3;color:#fff;font-size:40px;text-align:center;border: 1px solid black;")
        label.setAlignment(Qt.AlignCenter)
        horizontal.addWidget(label)
        vertical_layout.addLayout(horizontal)
        self.vertical_2.addWidget(frame)
        self.vertical_2.addStretch()
        frame.setLayout(vertical_layout)
        horizontal1 = QHBoxLayout()
        add = QPushButton("Start recognition")
        add.clicked.connect(recognition)
        openfile1 = QPushButton("Browse Video")
        openfile1.clicked.connect(pushButton_handler)


        horizontal1.addWidget(add)
        horizontal1.addWidget(openfile1)
        vertical_layout.addLayout(horizontal1)

    
    def addtraining(self):
        vertical_layout = QVBoxLayout()
        frame = QFrame()
        frame.setStyleSheet("background-color:white;")


        horizontal = QHBoxLayout()
        label = QLabel("Training")
        horizontal.addWidget(label)
        label.setStyleSheet("background-color:#6fbbd3;color:#fff;font-size:40px;text-align:center;border: 1px solid black;")
        label.setAlignment(Qt.AlignCenter)
        vertical_layout.addLayout(horizontal)
        self.vertical_3.addWidget(frame)
        self.vertical_3.addStretch()
        frame.setLayout(vertical_layout)



        horizontal1 = QHBoxLayout()
        add = QPushButton("Start training")
        add.clicked.connect(TrainData)
        horizontal1.addWidget(add)
        vertical_layout.addLayout(horizontal1)

    def addAbout(self):
        vertical_layout = QVBoxLayout()
        frame = QFrame()
        frame.setStyleSheet("background-color:white;")


        horizontal = QHBoxLayout()
        label = QLabel("About")
        label.setStyleSheet("background-color:#6fbbd3;color:#fff;font-size:40px;text-align:center;border: 1px solid black;")
        label.setAlignment(Qt.AlignCenter)
        horizontal.addWidget(label)
        vertical_layout.addLayout(horizontal)
        self.vertical_4.addWidget(frame)
        self.vertical_4.addStretch()
        frame.setLayout(vertical_layout)

        horizontal1 = QHBoxLayout()
        lableImage = QLabel()
        pixmap1 = QPixmap("criminal.jpg")
        lableImage.setPixmap(pixmap1)
        pixmap = pixmap1.scaled(390,380)
        lableImage.setPixmap(pixmap)
        lableImage.setMinimumSize(1, 1)
        horizontal1.addWidget(lableImage)
        vertical_layout.addLayout(horizontal1)


        

    def addIntro(self):
        vertical_layout = QVBoxLayout()
        frame = QFrame()
        frame.setStyleSheet("background-color:white;")

        horizontal1 = QHBoxLayout()
        lableImage = QLabel()
        pixmap1 = QPixmap("Webcam_grayscale.jpg")
        lableImage.setPixmap(pixmap1)
        pixmap = pixmap1.scaled(lableImage.width(), lableImage.height())
        lableImage.setPixmap(pixmap)
        lableImage.setMinimumSize(1, 1)
        horizontal1.addWidget(lableImage)
        vertical_layout.addLayout(horizontal1)

        horizontal = QHBoxLayout()
        label = QLabel("Criminal")
        label.setStyleSheet("background-color:Red;font-size:40px;color:white;text-align:center;border: 1px solid black;")
        label.setAlignment(Qt.AlignCenter)
        horizontal.addWidget(label)
        vertical_layout.addLayout(horizontal)
        self.vertical_5.addWidget(frame)
        self.vertical_5.addStretch()
        frame.setLayout(vertical_layout)

        horizontalA = QHBoxLayout()
        labelA = QLabel("Detection")
        labelA.setStyleSheet("background-color:#6fbbd3;font-size:40px;color:white;text-align:center;border: 1px solid black;")
        labelA.setAlignment(Qt.AlignCenter)
        horizontalA.addWidget(labelA)
        vertical_layout.addLayout(horizontalA)

        horizontalB = QHBoxLayout()
        labelB = QLabel("System")
        labelB.setStyleSheet("background-color:Green;font-size:40px;color:white;text-align:center;border: 1px solid black;")
        labelB.setAlignment(Qt.AlignCenter)
        horizontalB.addWidget(labelB)
        vertical_layout.addLayout(horizontalB)


    def center(self):
        qr = self.frameGeometry() #Keeps the software window in the center of the screen

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())


if __name__ == "__main__":
    import sys, time
    app = QApplication(sys.argv) # Generate a Qapplication, in this case the main window
    home = HomeScreen() # home is the object of the class HomeScreen
    splash_image_path = os.path.join(os.path.dirname(__file__),
                                     'loading.png')
    splash_image = QPixmap(splash_image_path)
    splash_screen = QSplashScreen(splash_image, Qt.WindowStaysOnTopHint)
    splash_screen.setMask(splash_image.mask())
    splash_screen.show()
    app.processEvents()
    splash_screen.finish(home)
    home.show()
    sys.exit(app.exec_()) # Exectues the entire main window
