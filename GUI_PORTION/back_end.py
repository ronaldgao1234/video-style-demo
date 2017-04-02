import htmlPy
import demo


class BackEnd(htmlPy.Object):

    def __init__(self, app):
        super(BackEnd, self).__init__()
        self.app = app

    @htmlPy.Slot()
    def say_hello_world(self):
       demo.main_func()\