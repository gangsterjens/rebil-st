import streamlit as st
import requests

with st.sidebar:
  regnr = st.text_input('skriv inn regnr her')


url = f'https://kjoretoyoppslag.atlas.vegvesen.no/ws/no/vegvesen/kjoretoy/kjoretoyoppslag/v1/kjennemerkeoppslag/kjoretoy/{regnr}'
st.markdown(url)
data = requests.get(url)
data = data.json()

st.write(data)

last_checked = data['periodiskKjoretoykontroll']['sistKontrollert']
next_check = data['periodiskKjoretoykontroll']['nesteKontroll']

lastegenskaper = data["tekniskKjoretoy"]["lastegenskaper"]

tilhengervekt_med_brems = lastegenskaper["tillattTilhengervektMedBrems"]
tilhengervekt_uten_brems = lastegenskaper["tillattTilhengervektUtenBrems"]
vertikal_koplingslast = lastegenskaper["tillattVertikalKoplingslast"]
vogntogvekt = lastegenskaper["tillattVogntogvekt"]

modell = data['tekniskKjoretoy']['handelsbetegnelse']
merke = data['tekniskKjoretoy']['merke']



st.markdown(f'siste eu-kotnroll: {last_checked}')
st.markdoown(f'neste eu-kotrnoll: {next_check}')




