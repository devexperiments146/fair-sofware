from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from view.tableModel import TableModel
import pandas as pd

class DisplayProjectView(QWidget):

    def __init__(self,store,appController,projectController,parameterController):
        super().__init__()
        self.appController = appController
        self.projectController = projectController
        self.parameterController = parameterController
        label = QLabel("Projets")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.appController = appController
        self.projects = store.getProjects()

        project = QtWidgets.QTableView()
        
        rows = []
        datas = []
        for i in range(0,len(self.projects),1):
            datas.append([self.projects[i].name])
            rows.append(self.projects[i].id)
         
        data = pd.DataFrame(datas, columns = ['Name'], index=rows)   
        self.model = TableModel(data)
        
        project.setModel(self.model)
        
        layout.addWidget(project)
        project.resizeRowsToContents()
        
        bouton = QPushButton("Fermer")
        bouton.clicked.connect(self.close)
        layout.addWidget(bouton)
        
        self.setLayout(layout)
        project.doubleClicked.connect(self.select_project)

    def select_project(self, mi):
        if mi :
            selectedProject = self.projects[mi.row()]
            self.projectController.loadProject(selectedProject)
            self.parameterController.updateParameter("CURRENT_PROJECT",str(selectedProject.id))

    def close(self):
        self.appController.goBack()