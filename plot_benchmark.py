import ROOT as rt
import tdr
import array
from numpy import *
from ROOT import TCanvas, TGraph, TLine
from ROOT import kBlack, kBlue, kRed, kWhite, kOrange


def ratio_gaph(gr1,gr2):
    gr3=gr1.Clone()
    x1, y1, x2, y2 = rt.Double(0), rt.Double(0), rt.Double(0), rt.Double(0)
    for i in range(gr1.GetN()):
        gr1.GetPoint(i,x1,y1)
        gr2.GetPoint(i,x2,y2)
        gr3.SetPoint(i,x1,y1/y2)
    return gr3


#set the tdr style
tdr.setTDRStyle()

W = 800;
H = 800;

# references for T, B, L, R
T = 0.08*W
B = 0.10*W 
L = 0.10*W
R = 0.10*W

#LL results
#scetlib ="../inputs/scetlib/scetlib_5gen_QmZ_Y0_LL_level1_qt.txt"
#resolve ="../inputs/resolve/results_30_06_19/reSolve_5gen_QmZ_Y0_LL_level1_qt.txt"
#nanga="../inputs/nangaparbat/nangaparbat_5gen_QmZ_Y0_LL_level1_qt.txt"
#dyres="../inputs/dyres/dyres_5gen_QmZ_Y0_LL_level1_qt.txt"

#NLL results
#scetlib ="../inputs/scetlib/scetlib_5gen_QmZ_Y0_NLL_level1_qt.txt"
#resolve ="../inputs/resolve/results_30_06_19/reSolve_5gen_QmZ_Y0_LL_level1_qt.txt"
#cute ="../inputs/cute/CuTe_5gen_QmZ_Y0_NLL_level1_qt.txt"
#nanga="../inputs/nangaparbat/nangaparbat_5gen_QmZ_Y0_NLL_level1_qt.txt"

#NLLp results
#scetlib ="../inputs/scetlib/scetlib_5gen_QmZ_Y0_NLLp_level1_qt.txt"
#resolve ="../inputs/resolve/results_30_06_19/reSolve_5gen_QmZ_Y0_NLLp_level1_qt.txt"
#cute ="../inputs/cute/CuTe_5gen_QmZ_Y0_NLL_level1_qt.txt"
#nanga="../inputs/nangaparbat/nangaparbat_5gen_QmZ_Y0_NLL_level1_qt.txt"

#NNLLp results
#scetlib ="../inputs/scetlib/scetlib_5gen_QmZ_Y0_NNLLp_level1_qt.txt"
#resolve ="../inputs/resolve/results_30_06_19/reSolve_5gen_QmZ_Y0_NNLLp_level1_qt.txt"
#cute ="../inputs/cute/CuTe_5gen_QmZ_Y0_NNLL_level1_qt.txt"
#nanga="../inputs/nangaparbat/nangaparbat_5gen_QmZ_Y0_NNLLp_level1_qt.txt"

#NNLL results
#scetlib ="../inputs/scetlib/scetlib_5gen_QmZ_Y0_NNLL_level1_qt.txt"
#resolve ="../inputs/resolve/results_30_06_19/reSolve_5gen_QmZ_Y0_NNLLp_level1_qt.txt"
#cute ="../inputs/cute/CuTe_5gen_QmZ_Y0_NNLL_level1_qt.txt"
#nanga="../inputs/nangaparbat/NangaParbat_5gen_QmZ_Y0_NNLL_level1_qt.txt"
#radish="../inputs/radish/RadISH_5gen_QmZ_Y0_NNLL_level1_qt.txt"
#dyres="../inputs/dyres/dyres_5gen_QmZ_Y0_NNLL_level1_qt.txt"

#LL results
#scetlib ="../inputs/scetlib/scetlib_5gen_QmZ_Y0_LL_level1_qt.txt"
#resolve ="../inputs/resolve/results_30_06_19/reSolve_can_LL_y0_mZ_qtlin_benchmark_new_histo_0_qT.dat"
#cute ="../inputs/cute/CuTe_5gen_QmZ_Y0_NLL_level1_qt.txt"
#nanga="../inputs/nangaparbat/NangaParbat_5gen_QmZ_Y0_LL_level1_qt.txt"
#radish="../inputs/radish/RadISH_5gen_QmZ_Y0_NLL_level1_qt.txt"
#pbtmd="../inputs/PB-TMD/group_5gen_Qmz_Y0_level1_qt.txt"
#artemide="../inputs/artemide/round2/Qmz_Y0/xSec_DY_Z_Qmz_Y0_LL.txt"
#dyres="../inputs/dyres/dyres_5gen_QmZ_Y0_LL_level1_qt.txt"

