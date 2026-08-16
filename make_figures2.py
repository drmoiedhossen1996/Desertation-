# -*- coding: utf-8 -*-
import os, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon, Rectangle, Ellipse, Circle

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,"axes.linewidth":0.8,"savefig.dpi":220})
OUT="/projects/sandbox/figs"; os.makedirs(OUT,exist_ok=True)
INK="#1A1A1A"; BOX="#E8EEF7"; EDGE="#2C3E50"; HL="#FDEBD0"; HLE="#E67E22"
GREY="#ECECEC"; GREYE="#B0B0B0"; GREEN="#D5EAD8"; GREENE="#3B7A57"; RED="#F5D5D0"; REDE="#C0392B"; BLUE="#2E86C1"

def box(ax,x,y,w,h,title="",body="",fc=BOX,ec=EDGE,ts=9,bs=7.6):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.02,rounding_size=0.06",fc=fc,ec=ec,lw=1.3))
    if title: ax.text(x+w/2,y+h-0.34,title,ha="center",va="center",fontsize=ts,weight="bold")
    if body: ax.text(x+w/2,y+(h-0.6)/2,body,ha="center",va="center",fontsize=bs,color="#333")
def arrow(ax,x1,y1,x2,y2,color=EDGE,lw=1.7,style="-|>",ls="-"):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle=style,mutation_scale=14,lw=lw,color=color,linestyle=ls,shrinkA=0,shrinkB=0))

# ---------- FIGURE 1 : AS assessment & TTE limitations ----------
def fig1():
    fig,(a,b)=plt.subplots(1,2,figsize=(11,4.7))
    a.set_xlim(0,10); a.set_ylim(0,10); a.axis("off")
    a.set_title("A  Aortic stenosis: obstruction to ventricular consequences",fontsize=9.5,weight="bold",loc="left")
    seq=[("Aortic valve stenosis","calcification \u00b7 leaflet restriction"),
         ("\u2191 LV pressure overload","obstruction to LV outflow"),
         ("Concentric hypertrophy","adaptive wall thickening"),
         ("Fibrosis / dysfunction","maladaptive; adverse outcomes")]
    y=7.6
    for i,(t,s) in enumerate(seq):
        fc=HL if i==0 else BOX
        box(a,2.0,y,6.0,1.55,t,s,fc=fc,ec=(HLE if i==0 else EDGE),ts=9,bs=7.4)
        if i<3: arrow(a,5.0,y,5.0,y-0.6,color=EDGE,lw=1.8)
        y-=2.15
    b.set_xlim(0,10); b.set_ylim(0,10); b.axis("off")
    b.set_title("B  Why echocardiographic assessment can mislead",fontsize=9.5,weight="bold",loc="left")
    # LVOT ellipse vs assumed circle
    b.add_patch(Ellipse((3.0,7.0),3.2,1.7,fc="#D6EAF8",ec=BLUE,lw=1.6))
    b.add_patch(Circle((3.0,7.0),0.85,fc="none",ec=REDE,lw=1.6,ls=(0,(4,2))))
    b.annotate("",xy=(4.6,7.0),xytext=(1.4,7.0),arrowprops=dict(arrowstyle="<->",color=BLUE,lw=1.2))
    b.text(3.0,8.15,"true elliptical LVOT",ha="center",fontsize=7.8,color=BLUE)
    b.text(3.0,5.25,"assumed circle\n(single diameter)",ha="center",fontsize=7.6,color=REDE)
    b.text(6.4,7.0,"Continuity equation\nassumes a circular LVOT \u2192\nsingle diameter underestimates\narea \u2192 AVA error",ha="left",va="center",fontsize=8.0)
    # jet alignment forward-reference
    arrow(b,1.6,3.3,4.0,4.4,color=REDE,lw=2.0)
    arrow(b,1.6,3.0,3.7,3.0,color=BLUE,lw=1.6,ls=(0,(4,2)))
    b.text(1.4,3.5,"eccentric jet",fontsize=7.6,color=REDE,ha="left")
    b.text(1.4,2.5,"Doppler beam",fontsize=7.6,color=BLUE,ha="left")
    b.text(5.6,3.4,"beam\u2013jet misalignment\ncan underestimate V$_{peak}$\n(see Figure 6)",ha="left",va="center",fontsize=8.0,color=REDE)
    b.add_patch(FancyBboxPatch((0.2,0.35),9.6,1.2,boxstyle="round,pad=0.02,rounding_size=0.05",fc="#F7F9FB",ec=EDGE,lw=1.1))
    b.text(5.0,0.95,"Severe high-gradient AS:  V$_{peak}$ \u2265 4.0 m/s  \u00b7  mean gradient \u2265 40 mmHg  \u00b7  AVA \u2264 1.0 cm\u00b2",
           ha="center",va="center",fontsize=7.7,weight="bold",color=EDGE)
    fig.tight_layout(); fig.savefig(f"{OUT}/fig1_as_tte.png",bbox_inches="tight"); plt.close(fig)

