
from PyQt6.QtPrintSupport  import QPrinter
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class PrintPdf:
  
  def __init__(self, views,exponent = None):
    self.views = views

  def execute(self):
      qfd = QFileDialog()
      filename, _  = QFileDialog.getSaveFileName(qfd, "Exporter PDF", None, "PDF files (.pdf);;All Files()")
      if filename:
          if QFileInfo(filename).suffix() == "":
              filename += ".pdf"
          self.print_widget(self.views, filename)

  def print_widget(self, views, filename):
      printer = QPrinter()
      painter = QPainter()

      printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
      printer.setOutputFileName(filename)
      printer.setFullPage(True)
      printer.setPageOrientation(QPageLayout.Orientation.Landscape)
      printer.setPageSize(QPageSize(QPageSize.PageSizeId.A3))
      
      painter.begin(printer)
      views[0].scene.render(painter)
      printer.newPage()
      printer.setPageSize(QPageSize(QPageSize.PageSizeId.A4))
      views[1].scene.render(painter)
      painter.end()