#NLL results
#scetlib ="../inputs/scetlib/scetlib_5gen_QmZ_Y0_NLL_level1_qt.txt"
#resolve ="../inputs/resolve/results_30_06_19/reSolve_5gen_QmZ_Y0_NLLp_level1_qt.txt"
#cute ="../inputs/cute/CuTe_5gen_QmZ_Y0_NLL_level1_qt.txt"
#nanga="../inputs/nangaparbat/NangaParbat_5gen_QmZ_Y0_NLL_level1_qt.txt"
#radish="../inputs/radish/RadISH_5gen_QmZ_Y0_NLL_level1_qt.txt"
#pbtmd="../inputs/PB-TMD/group_5gen_Qmz_Y0_level1_qt.txt"
#artemide="../inputs/artemide/round2/Qmz_Y0/xSec_DY_Z_Qmz_Y0_NLL.txt"
#dyres="../inputs/dyres/dyres_5gen_QmZ_Y0_NLL_level1_qt.txt"

#NNLL results
#scetlib ="../inputs/scetlib/scetlib_5gen_QmZ_Y0_NNLL_level1_qt.txt"
#resolve ="../inputs/resolve/results_30_06_19/reSolve_can_NLLp_y0_mZ_qtlin_benchmark_new_histo_0_qT.dat"
#cute ="../inputs/cute/CuTe_5gen_QmZ_Y0_NNLL_level1_qt.txt"
#nanga="../inputs/nangaparbat/NangaParbat_5gen_QmZ_Y0_NNLL_level1_qt.txt"
#radish="../inputs/radish/RadISH_5gen_QmZ_Y0_NNLL_level1_qt.txt"
#pbtmd="../inputs/PB-TMD/group_5gen_Qmz_Y0_level1_qt.txt"
#artemide="../inputs/artemide/round2/Qmz_Y0/xSec_DY_Z_Qmz_Y0_NNLL.txt"
#dyres="../inputs/dyres/dyres_5gen_QmZ_Y0_NLL_level1_qt.txt"

#NNNLL results
scetlib ="../inputs/scetlib/scetlib_5gen_QmZ_Y0_N3LL_level1_qt.txt"
resolve ="../inputs/resolve/results_30_06_19/reSolve_can_NNLLp_y0_mZ_qtlin_benchmark_new_histo_0_qT.dat"
cute ="../inputs/cute/CuTe_5gen_QmZ_Y0_NNNLL_level1_qt.txt"
nanga="../inputs/nangaparbat/NangaParbat_5gen_QmZ_Y0_NNNLL_level1_qt.txt"
radish="../inputs/radish/RadISH_5gen_QmZ_Y0_NNNLL_level1_qt.txt"
pbtmd="../inputs/PB-TMD/group_5gen_Qmz_Y0_level1_qt.txt"
artemide="../inputs/artemide/round2/Qmz_Y0/xSec_DY_Z_Qmz_Y0_N3LL.txt"
dyres="../inputs/dyres/dyres_5gen_QmZ_Y0_NNLL_level1_qt.txt"

#NNNLL log10qt results
#scetlib ="../inputs/scetlib/scetlib_5gen_QmZ_Y0_LL_level1_logqt.txt"
#resolve ="../inputs/resolve/results_30_06_19/reSolve_5gen_QmZ_Y0_LL_level1_qtlog.txt"
#cute ="../inputs/cute/CuTe_5gen_QmZ_Y0_NNNLL_level1_qt.txt"
#nanga="../inputs/nangaparbat/NangaParbat_5gen_QmZ_Y0_LL_level1_logqt.txt"
#radish="../inputs/radish/RadISH_5gen_QmZ_Y0_NNNLL_level1_qt.txt"

#2 gen results
#scetlib ="../inputs/scetlib/scetlib_2gen_QmZ_Y0_NLL_level1_qt.txt"
#resolve ="../inputs/scetlib/scetlib_5gen_QmZ_Y0_NLL_level1_qt.txt"
#cute ="../inputs/cute/CuTe_2gen_QmZ_Y0_NLL_level1_qt.txt"
#nanga="../inputs/cute/CuTe_5gen_QmZ_Y0_NLL_level1_qt.txt"

#NNLLp results, |Y|=2.4, Q=MZ
#scetlib ="../inputs/scetlib/scetlib_5gen_QmZ_Y0_NNLLp_level1_qt.txt"
#resolve ="../inputs/resolve/results_30_06_19/reSolve_5gen_QmZ_Y2.4_NLLp_level1_qt.txt"
#cute ="../inputs/cute/CuTe_5gen_QmZ_Y2p4_NLL_level1_qt.txt"
#nanga="../inputs/nangaparbat/nangaparbat_5gen_QmZ_Y2.4_NLLp_level1_qt.txt"

