'''

- Source: [【Streamlit超入門】データ可視化・分析アプリを爆速で作成できるPythonライブラリStreamlitの基礎を70分でマスター](https://www.youtube.com/watch?v=zp-kAt1Ih5k)
- Updated on: Dec 2020

'''


import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit　Basics')
# st.sidebar.title('Streamlit　Basics')



# Table
st.write('DataFrame')

df = pd.DataFrame({
	'column１': [1, 2, 3, 4],
	'column 2': [10, 20, 30, 40]
	})


# Interactive Table

# st.write(df)

# Dataframe offers paramaters.
# st.dataframe(df, width=100, height=100)
st.dataframe(df.style.highlight_max(axis=0))


# Static Table

st.table(df.style.highlight_max(axis=0))



# Markdown

"""
# Chapter
## Section
### Item

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""



# Chart

df = pd.DataFrame(
	np.random.rand(20, 3),
	columns=['a', 'b', 'c']
	)

st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)




# Map Plot

df = pd.DataFrame(
	np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
	columns=['lat', 'lon']
	)

st.map(df)



# Show an image

st.write('Display Image')

img = Image.open('sample.jpg')
st.image(img, caption='Kohei Imanishi', use_column_width=True)



# Interactive Widget

# Check Box
if st.checkbox('Show Image'):
	img = Image.open('sample.jpg')
	st.image(img, caption='Kohei Imanishi', use_column_width=True)

if st.checkbox('Show Line Chart'):
	chart_df = pd.DataFrame(
		np.random.randn(20, 3),
		columns=['a', 'b', 'c']
		)
	st.line_chart(chart_df)

# Select Box
option = st.selectbox(
	'Tell me your favorite number.',
	list(range(1, 11))
	)
'Your favorite number is', option, '.'

# Text Input
st.write('Interactive Widgets')
text = st.text_input('Tell me your another hobby.')
'Your Another Hobby:', text

# Slider
condition = st.slider('How are you right now?', 0, 100, 50)
'Current Status：', condition




# Layout

# Sidebar
# st.sidebar.write('Interactive Widgets')
st.sidebar.header('Interactive Widgets')
text2 = st.sidebar.text_input('Tell me you hobby')
condition2 = st.sidebar.slider('How are you?', 0, 100, 50)

'Your Hobby：', text2
'Status：', condition2

# ２ Column Layout
left_column, right_column = st.beta_columns(2)
button = left_column.button('Show text in the right column')
if button:
	right_column.write('Here is the right column.')




# Progress Bar
st.write('Show a progress bar')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
	latest_iteration.text(f'Iteration {i+1}')
	bar.progress(i+1)
	time.sleep(0.1)

'Done!!!'

# Expander
expander1 = st.beta_expander('Query1')
expander1.write('Answer to Query1')
expander2 = st.beta_expander('Query2')
expander2.write('Answer to Query2')
expander3 = st.beta_expander('Query3')
expander3.write('Answer to Query3')






