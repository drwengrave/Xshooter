#!/usr/bin/python
# -*- coding: utf-8 -*-
#Martin Sparre, DARK, 2nd November 2011
#version 5.9.0

from PipelineManager import *
import glob

VIS = PipelineManager()
VIS.SetOutputDir('Output')


############################################################
###  XSH_SCIRED_SLIT_NOD
############################################################

EsorexName='xsh_scired_slit_nod'
SOFFileName = EsorexName

VIS.DeclareNewRecipe(EsorexName)
VIS.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_NOD_VIS", "1..n", "any", "100k")
VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_VIS", "?", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_VIS", "?", "-" ,"-")
VIS.DeclareRecipeInputTag(SOFFileName,"RESPONSE_MERGE1D_SLIT_VIS", "?", "-" , "-")
VIS.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_VIS", "?", "-" , "-")

VIS.EnableRecipe(SOFFileName)

#VIS.SetRecipeOptions(SOFFileName,'--rectify-bin-lambda=0.025')

############################################################
###  XSH_SCIRED_SLIT_STARE
############################################################

EsorexName='xsh_scired_slit_stare'
SOFFileName = EsorexName

VIS.DeclareNewRecipe(EsorexName)
VIS.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_STARE_VIS", "1..n", "any", "100k")
VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_VIS", "?", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_VIS", "?", "-" ,"-")
VIS.DeclareRecipeInputTag(SOFFileName,"RESPONSE_MERGE1D_SLIT_VIS", "?", "-" , "-")
VIS.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_VIS", "?", "-" , "-")

#VIS.EnableRecipe(SOFFileName)


############################################################
###  XSH_SCIRED_SLIT_OFFSET
############################################################

EsorexName='xsh_scired_slit_offset'
SOFFileName = EsorexName

VIS.DeclareNewRecipe(EsorexName)
VIS.DeclareRecipeInputTag(SOFFileName, "OBJECT_SLIT_OFFSET_VIS", "1..n", "any", "100k")
VIS.DeclareRecipeInputTag(SOFFileName, "SKY_SLIT_VIS", "1..n", "match", "100k")
VIS.DeclareRecipeInputTag(SOFFileName, "SPECTRAL_FORMAT_TAB_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_FLAT_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BIAS_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "ORDER_TAB_EDGES_SLIT_VIS", "1", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "XSH_MOD_CFG_OPT_2D_VIS", "1", "-", "-")
VIS.DeclareRecipeInputTag(SOFFileName, "MASTER_BP_MAP_VIS", "?", "match", "match")
VIS.DeclareRecipeInputTag(SOFFileName, "DISP_TAB_VIS", "?", "1x1", "400k")
VIS.DeclareRecipeInputTag(SOFFileName,"FLUX_STD_CATALOG_VIS", "?", "-" ,"-")
VIS.DeclareRecipeInputTag(SOFFileName,"RESPONSE_MERGE1D_SLIT_VIS", "?", "-" , "-")
VIS.DeclareRecipeInputTag(SOFFileName,"ATMOS_EXT_VIS", "?", "-" , "-")

#VIS.EnableRecipe(SOFFileName)

############################################################
###  INPUT-FILES
############################################################

#CALIB and RAW
VIS.SetFiles('MASTER_BIAS_VIS',['static_calibs/MASTER_BIAS_VIS.fits'])
VIS.SetFiles('MASTER_FLAT_SLIT_VIS',['static_calibs/MASTER_FLAT_SLIT_VIS.fits'])
VIS.SetFiles('ORDER_TAB_EDGES_SLIT_VIS',['static_calibs/ORDER_TAB_EDGES_SLIT_VIS.fits'])
VIS.SetFiles('XSH_MOD_CFG_OPT_2D_VIS',['static_calibs/XSH_MOD_CFG_OPT_2D_VIS.fits'])
VIS.SetFiles('RESPONSE_MERGE1D_SLIT_VIS',['static_calibs/RESPONSE_MERGE1D_SLIT_VIS.fits'])
VIS.SetFiles('DISP_TAB_VIS',['static_calibs/DISP_TAB_VIS.fits'])
VIS.SetFiles('OBJECT_SLIT_NOD_VIS', glob.glob('test_data/*'))

#REF-files:
VIS.SetFiles("SPECTRAL_FORMAT_TAB_VIS",["/opt/local/share/esopipes/datastatic/xshoo-3.2.0/SPECTRAL_FORMAT_TAB_VIS.fits"])
VIS.SetFiles("ARC_LINE_LIST_VIS",["/opt/local/share/esopipes/datastatic/xshoo-3.2.0/ThAr_vis_custom.fits"])
VIS.SetFiles("XSH_MOD_CFG_TAB_VIS",["/opt/local/share/esopipes/datastatic/xshoo-3.2.0/XS_GMCT_110710A_VIS.fits"])
VIS.SetFiles("FLUX_STD_CATALOG_VIS",['/opt/local/share/esopipes/datastatic/xshoo-3.2.0/xsh_star_catalog_VIS.fits'])
VIS.SetFiles("ATMOS_EXT_VIS",['/opt/local/share/esopipes/datastatic/xshoo-3.2.0/xsh_paranal_extinct_model_VIS.fits'])
VIS.SetFiles("SKY_LINE_LIST_VIS",['/opt/local/share/esopipes/datastatic/xshoo-3.2.0/SKY_LINE_LIST_VIS.fits'])
VIS.SetFiles('MASTER_BP_MAP_VIS',['/opt/local/share/esopipes/datastatic/xshoo-3.2.0/BP_MAP_RP_VIS_1x2.fits'])

#Run
VIS.RunPipeline()
