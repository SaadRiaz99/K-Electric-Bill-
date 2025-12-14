# K-Electric-Bill-
Slab-wise (piecewise) bill calculation

Supports Protected consumers (up to 200 units)

Supports Unprotected consumers (above 200 units)

Written in simple Python (beginner-friendly)

Output rounded to 2 decimal places

⚡ Tariff Details
🟢 Protected Consumers
Units Range	Rate (Rs/unit)
1 – 100	10.54
101 – 200	13.01

Note: If usage exceeds 200 units, the consumer is not protected.

🔵 Unprotected Consumers
Units Range	Rate (Rs/unit)
1 – 100	22.44
101 – 200	28.91
201 – 300	33.10
301 – 400	37.10
401 – 500	40.20
501 – 600	41.62
601 – 700	42.76
Above 700	47.69
🧮 Piecewise Logic (Concept)

The bill is calculated cumulatively:

First slab cost is always included

Next slab cost is added only for extra units

Example:

156 units (Protected)

First 100 units → 10.54

Next 56 units → 13.01