# ---------- FIGURE 3 : retrospective plane placement ----------
def fig3():
    fig,(a,b)=plt.subplots(1,2,figsize=(11,4.6))
    for ax in (a,b): ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis("off")
    a.set_title("A  2D phase-contrast",fontsize=9.5,weight="bold",loc="left")
    # vessel with a single fixed plane; eccentric jet off-plane
    a.add_patch(Polygon([(3.4,0.5),(3.4,9.5),(6.6,9.5),(6.6,0.5)],closed=True,fc="#F2F4F7",ec="#9AA6B2"))
    a.add_patch(Rectangle((3.4,5.0),3.2,0.35,fc="#7F8C8D",alpha=0.8))
    a.text(6.8,5.2,"single plane\nfixed before scan",ha="left",va="center",fontsize=7.8,color="#555")
    arrow(a,5.0,1.0,7.0,9.0,color=REDE,lw=2.4)
    a.text(7.1,9.1,"eccentric jet\nmay be off-plane",ha="left",va="center",fontsize=7.8,color=REDE)
    a.text(5.0,0.2,"plane orientation must be chosen in advance",ha="center",fontsize=8,color="#555")
    b.set_title("B  4D flow (volumetric)",fontsize=9.5,weight="bold",loc="left")
    # pseudo-3D cuboid = acquired velocity volume
    def cuboid(ax,x,y,w,h,d,fc):
        ax.add_patch(Polygon([(x,y),(x+w,y),(x+w,y+h),(x,y+h)],closed=True,fc=fc,ec=EDGE,lw=1.3))
        ax.add_patch(Polygon([(x,y+h),(x+d,y+h+d*0.6),(x+w+d,y+h+d*0.6),(x+w,y+h)],closed=True,fc="#Dfe7f0",ec=EDGE,lw=1.1))
        ax.add_patch(Polygon([(x+w,y),(x+w+d,y+d*0.6),(x+w+d,y+h+d*0.6),(x+w,y+h)],closed=True,fc="#Cdd8e6",ec=EDGE,lw=1.1))
    cuboid(b,2.2,2.6,4.6,4.6,1.3,"#EAF0F8")
    b.text(4.5,7.9,"velocity acquired throughout a 3D volume",ha="center",fontsize=8,color="#555")
    # candidate planes (thin) + selected (highlight)
    for yy,c,lw in [(3.6,"#9AA6B2",1.0),(4.6,"#9AA6B2",1.0),(5.6,HLE,2.6)]:
        b.add_patch(Rectangle((2.2,yy),4.6,0.18,fc=c,alpha=0.9))
    b.text(7.1,5.7,"peak-velocity plane\nchosen AFTER acquisition",ha="left",va="center",fontsize=7.8,color=HLE,weight="bold")
    b.text(4.5,1.9,"retrospective plane placement",ha="center",fontsize=8.6,weight="bold",color=HLE)
    b.text(4.5,1.3,"reduces dependence on a predefined plane orientation",ha="center",fontsize=7.8,color="#555")
    fig.tight_layout(); fig.savefig(f"{OUT}/fig3_retrospective_plane.png",bbox_inches="tight"); plt.close(fig)

