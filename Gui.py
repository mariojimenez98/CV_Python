import wx

from container import MainContainer


def start():
    app = wx.App(False)
    frame = Gui(None, "Word Scanner")
    sizer = wx.BoxSizer(wx.VERTICAL)
    frame.SetSizer(sizer)
    MainContainer.MainContainer(frame)
    app.MainLoop()


class Gui(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600, 400), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        self.CreateStatusBar()

        fileMenu = wx.Menu()
        aboutMenu = fileMenu.Append(wx.ID_ABOUT, "&Acerca", " Acerca del programa")
        fileMenu.AppendSeparator()
        exitMenu = fileMenu.Append(wx.ID_EXIT, "E&xit", "Salir")

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        self.SetMenuBar(menuBar)
        self.Show(True)

        self.Bind(wx.EVT_MENU, self.onAbout, aboutMenu)
        self.Bind(wx.EVT_MENU, self.onExit, exitMenu)


    def onAbout(self, event):
        print({"Click en about", event})

    def onExit(self, event):
        print({"Click en exit", event})
