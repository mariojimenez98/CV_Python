import wx

from container.MainContainer import MainContainer
from frame.AboutFrame import AboutFrame
from frame.InstructionsFrame import InstructionsFrame


def start():
    app = wx.App(False)
    frame = Gui(None, "Word Scanner")
    sizer = wx.BoxSizer(wx.VERTICAL)
    frame.SetSizer(sizer)
    MainContainer(frame)
    app.MainLoop()


class Gui(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600, 400), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        self.CreateStatusBar()

        fileMenu = wx.Menu()
        aboutMenu = fileMenu.Append(wx.ID_ABOUT, "&Acerca", "Acerca del programa")
        instructionsMenu = fileMenu.Append(wx.ID_HELP, "Instrucciones", "Instrucciones para ejecutar programa")
        fileMenu.AppendSeparator()
        exitMenu = fileMenu.Append(wx.ID_EXIT, "E&xit", "Salir")

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        self.SetMenuBar(menuBar)
        self.Show(True)

        self.Bind(wx.EVT_MENU, self.onAbout, aboutMenu)
        self.Bind(wx.EVT_MENU, self.onExit, exitMenu)
        self.Bind(wx.EVT_MENU, self.onInstructions, instructionsMenu)

    def onInstructions(self, event):
        InstructionsFrame(event)

    def onAbout(self, event):
        AboutFrame(event)

    def onExit(self, event):
        wx.Exit()
