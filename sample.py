# 実行はVSC内のターミナルを開いて'streamlit run main.py'
# コマンド一覧：Welcome to Streamlit -> REFERENCE GUIDES -> API reference
# https://docs.streamlit.io/library/api-reference

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('DataFrame')
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40],
})

# 表
# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
# st.dataframe(df.style.highlight_max(axis=0))
st.table(df.style.highlight_max(axis=0))

# マークダウン
"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

# グラフ
df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

df_map = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.7],
    columns=['lat', 'lon'] # 緯度, 経度
)
st.map(df_map)

st.write('Disply Image')
img = Image.open('切断部.PNG')
st.image(img, caption='切断部', use_column_width=True)
