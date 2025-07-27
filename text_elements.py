import streamlit as st


st.title("Super big text(title)")
st.header("a bit smaller than the title(header)")
st.subheader("a bit smaller than the header(subheader)")
st.markdown("this is **Markdown**")#bolds the text in the **text**
st.markdown("this is _Markdown_") #this gives italic _text_
st.caption("small text") # a really small text size colored as caption

# to render a code in streamlit page
code_ex= """
    def greet(name):
    print("hello", name)
"""
st.code(code_ex, language='python')
st.divider()


# adding an image
import os
st.image(os.path.join(os.getcwd(), "static", 'image.png'), width=500)