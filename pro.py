import sys

from PIL.ImageQt import ImageQt
from PyQt5.Qt import Qt

from PyQt5 import uic
from PIL import Image, ImageFont
from PIL import ImageFilter, ImageDraw
from PyQt5.QtGui import QPixmap

from custom_dialog import MyDialog


from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication, QInputDialog, QColorDialog,  QLabel)





class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        uic.loadUi('untitled.ui', self)
        self.fname = ''
        self.im = ''
        self.obzor.clicked.connect(self.obzor_f)
        self.save.clicked.connect(self.save_f)
        self.filtrs.clicked.connect(self.filtrs_f)
        self.contrast.clicked.connect(self.contrast_f)
        self.rotate.clicked.connect(self.rotate_f)
        self.brightness.clicked.connect(self.brightness_f)
        self.text.clicked.connect(self.text_f)
        self.save.setEnabled(False)
        self.contrast.setEnabled(False)
        self.rotate.setEnabled(False)
        self.brightness.setEnabled(False)
        self.text.setEnabled(False)
        self.filtrs.setEnabled(False)






    def save_f(self):
        self.imName, _ = QFileDialog.getSaveFileName(self, "Save File", "",  "IMAGE FILES (*.JPEG)")
        self.im.save(self.imName, 'jpeg')




    def obzor_f(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        self.pixmap_f(self.fname)
        if self.fname != '':
            self.save.setEnabled(True)
            self.contrast.setEnabled(True)
            self.rotate.setEnabled(True)
            self.brightness.setEnabled(True)
            self.text.setEnabled(True)
            self.filtrs.setEnabled(True)


    def pixmap_f(self, im):
        if isinstance(im, str):

            pixmap = QPixmap(im)
        else:
            pixmap = QPixmap.fromImage(im)
        self.label.setPixmap(pixmap)
        myScaledPixmap = pixmap.scaled(self.label.size(), Qt.KeepAspectRatio)
        self.label.setPixmap(myScaledPixmap)



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

            self.filtr_edit(filtr, self.fname)

    def filtr_edit(self, filtr, file):
            self.im = Image.open(file)
            pixels = self.im.load()  # список с пикселями
            x, y = self.im.size
            if filtr == 'DISCOLORED':
                for i in range(x):
                    for j in range(y):
                        r, g, b = pixels[i, j]
                        bw = (r + g + b) // 3
                        pixels[i, j] = bw, bw, bw
                self.pixmap_f(ImageQt(self.im))

                # im.save('/home/odmin/DISCOLORED.jpg')
            if filtr == 'INVERSION':
                for i in range(x):
                    for j in range(y):
                        r, g, b = pixels[i, j]
                        pixels[i, j] = 255 - r, 255 - g, 255 - b
                self.pixmap_f(ImageQt(self.im))

                # im.save('/home/odmin/INVERSION.jpg')
            if filtr == 'BLUR':
                self.im = self.im.filter(ImageFilter.BLUR)
                self.pixmap_f(ImageQt(self.im))

                # out_im.save('/home/odmin/BLUR.jpg')
            if filtr == 'CONTOUR':
                self.im = self.im.filter(ImageFilter.CONTOUR)
                self.pixmap_f(ImageQt(self.im))

                # out_im.save('/home/odmin/CONTOUR.jpg')
            if filtr == 'DETAIL':
                self.im = self.im.filter(ImageFilter.DETAIL)
                self.pixmap_f(ImageQt(self.im))

                # out_im.save('/home/odmin/DETAIL.jpg')
            if filtr == 'EDGE_ENHANCE':
                self.im = self.im.filter(ImageFilter.EDGE_ENHANCE)
                self.pixmap_f(ImageQt(self.im))

                # out_im.save('/home/odmin/EDGE_ENHANCE.jpg')
            if filtr == 'EDGE_ENHANCE_MORE':
                self.im = self.im.filter(ImageFilter.EDGE_ENHANCE_MORE)
                self.pixmap_f(ImageQt(self.im))

                # out_im.save('/home/odmin/EDGE_ENHANCE_MORE.jpg')
            if filtr == 'EMBOSS':
                self.im = self.im.filter(ImageFilter.EMBOSS)
                self.pixmap_f(ImageQt(self.im))
                # out_im.save('/home/odmin/EMBOSS.jpg')
            if filtr == 'FIND_EDGES':
                self.im = self.im.filter(ImageFilter.FIND_EDGES)
                self.pixmap_f(ImageQt(self.im))
                # out_im.save('/home/odmin/FIND_EDGES.jpg')
            if filtr == 'SMOOTH':
                self.im = self.im.filter(ImageFilter.SMOOTH)
                self.pixmap_f(ImageQt(self.im))

                # out_im.save('/home/odmin/SMOOTH.jpg')
            if filtr == 'SHARPEN':
                self.im = self.im.filter(ImageFilter.SHARPEN)
                self.pixmap_f(ImageQt(self.im))

                # out_im.save('/home/odmin/SHARPEN.jpg')
            if filtr == 'SMOOTH_MORE':
                self.im = self.im.filter(ImageFilter.SMOOTH_MORE)
                self.pixmap_f(ImageQt(self.im))

                # out_im.save('/home/odmin/SMOOTH_MORE.jpg')

    def rotate_f(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Введите число", "Градусы"
        )
        if okBtnPressed:
            value_gradus = i
            self.rotate_edit(value_gradus, self.fname)

    def rotate_edit(self, value_gradus, file):
        self.im = Image.open(file)  # открываем картинку
        self.im = self.im.rotate(int(value_gradus))
        self.pixmap_f(ImageQt(self.im))
        # im.save('/home/odmin/ROTATE.jpg')

    def text_edit(self, value_x, value_y, text_im, text_color, font, file):
        self.im = Image.open(file)
        draw = ImageDraw.Draw(self.im)
        draw.text((int(value_x), int(value_y)), text_im, text_color, font=font)
        self.pixmap_f(ImageQt(self.im))
        # im.save("/home/odmin/TEXT.jpg")

    def text_f(self):
        global text_im, text_color, font
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
            text_im = i

        color = QColorDialog.getColor()
        if color.isValid():
            text_color = color.name()

        i, okBtnPressed = QInputDialog.getItem(
            self,
            "Выберите шрифт",
            "Шрифты",
            ('Abyssinica SIL', 'Symbola_hint', 'Ubuntu_B'),
            1, False
        )
        if okBtnPressed:
            font = i

        i, okBtnPressed = QInputDialog.getText(
            self, "Введите число", "Размер шрифта"
        )
        if okBtnPressed:
            value_font = i

        if font == 'Abyssinica SIL':
            font = ImageFont.truetype('AbyssinicaSIL-R.ttf', int(value_font))
        elif font == 'Symbola_hint':
            font = ImageFont.truetype('Symbola_hint.ttf', int(value_font))
        elif font == 'Ubuntu_B':
            font = ImageFont.truetype('Ubuntu-B.ttf', int(value_font))

        self.text_edit(value_x, value_y, text_im, text_color, font, self.fname)

    def brightness_f(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Введите число", "Яркость"
        )
        if okBtnPressed:
            brightness = i
            self.brightness_edit(brightness)


    def brightness_edit(self, brightness):
        self.im = self.fname
        source = Image.open(self.im)
        result = Image.new('RGB', source.size)
        for x in range(source.size[0]):
            for y in range(source.size[1]):
                r, g, b = source.getpixel((x, y))

                red = int(r * int(brightness))
                red = min(255, max(0, red))

                green = int(g * int(brightness))
                green = min(255, max(0, green))

                blue = int(b * int(brightness))
                blue = min(255, max(0, blue))

                result.putpixel((x, y), (red, green, blue))
        self.pixmap_f(ImageQt(result))
        # result.save('/home/odmin/BRIGHTNESS.jpg')

    def contrast_f(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Введите число", "Контрастность"
        )
        if okBtnPressed:
            contrast = i
            self.contrast_edit(contrast)

    def contrast_edit(self, contrast):
        source = Image.open(self.fname)
        self.im = Image.new('RGB', source.size)

        avg = 0
        for x in range(source.size[0]):
            for y in range(source.size[1]):
                r, g, b = source.getpixel((x, y))
                avg += r * 0.299 + g * 0.587 + b * 0.114
        avg /= source.size[0] * source.size[1]

        palette = []
        for i in range(256):
            temp = int(avg + int(contrast) * (i - avg))
            if temp < 0:
                temp = 0
            elif temp > 255:
                temp = 255
            palette.append(temp)

        for x in range(source.size[0]):
            for y in range(source.size[1]):
                r, g, b = source.getpixel((x, y))
                self.im.putpixel((x, y), (palette[r], palette[g], palette[b]))
        self.pixmap_f(ImageQt(self.im))
        # result.save("/home/odmin/CONTRAST.jpg")


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
