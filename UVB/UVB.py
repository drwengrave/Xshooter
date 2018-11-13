#!/usr/bin/python
# -*- coding: utf-8 -*-
#Martin Sparre, DARK, 2nd November 2011
#version 5.9.0

from PipelineManager import *
import glob

UVB = PipelineManager()
UVB.SetOutputDir('Output')



############################################################
###  XSH_SCIRED_SLIT_NOD
############################################################

EsorexName='xsh_scired_slit_nod'
SOFFileName = EsorexName

UVB.DeclareNewRecipe(EsorexName)
UVB.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_NOD_UVB", "1..n", "any", "100k")
UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_UVB", "?", "1x1", "400k")
UVB.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_UVB", "?", "-" ,"-")
UVB.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_UVB", "?", "-" , "-")
UVB.DeclareRecipeInputTag(SOFFileName,"RESPONSE_MERGE1D_SLIT_UVB", "?", "-" , "-")

UVB.EnableRecipe(SOFFileName)

############################################################
###  XSH_SCIRED_SLIT_STARE
############################################################

EsorexName='xsh_scired_slit_stare'
SOFFileName = EsorexName

UVB.DeclareNewRecipe(EsorexName)
UVB.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_STARE_UVB", "1", "any", "any")
UVB.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_UVB", "1", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_UVB", "1", "-", "-")
UVB.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_UVB", "?", "match", "match")
UVB.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_UVB", "?", "1x1", "400k")
UVB.DeclareRecipeInputTag(SOFFileName, "FLUX_STD_CATALOG_UVB", "?", "-" ,"-")
UVB.DeclareRecipeInputTag(SOFFileName, "ATMOS_EXT_UVB", "?", "-" , "-")
UVB.DeclareRecipeInputTag(SOFFileName, "RESPONSE_MERGE1D_SLIT_UVB", "?", "-" , "-")
UVB.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_TAB_UVB", "1", "-", "-")

# UVB.EnableRecipe(SOFFileName)

############################################################
###  INPUT-FILES
############################################################

# Input files
files = glob.glob('test_data/*') # /target

# Object files
# UVB.SetFiles('OBJECT_SLIT_STARE_UVB', files)
UVB.SetFiles('OBJECT_SLIT_NOD_UVB', files)

# Static CALIBs
UVB.SetFiles('MASTER_BIAS_UVB',['static_calibs/MASTER_BIAS_UVB.fits'])
UVB.SetFiles('MASTER_FLAT_SLIT_UVB',['static_calibs/MASTER_FLAT_SLIT_UVB.fits'])
UVB.SetFiles('ORDER_TAB_EDGES_SLIT_UVB',['static_calibs/ORDER_TAB_EDGES_SLIT_UVB.fits'])
UVB.SetFiles('XSH_MOD_CFG_OPT_2D_UVB',['static_calibs/XSH_MOD_CFG_OPT_2D_UVB.fits'])
UVB.SetFiles('RESPONSE_MERGE1D_SLIT_UVB',['static_calibs/RESPONSE_MERGE1D_SLIT_UVB.fits'])
UVB.SetFiles('DISP_TAB_UVB',['static_calibs/DISP_TAB_UVB.fits'])

#REF-files:
UVB.SetFiles("SPECTRAL_FORMAT_TAB_UVB",["static_calibs/SPECTRAL_FORMAT_TAB_UVB.fits"])
UVB.SetFiles("ARC_LINE_LIST_UVB",["static_calibs/ThAr_uvb_2012PBR.fits"])
UVB.SetFiles("XSH_MOD_CFG_TAB_UVB",["static_calibs/XS_GMCT_110710A_UVB.fits"])
UVB.SetFiles("FLUX_STD_CATALOG_UVB",['static_calibs/xsh_star_catalog_uvb.fits'])
UVB.SetFiles("ATMOS_EXT_UVB",['static_calibs/xsh_paranal_extinct_model_uvb.fits'])
UVB.SetFiles("SKY_LINE_LIST_UVB",['static_calibs/SKY_LINE_LIST_UVB.fits'])
UVB.SetFiles('MASTER_BP_MAP_UVB',['static_calibs/BP_MAP_RP_UVB_1x2.fits'])

#Run
UVB.RunPipeline()
