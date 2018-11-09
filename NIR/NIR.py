# -*- coding: utf-8 -*-
#!/usr/bin/python
# -*- coding: utf-8 -*-
#Martin Sparre, DARK, 2nd November 2011
#version 5.9.0

from PipelineManager import *
import glob

NIR = PipelineManager()
NIR.SetOutputDir('Output')


############################################################
###  XSH_SCIRED_SLIT_NOD
############################################################

EsorexName='xsh_scired_slit_nod'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)
NIR.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_NOD_NIR", "1..n", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_NIR", "?", "-" ,"-")
NIR.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName,"RESPONSE_MERGE1D_SLIT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_NIR", "1", "-", "-")

NIR.EnableRecipe(SOFFileName)

############################################################
###  XSH_SCIRED_SLIT_STARE
############################################################

EsorexName='xsh_scired_slit_stare'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)
NIR.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_STARE_NIR", "1..n", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_NIR", "?", "-" ,"-")
NIR.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName,"RESPONSE_MERGE1D_SLIT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_NIR", "1", "-", "-")
#NIR.EnableRecipe(SOFFileName)

#NIR.SetRecipeOptions(SOFFileName, "--sky-method=MEDIAN")#MEDIAN is more stable than bspline
#NIR.SetRecipeOptions(SOFFileName, "--sky-bspline-order=4")
#NIR.SetRecipeOptions(SOFFileName, "--sky-subtract=FALSE")

#options from Stefan and Sune (these options might give better sky-subtraction):
#NIR.SetRecipeOptions(SOFFileName, "--background-nb-y=50 --background-radius-y=40 --background-method=median --rectify-bin-lambda=.05 --rectify-bin-slit=.2 --removecrhsingle-niter=3 --extract-method=FULL --compute-map=TRUE --rectify-conserve-flux=FALSE --sky-subtract=TRUE --sky-bspline-nbkpts-first=500 --sky-bspline-nbkpts-second=500 --sky-method=MEDIAN  --rectify-radius=1 --mergeord-method=0")

############################################################
###  XSH_SCIRED_SLIT_OFFSET
############################################################

EsorexName='xsh_scired_slit_offset'
SOFFileName = EsorexName

NIR.DeclareNewRecipe(EsorexName)
NIR.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_OFFSET_NIR", "1..n", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SKY_SLIT_NIR", "1..n", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_NIR", "1", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_DARK_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_NIR", "?", "-", "-")
NIR.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_NIR", "?", "-" ,"-")
NIR.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName,"RESPONSE_MERGE1D_SLIT_NIR", "?", "-" , "-")
NIR.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_NIR", "1", "-", "-")
#NIR.EnableRecipe(SOFFileName)

############################################################
###  INPUT-FILES
############################################################

# Input files
NIR.SetFiles('OBJECT_SLIT_NOD_NIR', glob.glob('test_data/*'))


#STATIC
NIR.SetFiles('MASTER_DARK_NIR',['static_calibs/MASTER_DARK_NIR_600.fits'])
NIR.SetFiles('MASTER_FLAT_SLIT_NIR',['static_calibs/MASTER_FLAT_SLIT_NIR.fits'])
NIR.SetFiles('ORDER_TAB_EDGES_SLIT_NIR',['static_calibs/ORDER_TAB_EDGES_SLIT_NIR.fits'])
NIR.SetFiles('XSH_MOD_CFG_OPT_2D_NIR',['static_calibs/XSH_MOD_CFG_OPT_2D_NIR.fits'])
NIR.SetFiles('RESPONSE_MERGE1D_SLIT_NIR',['static_calibs/RESPONSE_MERGE1D_SLIT_NIR.fits'])
NIR.SetFiles('DISP_TAB_NIR',['static_calibs/DISP_TAB_NIR.fits'])



#REF-files:
NIR.SetFiles("SPECTRAL_FORMAT_TAB_NIR",["/opt/local/share/esopipes/datastatic/xshoo-3.2.0/SPECTRAL_FORMAT_TAB_NIR.fits"])
NIR.SetFiles("ARC_LINE_LIST_NIR",["/opt/local/share/esopipes/datastatic/xshoo-3.2.0/ARC_LINE_LIST_AFC_NIR.fits"])
NIR.SetFiles("XSH_MOD_CFG_TAB_NIR",["/opt/local/share/esopipes/datastatic/xshoo-3.2.0/XS_GMCT_110710A_NIR.fits"])
NIR.SetFiles("FLUX_STD_CATALOG_NIR",['/opt/local/share/esopipes/datastatic/xshoo-3.2.0/xsh_star_catalog_NIR.fits'])
NIR.SetFiles("ATMOS_EXT_NIR",['/opt/local/share/esopipes/datastatic/xshoo-3.2.0/xsh_paranal_extinct_model_NIR.fits'])
NIR.SetFiles('MASTER_BP_MAP_NIR',['/opt/local/share/esopipes/datastatic/xshoo-3.2.0/BP_MAP_RP_NIR.fits'])
#Run
NIR.RunPipeline()


