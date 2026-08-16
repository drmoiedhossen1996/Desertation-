# -*- coding: utf-8 -*-
import os, numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon, Rectangle, Arc

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.linewidth": 0.8,
    "savefig.dpi": 220,
})
OUT = "/projects/sandbox/figs"; os.makedirs(OUT, exist_ok=True)

INK="#1A1A1A"; BOX="#E8EEF7"; EDGE="#2C3E50"; HL="#FDEBD0"; HLE="#E67E22"
GREY="#ECECEC"; GREYE="#B0B0B0"; GREEN="#D5EAD8"; GREENE="#3B7A57"; RED="#F5D5D0"

def box(ax, x, y, w, h, text, fc=BOX, ec=EDGE, fs=9, bold=False, tc=INK):
    p=FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.02,rounding_size=0.06",
                     fc=fc,ec=ec,lw=1.3); ax.add_patch(p)
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",fontsize=fs,
            color=tc,weight=("bold" if bold else "normal"),wrap=True)

def arrow(ax,x1,y1,x2,y2,color=EDGE,lw=1.6,style="-|>",ls="-"):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle=style,mutation_scale=14,
                 lw=lw,color=color,linestyle=ls,shrinkA=0,shrinkB=0))

# ---------- FIGURE 5 : two discrepancy mechanisms (keystone) ----------
def fig5():
    fig,(a,b)=plt.subplots(1,2,figsize=(11,5.2))
    # Panel A -- misalignment
    a.set_xlim(0,10); a.set_ylim(0,10); a.axis("off")
    a.set_title("A  Eccentric jet and Doppler beam misalignment",fontsize=10,weight="bold",loc="left")
    # vessel walls (aortic root) narrowing at valve
    a.add_patch(Polygon([(3.2,0.5),(4.3,4.6),(4.3,9.5),(3.4,9.5),(3.4,4.8),(2.4,0.5)],closed=True,fc="#F2F4F7",ec="#9AA6B2"))
    a.add_patch(Polygon([(6.8,0.5),(5.7,4.6),(5.7,9.5),(6.6,9.5),(6.6,4.8),(7.6,0.5)],closed=True,fc="#F2F4F7",ec="#9AA6B2"))
    a.text(5,0.9,"LV",ha="center",fontsize=9,color="#555")
    a.text(5,9.1,"aorta",ha="center",fontsize=9,color="#555")
    # stenotic orifice
    a.add_patch(Rectangle((4.3,4.5),1.4,0.5,fc="#C0392B",ec="none",alpha=0.5))
    a.text(5,4.2,"stenotic orifice",ha="center",fontsize=8,color="#C0392B")
    ox,oy=5,4.9
    # eccentric jet (up-right)
    arrow(a,ox,oy,7.6,9.2,color="#C0392B",lw=2.6)
    a.text(7.7,9.3,"eccentric\njet",fontsize=8.5,color="#C0392B",ha="left",va="center")
    # doppler beam (from transducer bottom-left, misaligned)
    arrow(a,2.0,0.6,6.2,9.2,color="#2E86C1",lw=2.0,style="-|>",ls=(0,(4,2)))
    a.text(1.6,0.5,"Doppler\nbeam",fontsize=8.5,color="#2E86C1",ha="left",va="top")
    # angle theta
    a.add_patch(Arc((ox,oy),3.2,3.2,angle=0,theta1=58,theta2=78,color=INK,lw=1.4))
    a.text(6.05,7.0,r"$\theta$",fontsize=13,color=INK)
    a.text(5.0,2.6,r"$V_{measured}=V_{true}\cdot\cos\theta$",ha="center",fontsize=10,
           bbox=dict(boxstyle="round,pad=0.3",fc="white",ec=EDGE))
    a.text(5.0,1.7,"misalignment  \u2192  V$_{peak}$ underestimated",ha="center",fontsize=9,color="#C0392B",weight="bold")

    # Panel B -- pressure gradients + recovery
    b.set_title("B  Doppler vs catheter pressure gradient",fontsize=10,weight="bold",loc="left")
    t=np.linspace(0,1,400)
    LV=np.where(t<0.6, 175*np.sin(np.pi*t/0.6)**1.0, 0)
    Ao=np.where((t>0.05)&(t<0.7), 120*np.sin(np.pi*(t-0.05)/0.65)**1.1, 0)
    Ao_rec=np.where((t>0.05)&(t<0.7), 138*np.sin(np.pi*(t-0.05)/0.65)**1.1, 0)  # recovered (higher, so smaller gradient)
    b.plot(t,LV,color="#8E44AD",lw=2.2,label="LV pressure")
    b.plot(t,Ao,color="#2E86C1",lw=2.2,label="Aortic pressure (at vena contracta)")
    b.plot(t,Ao_rec,color="#2E86C1",lw=1.6,ls=(0,(4,2)),label="Aortic pressure (recovered, downstream)")
    # max instantaneous gradient
    diff=LV-Ao; k=np.argmax(diff); 
    b.annotate("",xy=(t[k],LV[k]),xytext=(t[k],Ao[k]),arrowprops=dict(arrowstyle="<->",color="#C0392B",lw=1.8))
    b.text(t[k]-0.02,(LV[k]+Ao[k])/2,"Doppler\nmax instantaneous",ha="right",va="center",fontsize=8.2,color="#C0392B")
    # peak-to-peak
    iLV=np.argmax(LV); iAo=np.argmax(Ao)
    b.annotate("",xy=(0.86,LV[iLV]),xytext=(0.86,Ao[iAo]),arrowprops=dict(arrowstyle="<->",color="#1E8449",lw=1.8))
    b.text(0.88,(LV[iLV]+Ao[iAo])/2,"catheter\npeak-to-peak",ha="left",va="center",fontsize=8.2,color="#1E8449")
    b.plot([t[iLV],0.86],[LV[iLV],LV[iLV]],color="#8E44AD",lw=0.7,ls=":")
    b.plot([t[iAo],0.86],[Ao[iAo],Ao[iAo]],color="#2E86C1",lw=0.7,ls=":")
    # recovery annotation
    b.annotate("pressure\nrecovery",xy=(0.42,Ao_rec[int(0.42*399)]),xytext=(0.52,155),
               fontsize=8.2,color="#2E86C1",ha="left",arrowprops=dict(arrowstyle="-|>",color="#2E86C1",lw=1.2))
    b.set_xlabel("time (systole)"); b.set_ylabel("pressure (mmHg)")
    b.set_xlim(0,1.0); b.set_ylim(0,190); b.set_xticks([])
    b.spines["top"].set_visible(False); b.spines["right"].set_visible(False)
    b.legend(fontsize=7.3,loc="upper right",frameon=False)
    fig.text(0.5,0.015,"Two distinct mechanisms of measurement discrepancy \u2014 they must not be conflated",
             ha="center",fontsize=10,weight="bold",color=EDGE)
    fig.tight_layout(rect=[0,0.05,1,1])
    fig.savefig(f"{OUT}/fig5_two_mechanisms.png",bbox_inches="tight"); plt.close(fig)

