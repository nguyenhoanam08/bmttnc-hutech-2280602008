import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.exec_()
            else:
                print(f"Error while calling API: Status {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        plain_text = self.ui.txt_plain_text.toPlainText().strip()
        if not plain_text:
            QMessageBox.critical(self, "Error", "Plain text is empty!")
            return
        payload = {
            "message": plain_text,
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data["encrypted_message"])
            else:
                print(f"Error while calling API: Status {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        ciphertext = self.ui.txt_cipher_text.toPlainText().strip()
        if not ciphertext:
            QMessageBox.critical(self, "Error", "Cipher text is empty!")
            return
        payload = {
            "ciphertext": ciphertext,
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setText(data["decrypted_message"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print(f"Error while calling API: Status {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        message = self.ui.txt_info.toPlainText().strip()
        if not message:
            QMessageBox.critical(self, "Error", "Message for signing is empty!")
            return
        payload = {
            "message": message
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_sign.setText(data["signature"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed Successfully")
                msg.exec_()
            else:
                print(f"Error while calling API: Status {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        message = self.ui.txt_info.toPlainText().strip()
        signature = self.ui.txt_sign.toPlainText().strip()
        if not message or not signature:
            QMessageBox.critical(self, "Error", "Message or signature is empty!")
            return
        payload = {
            "message": message,
            "signature": signature
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data["is_verified"]:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verified Successfully")
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verified Fail")
                    msg.exec_()
            else:
                print(f"Error while calling API: Status {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())