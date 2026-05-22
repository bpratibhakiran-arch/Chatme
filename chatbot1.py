import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Het-Jet AI")

st.title("Het-Jet AI")
st.write("How can I help you today?")

a = st.button("Simple Calculator")
b = st.button("Play Games")
c = st.button("Table Teller")
d = st.button("Check Time")



if b:

    st.subheader("Choose a Game")

    e = st.button("Rock Paper Scissors")
    f = st.button("Roll Dice")

    if e:

        user = st.selectbox(
            ["Rock", "Paper", "Scissors"]
        )
        computer = random.choice(
                ["Rock", "Paper", "Scissors"]
            )

        st.write("Computer chose:", computer)

        if user == computer:

            st.success("Draw!")

        elif (
            (user == "Rock" and computer == "Scissors")
            or
            (user == "Paper" and computer == "Rock")
            or
            (user == "Scissors" and computer == "Paper")
            ):

            st.success("You Win!")

        else:

            st.error("Computer Wins!")


    if f:

        dice = random.randint(1, 6)

        st.success(f"You got {dice}")



if a:

    num1 = st.number_input("Enter first no. : ")
    num2 = st.number_input("Enter second no. : ")

    col1, col2, col3 = st.columns(3)

    with col1:
        add = st.button("Add")
        div = st.button("Divide")

    with col2:
        sub = st.button("Subtract")
        pow = st.button("Power")

    with col3:
        mul = st.button("Multiply")
        per = st.button("Percentage")

    if add:
        result = (num1 + num2)
        st.markdown(f"""Answer = {result}""")

    elif sub:
        result = (num1 - num2)
        st.markdown(f"""Answer = {result}""")
    
    elif mul:
        result = (num1 * num2)
        st.markdown(f"""Answer = {result}""")

    elif div:
        result = (num1 / num2)
        st.markdown(f"""Answer = {result}""")

    elif pow:
        result = (num1 ** num2)
        st.markdown(f"""Answer = {result}""")

    elif per:
        result = ((num1 / 100) * num2)
        st.markdown(f"""Answer = {result}""")
        

if c:

    num = st.number_input(
        "Enter Number",
        step=1
    )
    g = st.button("Show Table")
    if g:

        for i in range(1, 11):

            st.write(f"{num} x {i} = {num*i}")
            

if d:

    current_time = datetime.now().strftime(
        "%H:%M:%S"
    )

    st.success(f"Current Time: {current_time}")