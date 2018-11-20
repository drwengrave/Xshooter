#!/usr/bin/python
# -*- coding: utf-8 -*-
#Martin Sparre, DARK, 2nd November 2011
#version 5.9.0

from PipelineManager import *
import glob
import numpy as np

VIS = PipelineManager()
VIS.SetOutputDir('Output')


############################################################
###  XSH_SCIRED_SLIT_NOD
############################################################

EsorexName='xsh_scired_slit_nod'
SOFFileName1 = EsorexName

VIS.DeclareNewRecipe(EsorexName)
VIS.DeclareRecipeInputTag(SOFFileName1, "OBJECT_SLIT_NOD_VIS", "1..n", "any", "100k")
VIS.DeclareRecipeInputTag(SOFFileName1, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName1, "MASTER_FLAT_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName1, "MASTER_BIAS_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName1, "ORDER_TAB_EDGES_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName1, "XSH_MOD_CFG_OPT_2D_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName1, "MASTER_BP_MAP_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName1, "DISP_TAB_VIS", "?", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName1,"FLUX_STD_CATALOG_VIS", "?", "-" ,"-")
VIS.DeclareRecipeInputTag(SOFFileName1,"RESPONSE_MERGE1D_SLIT_VIS", "?", "-" , "-")
VIS.DeclareRecipeInputTag(SOFFileName1,"ATMOS_EXT_VIS", "?", "-" , "-")

############################################################
###  XSH_SCIRED_SLIT_STARE
############################################################

EsorexName='xsh_scired_slit_stare'
SOFFileName2 = EsorexName

VIS.DeclareNewRecipe(EsorexName)
VIS.DeclareRecipeInputTag(SOFFileName2, "OBJECT_SLIT_STARE_VIS", "1..n", "any", "100k")
VIS.DeclareRecipeInputTag(SOFFileName2, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName2, "MASTER_FLAT_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName2, "MASTER_BIAS_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName2, "ORDER_TAB_EDGES_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName2, "XSH_MOD_CFG_OPT_2D_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName2, "MASTER_BP_MAP_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName2, "DISP_TAB_VIS", "?", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName2,"FLUX_STD_CATALOG_VIS", "?", "-" ,"-")
VIS.DeclareRecipeInputTag(SOFFileName2,"RESPONSE_MERGE1D_SLIT_VIS", "?", "-" , "-")
VIS.DeclareRecipeInputTag(SOFFileName2,"ATMOS_EXT_VIS", "?", "-" , "-")

############################################################
###  INPUT-FILES: TO BE MODIFIED
############################################################

## FOLDER WITH IMAGES
files = glob.glob('target/*') # /target

##
## NODDING MODE
##
VIS.EnableRecipe(SOFFileName1)
VIS.SetFiles('OBJECT_SLIT_NOD_VIS', files)

##
## STARING MODE
##
#VIS.EnableRecipe(SOFFileName2)
#VIS.SetFiles('OBJECT_SLIT_STARE_VIS', files)

############################################################

# Static CALIBs
VIS.SetFiles('MASTER_BIAS_VIS',['static_calibs/MASTER_BIAS_VIS.fits'])
VIS.SetFiles('MASTER_FLAT_SLIT_VIS',['static_calibs/MASTER_FLAT_SLIT_VIS.fits'])
VIS.SetFiles('ORDER_TAB_EDGES_SLIT_VIS',['static_calibs/ORDER_TAB_EDGES_SLIT_VIS.fits'])
VIS.SetFiles('XSH_MOD_CFG_OPT_2D_VIS',['static_calibs/XSH_MOD_CFG_OPT_2D_VIS.fits'])
VIS.SetFiles('RESPONSE_MERGE1D_SLIT_VIS',['static_calibs/RESPONSE_MERGE1D_SLIT_VIS.fits'])
VIS.SetFiles('DISP_TAB_VIS',['static_calibs/DISP_TAB_VIS.fits'])

#REF-files:
VIS.SetFiles("SPECTRAL_FORMAT_TAB_VIS",["static_calibs/SPECTRAL_FORMAT_TAB_VIS.fits"])
VIS.SetFiles("ARC_LINE_LIST_VIS",["static_calibs/ThAr_vis_custom.fits"])
VIS.SetFiles("XSH_MOD_CFG_TAB_VIS",["static_calibs/XS_GMCT_110710A_VIS.fits"])
VIS.SetFiles("FLUX_STD_CATALOG_VIS",['static_calibs/xsh_star_catalog_vis.fits'])
VIS.SetFiles("ATMOS_EXT_VIS",['static_calibs/xsh_paranal_extinct_model_vis.fits'])
VIS.SetFiles("SKY_LINE_LIST_VIS",['static_calibs/SKY_LINE_LIST_VIS.fits'])
VIS.SetFiles('MASTER_BP_MAP_VIS',['static_calibs/BP_MAP_RP_VIS_1x2.fits'])

#Run
VIS.RunPipeline()

# Convert 1D file to ASCII
out1d = glob.glob("Output/*FLUX_MERGE1D_VIS*.fits")
fitsfile = fits.open(out1d[0])
wave = 10.*(np.arange((np.shape(fitsfile[0].data)[0]))*fitsfile[0].header['CDELT1']+fitsfile[0].header['CRVAL1'])
np.savetxt("Output/VIS_ASCII1D_spectrum.dat", list(zip(wave, fitsfile[0].data, fitsfile[1].data)), fmt='%1.4e %1.4e %1.4e')





