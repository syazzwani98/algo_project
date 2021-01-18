#Q2 code
from geopy.distance import geodesic

A = (3.139003, 101.686852) # A for Kuala Lumpur,
B = (35.86166, 104.195396) # B for China,
C = (51.507351, -0.127758) # C for London,
D = (20.593683, 78.962883) # D for India,
E = (61.52401, 105.318756) # E for Russia,
F = (37.09024, -95.712891) # F for United States,
G = (15.870032, 100.992538) # G for Thailand,
H = (40.463669, -3.74922) # H for Spain,
I = (-14.235004, -51.925282) # I for Brazil,

russia1 = (geodesic(A,G,B,E ).km)  # KL – THAI - CHINA - RUSSIA
russia2 = (geodesic(A,G,E ).km)  #  KL - THAI - RUSSIA
russia3 = (geodesic(A,D,E ).km)  #  KL - INDIA - RUSSIA
russia4 = (geodesic(A,D,B,E ).km)  #  KL - INDIA - CHINA - RUSSIA

london1 = (geodesic(A,G,C ).km) # KL - THAI - LONDON
london2 = (geodesic(A,D,C ).km) # KL - INDIA - LONDON
london3 = (geodesic(A,D,H,C ).km) # KL - INDIA - SPAIN - LONDON
london4 = (geodesic(A,I,H,C).km) # KL - BRAZIL - SPAIN - LONDON

spain1 = (geodesic(A,B,H ).km) # KL - INDIA - SPAIN
spain2 = (geodesic(A,I,H ).km) # KL - BRAZIL - SPAIN

china1 = (geodesic(A,D,B ).km) # KL - INDIA - CHINA
china2 = (geodesic(A,G,B ).km) # KL - THAI - CHINA

us1 = (geodesic(A,I,F).km) # KL - BRAZIL - US
us2 = (geodesic(A,I,H,C,F ).km) # KL - BRAZIL - SPAIN - LONDON - US
us3 = (geodesic(A,D,H,F).km) # KL - INDIA - SPAIN - US


TotalDist_russia = russia1 + russia2 + russia3 + russia4
distR1 = russia1 / TotalDist_russia
distR2 = russia2 / TotalDist_russia
distR3 = russia3 / TotalDist_russia
distR4 = russia4 / TotalDist_russia

TotalDist_london = london1 + london2 + london3 + london4
distL1 = london1 / TotalDist_london
distL2 = london2 / TotalDist_london
distL3 = london3 / TotalDist_london
distL4 = london4 / TotalDist_london

TotalDist_spain = spain1 + spain2
distS1 = spain1 / TotalDist_spain
distS2 = spain2 / TotalDist_spain


TotalDist_china = china1 + china2
distC1 = china1 / TotalDist_china
distC2 = china2 / TotalDist_china

TotalDist_us = us1 + us2 + us3
distU1 = us1 / TotalDist_us
distU2 = us2 / TotalDist_us
distU3 = us3 / TotalDist_us

print("\nKL --> RUSSIA")
print("\nRoute KL – THAI - CHINA - RUSSIA  = ", round(distR1,2) ,
      "\nRoute KL - THAI - RUSSIA = ", round(distR2,2),
      "\nRoute KL - INDIA - RUSSIA = ", round(distR3,2),
      "\nRoute KL - INDIA - CHINA - RUSSIA = ",round(distR4,2))

print("\nKL --> LONDON")
print("\nRoute KL - THAI - LONDON  = ", round(distL1,2) ,
      "\nRoute KL - INDIA - LONDON = ", round(distL2,2),
      "\nRoute KL - INDIA - SPAIN - LONDON = ", round(distL3,2),
      "\nRoute KL - BRAZIL - SPAIN - LONDON = ",round(distL4,2))

print("\nKL --> SPAIN")
print("\nRoute KL - INDIA - SPAIN  = ", round(distS1,2) ,
      "\nRoute KL - BRAZIL - SPAIN = ", round(distS2,2))

print("\nKL --> CHINA")
print("\nRoute KL - INDIA - CHINA  = ", round(distC1,2) ,
      "\nRoute KL - THAI - CHINA = ", round(distC2,2))

print("\nKL --> UNITED STATES")
print("\nRoute KL - BRAZIL - US = ", round(distU1,2) ,
      "\nRoute KL - BRAZIL - SPAIN - LONDON - US = ", round(distU2,2),
      "\nRoute KL - INDIA - SPAIN - US = ", round(distU3,2))