scetx, scety = loadtxt(scetlib, unpack=True, usecols=[0,1])
resolvex, resolvey = loadtxt(resolve, unpack=True, usecols=[0,1])
cutex, cutey = loadtxt(cute, unpack=True, usecols=[0,1])
nangax, nangay = loadtxt(nanga, unpack=True, usecols=[0,1])
radishx, radishy = loadtxt(radish, unpack=True, usecols=[0,1])
dyresx, dyresy = loadtxt(dyres, unpack=True, usecols=[0,1])
pbtmdx, pbtmdy = loadtxt(pbtmd, unpack=True, usecols=[0,1])
artemidex, artemidey = loadtxt(artemide, unpack=True, usecols=[1,3])

xrange=102

#print(scetx)
#print("now the y axis")
#print(len(scety))

canvas = rt.TCanvas("c2","c2",50,50,W,H)
canvas.SetFillColor(0)
canvas.SetBorderMode(0)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)
canvas.SetLeftMargin( L/W )
canvas.SetRightMargin( R/W )
canvas.SetTopMargin( T/H )
canvas.SetBottomMargin( B/H )
canvas.SetTickx(1)
canvas.SetTicky(1)

split_point=0.29
gap=0.005
upper = rt.TPad("upper", "upper", 0., 0., 1., 1.)
upper.SetBottomMargin(split_point + gap)
upper.SetFillStyle(4000)
upper.Draw()
lower = rt.TPad("lower", "lower", 0., 0., 1., 1.)
lower.SetTopMargin(1 - split_point + gap)
lower.SetFillStyle(4000)
lower.Draw()
upper.cd()

gr_scet = TGraph( len(scetx), array(scetx), array(scety) )
#gr_scet = TGraph( len(nangax), array(nangax), array(nangay) )
gr_scet.SetLineColor(kRed)
gr_scet.SetMarkerStyle(20)
gr_scet.SetMarkerColor(kRed)
gr_scet.SetLineWidth(2)
gr_scet.SetMarkerSize(1.1)
gr_scet.GetXaxis().SetTitle("q_{T} (GeV)")
gr_scet.GetYaxis().SetTitle("d#sigma/dq_{T} (pb/GeV)")
#gr_scet.GetXaxis().SetTitle("log_{10}(q_{T})")
#gr_scet.GetYaxis().SetTitle("d#sigma/dlog_{10}(q_{T})")
gr_scet.GetYaxis().SetTitleOffset(1.05)
gr_scet.GetYaxis().SetNdivisions(510)
gr_scet.GetXaxis().SetRangeUser(0.0,xrange)
gr_scet.SetMaximum(5.0)
gr_scet.SetMinimum(-0.2)
gr_resolve = TGraph( len(resolvex), array(resolvex), array(resolvey) )
gr_resolve.SetLineColor(kBlue)
gr_resolve.SetMarkerStyle(22)
gr_resolve.SetMarkerColor(kBlue)
gr_resolve.SetLineWidth(2)
gr_resolve.SetMarkerSize(1.1)
gr_cute = TGraph( len(cutex), array(cutex), array(cutey) )
gr_cute.SetLineColor(kOrange)
gr_cute.SetMarkerStyle(22)
gr_cute.SetMarkerColor(kOrange)
gr_cute.SetLineWidth(2)
gr_cute.SetMarkerSize(1.1)
gr_nanga = TGraph( len(nangax), array(nangax), array(nangay) )
gr_nanga.SetLineColor(kBlack)
gr_nanga.SetMarkerStyle(22)
gr_nanga.SetMarkerColor(kBlack)
gr_nanga.SetLineWidth(2)
gr_nanga.SetMarkerSize(1.1)
gr_radish = TGraph( len(radishx), array(radishx), array(radishy) )
gr_radish.SetLineColor(9)
gr_radish.SetMarkerStyle(22)
gr_radish.SetMarkerColor(9)
gr_radish.SetLineWidth(2)
gr_radish.SetMarkerSize(1.1)
gr_dyres = TGraph( len(dyresx), array(dyresx), array(dyresy) )
gr_dyres.SetLineColor(6)
gr_dyres.SetMarkerStyle(22)
gr_dyres.SetMarkerColor(6)
gr_dyres.SetLineWidth(2)
gr_dyres.SetMarkerSize(1.1)
gr_pbtmd = TGraph( len(pbtmdx), array(pbtmdx), array(pbtmdy) )
gr_pbtmd.SetLineColor(46)
gr_pbtmd.SetMarkerStyle(22)
gr_pbtmd.SetMarkerColor(46)
gr_pbtmd.SetLineWidth(2)
gr_pbtmd.SetMarkerSize(1.1)
gr_artemide = TGraph( len(artemidex), array(artemidex), array(artemidey) )
gr_artemide.SetLineColor(38)
gr_artemide.SetMarkerStyle(22)
gr_artemide.SetMarkerColor(38)
gr_artemide.SetLineWidth(2)
gr_artemide.SetMarkerSize(1.1)

