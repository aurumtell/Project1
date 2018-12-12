import sys

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

        self.obzor.clicked.connect(self.obzor_f)
        self.filtrs.clicked.connect(self.filtrs_f)
        self.contrast.clicked.connect(self.contrast_f)
        self.rotate.clicked.connect(self.rotate_f)
        self.brightness.clicked.connect(self.brightness_f)
        self.text.clicked.connect(self.text_f)

    def obzor_f(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        global f
        f = open(fname, 'r')

        pixmap = QPixmap(f.name)

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

    def text_edit(self, value_x, value_y, text_im, text_color, font):
        im = Image.open(f.name)
        draw = ImageDraw.Draw(im)
        draw.text((int(value_x), int(value_y)), text_im, text_color, font=font)
        im.save("/home/odmin/TEXT.jpg")

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
            font = ImageFont.truetype('Ubuntu_B.ttf', int(value_font))

        self.text_edit(value_x, value_y, text_im, text_color, font)

    def brightness_f(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Введите число", "Яркость"
        )
        if okBtnPressed:
            brightness = i
            self.brightness_edit(brightness)


    def brightness_edit(self, brightness):
        im = f.name
        source = Image.open(im)
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
        result.save('/home/odmin/BRIGHTNESS.jpg')

    def contrast_f(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Введите число", "Контрастность"
        )
        if okBtnPressed:
            contrast = i
            self.contrast_edit(contrast)

    def contrast_edit(self, contrast):
        source = Image.open(f.name)
        result = Image.new('RGB', source.size)

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
                result.putpixel((x, y), (palette[r], palette[g], palette[b]))

        result.save("/home/odmin/CONTRAST.jpg")




app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
