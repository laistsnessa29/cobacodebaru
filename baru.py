from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtGui import QFont, QPalette, QLinearGradient, QColor, QBrush
from PyQt5.QtCore import Qt

app = QApplication([])

window = QWidget()
window.setWindowTitle("Login")
window.setFixedSize(400, 300)

# Background gradient
palette = QPalette()
gradient = QLinearGradient(0, 0, 400, 300)
gradient.setColorAt(0.0, QColor("#a2d4f5"))
gradient.setColorAt(1.0, QColor("#ffffff"))
palette.setBrush(QPalette.Window, QBrush(gradient))
window.setPalette(palette)
window.setAutoFillBackground(True)

layout = QVBoxLayout()

# Logo / Judul
logo = QLabel("PhvSi")
logo.setAlignment(Qt.AlignCenter)
logo_font = QFont("Arial", 48, QFont.Bold)
logo.setFont(logo_font)
logo.setMinimumHeight(70)  # ✨ Tambahkan tinggi minimum
logo.setStyleSheet("color: black;")

layout.addWidget(logo)

# NIM input
nim = QLineEdit()
nim.setPlaceholderText("NTM")
layout.addWidget(nim)

# Password input
password = QLineEdit()
password.setPlaceholderText("PASSWORD")
password.setEchoMode(QLineEdit.Password)
layout.addWidget(password)

# Login button
login_btn = QPushButton("LOGIN")
login_btn.setStyleSheet("background-color: #00aaff; color: white; padding: 6px 12px; border-radius: 6px;")
layout.addWidget(login_btn, alignment=Qt.AlignCenter)

window.setLayout(layout)
window.show()
app.exec_()
