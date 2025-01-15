import streamlit
import pandas as pd
from streamlit_folium import st_folium
import folium

#Test utilisation de streamlit MAP

df_sgTT=pd.read_csv('soliguideTT.csv', sep=";")
df_sgTT=pd.DataFrame(df_sgTT)
lieuxTT =pd.DataFrame(df_sgTT, columns=["Nom de la structure", "Adresse","lat","lng"]) 

streamlit.header('Essai Streamlit sur different thème')

streamlit.selectbox('Menu',('http://localhost:8504/#guide-solinium-pour-les-departements-33-75-et-93','http://192.168.1.162:8504/#ce7e7138','http://192.168.1.162:8504/#streamlit-avec-folium'))

streamlit.status(label='Dans quel état suis-je')

streamlit.title('Guide Solinium pour les departements 33, 75 et 93')

streamlit.button('email')

streamlit.dataframe(data=lieuxTT)
streamlit.map(data=lieuxTT,latitude='lat',longitude='lng',color='#000ff0')

#autre test avec passages a niveau

streamlit.title('Passages à niveau')

df_PN=pd.read_csv('liste-des-passages-a-niveau.csv', sep=";")
df_PN=pd.DataFrame(df_PN)

streamlit.dataframe(data=df_PN)
streamlit.map(data=df_PN,latitude='Lat',longitude='Lng',color='#0f0ff0')

#Test streamlit avec Folium

streamlit.title('Streamlit avec Folium')

m = folium.Map(location=[43.91480092960565, 2.148532962035286],zoom_start=20)
    
folium.Marker(
    location=[43.91480092960565, 2.148532962035286],
    popup=["416+244"],
    icon=folium.Icon(color='green')).add_to(m)

st_data=st_folium(m, width=725)