# ---------- FIGURE 8 : flow energy vs myocardial work ----------
def fig8():
    fig,ax=plt.subplots(figsize=(11,4.8)); ax.set_xlim(0,12); ax.set_ylim(0,7.5); ax.axis("off")
    box(ax,0.3,1.6,3.2,4.2,"",fc=BOX); 
    ax.text(1.9,5.35,"Blood-flow energy\n(4D flow CMR)",ha="center",va="center",fontsize=9.5,weight="bold")
    ax.text(1.9,3.4,"\u2022 Intracavitary kinetic energy\n\u2022 Turbulent kinetic energy (TKE)\n\u2022 Viscous energy loss (VEL)",
            ha="center",va="center",fontsize=8.8)
    box(ax,4.4,1.6,3.2,4.2,"",fc=HL,ec=HLE)
    ax.text(6.0,5.35,"Aortic stenosis",ha="center",va="center",fontsize=9.5,weight="bold")
    ax.text(6.0,3.4,"\u2022 Valvular obstruction\n\u2022 Altered / eccentric flow\n\u2022 \u2191 LV pressure load",
            ha="center",va="center",fontsize=8.8)
    box(ax,8.5,1.6,3.2,4.2,"",fc=GREEN,ec=GREENE)
    ax.text(10.1,5.35,"Myocardial\nmechanical energy",ha="center",va="center",fontsize=9.5,weight="bold")
    ax.text(10.1,3.35,"\u2022 PV-loop stroke work\n\u2022 Pressure\u2013volume area (PVA)\n\u2022 Ventricular efficiency",
            ha="center",va="center",fontsize=8.8)
    arrow(ax,4.4,3.7,3.5,3.7,color=HLE,lw=2.0)   # AS -> flow energy
    arrow(ax,7.6,3.7,8.5,3.7,color=HLE,lw=2.0)   # AS -> myocardial
    ax.text(4.0,4.05,"altered flow",fontsize=7.6,color=HLE,ha="center")
    ax.text(8.05,4.05,"pressure load",fontsize=7.6,color=HLE,ha="center")
    # relationship arrow between left and right
    ax.add_patch(FancyArrowPatch((1.9,1.5),(10.1,1.5),arrowstyle="<->",mutation_scale=16,lw=1.6,color=EDGE,
                 connectionstyle="arc3,rad=-0.25"))
    ax.text(6.0,0.35,"physiologically related  \u2014  but NOT interchangeable",
            ha="center",fontsize=10,weight="bold",color="#C0392B")
    fig.tight_layout(); fig.savefig(f"{OUT}/fig8_flow_vs_work.png",bbox_inches="tight"); plt.close(fig)

