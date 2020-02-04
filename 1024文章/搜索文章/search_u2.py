import sys
from PyQt5.QtWidgets import QWidget, QApplication
from search import Ui_Form
from config import Tools_cl
from gevent import monkey
monkey.patch_all()
import gevent


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.resize(600, 300)
        self.setupUi(self)
        self.setWindowTitle("CL搜索")
        self.tool = Tools_cl()

    def change_leibie(self):
        print("改变分类")
        fenlei = self.leibie.currentText()
        self.tool.change_lei(fenlei)

    def search_file(self):
        print("开始搜索")
        g1 = gevent.spawn(self.thread_start)
        g1.join()

    def thread_start(self):
        print("开启线程")
        keyword = self.key_line.text()
        if keyword:
            content = self.tool.search(keyword)
            self.add_content(content)

    def add_content(self, content):
        print("添加文章", content)
        self.textBrowser.setHtml(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
