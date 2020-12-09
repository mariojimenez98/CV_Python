import wx
import app


class MainContainer:
    def __init__(self, main_frame: wx.Frame):
        self.main_frame = main_frame
        self.tess_path = ''

        panel = wx.Panel(main_frame)
        panel.SetSize(25, 25, 525, 275)
        panel.SetBackgroundColour('WHITE')

        text = wx.StaticText(
            panel, label="Bienvenido a Word Scanner", size=(525, 20), pos=(0, 20), style=wx.ALIGN_CENTRE_HORIZONTAL
        )
        font = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        text.SetFont(font)

        configure_button = wx.Button(panel, pos=(30, 175), size=(100, 50))
        configure_button.SetLabelText('Configurar')
        configure_button.Bind(wx.EVT_BUTTON, self._on_configure_click)

        launch_button = wx.Button(panel, pos=(395, 175), size=(100, 50))
        launch_button.SetLabelText('Iniciar')
        launch_button.Bind(wx.EVT_BUTTON, self._on_start_click)

    def _on_configure_click(self, event):
        with wx.FileDialog(
                self.main_frame,
                "Abrir tesserac exe",
                wildcard="Executable files (*.exe)|*.exe",
                style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        ) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            self.tess_path = fileDialog.GetPath()
            return

    def _on_start_click(self, event):
        app.launch_app(self.tess_path)
        return


