import pandas as pd
import plotly.express as px
import streamlit as st

st.title('VACINAÇÃO - Um Painel de Informações sobre a Vacinação contra COVID-19 - Ano 2021')

st.set_page_config(page_title = 'DASHVACINA', layout = 'wide')

df = pd.read_csv('vacinacao_corrigido.csv')

df['date'] = pd.to_datetime(df['date'])

fig1 = px.line(df, x = 'date', y = 'total_vaccinations', 
               color = 'location', 
               title = 'Total de pessoas vacinadas por data e paísSegundo a OMS') 
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'Total de pessoas vacinadas')
fig1.show()

st.plotly_chart(fig1, use_container_width=True)

df_filtro = df.query('location == "BRAZIL" or location == "INDIA" or location == "UNITED STATES"') 
fig2 = px.pie(df_filtro, 
              values = 'people_fully_vaccinated', 
              names = 'location', title = 'Dados comparativos de pessoas totalmente vacinadas') 
fig2.show()

st.plotly_chart(fig2, use_container_width=True)
