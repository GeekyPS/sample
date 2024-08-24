import sys
import requests
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QTextBrowser
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl
from data import company_testimonials, save_testimonials  # Import from data.py

class DataFetcher(QThread):
    data_fetched = pyqtSignal()

    def run(self):
        # Simulate data fetching
        for _ in company_testimonials:
            QThread.sleep(1)  # Simulate a delay for each item
            self.data_fetched.emit()

class TestimonialApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Company Testimonials")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout for the main window
        self.layout = QVBoxLayout(self.central_widget)

        # Table widget to display testimonials
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Company", "Web Pages"])
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)  # Make cells non-editable
        self.layout.addWidget(self.table_widget)
        
        # Form for adding new company and URL
        self.form_layout = QFormLayout()
        
        self.company_input = QLineEdit()
        self.url_input = QLineEdit()
        
        self.form_layout.addRow(QLabel("Company:"), self.company_input)
        self.form_layout.addRow(QLabel("URL:"), self.url_input)
        
        self.add_button = QPushButton("Add Testimonial")
        self.add_button.clicked.connect(self.add_testimonial)
        
        self.form_layout.addWidget(self.add_button)
        
        self.layout.addLayout(self.form_layout)

        # Start data fetching in a separate thread
        self.data_fetcher = DataFetcher()
        self.data_fetcher.data_fetched.connect(self.update_table_widget)
        self.data_fetcher.start()

        # Initial call to update the table widget
        self.update_table_widget()

    def open_link(self, url):
        QDesktopServices.openUrl(QUrl(url))

    def update_table_widget(self):
        self.table_widget.setRowCount(0)
        for testimonial in company_testimonials:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)
            self.table_widget.setItem(row_position, 0, QTableWidgetItem(testimonial['company']))

            # Create a QTextBrowser with clickable links for URLs
            urls = [f'<a href="{url}">{url}</a>' for url in testimonial['web_url']]
            urls_text = "<br>".join(urls)
            text_browser = QTextBrowser()
            text_browser.setHtml(urls_text)
            text_browser.setOpenExternalLinks(True)  # Allows external links to open in the browser
            
            # Adjust row height based on the content of the QTextBrowser
            text_browser.setFixedHeight(max(50, len(urls) * 30))  # Adjust 30 pixels per URL as needed
            
            self.table_widget.setCellWidget(row_position, 1, text_browser)

        # Set minimum row height
        self.table_widget.setRowHeight(0, 100)  # Adjust the minimum height as needed

    def add_testimonial(self):
        company_name = self.company_input.text()
        url = self.url_input.text()

        if company_name and url:
            found = False
            for testimonial in company_testimonials:
                if testimonial['company'] == company_name:
                    testimonial['web_url'].append(url)
                    found = True
                    break

            if not found:
                company_testimonials.append({
                    'company': company_name,
                    'web_url': [url]
                })

            # Save the updated testimonials to the data.py file
            save_testimonials(repr(company_testimonials))

            self.company_input.clear()
            self.url_input.clear()
            self.update_table_widget()

app = QApplication(sys.argv)

window = TestimonialApp()
window.show()
sys.exit(app.exec())