# ---------- FIGURE 2 : 4D-flow workflow ----------
def fig2():
    fig,ax=plt.subplots(figsize=(14,3.4)); ax.set_xlim(0,14); ax.set_ylim(0,4); ax.axis("off")
    steps=[("Acquisition","3-directional velocity\nencoding \u00b7 ECG gating \u00b7 VENC",BOX,EDGE),
           ("Corrections","background phase \u00b7\nconcomitant gradient \u00b7 aliasing",BOX,EDGE),
           ("Segmentation","aorta / chambers of\ninterest",BOX,EDGE),
           ("Retrospective\nplane placement","peak-velocity plane chosen\nAFTER acquisition",HL,HLE),
           ("Quantification","V$_{peak}$ \u00b7 pressure\ngradient \u00b7 flow",BOX,EDGE),
           ("Advanced\nparameters","TKE \u00b7 VEL \u00b7 WSS",BOX,EDGE)]
    w=2.05; gap=0.25; x=0.15; y=1.1; h=1.9
    for i,(t,s,fc,ec) in enumerate(steps):
        box(ax,x,y,w,h,"",fc=fc,ec=ec)
        ax.text(x+w/2,y+h-0.45,t,ha="center",va="center",fontsize=8.6,weight="bold")
        ax.text(x+w/2,y+0.62,s,ha="center",va="center",fontsize=7.2,color="#333")
        if i<len(steps)-1:
            arrow(ax,x+w,y+h/2,x+w+gap,y+h/2,color=EDGE,lw=1.8)
        x+=w+gap
    ax.text(0.15+3*(w+gap)+w/2,0.6,"key advantage in aortic stenosis",ha="center",fontsize=7.8,
            color=HLE,weight="bold")
    fig.tight_layout(); fig.savefig(f"{OUT}/fig2_workflow.png",bbox_inches="tight"); plt.close(fig)

