import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(13, 5.1), dpi=200)
ax.set_xlim(0, 13); ax.set_ylim(1.1, 6.2); ax.axis("off")

stages = [
 ("1. Supplier /\nSourcing", "#DCE6F2", "Supplier lead time\nSupplier defect rate"),
 ("2. Procurement", "#C9DBEE", "PO cycle time\nCost per PO"),
 ("3. Inbound\nLogistics", "#B7D0EA", "Transit time\nOn-time arrival %"),
 ("4. Warehouse &\nInventory", "#F6E3C4", "Inventory turnover\nStockout rate"),
 ("5. Order\nFulfilment", "#F2D3A5", "Order accuracy\nPick/pack time"),
 ("6. Distribution /\nTransportation", "#D5EAD3", "On-time delivery %\nCost per mile"),
 ("7. Customer", "#BFE0BC", "Customer satisfaction\nReturn rate"),
]
n = len(stages); w = 1.55; gap = 0.33
x0 = (13 - (n*w + (n-1)*gap))/2
y = 3.3; h = 1.15
centers = []
for i,(t,c,k) in enumerate(stages):
    x = x0 + i*(w+gap)
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.03,rounding_size=0.12",fc=c,ec="#2F3E4E",lw=1.4))
    ax.text(x+w/2,y+h/2,t,ha="center",va="center",fontsize=8.8,fontweight="bold",color="#1B2733")
    ax.add_patch(FancyBboxPatch((x,y-1.25),w,0.95,boxstyle="round,pad=0.03,rounding_size=0.08",fc="white",ec="#7A8794",lw=1,ls="--"))
    ax.text(x+w/2,y-0.78,k,ha="center",va="center",fontsize=7.6,color="#33414F")
    ax.plot([x+w/2,x+w/2],[y,y-0.3],color="#7A8794",lw=1,ls=":")
    centers.append((x,x+w))
    if i>0:
        px = centers[i-1][1]
        ax.add_patch(FancyArrowPatch((px+0.04,y+h/2),(x-0.04,y+h/2),arrowstyle="-|>",mutation_scale=14,lw=1.8,color="#2F3E4E"))

# info flow
ax.text(6.5,5.95,"Supply Chain Process Map: Material, Information and Data Flow",ha="center",fontsize=13,fontweight="bold",color="#1B2733")
ax.text(6.5,5.6,"Solid arrows = material flow   |   Dashed boxes = KPIs / data captured at each stage",ha="center",fontsize=8.5,color="#55636F")

# feedback loop: demand forecast from customer back to procurement
xs = (centers[6][0]+centers[6][1])/2; xp = (centers[1][0]+centers[1][1])/2
ax.add_patch(FancyArrowPatch((xs,y+h+0.04),(xp,y+h+0.04),connectionstyle="arc3,rad=0.22",arrowstyle="-|>",mutation_scale=14,lw=1.6,color="#B5462F",ls="--"))
ax.text((xs+xp)/2,4.95,"Information flow: demand signals, sales data, forecasts, returns",ha="center",fontsize=8.5,color="#B5462F",style="italic")

# bottleneck markers
for idx,label in [(2,"Bottleneck risk:\ncustoms / port delay"),(3,"Bottleneck risk:\noverstock / stockout"),(5,"Bottleneck risk:\nlast-mile delay")]:
    x = centers[idx][0]
    ax.text(x+w/2,1.55,"⚠ "+label,ha="center",va="center",fontsize=7.6,color="#B5462F",
            bbox=dict(boxstyle="round,pad=0.25",fc="#FBE9E5",ec="#B5462F",lw=0.8))
    ax.plot([x+w/2,x+w/2],[y-1.28,1.85],color="#B5462F",lw=0.8,ls=":")
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images", "process_map.png")
plt.savefig(OUT,bbox_inches="tight",facecolor="white")
