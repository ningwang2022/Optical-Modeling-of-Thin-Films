# -*- coding: utf-8 -*-
"""
citation：
@author: C. Marcus Chuang, 2015
updated：
@author: Ning Wang, 2023
"""
from TransferMatrix import OpticalModeling
import matplotlib.pyplot as plt
import os
import datetime
plt.style.use('ggplot')  # or use 'classic' or any in plt.style.available


"""
Device Information
"""
Device = [
          ("Glass"  , 30),
          ("ITO"    , 30),
          ("PEDOT:PSS"    , 30),
          ("PM6L8BOOFIB"    , 120),
          ("PDINN"     , 30)
         ]


"""
file name setting
"""
SampleName = "PM6L8BOOFIB"
libname = SampleName + ".csv"

if not os.path.exists("Result"):
    os.makedirs("Result")
TimeTable = datetime.datetime.now().strftime('%Y%m%d %H%M%S')
os.mkdir("Result/" + TimeTable)
SaveName = "Result/" + TimeTable + "/"  # prefix of the file names

# file name of the AM1.5 solar spectra
Solarfile = "SolarAM15.csv"  # Wavelength vs  mW*cm-2*nm-1
wavelength_range = [300, 1000]  # wavelength range (nm) to model [min, max]

# ------------------- End of Mandatary input -------------------------------
# optioanl input ------

posstep = 1.0  # step size for thickness, must be <= the thinnest layer
WLstep = 2.0  # wavelength step size (nm)

# selected wavelengths for "E vs position plot",
# can be several values or a single value,
# if set to None or not provided, automatically select 1 or 3 values
# with gap of a multiple of 50 nm
plotWL = [451, 605, 751, 954]

plotE = True   # whehter to plot E-field vs wavelength
plotAbs = True  # whether to plot absorption vs wavelength
plotGen = True  # whether to plot generation rate and spectral absorption rate

# whether to save the data as csv files
saveDataE, saveDataAbs, saveDataGen = True, True, True #False, False, False
# wherther to save the figures
# default format is vector graphic 'pdf' (with non-transparent background)
# can also use 'png', 'jpg' or someother format matplotlib supports
figformat = 'pdf'
saveFigE, saveFigAbs, saveFigGen = True, True, True #False, False, False

# ------------------- End of user input -------------------------------


if __name__ == "__main__":

    # ### --------------- run with Mandatary input only --------
    # initialize an OpticalModeling obj OM
    # OM = OpticalModeling(Device, libname=libname, WLrange=wavelength_range)
    # do all the caculation
    # OM.RunSim()
    # ## ---------------------------------------------------------------------

    # ### --------------- run with all the user input  --------
    # initialize an OpticalModeling obj OM
    OM = OpticalModeling(Device, libname=libname, WLrange=wavelength_range,
                         plotWL=plotWL, WLstep=WLstep, posstep=posstep)
    OM.RunSim(plotE=plotE, plotAbs=plotAbs, plotGen=plotGen,
              saveFigE=saveFigE, saveFigAbs=saveFigAbs, saveFigGen=saveFigGen,
              figformat='pdf', savename=SaveName)
    # ###----------------------------------------------------------------------
    plt.show()

    summary = OM.JscReport()  # print and return a summary report
    # ## save data as csv or not
    OM.SaveData(savename=SaveName,
                saveE=saveDataE, saveAbs=saveDataAbs, saveGen=saveDataGen)



