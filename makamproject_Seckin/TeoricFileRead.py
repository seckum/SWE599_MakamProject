from makamproject_Seckin.histogramAnalyse import HistAnalyse
from makamproject_Seckin.pitchAnalyse    import pitchCalc
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

class getMakam:
    def getTemplateNames():
        templateNames=["Oniki_Tet_ussak","Oniki_Tet_huseyni",
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
        "Yekta_Arel_karcigar"	
    ]
        return templateNames
    def initTemplates():
    #12Tet Teorik Makamlar
        Oniki_Tet_ussak=[0,4.4167*22.64,8.8333*22.64,   13.2500*22.64,   17.6667*22.64,   22.0833*22.64,   26.5000*22.64,   30.9167*22.64,   35.3333*22.64,   39.7500*22.64,   44.1667*22.64,   48.5833*22.64,   53.0000*22.64]
        Oniki_Tet_huseyni=[0,4.4167*22.64,    8.8333*22.64,   13.2500*22.64,   17.6667*22.64,   22.0833*22.64,   26.5000*22.64,   30.9167*22.64,   35.3333*22.64,   39.7500*22.64,   44.1667*22.64,   48.5833*22.64,   53.0000*22.64]
        Oniki_Tet_hicaz=[0,4.4167*22.64,    8.8333*22.64,   13.2500*22.64,   17.6667*22.64,   22.0833*22.64,   26.5000*22.64,   30.9167*22.64,   35.3333*22.64,   39.7500*22.64,   44.1667*22.64,   48.5833*22.64,   53.0000*22.64]
        Oniki_Tet_saba=[0,4.4167*22.64,    8.8333*22.64,   13.2500*22.64,   17.6667*22.64,   22.0833*22.64,   26.5000*22.64,   30.9167*22.64,   35.3333*22.64,   39.7500*22.64,   44.1667*22.64,   48.5833*22.64,   53.0000*22.64]
        Oniki_Tet_kurdilihicazkar=[0,4.4167*22.64,    8.8333*22.64,   13.2500*22.64,   17.6667*22.64,   22.0833*22.64,   26.5000*22.64,   30.9167*22.64,   35.3333*22.64,   39.7500*22.64,   44.1667*22.64,   48.5833*22.64,   53.0000*22.64]
        Oniki_Tet_segah=[0,4.4167*22.64,    8.8333*22.64,   13.2500*22.64,   17.6667*22.64,   22.0833*22.64,   26.5000*22.64,   30.9167*22.64,   35.3333*22.64,   39.7500*22.64,   44.1667*22.64,   48.5833*22.64,   53.0000*22.64]
        #Oniki_Tet_huzzam=[0,4.4167*22.64,    8.8333*22.64,   13.2500*22.64,   17.6667*22.64,   22.0833*22.64,   26.5000*22.64,   30.9167*22.64,   35.3333*22.64,   39.7500*22.64,   44.1667*22.64,   48.5833*22.64,   53.0000*22.64]
        Oniki_Tet_nihavend=[0,4.4167*22.64,    8.8333*22.64,   13.2500*22.64,   17.6667*22.64,   22.0833*22.64,   26.5000*22.64,   30.9167*22.64,   35.3333*22.64,   39.7500*22.64,   44.1667*22.64,   48.5833*22.64,   53.0000*22.64]
        #Oniki_Tet_rast=[0,4.4167,    8.8333,   13.2500,   17.6667,   22.0833,   26.5000,   30.9167,   35.3333,   39.7500,   44.1667,   48.5833,   53.0000]
        
        Töre_Karadeniz_segah=	[0,5*22.64,      14*22.64,      22*22.64,      31*22.64,      36*22.64,      45*22.64,       49*22.64,           53*22.64]
        Töre_Karadeniz_huzzam=	[0,5*22.64,      14*22.64,      19.5*22.64,       31*22.64,      36*22.64,      45*22.64,       49*22.64,           53*22.64]
        Töre_Karadeniz_rast=	[0,9*22.64,      17*22.64,      22*22.64,      31*22.64,      39*22.64,      44*22.64,      48*22.64,           53*22.64,]
        Töre_Karadeniz_hicaz=	[0,5.5*22.64,      18.5*22.64,      22*22.64,       31*22.64,       35*22.64,      39*22.64,     44.5*22.64,           53*22.64]
        Töre_Karadeniz_saba=	[0,8*22.64,       13*22.64,      21*22.64,   30*22.64   ]
        Töre_Karadeniz_ussak=	[0,7*22.64,      8*22.64,       13*22.64,      22*22.64,       31*22.64,       35*22.64,      39*22.64,      44*22.64,           53*22.64]
        Töre_Karadeniz_huseyni=	[0,7*22.64,      8*22.64,       13*22.64,      22*22.64,       31*22.64,       35*22.64,      39*22.64,      44*22.64,           53*22.64]
        Töre_Karadeniz_buselik=	[0,9.5*22.64,      13*22.64,      22*22.64,       31*22.64  ]     
        Töre_Karadeniz_nikriz=	[0,9*22.64,      14.5*22.64,      27.5*22.64,       31*22.64    ]
        Töre_Karadeniz_ferahnak=	[0,5*22.64,      14*22.64,      22*22.64,       31*22.64]
        Töre_Karadeniz_nisabur=	[0,9*22.64,      12.5*22.64,      21.5*22.64,       25.5*22.64 ]
        Töre_Karadeniz_cargah=	[0,9*22.64,      18*22.64,      22*22.64,       31*22.64]
        Töre_Karadeniz_kurdi=	[0,5,5*22.64,      13*22.64,      22*22.64,       31*22.64 ]
        Töre_Karadeniz_pencgah=	[0,9*22.64,      18.5*22.64,      27.5*22.64,       31*22.64]        
        Töre_Karadeniz_mustear=	[0,10.5*22.64,      14*22.64,      22*22.64,       31*22.64] 
        Töre_Karadeniz_nihavend=	[0,9*22.64,       12.979*22.64,      21.9779*22.64,       31.003*22.64,       34.976*22.64,      44.0035*22.64,      48.0652*22.64,           53*22.64,]
        Töre_Karadeniz_kurdilihicazkar=	[0,4*22.64,       13*22.64,      22*22.64,       31*22.64,       35*22.64,      44*22.64,           53*22.64]
        Yekta_Arel_buselik=		[0,9.01*22.64,    12.99*22.64,    22*22.64,    31.01*22.64,     35*22.64,     44*22.64,     53*22.64 ]
        Yekta_Arel_cargah=		[0,9.01*22.64,    18.02*22.64,     22*22.64,     31.01*22.64,     35*22.64,     44*22.64,     53*22.64 ]
        Yekta_Arel_ferahnak=	[0,5.02*22.64,     14.03*22.64,     23.04*22.64,     31.01*22.64,     36*22.64,     45*22.64,     53*22.64 ]
        Yekta_Arel_hicaz=		[0,5.02*22.64,     16.98*22.64,  	 22*22.64,     31.01*22.64,     34.99*22.64,  38.97*22.64,  43.99*22.64,     53*22.64 ]
        Yekta_Arel_huseyni=		[0,7.97*22.64,  	12.99*22.64,  	22*22.64,     31.01*22.64,     38.97*22.64,  43.99*22.64,  53*22.64 ]
        Yekta_Arel_huzzam=		[0,5.02*22.64,  	14.03*22.64,  	 19.05*22.64,  31.01*22.64,     36.02*22.64,  49.02*22.64,  53*22.64 ]
        Yekta_Arel_kurdi=		[0,3.98*22.64,     12.99*22.64,     22*22.64,     31.01*22.64,     35*22.64,     44*22.64,     53*22.64]
        Yekta_Arel_mustear=		[0,9.01*22.64,     14.03*22.64,     22*22.64,     31.01*22.64,     36*22.64,     49*22.64,     53*22.64 ]
        Yekta_Arel_nikriz=		[0,9.01*22.64,     14.03*22.64,     25.98*22.64,     31.01*22.64,     40*22.64,     44*22.64,  48*22.64,  53*22.64 ]
        Yekta_Arel_nisabur=		[0,7.97*22.64,     12.99*22.64,     22*22.64,     25.98*22.64 ]
        Yekta_Arel_pencgah=		[0,9.01*22.64,     18.02*22.64,     25.99*22.64,     31.01*22.64 ]
        Yekta_Arel_rast=		[0,9.01*22.64,  16.98*22.64,  22*22.64,     31.01*22.64,     40.01*22.64,  47.98*22.64,  53*22.64]
        Yekta_Arel_saba=		[0,7.97*22.64,  12.99*22.64,  18.01*22.64,  31.01*22.64,     34.99*22.64,  43.99*22.64,  49.02*22.64,     61*22.64]
        Yekta_Arel_segah=		[0,5.02*22.64,  14.03*22.64,  22*22.64,     31.01*22.64,     36.02*22.64,  45.03*22.64,  49.02*22.64,     53*22.64 ]
        Yekta_Arel_ussak=		 [0,7.97*22.64,     12.99*22.64,     22*22.64,     31.01*22.64,        34.99*22.64,  43.99*22.64,  53*22.64 ]
        Yekta_Arel_beyati=		[0,8*22.64,     13*22.64,     22*22.64,     31*22.64,     35*22.64,     44*22.64,     53*22.64 ]
        Yekta_Arel_neva=		[0,8*22.64,     13*22.64,     22*22.64,     31*22.64,     39*22.64,     44*22.64,     53*22.64 ]
        Yekta_Arel_nisaburek=	[0,9*22.64,     17*22.64,     22*22.64,     31*22.64,     40*22.64,     44*22.64,     53*22.64 ]
        Yekta_Arel_acem=		[0,8*22.64,     13*22.64,     22*22.64,     31*22.64,     35*22.64,     44*22.64,     53*22.64 ]
        Yekta_Arel_ferahfeza=	[0,4*22.64,     13*22.64,     22*22.64,     31*22.64,     35*22.64,     44*22.64,     53*22.64 ]
        Yekta_Arel_kurdilihicazkar=	[0,3.99*22.64,  12.99*22.64,  22*22.64,     31*22.64,     34.99*22.64,  43.99*22.64,  53*22.64 ]
        Yekta_Arel_sehnaz=		[0,5*22.64,     17*22.64,     22*22.64,     31*22.64,     36*22.64,     48*22.64,     53*22.64 ]
        Yekta_Arel_hicazkar=		[0,5*22.64,     17*22.64,     22*22.64,     31*22.64,     36*22.64,     48*22.64,     53*22.64 ]
        Yekta_Arel_sedaraban=	[0,5*22.64,     17*22.64,     22*22.64,     31*22.64,     36*22.64,     48*22.64,     53*22.64 ]
        Yekta_Arel_neveser=		[0,5*22.64,     17*22.64,     22*22.64,     27*22.64,     39*22.64,     44*22.64,     53*22.64 ]
        Yekta_Arel_sultaniyegah=	[0,9*22.64,     13*22.64,     22*22.64,     31*22.64,     36*22.64,     48*22.64,     53*22.64 ]
        Yekta_Arel_suzidil=		[0,5*22.64,     18*22.64,     22*22.64,     31*22.64,     36*22.64,     48*22.64,     53*22.64 ]
        Yekta_Arel_gulizar=		[0,8*22.64,     13*22.64,     22*22.64,     31*22.64,     39*22.64,     44*22.64,     53*22.64 ]
        Yekta_Arel_tahirbuselik=	[0,8*22.64,     13*22.64,     22*22.64,     31*22.64,     39*22.64,     44*22.64,     53*22.64 ]
        Yekta_Arel_tahir=		[0,8*22.64,     13*22.64,     22*22.64,     31*22.64,     39*22.64,     44*22.64,     53*22.64 ]
        Yekta_Arel_muhayyer=	[0,8*22.64,     13*22.64,     22*22.64,     31*22.64,     39*22.64,     44*22.64,     53*22.64 ]
        Yekta_Arel_isfahan=		[0,8*22.64,     13*22.64,     22*22.64,     31*22.64,     35*22.64,     44*22.64,     53*22.64 ]
        Yekta_Arel_nuhuft=		[0,8*22.64,     13*22.64,     22*22.64,     30*22.64,     35*22.64,     44*22.64,     53*22.64 ]
        Yekta_Arel_beyatiaraban=	[0,8*22.64,     13*22.64,     22*22.64,     27*22.64,     39*22.64,     44*22.64,     53*22.64 ]
        Yekta_Arel_sevkefza=	[0,9*22.64,     18*22.64,     22*22.64,     26*22.64,  31*22.64, 36*22.64,  40*22.64,  48*22.64,     53*22.64 ]
        Yekta_Arel_nihavend=	[0,9.01*22.64,  12.99*22.64,  22*22.64,     31*22.64,     34.99*22.64,  43.99*22.64,  53*22.64 ]
        Yekta_Arel_pesendide=	[0,9*22.64,     17*22.64,     22*22.64,     31*22.64,     40*22.64,     48*22.64,     53*22.64 ]
        Yekta_Arel_suzinak=		[0,9*22.64,     17*22.64,     22*22.64,     31*22.64,     36*22.64,     48*22.64,     53*22.64 ]
        Yekta_Arel_yegah=		[0,9*22.64,     17*22.64,     22*22.64,     31*22.64,     39*22.64,     44*22.64,     53*22.64 ]
        Yekta_Arel_acemasiran=	[0,9*22.64,     18*22.64,     22*22.64,     31*22.64,     40*22.64,     49*22.64,     53*22.64 ]
        Yekta_Arel_mahur=		[0,9*22.64,     18*22.64,     22*22.64,     31*22.64,     40*22.64,     49*22.64,     53*22.64 ]
        Yekta_Arel_bestenigar=	[0,5*22.64,     14*22.64,     22*22.64,     27*22.64,     32*22.64,     45*22.64,     53*22.64 ]
        Yekta_Arel_evic=		[0,5*22.64,     14*22.64,     22*22.64,     31*22.64,     36*22.64,     49*22.64,     53*22.64 ]
        Yekta_Arel_irak=		[0, 5*22.64,     14*22.64,     22*22.64,     27*22.64,     36*22.64,     45*22.64,     53*22.64 ]
        Yekta_Arel_evcara=		[0, 5*22.64,     17*22.64,     22*22.64,     31*22.64,     36*22.64,     48*22.64,     53*22.64 ]
        Yekta_Arel_karcigar=	[0, 8*22.64,     13*22.64,     22*22.64,     27*22.64,     39*22.64,     44*22.64,     53*22.64 ]




        Templates=[Oniki_Tet_ussak,Oniki_Tet_huseyni,
        Oniki_Tet_hicaz,Oniki_Tet_saba,Oniki_Tet_kurdilihicazkar,Oniki_Tet_segah,
        Oniki_Tet_nihavend,Töre_Karadeniz_segah,Töre_Karadeniz_huzzam,Töre_Karadeniz_rast,
        Töre_Karadeniz_hicaz,Töre_Karadeniz_saba,Töre_Karadeniz_ussak,Töre_Karadeniz_huseyni,
        Töre_Karadeniz_buselik,Töre_Karadeniz_nikriz,Töre_Karadeniz_ferahnak,Töre_Karadeniz_nisabur,
        Töre_Karadeniz_cargah,Töre_Karadeniz_kurdi,Töre_Karadeniz_pencgah,Töre_Karadeniz_mustear,Töre_Karadeniz_nihavend,
        Töre_Karadeniz_kurdilihicazkar,Yekta_Arel_buselik,Yekta_Arel_cargah,Yekta_Arel_ferahnak,Yekta_Arel_hicaz,Yekta_Arel_huseyni,		
        Yekta_Arel_huzzam,Yekta_Arel_kurdi,	Yekta_Arel_mustear,Yekta_Arel_nikriz,Yekta_Arel_nisabur,		
        Yekta_Arel_pencgah,Yekta_Arel_rast,Yekta_Arel_saba,Yekta_Arel_segah,Yekta_Arel_ussak,Yekta_Arel_beyati,		
        Yekta_Arel_neva,Yekta_Arel_nisaburek,Yekta_Arel_acem,Yekta_Arel_ferahfeza,Yekta_Arel_kurdilihicazkar,	
    Yekta_Arel_sehnaz,Yekta_Arel_hicazkar,Yekta_Arel_sedaraban,Yekta_Arel_neveser,		
        Yekta_Arel_sultaniyegah,Yekta_Arel_suzidil,	Yekta_Arel_gulizar,	Yekta_Arel_tahirbuselik,	
        Yekta_Arel_tahir,Yekta_Arel_muhayyer,Yekta_Arel_isfahan,Yekta_Arel_nuhuft,		
        Yekta_Arel_beyatiaraban,Yekta_Arel_sevkefza,Yekta_Arel_nihavend,	
        Yekta_Arel_pesendide,Yekta_Arel_suzinak,Yekta_Arel_yegah,		
        Yekta_Arel_acemasiran,Yekta_Arel_mahur,Yekta_Arel_bestenigar,	
        Yekta_Arel_evic	,Yekta_Arel_irak,Yekta_Arel_evcara,		
        Yekta_Arel_karcigar	
    ]
        return Templates

    def getDataHist():
        peakshistogram=HistAnalyse.getHistDataNorm()
        return peakshistogram
    def findShiftAmount():
        peakhistdata=[]
        peakshistogram = getMakam.getDataHist()
        for i in range(len(peakshistogram)):
            peakhistdata.append(float(peakshistogram[i]))
        max_value = max(peakhistdata) 
        print("max_value----->", max_value)    
        shiftAmount = peakhistdata.index(max_value)
        print("shiftAmount----->",shiftAmount)    
        return shiftAmount

    def findPeakPoints():
        peakshistogram = getMakam.getDataHist()
        print("peakshist",peakshistogram)
        np.savetxt("peaakshistogram.txt", peakshistogram, fmt="%s")   
        peaksk, _ = find_peaks(peakshistogram, distance=90,height=5000)
        print("peaks",peaksk)
        return peaksk


    def reposition():
        shiftedPeakList=[]
        zeroShiftedPeakList=[]    
        peaksly=getMakam.findPeakPoints()
        shift=getMakam.findShiftAmount()
        print("peaksly....",peaksly) 
        print("shift....",shift) 
        for i in range(len(peaksly)):
            shiftedPeakList.append(peaksly[i]-shift)
        for y in range(len(shiftedPeakList)):
            if shiftedPeakList[y]>=0:
                zeroShiftedPeakList.append(shiftedPeakList[y])
        print("ZeroShifted....",zeroShiftedPeakList)        
        return zeroShiftedPeakList

    def findMakam():
        templatenames=getMakam.getTemplateNames()
        templates = getMakam.initTemplates()
        difflist=[]
        diffref=[]
        sumlist=[]
        indexes=[]
        peaks=getMakam.reposition()
        print("array", peaks)
        array=np.diff(peaks)
        print("array", array)
        for i in range(len(templates)):
            difflist.append(np.diff(templates[i]))
        for y in range(len(difflist)):   
            diffref.append(abs(np.subtract(array[:4],difflist[y][:4]))) 
        for z in range(len(diffref)):
            sumlist.append(sum(diffref[z]))
        #sorted(sumlist,reverse=True)
        min((abs(x), x) for x in sumlist)[1]
        print(min(sumlist, key=abs))
        index=sumlist.index(min(sumlist, key=abs))
        res = str.split(templatenames[index],"_")
        fir = res[0]
        fin = res[len(res)-1]
        matching = [s for s in templatenames if fin in s]
        for k in range(len(matching)):
            indexes.append(templatenames.index(matching[k]))
        print(matching)
        print(indexes)
        print(templates[index])
        print(peaks)
        return templates[index]

    def getMakamName():
        templatenames=getMakam.getTemplateNames()
        templates = getMakam.initTemplates()
        difflist=[]
        diffref=[]
        sumlist=[]
        indexes=[]
        peaks=getMakam.reposition()
        print("peaks", peaks)
        array=np.diff(peaks)
        print("array", array)
        for i in range(len(templates)):
            difflist.append(np.diff(templates[i]))
        for y in range(len(difflist)):   
            diffref.append(abs(np.subtract(array[:4],difflist[y][:4]))) 
        for z in range(len(diffref)):
            sumlist.append(sum(diffref[z]))
        #sorted(sumlist,reverse=True)
        min((abs(x), x) for x in sumlist)[1]
        index=sumlist.index(min(sumlist, key=abs))
        res = str.split(templatenames[index],"_")
        fir = res[0]
        fin = res[len(res)-1]
        matching = [s for s in templatenames if fin in s]
        for k in range(len(matching)):
            indexes.append(templatenames.index(matching[k]))
        return templatenames[index]

    def shiftedHistogram():    
        peakhistdata=[]
        Xarray=[]
        shiftedx=[]
        shiftAmount=getMakam.findShiftAmount()
        peakshistogram = HistAnalyse.getHistDataNorm()
        for i in peakshistogram:
            peakhistdata.append(float(i))
        for x in range(len(peakhistdata)):
            Xarray.append(x)
        for k in range(len(Xarray)):
            shiftedx.append(k-shiftAmount)
        return shiftedx

    def plot():
        #peaks=findPeakPoints()
        shiftedpeaks=getMakam.reposition()
        xaxis=getMakam.shiftedHistogram()
        yaxis=getMakam.getDataHist()
        makampoints=getMakam.findMakam()
        makamname=getMakam.getMakamName()
        peakhistdata=[]
        yarray=[]
        yarray1=[]
        for y in range(len(makampoints)):
            yarray1.append(12000)
        peakshistogram = HistAnalyse.getHistDataNorm()
        for i in peakshistogram:
            peakhistdata.append(float(i))
        for x in range(len(shiftedpeaks)):
            yarray.append(10000)

        #plt.annotate("TahminEdilenMakam",(makampoints,yarray1), arrowprops=dict(facecolor='black', shrink=0.05))
        plt.figure(3)
        plt.xlim(-200,800)
        plt.xticks(np.arange(-200,800,step=20),rotation=90, fontsize=8)     
        plt.scatter(makampoints,yarray1,color='green')  
        plt.scatter(shiftedpeaks,yarray,color="red")
        plt.plot(xaxis,yaxis,color="blue")
        plt.legend(('Teorik_Tahmin'+makamname,'İşlenen_Eser','İşlenen Eser Histogram'),loc='upper left')
        plt.title("Tahmin Edilen Makam " + makamname)
        #plt.axvline(makampoints, 0, 0.8, color='green', label='plot a green vertical line')
        plt.stem(makampoints, yarray1)
        plt.show()    
    