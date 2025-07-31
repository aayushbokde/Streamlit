import streamlit as st
import pandas as pd

st.title('Streamlit Element Demo')
st.subheader("Dataframe")
#dataframe
df = pd.DataFrame({
    'name' : ['Alice', 'bob', 'charlie', "David"],
    'age' : [23, 24, 45, 65],
    'Occupation' : ['Engineer', 'Doctor', 'Artist', 'chef']    
})
 
st.dataframe(df) #this is specifically used for pandas dataframe

#data editable 

st.subheader("Data Editor")
editable_df = st.data_editor(df)

#static table
st.subheader("Static Table")
st.table(df)

#metrics Section
st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=round(df['age'].mean(), 1))

#JSON and Dict 
st.subheader("Json and Dictionary")
sample_dict = {
    'name':'Alice',
    'age' : 23,
    'Skills' : ["pyhton", "data science", "Machine Learning"]
}
st.json(sample_dict)

#also show it as dictionary
st.write("dictionary view: ", sample_dict )