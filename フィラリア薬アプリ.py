import streamlit as st

def calculate_fee(medicines, weight, discount):
    fees = {
        "イベルメック": {"~5.6kg": 770, "5.6~11.3kg": 990, "11.3~22.6kg": 1210, "22.6~45.3kg": 1430},
        "クレデリオプラス": {"~2.8kg": 2420, "2.8~5.5kg": 2860, "5.5~11kg": 3300, "11~22kg": 3740, "22~45kg": 4180},
        "ネクスガードスペクトラ": {"~3.6kg": 2640, "3.6~7.5kg": 3080, "7.5~15kg": 3520, "15~30kg": 3960, "30~55kg": 4400},
        "ブラベクト": {"~4.5kg": 5500, "4.5~10kg": 6380, "10~20kg": 7040, "20~40kg": 7590},
        "クレデリオ": {"~2.5kg": 1760, "2.5~5.5kg": 1980, "5.5~11kg": 2200, "11~22kg": 2420, "22~45kg": 2640},
        "ネクスガード": {"~4.5kg": 1980, "4.5~11kg": 2200, "11~27kg": 2420, "27~55kg": 2640}
    }
    
    def get_size(medicine, weight):
        for size, price in fees[medicine].items():
            lower, upper = size.replace("kg", "").split("~")
            lower = float(lower) if lower else 0
            upper = float(upper) if upper else float("inf")
            if lower <= weight < upper:
                return size
        return "45kg~"
    
    total_price = 0
    for medicine, quantity in medicines.items():
        if medicine in fees:
            size = get_size(medicine, weight)
            base_price = fees[medicine][size]
            total_price += base_price * quantity
    
    discounted_price = total_price * (1 - discount / 100)
    discount_amount = total_price - discounted_price
    return total_price, discounted_price, discount_amount

st.title("動物病院 予防薬料金シミュレーター")

weight = st.number_input("体重 (kg)", min_value=0.1, step=0.1)
discount = st.number_input("割引率 (%)", min_value=0, max_value=100, step=1)

medicines = {}
options = ["イベルメック", "クレデリオプラス", "ネクスガードスペクトラ", "ブラベクト", "クレデリオ", "ネクスガード"]
selected_medicines = [medicine for medicine in options if st.checkbox(medicine)]

for medicine in selected_medicines:
    quantity = st.number_input(f"{medicine} の個数", min_value=1, step=1, key=f"quantity_{medicine}")
    medicines[medicine] = quantity

if st.button("計算"):
    total_fee, discounted_fee, discount_amount = calculate_fee(medicines, weight, discount)
    st.success(f"合計料金: {total_fee} 円")
    st.success(f"割引後の料金: {discounted_fee:.0f} 円")
    st.info(f"割引額: {discount_amount:.0f} 円")
st.title("動物病院 予防薬料金シミュレーター")

weight = st.number_input("体重 (kg)", min_value=0.1, step=0.1)
discount = st.number_input("割引率 (%)", min_value=0, max_value=100, step=1)

medicines = {}
options = ["イベルメック", "クレデリオプラス", "ネクスガードスペクトラ", "ブラベクト", "クレデリオ", "ネクスガード"]
selected_medicines = [medicine for medicine in options if st.checkbox(medicine)]

for medicine in selected_medicines:
    quantity = st.number_input(f"{medicine} の個数", min_value=1, step=1, key=f"quantity_{medicine}")
    medicines[medicine] = quantity

if st.button("計算"):
    total_fee, discounted_fee, discount_amount = calculate_fee(medicines, weight, discount)
    st.success(f"合計料金: {total_fee} 円")
    st.success(f"割引後の料金: {discounted_fee:.0f} 円")
    st.info(f"割引額: {discount_amount:.0f} 円")


weight = st.number_input("体重 (kg)", min_value=0.1, step=0.1)
num_medicines = st.number_input("使用する薬の種類数", min_value=1, max_value=4, step=1)
medicines = {}

for i in range(num_medicines):
    st.subheader(f"薬 {i+1}")
    medicine_type = st.selectbox("薬の種類", ["イベルメック", "クレデリオプラス", "ネクスガードスペクトラ", "ブラベクト"], key=f"medicine_{i}")
    quantity = st.number_input("個数", min_value=1, step=1, key=f"quantity_{i}")
    medicines[medicine_type] = quantity

if st.button("計算"):
    total_fee = calculate_fee(medicines, weight)
    st.success(f"合計料金: {total_fee} 円")
