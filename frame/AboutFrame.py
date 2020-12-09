import wx
from frame import SecondaryFrame


class AboutFrame:
    def __init__(self, event):
        title = 'Acerca de Word Scanner'
        frame = SecondaryFrame(title=title)
        frame.SetSize(300, 400)
        sizer = wx.BoxSizer(wx.VERTICAL)
        frame.SetSizer(sizer)

        panel = wx.Panel(frame)
        panel.SetSize(10, 10, 265, 340)
        panel.SetBackgroundColour('WHITE')

        fontBig = wx.Font(16, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        fontMedium = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)

        textTitle = wx.StaticText(
            panel, label="Word Scanner", size=(265, 20), pos=(0, 20), style=wx.ALIGN_CENTRE_HORIZONTAL
        )
        textTitle.SetFont(fontBig)

        textAuthors = wx.StaticText(
            panel, label="Hecho por Benjamin y Mario", size=(265, 40), pos=(0, 100), style=wx.ALIGN_CENTRE_HORIZONTAL
        )
        textAuthors.SetFont(fontMedium)

        textCopy = wx.StaticText(
            panel, label="Copyright 2020", size=(265, 20), pos=(0, 300), style=wx.ALIGN_CENTRE_HORIZONTAL
        )
        textCopy.SetFont(fontMedium)
