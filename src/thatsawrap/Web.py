from flask import Flask
from src.thatsawrap.web.MenuController import MenuController
from src.thatsawrap.web.CustomController import CustomController
from typing import List


class Web:

    @staticmethod
    def main(args: List[str]):
        app = Flask(__name__)
        MenuController.register(app)
        CustomController.register(app)
        app.config['WTF_CSRF_ENABLED'] = False
        app.debug = True
        return app
