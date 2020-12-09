from frame import SecondaryFrame
import wx


class InstructionsFrame:
    def __init__(self, event):
        title = 'Instrucciones'
        frame = SecondaryFrame(title=title)
        frame.SetSize(800, 600)
        sizer = wx.BoxSizer(wx.VERTICAL)
        frame.SetSizer(sizer)

        panel = wx.Panel(frame)
        panel.SetSize(20, 20, 750, 525)
        panel.SetBackgroundColour('WHITE')

        fontBig = wx.Font(16, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        fontMedium = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)

        textTitle = wx.StaticText(
            panel, label="Instrucciones", size=(750, 40), pos=(0, 20), style=wx.ALIGN_CENTRE_HORIZONTAL
        )
        textTitle.SetFont(fontBig)

        textStepOne = wx.StaticText(
            panel,
            label="Paso 1. Descargar tesserac.exe de https://github.com/tesseract-ocr/tesseract/releases",
            size=(750, 40), pos=(10, 100)
        )
        textStepOne.SetFont(fontMedium)

        textStepTwo = wx.StaticText(
            panel,
            label="Paso 2. Darle click en 'configurar', seleccionar el tesserac.exe",
            size=(750, 40), pos=(10, 150)
        )
        textStepTwo.SetFont(fontMedium)

        textStepThree = wx.StaticText(
            panel,
            label="Paso 3. Dar click en 'Iniciar'",
            size=(750, 40), pos=(10, 200)
        )
        textStepThree.SetFont(fontMedium)