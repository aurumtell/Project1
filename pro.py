import sys
from PyQt5 import uic
from PIL import Image
from PIL import ImageFilter, ImageDraw

from custom_dialog import MyDialog


from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication, QInputDialog, QColorDialog, QFontDialog, QLabel, QDialog)




class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)

        self.obzor.clicked.connect(self.obzor_f)
        self.filtrs.clicked.connect(self.filtrs_f)
        self.rotate.clicked.connect(self.rotate_f)
        # self.brightness.clicked.connect(self.brightness_f)
        self.text.clicked.connect(self.text_f)

    def obzor_f(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        global f
        f = open(fname, 'r')

        with f:
            print(f.name)

    def filtrs_f(self):
        i, okBtnPressed = QInputDialog.getItem(
            self,
            "Выберите фильтр",
            "Фильтры",
            ('DISCOLORED', 'INVERSION', 'BLUR', 'CONTOUR', 'DETAIL', 'EDGE_ENHANCE', 'EDGE_ENHANCE_MORE', 'EMBOSS',
             'FIND_EDGES', 'SHARPEN', 'SMOOTH', 'SMOOTH_MORE'),
            1, False
        )
        if okBtnPressed:
            filtr = i
            self.filtr_edit(filtr, f.name)

    def filtr_edit(self, filtr, file):
            im = Image.open(file)
            pixels = im.load()  # список с пикселями
            x, y = im.size
            if filtr == 'DISCOLORED':
                for i in range(x):
                    for j in range(y):
                        r, g, b = pixels[i, j]
                        bw = (r + g + b) // 3
                        pixels[i, j] = bw, bw, bw
                im.save('/home/odmin/DISCOLORED.jpg')
            if filtr == 'INVERSION':
                for i in range(x):
                    for j in range(y):
                        r, g, b = pixels[i, j]
                        pixels[i, j] = 255 - r, 255 - g, 255 - b
                im.save('/home/odmin/INVERSION.jpg')
            if filtr == 'BLUR':
                out_im = im.filter(ImageFilter.BLUR)
                out_im.save('/home/odmin/BLUR.jpg')
            if filtr == 'CONTOUR':
                out_im = im.filter(ImageFilter.CONTOUR)
                out_im.save('/home/odmin/CONTOUR.jpg')
            if filtr == 'DETAIL':
                out_im = im.filter(ImageFilter.DETAIL)
                out_im.save('/home/odmin/DETAIL.jpg')
            if filtr == 'EDGE_ENHANCE':
                out_im = im.filter(ImageFilter.EDGE_ENHANCE)
                out_im.save('/home/odmin/EDGE_ENHANCE.jpg')
            if filtr == 'EDGE_ENHANCE_MORE':
                out_im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
                out_im.save('/home/odmin/EDGE_ENHANCE_MORE.jpg')
            if filtr == 'EMBOSS':
                out_im = im.filter(ImageFilter.EMBOSS)
                out_im.save('/home/odmin/EMBOSS.jpg')
            if filtr == 'FIND_EDGES':
                out_im = im.filter(ImageFilter.FIND_EDGES)
                out_im.save('/home/odmin/FIND_EDGES.jpg')
            if filtr == 'SMOOTH':
                out_im = im.filter(ImageFilter.SMOOTH)
                out_im.save('/home/odmin/SMOOTH.jpg')
            if filtr == 'SHARPEN':
                out_im = im.filter(ImageFilter.SHARPEN)
                out_im.save('/home/odmin/SHARPEN.jpg')
            if filtr == 'SMOOTH_MORE':
                out_im = im.filter(ImageFilter.SMOOTH_MORE)
                out_im.save('/home/odmin/SMOOTH_MORE.jpg')

    def rotate_f(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Введите число", "Градусы"
        )
        if okBtnPressed:
            value_gradus = i
            self.rotate_edit(value_gradus, f.name)

    def rotate_edit(self, value_gradus, file):
        im = Image.open(file)  # открываем картинку
        out_im = im.rotate(int(value_gradus))
        out_im.save('/home/odmin/ROTATE.jpg')

    def text_f(self):
        self.myDialog = MyDialog()
        # self.myDialog.show()
        # self.connect(self.myDialog, SIGNAL("closed()"), self.OnCustomWinClosed)

        returnCode = self.myDialog.exec_()
        print(returnCode)
        value_x, value_y = self.myDialog.get_value()


        i, okBtnPressed = QInputDialog.getText(
            self, "Введите информацию для создания текста", "Текст"
        )
        if okBtnPressed:
            self.text_im = i

        color = QColorDialog.getColor()
        if color.isValid():
            self.text_color = color.name()

        font, ok = QFontDialog.getFont()

        out_im = Image.open(f.name)
        imgDrawer = ImageDraw.Draw(out_im)
        imgDrawer.text((value_x, value_y), self.text_im, font=font)
        out_im.save('/home/odmin/TEXT_APPEND.jpg')

        # word = '<span style=\" color: %s;\">%s</span>' % (self.text_color, self.text_im)
        # print(word)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
