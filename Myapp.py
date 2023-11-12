import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


dataset=pd.read_excel(r"C:\Users\yleka\OneDrive\Dokumente\ONLINEEEEE\AGE_GROUPE.xlsx")
dataset1=pd.read_excel(r"C:\Users\yleka\OneDrive\Dokumente\ONLINEEEEE\PROVINCE_GROUPE.xlsx")
dataset2=pd.read_excel(r"C:\Users\yleka\OneDrive\Dokumente\ONLINEEEEE\AREA.xlsx")
st.set_page_config(page_title="Labour Force Dahsboard", layout="wide")
st.title("Labour Force Dashboard")
st.sidebar.header("Filter by:")

age_range=st.sidebar.multiselect("Age:",

                                   options=dataset["Age Group"].unique(),
                                   default=dataset["Age Group"].unique()
                                   )

selection_query=dataset.query("OUTSIDELF==@age_range")

st.dataframe(dataset)



province_choice=st.sidebar.multiselect("Province:",

                                   options=dataset1["By Province"].unique(),
                                   default=dataset1["By Province"].unique())

selection_query1=dataset1.query("LFT1==@province_choice")

st.dataframe(dataset1)

st.line_chart(dataset2,x="By Province", y="LFT1")
lft_by_category=(dataset.groupby(by=["Age Group"]).sum()[["LFPR"]])
outside_by_province=(dataset1.groupby(by=["By Province"]).sum()[["OUTSIDELF"]])

fig=px.bar(
    outside_by_province,

    x="OUTSIDELF",
    y=outside_by_province.index, 
    title="Outside Labour Force by Province",   
    orientation="h", 
     
      )


fig.update_layout(plot_bgcolor="rgba(0,0,0,0)",xaxis=(dict(showgrid=False)))


fog=px.pie(lft_by_category,names=lft_by_category.index,values="LFPR",title="Labour force particpation rate by age group",hole=.3,color=lft_by_category.index)

left_column,right_column=st.columns(2)
left_column.plotly_chart(fig,use_container_width=True)
right_column.plotly_chart(fog,use_container_width=True)