# ---------- FIGURE (directional conflict) ----------
def figconflict():
    fig,ax=plt.subplots(figsize=(9.4,3.9)); ax.set_xlim(-3,3); ax.set_ylim(0,10); ax.axis("off")
    ax.set_title("Directional inconsistency: 4D flow versus Doppler peak velocity",fontsize=10,weight="bold")
    ax.annotate("",xy=(2.7,5),xytext=(-2.7,5),arrowprops=dict(arrowstyle="<->",lw=2,color=EDGE))
    ax.axvline(0,ymin=0.35,ymax=0.65,color="#555",lw=1)
    ax.text(0,4.2,"agreement",ha="center",fontsize=8,color="#555")
    ax.text(-2.7,5.6,"4D flow LOWER than Doppler",ha="left",fontsize=8.5,color=BLUE,weight="bold")
    ax.text(2.7,5.6,"4D flow HIGHER than Doppler",ha="right",fontsize=8.5,color=REDE,weight="bold")
    # markers
    def marker(x,updown,label,color):
        y=6.6 if updown>0 else 3.4
        ax.plot([x],[5],marker="o",ms=11,color=color,zorder=5)
        ax.annotate(label,xy=(x,5),xytext=(x,y),ha="center",fontsize=8.2,color=color,
                    arrowprops=dict(arrowstyle="-",color=color,lw=1))
    marker(-1.6,+1,"H\u00e4lv\u00e4\u2079\n4D lower\n(bias \u22121.1 m/s)",BLUE)
    marker(1.0,-1,"Grafton-Clarke\u2078\n4D higher\n(+0.5 m/s)",REDE)
    marker(2.0,+1,"Adriaans\u00b3\n4D higher\n(V$_{peak}$ +16.4%)",REDE)
    ax.text(0,1.4,"the net direction differs between studies \u2014 4D flow is not uniformly higher or more accurate",
            ha="center",fontsize=8.3,color="#555")
    fig.tight_layout(); fig.savefig(f"{OUT}/figX_vpeak_conflict.png",bbox_inches="tight"); plt.close(fig)

# ---------- FIGURE (Elhawaz KE components) ----------
def figelhawaz():
    fig,ax=plt.subplots(figsize=(7.0,4.8))
    comps=["Direct","Delayed","Retained","Residual"]
    pre=[4.9,2.46,1.07,0.84]; post=[1.86,1.38,0.91,0.98]; sig=["*","*","ns","ns"]
    x=np.arange(4)
    for i in range(4):
        ax.plot([x[i]-0.13,x[i]+0.13],[pre[i],post[i]],color="#B0B0B0",lw=1.4,zorder=1)
    ax.plot(x-0.13,pre,"o",ms=10,color="#2C3E50",label="pre-intervention",zorder=3)
    ax.plot(x+0.13,post,"o",ms=10,mfc="white",mec="#2C3E50",mew=1.8,label="post-intervention",zorder=3)
    for i in range(4):
        ax.text(x[i],max(pre[i],post[i])+0.35,sig[i],ha="center",fontsize=10,
                color=(REDE if sig[i]=="*" else "#888"),weight="bold")
    ax.set_xticks(x); ax.set_xticklabels([c+"\nflow" for c in comps])
    ax.set_ylabel("LV blood-flow kinetic energy (\u03bcJ)"); ax.set_ylim(0,6.2)
    ax.legend(fontsize=8,frameon=False,loc="upper right")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.text(0.02,0.02,"median values; no error bars (skewed data, reported as median [IQR])",
            transform=ax.transAxes,fontsize=7.2,color="#555")
    fig.tight_layout(); fig.savefig(f"{OUT}/figY_elhawaz_ke.png",bbox_inches="tight"); plt.close(fig)

# ---------- FIGURE (Grafton-Clarke Vpeak by intervention) ----------
def figgc():
    fig,ax=plt.subplots(figsize=(6.8,4.8))
    groups=["Doppler (CWD)","4D flow CMR"]
    noiv=[2.6,2.7]; iv=[3.4,4.2]; x=np.arange(2); w=0.34
    ax.bar(x-w/2,noiv,w,label="no intervention",color="#AEB6BF",edgecolor=EDGE,lw=1)
    ax.bar(x+w/2,iv,w,label="intervention",color="#7FB3D5",edgecolor=EDGE,lw=1)
    for i in range(2):
        ax.text(x[i]-w/2,noiv[i]+0.05,f"{noiv[i]}",ha="center",fontsize=8.5)
        ax.text(x[i]+w/2,iv[i]+0.05,f"{iv[i]}",ha="center",fontsize=8.5)
    ax.text(0,4.5,"P = 0.0025",ha="center",fontsize=8); ax.text(1,4.7,"P < 0.0001",ha="center",fontsize=8)
    ax.axhline(3.5,color=REDE,ls=(0,(5,3)),lw=1.4)
    ax.text(1.48,3.58,"3.5 m/s (exploratory)",ha="right",fontsize=7.8,color=REDE)
    ax.set_xticks(x); ax.set_xticklabels(groups)
    ax.set_ylabel("Peak velocity (m/s)"); ax.set_ylim(0,5.2)
    ax.legend(fontsize=8,frameon=False,loc="upper left")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    fig.tight_layout(); fig.savefig(f"{OUT}/figZ_gc_vpeak.png",bbox_inches="tight"); plt.close(fig)

for f in (fig1,fig3,figconflict,figelhawaz,figgc):
    f(); print("built", f.__name__)
