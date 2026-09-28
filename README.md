# Supply Chain Process Mapping and Visualization

**Week 3 Task:** Design a process map of a typical supply chain (procurement, inventory management and distribution), explain each step, and show where data analytics can find bottlenecks.

## Overview

A supply chain moves materials, products and information from suppliers to customers. This project maps that flow in seven stages, links each stage to the KPIs normally recorded there, and explains how data analytics can identify bottlenecks and improve performance. Only publicly known supply chain concepts are used; no private or company data is included.

## Process Map

![Process Map](images/process_map.png)

## Stages Covered

| # | Stage | Example KPIs |
|---|-------|--------------|
| 1 | Supplier / Sourcing | Supplier lead time, defect rate |
| 2 | Procurement | PO cycle time, cost per PO |
| 3 | Inbound Logistics | Transit time, on-time arrival % |
| 4 | Warehouse and Inventory | Inventory turnover, stockout rate |
| 5 | Order Fulfilment | Order accuracy, pick/pack time |
| 6 | Distribution / Transportation | On-time delivery %, cost per mile |
| 7 | Customer and Returns | Customer satisfaction, return rate |

## Repository Structure

```
Supply-Chain-Process-Mapping-and-Visualization/
├── README.md
├── report/
│   └── Week3_Supply_Chain_Process_Mapping.docx   # Full report
├── images/
│   └── process_map.png                           # Process map image
├── code/
│   └── map.py                                    # Script that draws the map
└── requirements.txt
```

## Tools and Method

- **Python + Matplotlib** were used to draw the process map and export it as a PNG.
- The same map can also be built in Visio, PowerPoint or draw.io.
- Method: research the stages, identify data points for each stage, draw the map, then document each step with its analytical challenges.

## How to Recreate the Map

```bash
pip install -r requirements.txt
python code/map.py
```

The image is saved to `images/process_map.png`.

## Report Contents

1. Introduction and objective
2. Research: typical stages of a supply chain
3. Tools and method used
4. The supply chain process map
5. Explanation of each stage (key data points and analytical challenges)
6. Identifying bottlenecks using data analytics
7. Challenges observed
8. Where further data analysis can improve performance
9. Conclusion

## Key Ideas

- Bottlenecks show up as long or highly variable times at one stage, so timestamps and quantities should be captured at every step.
- Useful methods include cycle-time analysis, control charts, ABC analysis, timestamp analysis and route-level on-time analysis.
- Further analysis opportunities: demand forecasting, supplier scorecards, inventory optimisation, route optimisation and predictive delay alerts.

## Related Tasks

- Week 1: Data Collection and Preliminary Analysis
- Week 2: Supply Chain KPI Identification and Analysis