# ---------- FIGURE 7 : PV loop ----------
def fig7():
    fig,ax=plt.subplots(figsize=(6.4,5.4))
    ESV,EDV=45,125; Pao=120; Pfill=8; Pes=125
    # loop corners
    # filling: ESV? actually filling from ESV to EDV along low pressure; here draw standard loop
    # Points: A=(EDV,Pfill) end-diastole; B=(EDV, Pao) start ejection (isovol contraction);
    # ejection top C=(ESV,Pes); isovol relax down to D=(ESV, Pfill-ish low), then filling back to A
    xA,yA=EDV,Pfill
    xB,yB=EDV,Pao
    xC,yC=ESV,Pes
    xD,yD=ESV,12
    # ejection curve (slight arch)
    exx=np.linspace(EDV,ESV,60); eyy=np.linspace(Pao,Pes,60)+10*np.sin(np.linspace(0,np.pi,60))
    # filling curve
    fxx=np.linspace(ESV,EDV,60); fyy=Pfill+ (np.linspace(0,1,60)**2)*(yA-yD)+2*np.sin(np.linspace(0,np.pi,60))
    # build polygon for stroke-work fill
    loopx=np.concatenate([[xA,xB],exx,[xD],fxx]); loopy=np.concatenate([[yA,yB],eyy,[yD],fyy])
    ax.fill(loopx,loopy,color="#E8EEF7",alpha=0.9,zorder=0)
    # edges
    ax.plot([xA,xB],[yA,yB],color=EDGE,lw=2)          # isovolumetric contraction
    ax.plot(exx,eyy,color=EDGE,lw=2)                  # ejection
    ax.plot([xC,xD],[yC,yD],color=EDGE,lw=2)          # isovolumetric relaxation
    ax.plot(fxx,fyy,color=EDGE,lw=2)                  # filling
    # ESPVR & EDPVR
    ax.plot([20,ESV+3],[0,Pes+8],color="#C0392B",lw=1.3,ls=(0,(5,3)))
    ax.text(ESV-2,Pes+14,"ESPVR",color="#C0392B",fontsize=8)
    exx2=np.linspace(20,140,50); ax.plot(exx2,2+0.0009*(exx2-20)**2.05,color="#1E8449",lw=1.3,ls=(0,(5,3)))
    ax.text(132,20,"EDPVR",color="#1E8449",fontsize=8)
    # labels
    ax.text((ESV+EDV)/2,70,"stroke\nwork",ha="center",va="center",fontsize=10,weight="bold",color=EDGE)
    ax.annotate("ejection",xy=(85,eyy[np.argmin(abs(exx-85))]),xytext=(70,150),fontsize=8,
                arrowprops=dict(arrowstyle="-|>",lw=1,color="#555"))
    ax.text(EDV+2,(yA+yB)/2,"isovolumetric\ncontraction",fontsize=7.6,color="#555",va="center")
    ax.text(ESV-23,(yC+yD)/2,"isovolumetric\nrelaxation",fontsize=7.6,color="#555",va="center")
    ax.text((ESV+EDV)/2,4,"filling",ha="center",fontsize=8,color="#555")
    ax.text(78,182,"PVA = stroke work + potential energy",ha="center",fontsize=8.6,color="#C0392B",
            bbox=dict(boxstyle="round,pad=0.3",fc="white",ec="#C0392B"))
    ax.set_xlabel("LV volume (mL)"); ax.set_ylabel("LV pressure (mmHg)")
    ax.set_xlim(15,150); ax.set_ylim(0,195)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    fig.tight_layout(); fig.savefig(f"{OUT}/fig7_pvloop.png",bbox_inches="tight"); plt.close(fig)

# ---------- FIGURE 4 : Archer PG by modality ----------
def fig4():
    fig,ax=plt.subplots(figsize=(6.2,4.8))
    labels=["Invasive","4D flow CMR","Doppler TTE"]; means=[50,54,61]; sds=[34,26,32]
    x=np.arange(3)
    ax.bar(x,means,yerr=sds,capsize=6,width=0.6,color=["#AEB6BF","#7FB3D5","#F1948A"],
           edgecolor=EDGE,linewidth=1.1,error_kw=dict(lw=1.3))
    for i,m in enumerate(means): ax.text(i,m+ sds[i]+2,f"{m}\u00b1{sds[i]}",ha="center",fontsize=9)
    # p-value annotations
    ax.plot([0,1],[95,95],color=INK,lw=1); ax.text(0.5,96,"P = 0.67 (ns)",ha="center",fontsize=8)
    ax.plot([0,2],[104,104],color=INK,lw=1); ax.text(1.0,105,"P = 0.0002",ha="center",fontsize=8)
    ax.set_xticks(x); ax.set_xticklabels(labels)
    ax.set_ylabel("Peak pressure gradient (mmHg)"); ax.set_ylim(0,120)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    fig.tight_layout(); fig.savefig(f"{OUT}/fig4_archer_pg.png",bbox_inches="tight"); plt.close(fig)

