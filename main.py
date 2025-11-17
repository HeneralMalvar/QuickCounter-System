import sys
from functools import partial
from PyQt6.QtWidgets import (
    QWidget, QApplication, QVBoxLayout, QHBoxLayout, QFrame, QLabel,
    QPushButton, QStackedWidget, QButtonGroup, QLineEdit, QGridLayout, QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt6.QtCore import Qt
import datetime



class CounterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quick Counter CnDev+")
        self.setGeometry(300, 300, 500, 600)
        self.setFixedSize(500, 600)
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        #--Top Layout--
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(15,15,15,0)
        top_layout.setSpacing(0)
        self.lbl_info = QLabel("F1: Checkup, F2: Follow-up Checkup, F3: Checkup +SSS")
        self.lbl_info.setStyleSheet("font-size: 16px; font-weight: bold; color: cyan;")
        self.lbl_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_counter = QLabel("Total Count: 0")
        self.lbl_total = QLabel("Total Income: 0")
        self.lbl_counter.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.lbl_total.setStyleSheet("font-size: 16px; font-weight: bold;")
        root.addWidget(self.lbl_info)
        top_layout.addWidget(self.lbl_counter)
        top_layout.addStretch()
        top_layout.addWidget(self.lbl_total)
        root.addLayout(top_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(["Count", "Description", "Price"])
        self.table.setRowCount(0)

        for i in range(0,2):
            self.table.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeMode.Fixed)
        self.table.setColumnWidth(0, 70)
        self.table.setColumnWidth(1, 300)
        self.table.setColumnWidth(2, 100)

        root.addWidget(self.table)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_F1:
            self.add_item("Checkup",300)
        elif event.key() == Qt.Key.Key_F2:
            self.add_item("Follow-Up Checkup",150)
        elif event.key() == Qt.Key.Key_F3:
            self.add_item("Checkup + SSS",500)
        elif event.key() == Qt.Key.Key_Backspace:
            self.delete_item()


    def add_item(self, description, price):
        row = self.table.rowCount()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.table.insertRow(row)
        row_counter = row + 1

        item_count = QTableWidgetItem(str(row_counter))
        item_count.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table.setItem(row, 0 , item_count)



        self.table.setItem(row,1,QTableWidgetItem(description + ":     " + now))
        item_price = QTableWidgetItem(str(price))
        item_price.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table.setItem(row, 2, item_price)

        self.update_totals()

    def delete_item(self):
        row = self.table.currentRow()

        if row >= 0:
            self.table.removeRow(row)
            #--Recount Row

            for r in range(self.table.rowCount()):
                self.table.setItem(r,0,QTableWidgetItem(str(r + 1)))
                item_count = QTableWidgetItem(str(r +1))
                item_count.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(r,0,item_count)

            self.update_totals()



    def update_totals(self):
        total_count = self.table.rowCount()
        total_income = sum(int(self.table.item(r,2).text()) for r in range(total_count))
        self.lbl_counter.setText(f"Total Count: {total_count}")
        self.lbl_total.setText(f"Total Income: {total_income}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    counter = CounterApp()
    counter.show()
    sys.exit(app.exec())