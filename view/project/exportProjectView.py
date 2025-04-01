
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class ExportProjectView(QWidget):

    def __init__(self,store,appController,projectController):
        super().__init__()
        self.appController = appController
        self.projectController = projectController
        label = QLabel("Exporter projet")   
        layout = QFormLayout()
        layout.addWidget(label)

        comboboxProjects= []
        self.projects = store.getProjects()
        for i in range(0,len(self.projects),1):
            comboboxProjects.append(self.projects[i].getName())
        self.project = QComboBox()
        self.project.addItems(comboboxProjects)
        self.project.activated.connect(self.check_index_project)
        layout.addRow("Projet :", self.project )

        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validProject)
        layout.addRow(cancelButton, validButton)

        self.setLayout(layout)
        
    def close(self):
        self.appController.goBack()


    def check_index_project(self, index):
        self.selectedProject = self.projects[index]

    def validProject(self):
        qfd = QFileDialog()
        path = "C:\\"
        filter = "*.json"
        filename, _  = QFileDialog.getSaveFileName(qfd, "Exporter fichier", path, filter)
        self.projectController.exportProject(self.selectedProject,filename)