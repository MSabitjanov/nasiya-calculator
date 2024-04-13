import streamlit as st

st.set_page_config(page_title="Nasiya calculator", page_icon="🧮")
st.title("🧮 Muddatli to`lovni hisoblash")

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("💵")
price = st.number_input("Maxsulot narxi", min_value=0, step=100)

st.subheader("🗓️")
months = st.number_input("Muddat:", min_value=0, step=1)

st.subheader("%")
percent = st.number_input("Foiz stavkasi", min_value=0, step=1)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


def get_calculated_price(price=0, months=0, percent=0):
    total_price = price + price * percent / 100
    monthly_price = total_price / months
    return total_price, monthly_price


total = st.container(border=True)
col1, col2 = total.columns(2)
if price and months and percent:
    total_price, monthly_price = get_calculated_price(price, months, percent)
else:
    total_price, monthly_price = 0, 0
with col1:
    st.subheader(f"{total_price} $")
    st.caption("Umumiy to'lov summasi")
with col2:
    st.subheader(f"{months} oy / {monthly_price:.2f}$ dan")
    st.caption("Oylik to'lov summasi")
