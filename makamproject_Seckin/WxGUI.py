from makamproject_Seckin.TeoricFileRead import getMakam
import wx
import os 
#from makamproject.WavPlayer import PlayerFrame
from makamproject_Seckin.pitchAnalyse import pitchCalc
from wx.core import Position
from makamproject_Seckin.PitcPlotSelectedArea import AreaPlot
from makamproject_Seckin.WavPlayer import PlaybackMoveEvent
from makamproject_Seckin.Just_Histogram_Draw import selectMakam
from makamproject_Seckin.histmakamPlot import selectMakamUser
import wxmplot
import numpy as np

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='MakamProject_V1')
        self.panel = wx.Panel(self)                
        self.my_btn = wx.Button(self.panel, label='Analiz Et')
        self.my_btn.Bind(wx.EVT_BUTTON, self.PlotShow, self.my_btn)
        self.my_btn.SetPosition((10,120))
        self.text = wx.TextCtrl(self.panel, size = (150,50), style = wx.TE_MULTILINE) 
        self.text.SetPosition((150,10))
        self.button1 = wx.Button(self.panel, label='Start')
        self.button1.Bind(wx.EVT_BUTTON, PlaybackMoveEvent.start, self.button1)
        self.button1.SetPosition((10,85))

        self.button2 = wx.Button(self.panel, label='Stop')
        self.button2.Bind(wx.EVT_BUTTON, PlaybackMoveEvent.stop, self.button2)
        self.button2.SetPosition((100,85))

        self.button3 = wx.Button(self.panel, label='Ses Dosyası Seç')
       # button3.Bind(wx.EVT_BUTTON, onButton)
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button3)
        self.button3.SetPosition((10,15))
          
        self.button4 = wx.Button(self.panel, label='Sadece Histogram')
       # button3.Bind(wx.EVT_BUTTON, onButton)
        self.Bind(wx.EVT_BUTTON, self.OnClickHist, self.button4)
        self.button4.SetPosition((10,50))

        self.button5 = wx.Button(self.panel, label='Makam Tahmin Analizi')
       # button3.Bind(wx.EVT_BUTTON, onButton)
        self.Bind(wx.EVT_BUTTON, self.HistPlotShow, self.button5)
        self.button5.SetPosition((100,120))

        self.button6 = wx.Button(self.panel, label='Makam & Histogram Analizi')
       # button3.Bind(wx.EVT_BUTTON, onButton)
        self.Bind(wx.EVT_BUTTON, self.HistMakPlotShow, self.button6)
        self.button6.SetPosition((100,150))
        
        
        self.counter=0
        #self.panel = wx.Panel(self) 
        self.box = wx.BoxSizer(wx.HORIZONTAL) 
      
        self.text_2 = wx.TextCtrl(self.panel,style = wx.TE_MULTILINE,pos=(210,180), size=(200,100)) 
          
        makamlar = ["Oniki_Tet_ussak","Oniki_Tet_huseyni",
          "Oniki_Tet_hicaz","Oniki_Tet_saba","Oniki_Tet_kurdilihiczkar","Oniki_Tet_segah",
          "Oniki_Tet_nihavend","Töre_Karadeniz_segah","Töre_Karadeniz_huzzam","Töre_Karadeniz_rast",
          "Töre_Karadeniz_hicaz","Töre_Karadeniz_saba","Töre_Karadeniz_ussak","Töre_Karadeniz_huseyni",
          "Töre_Karadeniz_buselik","Töre_Karadeniz_nikriz","Töre_Karadeniz_ferahnak","Töre_Karadeniz_nisabur",
          "Töre_Karadeniz_cargah","Töre_Karadeniz_kurdi","Töre_Karadeniz_pencgah","Töre_Karadeniz_mustear","Töre_Karadeniz_nihavend",
          "Töre_Karadeniz_kurdilihiczkar","Yekta_Arel_buselik","Yekta_Arel_cargah","Yekta_Arel_ferahnak",
          "Yekta_Arel_hicaz","Yekta_Arel_huseyni",		
          "Yekta_Arel_huzzam","Yekta_Arel_kurdi",	"Yekta_Arel_mustear","Yekta_Arel_nikriz","Yekta_Arel_nisabur",		
          "Yekta_Arel_pencgah","Yekta_Arel_rast","Yekta_Arel_saba","Yekta_Arel_segah","Yekta_Arel_ussak","Yekta_Arel_beyati",		
          "Yekta_Arel_neva","Yekta_Arel_nisaburek","Yekta_Arel_acem","Yekta_Arel_ferahfeza","Yekta_Arel_kurdilihiczkar",	
      "Yekta_Arel_sehnaz","Yekta_Arel_hiczkar","Yekta_Arel_sedaraban","Yekta_Arel_neveser",		
          "Yekta_Arel_sultaniyegah","Yekta_Arel_suzidil",	"Yekta_Arel_gulizar",	"Yekta_Arel_tahirbuselik",	
          "Yekta_Arel_tahir","Yekta_Arel_muhayyer","Yekta_Arel_isfahan","Yekta_Arel_nuhuft",		
          "Yekta_Arel_beyatiaraban","Yekta_Arel_sevkefza","Yekta_Arel_nihavend",	
          "Yekta_Arel_pesendide","Yekta_Arel_suzinak","Yekta_Arel_yegah",		
          "Yekta_Arel_acemasiran","Yekta_Arel_mahur","Yekta_Arel_bestenigar",	
          "Yekta_Arel_evic"	,"Yekta_Arel_irak","Yekta_Arel_evcara",		
          "Yekta_Arel_karcigar"]   
        self.lst = wx.ListBox(self.panel, size = (200,100), choices = makamlar, style = wx.LB_SINGLE ,pos=(10,180))
      
        self.box.Add(self.lst,0,wx.EXPAND) 
        self.box.Add(self.text, 1, wx.EXPAND) 
      
        #self.panel.SetSizer(self.box) 
        self.panel.Fit() 
      
        #self.Centre() 
        self.Bind(wx.EVT_LISTBOX, self.onListBox, self.lst) 
        self.Show(True)  
      
    def onListBox(self, event):
        if self.counter<1:   
          selectMakamUser.makamName1=self.lst.GetStringSelection()
          self.text_2.AppendText( "teorik makam 1: "+event.GetEventObject().GetStringSelection()+"\n")
          self.text_2.AppendText( "2 adet daha makam seçiniz")
          self.counter =self.counter+1
          print("counter1 ",self.counter)
          print("mn1  ",selectMakamUser.makamName1)
        elif self.counter>=1 and self.counter<2 : 
          selectMakamUser.makamName2=self.lst.GetStringSelection()
          self.text_2.AppendText( "teorik makam 2: "+event.GetEventObject().GetStringSelection()+"\n")
          self.text_2.AppendText( "1 adet daha makam seçiniz")
          self.counter = self.counter+1
          print("counter2 ",self.counter)
          print("mn2  ",selectMakamUser.makamName2)
        elif self.counter>=2 and self.counter<3: 
          selectMakamUser.makamName3=self.lst.GetStringSelection()
          self.text_2.AppendText( "teorik makam 3: "+event.GetEventObject().GetStringSelection()+"\n")
          self.text_2.AppendText( "Makam & Histogram Analizi tuşuna basınız")
          self.counter = self.counter+1
          print("counter3 ",self.counter)
          print("mn3  ",selectMakamUser.makamName3)
        elif self.counter>=3 :
          self.text_2.AppendText( "***3 tane teorik makam seçtiniz, lütfen analiz tuşuna basın!***")
          self.counter = self.counter+1
          print("counter3 ",self.counter)
          print("mn3  ",selectMakamUser.makamName3)

    def OnClick(self, e): 
      wildcard = "Text Files (*.*)|*.*" 
      dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", wildcard, wx.FD_OPEN)
		
      if dlg.ShowModal() == wx.ID_OK:
         #f = open(dlg.GetPath(), 'r')
         pitchCalc.sound_file_path=dlg.GetPath() 
         self.text.SetValue(pitchCalc.sound_file_path)   
      dlg.Destroy()

    def OnClickHist(self, e): 
        selectMakam.plotSelect()

    def PlotShow(self, e):
        AreaPlot.start()

    def HistPlotShow(self, e):
        getMakam.plot()

    def HistMakPlotShow(self, e):
        selectMakamUser.start()        
"""
    def plotDraw(self,e):
        noise = np.random.normal
        n = 201
        x  = np.linspace(0, 100, n)
        y1 = np.sin(x/3.4)/(0.2*x+2) + noise(size=n, scale=0.1)
        y2 = 92 + 65*np.cos(x/16.) * np.exp(-x*x/7e3) + noise(size=n, scale=0.3)
        pframe = wxmplot.PlotFrame()

        pframe.plot(x, y1, title='Test 2 Axes with different y scales',
                    xlabel='x (mm)', ylabel='y1', ymin=-0.75, ymax=0.75)
        pframe.oplot(x, y2, y2label='y2', side='right', ymin=0)
        pframe.Show()
  """  
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.SetSize(0,0,640,400)
    app.MainLoop()





