from geopy.distance import geodesic
import Q1, Q4before, Q4after, Q6before, Q6after

A = (3.139003, 101.686852) # A for Kuala Lumpur,
B = (35.86166, 104.195396) # B for China,
C = (51.507351, -0.127758) # C for London,
D = (20.593683, 78.962883) # D for India,
E = (61.52401, 105.318756) # E for Russia,
F = (37.09024, -95.712891) # F for United States,
G = (15.870032, 100.992538) # G for Thailand,
H = (40.463669, -3.74922) # H for Spain,
I = (-14.235004, -51.925282) # I for Brazil,

distanceKL_Thailand = (geodesic(A , G ).km)
AG = round(distanceKL_Thailand, 2)
distanceKL_India = (geodesic(A , D ).km)
AD = round(distanceKL_India, 2)
distanceKL_Brazil = (geodesic(A , I ).km)
AI = round(distanceKL_Brazil, 2)
distanceThailand_China = (geodesic(G , B ).km)
GB = round(distanceThailand_China, 2)
distanceThailand_Russia = (geodesic(G , E).km)
GE = round(distanceThailand_Russia, 2)
distanceThailand_London = (geodesic(G , C ).km)
GC = round(distanceThailand_London, 2)
distanceChina_Russia = (geodesic(B , E ).km)
BE = round(distanceChina_Russia, 2)
distanceIndia_Spain = (geodesic(D , H ).km)
DH = round(distanceIndia_Spain, 2)
distanceIndia_London = (geodesic(D , C ).km)
DC = round(distanceIndia_London, 2)
distanceIndia_China = (geodesic(D , B ).km)
DB = round(distanceIndia_China, 2)
distanceIndia_Russia = (geodesic(D , E ).km)
DE = round(distanceIndia_Russia, 2)
distanceBrazil_US = (geodesic(I , F ).km)
IF = round(distanceBrazil_US, 2)
distanceBrazil_Spain = (geodesic(I , H ).km)
IH = round(distanceBrazil_Spain, 2)
distanceSpain_US = (geodesic(H , F ).km)
HF = round(distanceSpain_US, 2)
distanceSpain_London = (geodesic(F , C ).km)
FC = round(distanceSpain_London, 2)
distanceLondon_US = (geodesic(C , F).km)
CF = round(distanceLondon_US, 2)
#Q2
print("SHOWING THE DISTANCE FOR ALL ROUTES IN FLIGHT SYSTEM 2.0\n")
print("The distance from Kuala Lumpur to Thailand is", AG, "km")
print("The distance from Kuala Lumpur to India is", AD, "km")
print("The distance from Kuala Lumpur to Brazil is", AI, "km" )
print("The distance from Thailand China is", GB, "km")
print("The distance from Thailand to Russia is", GE, "km")
print("The distance from Thailand to London is", GC, "km")
print("The distance from China to Russia is", BE, "km")
print("The distance from India to Spain is", DH, "km")
print("The distance from India to London is", DC, "km")
print("The distance from India to China is", DB, "km")
print("The distance from India to Russia is", DE, "km")
print("The distance from Brazil to United States is", IF, "km")
print("The distance from Brazil to Spain", IH, "km")
print("The distance from Spain to United States is", HF, "km")
print("The distance from Spain to London is", FC, "km")
print("The distance from London to United States is", CF, "km")
print("\n")

#Q3
import Q3

#Q5
import Q5

#Q7
print("\nThis is to check the political issues on each location")
import Q7

#Q8
import Q8

#Q9
print("\nThis is the sentiment conclusion for each location based on their political issues")
import Q9

#Q10
print("\nThis is the probability distribution for each destination and its route ")
import Q10