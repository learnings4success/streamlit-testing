import streamlit as st
import random
import streamlit.components.v1 as components # Import this for the print button

# Import your math logic
from tax_calculator import calculate_discount, calculate_gst

st.set_page_config(page_title="Pizza Receipt", page_icon="🍕")

st.title("🍕 Punjabi Pizza Hut")
st.write("Welcome! Order your fresh pizza below.")

# --- INPUTS ---
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Customer Name:")

with col2:
    menu = ["Margherita", "Vegi Pizza", "Farmhouse", "Paneer Tikka"]
    pizza = st.selectbox("Choose Pizza:", menu)

# --- CALCULATE BUTTON ---
if st.button("Generate Bill 🧾"):
    
    if name == "":
        st.error("Please enter a name first!")
    else:
        # 1. LOGIC
        pizza_price = random.randint(150, 500)
        pizza_discount = random.randint(15, 20)

        discount_amount = calculate_discount(pizza_price, pizza_discount)
        final_without_tax = pizza_price - discount_amount
        final_with_tax = calculate_gst(final_without_tax)
        gst_amount = final_with_tax - final_without_tax

        # 2. DISPLAY RECEIPT (This part will be printed)
        st.divider()
        st.subheader("🧾 Tax Invoice")
        st.write(f"**Customer:** {name}")
        st.write(f"**Item:** {pizza}")
        
        # Bill Table
        c1, c2 = st.columns([3, 1])
        
        with c1:
            st.write("Base Price")
            st.write(f"Discount ({pizza_discount}%)")
            st.write("GST (5%)")
            st.markdown("### TOTAL")
        
        with c2:
            st.write(f"₹ {pizza_price}")
            st.write(f"- ₹ {discount_amount:.2f}")
            st.write(f"+ ₹ {gst_amount:.2f}")
            st.markdown(f"### ₹ {final_with_tax:.2f}")
            
        st.success("Thank you for visiting!")
        st.divider()

        # 3. THE MAGIC PRINT BUTTON 🖨️
        # We inject HTML/CSS/JS directly into the browser
        
        print_code = """
        <script>
            function printReceipt() {
                window.print();
            }
        </script>
        
        <style>
            /* This CSS only applies when PRINTING */
            @media print {
                /* Hide the Sidebar, Header, and Footer */
                [data-testid="stSidebar"], 
                header, 
                footer, 
                .stApp > header {
                    display: none !important;
                }
                
                /* Hide the Print Button itself on the paper */
                .no-print {
                    display: none !important;
                }
                
                /* Make the font black for paper */
                body {
                    color: black !important;
                }
            }
            
            /* Button Style for the Website */
            .print-btn {
                background-color: #ff4b4b;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                font-weight: bold;
            }
            .print-btn:hover {
                background-color: #ff3333;
            }
        </style>
        
        <div style="text-align: center; margin-top: 20px;">
            <button class="print-btn no-print" onclick="printReceipt()">
                🖨️ Print Receipt Now
            </button>
        </div>
        """
        
        # Render the HTML button
        components.html(print_code, height=100)