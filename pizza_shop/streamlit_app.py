import streamlit as st
import random

# IMPORTING your custom functions
# This works exactly like the CLI version!
from tax_calculator import calculate_discount, calculate_gst

# Title and Greeting
st.title("🍕 Punjabi Pizza Hut")
st.write("Hello Sir/Madam! Welcome to the best Pizza in town.")

# --- INPUTS ---
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("What is your name:")

with col2:
    # Instead of printing options one by one, we make a Dropdown list
    menu = [
        "Margherita",
        "Vegi Pizza",
        "Farmhouse",
        "Paneer Tikka"
    ]
    pizza = st.selectbox("What would you like to order:", menu)

# --- ACTION ---
# We use a button to trigger the calculation (The Order)
if st.button("Calculate Bill 🧾"):
    
    if name == "":
        st.error("Please enter your name first!")
    else:
        # --- LOGIC (From your Python Script) ---
        # 1. Generate Random Price & Discount
        pizza_price = random.randint(150, 500)
        pizza_discount = random.randint(15, 20)

        # 2. Calculate using the imported functions
        discount_amount = calculate_discount(pizza_price, pizza_discount)
        
        final_price_without_tax = pizza_price - discount_amount
        final_price_with_tax = calculate_gst(final_price_without_tax)
        
        gst_amount = final_price_with_tax - final_price_without_tax

        # --- OUTPUT (The Receipt) ---
        st.balloons() # Fun animation!
        
        st.divider() # This replaces print("-" * 50)
        
        st.subheader(f"Order for: {name}")
        st.success(f"You selected: **{pizza}**")

        st.markdown("### 📝 Final Bill Details")

        # Using columns to make the bill look neat
        c1, c2 = st.columns([2, 1]) # Column 1 is wider (Text), Column 2 is narrower (Price)

        with c1:
            st.write("Base Price:")
            st.write(f"Discount ({pizza_discount}%):")
            st.write("Price After Discount:")
            st.write("GST (5%):")
            st.markdown("**TOTAL TO PAY:**") # Bold text

        with c2:
            st.write(f"₹ {pizza_price}")
            st.write(f"- ₹ {discount_amount:.2f}")
            st.write(f"₹ {final_price_without_tax:.2f}")
            st.write(f"+ ₹ {gst_amount:.2f}")
            st.markdown(f"**₹ {final_price_with_tax:.2f}**")
        
        st.divider()