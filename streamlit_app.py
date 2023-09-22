python
import streamlit as st
import random

# 世界のイケメンのリストを作成する
ikemen_list = ["Brad Pitt", "Chris Hemsworth", "Tom Cruise", "David Beckham", "Henry Cavill","William Franklyn Miller","Leonardo Dicaprio","Zain Javadd Malik"]

# タイトルを表示する
st.title("世界のイケメンガチャ")

# ボタンを作成する
button = st.button("イケメンガチャを引く")

# ボタンがクリックされたら、ランダムにイケメンを選択して表示する
if button:
    ikemen = random.choice(ikemen_list)
    st.write("あなたにおすすめのイケメンは...")
    st.write(ikemen)