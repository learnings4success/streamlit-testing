import streamlit as st
import random

# IMPORTING your custom module
# Make sure tax_calculator.py is in the same folder!
from tax_calculator import calculate_discount, calculate_gst

st.set_page_config(page_title="Burger Shop", page_icon="🍔")

# --- 1. HEADERS ---
st.title("🍔 Punjabi Burger Shop")
st.write("Welcome Sir/Madam! Please place your order.")

# --- 2. INPUTS ---
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("What is your name?")

with col2:
    # A list replaces the multiple print() statements
    menu_options = [
        "Allu tikki Burger", 
        "Double tikki Burger", 
        "Paneer Burger", 
        "Noodles Burger", 
        "Fried Burger"
    ]
    burger = st.selectbox("What would you like to order:", menu_options)

# --- 3. PROCESSING (Triggered by Button) ---
if st.button("Order Now 🧾"):
    
    if name == "":
        st.error("Please enter your name first!")
    else:
        # --- Random Logic from your script ---
        burger_price = random.randint(50, 100)
        burger_discount = random.randint(10, 20)

        # --- Calculations using Imported Functions ---
        discount_amount = calculate_discount(burger_price, burger_discount)
        final_price_without_tax = burger_price - discount_amount
        
        final_price_with_tax = calculate_gst(final_price_without_tax)
        
        gst_amount = final_price_with_tax - final_price_without_tax

        # --- 4. OUTPUT ( The Receipt ) ---
        st.divider()
        st.subheader(f"Thank you, {name}!")
        st.success(f"Order Placed: **{burger}**")

        # Let's make the receipt look fancy using columns
        st.write("### 🧾 Final Bill")
        
        # Row 1: Base Price
        c1, c2 = st.columns(2)
        c1.write("Original Price:")
        c2.write(f"₹ {burger_price}")
        
        # Row 2: Discount
        c1, c2 = st.columns(2)
        c1.write(f"Discount ({burger_discount}%):")
        c2.write(f"- ₹ {discount_amount:.2f}")
        
        # Row 3: Price after Discount
        c1, c2 = st.columns(2)
        c1.write("Price after Discount:")
        c2.write(f"₹ {final_price_without_tax:.2f}")
        
        # Row 4: GST
        c1, c2 = st.columns(2)
        c1.write("GST (5%):")
        c2.write(f"+ ₹ {gst_amount:.2f}")
        
        st.divider()
        
        # Final Total
        st.metric(label="TOTAL TO PAY", value=f"₹ {final_price_with_tax:.2f}")