gr_scet.GetXaxis().SetTitle("")
gr_scet.GetXaxis().SetLabelSize(0)

gr_scet.Draw("ACP")
gr_resolve.Draw("CP")
gr_cute.Draw("CP")
gr_nanga.Draw("CP")
gr_radish.Draw("CP")
gr_dyres.Draw("CP")
#gr_pbtmd.Draw("CP")
gr_artemide.Draw("CP")

lower.cd()

gr_ratio_resolve = ratio_gaph(gr_resolve,gr_scet)
gr_ratio_cute = ratio_gaph(gr_cute,gr_scet)
gr_ratio_nanga = ratio_gaph(gr_nanga,gr_scet)
gr_ratio_dyres = ratio_gaph(gr_dyres,gr_scet)
gr_ratio_radish = ratio_gaph(gr_radish,gr_scet)
#gr_ratio_pbtmd = ratio_gaph(gr_pbtmd,gr_scet)
gr_ratio_artemide = ratio_gaph(gr_artemide,gr_scet)

gr_ratio_resolve.GetXaxis().SetRangeUser(-1.0,xrange)
gr_ratio_resolve.GetXaxis().SetTitle("q_{T} (GeV)")
#gr_ratio_resolve.GetXaxis().SetTitle("log_{10}(q_{T})")
gr_ratio_resolve.GetXaxis().SetLabelSize(0.04)
gr_ratio_resolve.SetMinimum(0.5)
gr_ratio_resolve.SetMaximum(1.5)
gr_ratio_resolve.GetYaxis().SetTitle("Ratio")
gr_ratio_resolve.GetYaxis().SetTitleOffset(0.9);
gr_ratio_resolve.GetYaxis().CenterTitle(1);
gr_ratio_resolve.GetYaxis().SetLabelSize(0.02)
gr_ratio_resolve.GetYaxis().SetNdivisions(506)

gr_ratio_resolve.Draw("ACP")
gr_ratio_cute.Draw("CP")
gr_ratio_nanga.Draw("CP")
gr_ratio_dyres.Draw("CP")
gr_ratio_radish.Draw("CP")
#gr_ratio_pbtmd.Draw("CP")
gr_ratio_artemide.Draw("CP")

xmin=gr_ratio_resolve.GetXaxis().GetXmin()
xmax=xrange #gr_ratio_resolve.GetXaxis().GetXmax()
line=TLine(xmin,1,xmax,1)
line.SetLineStyle(2)
line.SetLineWidth(2)
line.Draw()

#print("SCETLIB {} + {}".format(len(scety),sum(scety)))
#print("RESOLVE {} + {}".format(len(resolvey),sum(resolvey)))
#print("CUTE {} + {}".format(len(cutey),sum(cutey)))
#print("NANGA {} + {}".format(len(nangay),sum(nangay)))

#lower.cd()


canvas.cd()
canvas.Update()
canvas.RedrawAxis()
#frame = canvas.GetFrame()
#frame.Draw()

leg = rt.TLegend(0.62,0.66,0.95,0.87)
leg.SetTextSize(0.04);
leg.SetBorderSize( 0 );
leg.SetFillStyle( 1001 );
leg.SetFillColor(kWhite); 
leg.AddEntry(gr_scet,"SCETLib","pl")
leg.AddEntry(gr_resolve,"ReSolve","pl")
leg.AddEntry(gr_cute,"CuTe","pl")
leg.AddEntry(gr_nanga,"NangaParbat","pl")
leg.AddEntry(gr_radish,"Radish","pl")
leg.AddEntry(gr_dyres,"DYRES","pl")
#leg.AddEntry(gr_pbtmd,"PB-TMD","pl")
leg.AddEntry(gr_artemide,"Artemide","pl")
#leg.AddEntry(gr_resolve,"SCETlib: 5gen","pl")
#leg.AddEntry(gr_nanga,"CuTe: 5gen","pl")
leg.Draw("same")

#update the canvas to draw the legend
canvas.Update()

raw_input("Press Enter to end")
