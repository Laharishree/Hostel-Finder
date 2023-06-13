# Import required libraries
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import folium

features = ['latitude', 'longitude', 'price', 'Rating', 'wifi', 'ac', 'laundry', 'security']
#features =	["latitude"	,"longitude"	,	"Rating",	"wifi",	"ac",	"laundry",	"security"	,"price"]
df1=pd.read_csv(r"E:\Hostel-Finder\HostelFinder\HostelPrediction\HostelCluster.csv")
# Preprocess data
X = df1[features]
#X = pd.get_dummies(X, columns=['review'])

# print(X.head())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine optimal number of clusters
silhouette_scores = []
for n_clusters in range(2, 5):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(X_scaled)
    silhouette_scores.append(silhouette_score(X_scaled, cluster_labels))
    

optimal_n_clusters = np.argmax(silhouette_scores)+2
# print(silhouette_scores)
print(optimal_n_clusters)



# Perform clustering
kmeans = KMeans(n_clusters=optimal_n_clusters, random_state=42)
cluster_labels = kmeans.fit_predict(X_scaled)

# Add cluster labels to original dataset
df1['cluster'] = cluster_labels
def recommend_hostels(latitude, longitude, price, wifi,ac,laundry, security,Rating):
    user_input = pd.DataFrame({
        'latitude': [latitude],
        'longitude': [longitude],
        'price': [price],
        'Rating':[Rating],
        'wifi': [wifi],
        'ac': [ac],
        'laundry': [laundry],
        'security': [security]
    })
    #user_input = pd.get_dummies(user_input, columns=['wifi', 'ac', 'laundry', 'security'])
    user_input_scaled = scaler.transform(user_input)
    # print(user_input_scaled)
    user_cluster = kmeans.predict(user_input_scaled)[0]
    recommended_hostels = df1[df1['cluster'] == user_cluster].sort_values('Rating', ascending=False)
    recommended_hostels['dist'] = recommended_hostels.apply(lambda row: distance(latitude, longitude, row['latitude'], row['longitude']), axis=1)
    recom= recommended_hostels.sort_values('dist', ascending=False)
    # print()
 
    return recommended_hostels[['Hostel_name','address', 'price', 'Rating','latitude', 'longitude',"BusStop","Distance","EmbeddedMap"]]

from math import radians, cos, sin, asin, sqrt

def distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two latitude and longitude coordinates.
    """
    # Convert latitude and longitude to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r





# print(recommend_hostels(latitude=12.8369852, longitude=77.985, price=8000, wifi= 0, ac=0, laundry= 1, security=1,Rating=3.7))