# ---------- FIGURE 6 : Aliabadi VEL by phenotype ----------
def fig6():
    fig,ax=plt.subplots(figsize=(6.6,4.8))
    labels=["TAV\ncontrol","BAV\nno complications","BAV\nregurgitation","BAV\nstenosis"]
    med=[4.1,6.4,11.4,16.2]
    lo=[3.4,5.1,9.5,9.1]; hi=[5.7,8.0,17.6,24.4]
    yerr=[[m-l for m,l in zip(med,lo)],[h-m for h,m in zip(hi,med)]]
    x=np.arange(4)
    ax.errorbar(x,med,yerr=yerr,fmt="o",ms=9,color="#2C3E50",ecolor="#5D6D7E",elinewidth=1.6,capsize=6,capthick=1.6)
    for i,m in enumerate(med): ax.text(i+0.12,m,f"{m}",fontsize=8.6,va="center")
    ax.text(1,8.0+0.6,"ns vs control",ha="center",fontsize=7.8,color="#C0392B")
    ax.set_xticks(x); ax.set_xticklabels(labels,fontsize=8.6)
    ax.set_ylabel("Peak-systolic viscous energy loss (mW)"); ax.set_ylim(0,27)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.text(0.02,0.98,"median \u00b7 whiskers = IQR",transform=ax.transAxes,fontsize=7.6,va="top",color="#555")
    fig.tight_layout(); fig.savefig(f"{OUT}/fig6_aliabadi_vel.png",bbox_inches="tight"); plt.close(fig)

# ---------- FIGURE 9 : evidence hierarchy ----------
def fig9():
    fig,ax=plt.subplots(figsize=(9.6,5.4)); ax.set_xlim(0,12); ax.set_ylim(0,10.5); ax.axis("off")
    tiers=[
        ("1  Measurement validity / agreement","Adriaans\u00b3 \u00b7 Grafton-Clarke\u2076 \u00b7 Archer\u00b9\u00b9",GREEN,GREENE),
        ("2  Association with symptoms / function","Archer\u00b9\u00b9 \u00b7 Elhawaz\u00b9\u2077 (6MWT)",GREEN,GREENE),
        ("3  Association with a clinical decision","Grafton-Clarke\u2078 (intervention; exploratory)",HL,HLE),
        ("4  Demonstrated clinical utility","no evidence yet",GREY,GREYE),
        ("5  Improved patient outcomes","no evidence yet",GREY,GREYE),
    ]
    # draw as stacked pyramid (narrowing upward)
    yb=0.7; h=1.65; cx=6.0
    for i,(t,s,fc,ec) in enumerate(tiers):
        halfw=4.7-0.55*i
        y=yb+i*(h+0.12)
        ax.add_patch(FancyBboxPatch((cx-halfw,y),2*halfw,h,boxstyle="round,pad=0.02,rounding_size=0.05",
                     fc=fc,ec=ec,lw=1.4))
        ax.text(cx,y+h*0.62,t,ha="center",va="center",fontsize=9,weight="bold",color=INK)
        col = "#C0392B" if s=="no evidence yet" else "#333"
        ax.text(cx,y+h*0.24,s,ha="center",va="center",fontsize=7.8,color=col,
                style=("italic" if s=="no evidence yet" else "normal"))
    arrow(ax,0.7,yb,0.7,yb+5*(h+0.12)-0.2,color=EDGE,lw=2)
    ax.text(0.35,yb+2.5*(h+0.12),"increasing clinical maturity",rotation=90,va="center",ha="center",fontsize=8.5,color=EDGE)
    ax.text(cx,yb-0.5,"strongest current evidence at the base; top tiers not yet supported",
            ha="center",fontsize=8.2,color="#555")
    fig.tight_layout(); fig.savefig(f"{OUT}/fig9_evidence_hierarchy.png",bbox_inches="tight"); plt.close(fig)

for f in (fig5,fig8,fig2,fig7,fig4,fig6,fig9):
    f(); print("built", f.__name__)

print("\nFiles:")
for fn in sorted(os.listdir(OUT)):
    print(" ", fn, os.path.getsize(os.path.join(OUT,fn)), "bytes")
