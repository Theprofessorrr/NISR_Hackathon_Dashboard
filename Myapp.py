import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Labour Force Dahsboard", layout="wide")




dataset=pd.read_excel('AGE_GROUPE.xlsx')
dataset1=pd.read_excel('PROVINCE_GROUPE.xlsx')
dataset2=pd.read_excel('Gender.xlsx')
dataset3=pd.read_excel('area.xlsx')

st.title("Labour Force Dashboard")
st.sidebar.header("Filter by:")

age_range=st.sidebar.multiselect("Age:",

                                   options=dataset["Age"].unique(),
                                   default=dataset["Age"].unique()
                                   )

selection_query=dataset.query("Age==@age_range")




province_choice=st.sidebar.multiselect("Province:",

                                   options=dataset1["Province"].unique(),
                                   default=dataset1["Province"].unique())

selection_query1=dataset1.query("Province==@province_choice")

gender_choice=st.sidebar.multiselect("Gender:",

                                    options=dataset2["Gender"].unique(),
                                    default=dataset2["Gender"].unique())

selection_query2=dataset2.query("Gender==@gender_choice")

area_choice=st.sidebar.multiselect("Area:",
                                   options=dataset3["Area"].unique(),
                                   default=dataset3["Area"].unique())
selection_query3=dataset3.query("Area==@area_choice")
                                   

total_labour=int(selection_query1["Labour_Force"].sum())
average_outsidef=round(selection_query1["OUTSIDELF"].mean(),1)
total_population=int(selection_query1["POPULATION"].sum())
total_employed=int(selection_query["Employment"].sum())
total_unemployed=int(selection_query["Unemployment"].sum())
unique_column,=st.columns(1)
unique_column.metric("Total Population",f"{total_population}")

st.markdown("---")

left_column0,middle_column1,right_colum3,middle_column0 = st.columns(4)
left_column0.metric("Total Labour Force ",f"{total_labour}")
middle_column1.metric("Total Employed",f"{total_employed}")
right_colum3.metric("Total Unemployed",f"{total_unemployed}")
middle_column0.metric("Average Outside Labour Force ",f"{average_outsidef}")
st.markdown("---")



emp_by_age=(selection_query.groupby(by=["Age"]).sum()[["Employment"]])
unemp_by_age=(selection_query.groupby(by=["Age"]).sum()[["Unemployment"]])
emp_by_province=(selection_query1.groupby(by=["Province"]).sum()[["Employment"]])
unemp_by_province=(selection_query1.groupby(by=["Province"]).sum()[["Unemployment"]])
emp_by_gender=(selection_query2.groupby(by=["Gender"]).sum()[["Employment"]])
unemp_area=(selection_query3.groupby(by=["Area"]).sum()[["Unemployment"]])
fig=px.bar(
    emp_by_province,

    x="Employment",
    y=emp_by_province.index, 
    title="Employment by Province", 
    orientation="h", 
     
      )
fig.update_layout(plot_bgcolor="#072223",xaxis=(dict(showgrid=False)))
feg=px.bar(
    unemp_by_province,
    x="Unemployment",
    y=unemp_by_province.index,
    title="Unemployment by Province",
    orientation="h",)
feg.update_layout(plot_bgcolor="#072223",xaxis=(dict(showgrid=False)))


fog=px.pie(emp_by_age,names=emp_by_age.index,values="Employment",title="Employment by age group",hole=.3,color=emp_by_age.index)
fag=px.pie(unemp_by_age,names=unemp_by_age.index,values="Unemployment",title="Unemployment by age group",hole=.3,color=unemp_by_age.index)
faag=px.pie(unemp_area,names=unemp_area.index,values="Unemployment",title="Unemployment by Area",hole=.3,color=unemp_area.index)
fug=px.pie(emp_by_gender,names=emp_by_gender.index,values="Employment",title="Employment by Gender",hole=.3,color=emp_by_gender.index)


left_column,right_column=st.columns(2)
left_column.plotly_chart(fog,use_container_width=True)
right_column.plotly_chart(fag,use_container_width=True)

left_column1,right_colum1=st.columns(2)
left_column1.plotly_chart(fig,use_container_width=True)
right_colum1.plotly_chart(feg,use_container_width=True)

left_column2, right_colum2=st.columns(2)
left_column2.plotly_chart(fug,use_container_width=True)
right_colum2.plotly_chart(faag,use_container_width=True)


