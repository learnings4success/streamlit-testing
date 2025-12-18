# https://streamlit.io/playground?example=blank&code=H4sIAAAAAAAAA41WzW7jNhC--ynG8iFyNtHG6R9gwC1Sd9cxNomDxEGQk0FLtE1EIgWSitYIAhS9Fz3vaS8FeugL9Hn2BbqP0CEpyVLs7YYXy-Rwfr75ZoYsSYXUoLSkJImZBqLwT4u5bUl4JJLyn2YJbbU60Avg-s305rIP7yhNQa8o8CyZU2k_FUko0AfKgS3sBklTkDQWJFIt3NoLRZJmmsqZu7QHXGhgHM0GiirFBJ8pTTTttwDX893g2XUYFF4G5odx7fcOoHfUbbXwpmY6pr73-eNfHz79-vunD7_9-88fcE6WLIQLd3uE3npdE9VxAOOLy5tpH0ZUW8cv8Ky1yOJ4xk1MA-OLpu_1jHH0wPfecHQD1iKTYKTASPWNMoyyulZFkUumqb_wOp0OnNI4FvBYCT2123ivEIzYA4uo9LvQgSuaxiSkClJpQvMOPdjH6Ex4DbXeGdV7KBWTNSwzxKuelSVaCILAKy514JsAziaj8bAPU5TyrjWR2gOVMx2uwK9s2jBhTdVrLkrvUHK2rNAIVzS8n4v3vndH1QGMgSSYahKtQQsn3C6tIiab2w6UIgLGF8L3xs5vGgEp_Z5TnVPkUc9o6x2BP0aeKFixKMLdzx___LtboGZW9dGBWyRdGD5DYSFF4gjq6ASWTpBTCNFlbQy7tGuRVroqjn2Nhrvc-LZilIV5JKKCdV49_CKBFjsSIYOXmzKqu56sQSEvXCK371-I3CSA0zqC9iISNNiF01JEs3p87rsk96nIIcmQD2olsjgyuY0ipxADQa4ZZ37yDiBhfPZA4owOsPCUpumgV6S8SHvNzo9wtEm9A-m7BkhvGScxjAwTGnKbOCf3ZN1Gb1bkgRqXMFxbgc5CAIiD46EtoxJNLTTqna-xyhv4NXWfcIzQeBCvKzLrTPJSSxHFGIRkSyeHmsX9TpwbWJtlQdoF9agqWGt8Y8bGyEXe93Yg6-D7PoCfb6bTyYXD7wobL2rwp-jgsmjIIYnDLCYaudv0zpZkMM-0Ftz3hqaW4XwNJ1zlyNFuM1Nb4Tj7Q1s7oDKVUq4oxOye2kERqBiHg9_duoNdZmXLKWWcY5vzhqV_iHJierNN0bZ1s2qaj7vQ2uHQ4eEhTE_fuAYHb68m53A3ubmC6-HV-HJqjndcwon2i8jmMXWAFaUNz0q7XJzmm8IpPvbh-CVw4ZA5wTLatIL_V14rnVe1k5dYwh5_SmLkD9NbpysSL2oRbCy-flkU2Nius7mWJNRVKWyJOS4PGsYOvwSpzdtX1q5s_xDA5GZq28ctPiGEhDOh6JagGcjOnYErw93sMtWARS0EVzuIW0iozI4WnORDwZeS6KK2VHOet-FOZJDjnDGUMkOvbSu0QCLHd9ajGenWr-6Tt22PxurLflIphUQfroWU68JYLPDAGglxl2JyXm6sUFs-Uvyxm9bYXW29PjpNTwcQ2TqJkFZmKhf7-8d4UmvGjxvi4sES33eV4KvG0cpQNLKaajwxyrAVq4JjKFDa75bPiSY4mxZ-S5htJAthX2bVO8T2lP8AW4HW5-0KAAA

# https://streamlit.io/playground?example=blank
import streamlit as st
import random
import time

if 'computer_number' not in st.session_state:
    st.session_state.computer_number = random.randint(1, 10)

st.title("🧙‍♂️ Magic Number Game")

full_name = st.text_input("Enter your full name:")

if full_name:
    st.write(f"### Hello {full_name}!!")
    st.divider()

    st.write("Let's play guess the number game...")

    start_game = st.checkbox("Yes, I am ready to start!")

    if start_game:
        st.info("I guessed a number between 1 to 10 (It is hidden 🤫)")
        
        number = st.session_state.computer_number
        
        st.write("I am adding the same number from my side...")
        st.write("Now, I need a number from you.")
        
        god_number = st.number_input("How much should I add from God's side?", min_value=1, step=1)

        if god_number > 0:
            st.write("Okay! I have added your number. Now I am dividing the total by 2...")
            st.write("And finally, I am returning the number I originally took from you.")
            
            value = st.number_input("Guess the final number I have now:", step=1)

            if st.button("Check My Answer"):
                
                with st.spinner("Calculating magic..."):
                    time.sleep(2) 

                new_number = number * 2
                
                new_number = god_number + new_number
                
                half_number = new_number / 2
                
                final = half_number - number

                if final == value:
                    st.balloons()
                    st.success(f"Congratulations {full_name}!!! You won the game! The number was {int(final)}")
                else:
                    st.error(f"Sorry!! You lost. The correct number was {int(final)}")
                    st.write(f"(I started with {number}, doubled it to {number*2}, added your {god_number}, got {number*2+god_number}, halved to {half_number}, and subtracted {number})")

    else:
        st.write("Waiting for you to start...")