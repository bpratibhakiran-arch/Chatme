import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Het-Jet AI")

st.title("Het-Jet AI")
st.write("How can I help you today?")

# ---------------- SESSION STATE ---------------- #

if "menu" not in st.session_state:
    st.session_state.menu = ""

# ---------------- MAIN MENU BUTTONS ---------------- #

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Calculator", key="calc_btn"):
        st.session_state.menu = "calculator"

with col2:
    if st.button("Games", key="games_btn"):
        st.session_state.menu = "games"

with col3:
    if st.button("Tables", key="table_btn"):
        st.session_state.menu = "table"

with col4:
    if st.button("Time", key="time_btn"):
        st.session_state.menu = "time"

# ---------------- CALCULATOR ---------------- #

if st.session_state.menu == "calculator":

    st.subheader("Simple Calculator")

    num1 = st.number_input(
        "Enter First Number",
        key="num1"
    )

    num2 = st.number_input(
        "Enter Second Number",
        key="num2"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        add = st.button("Add", key="add_btn")
        div = st.button("Divide", key="div_btn")

    with col2:
        sub = st.button("Subtract", key="sub_btn")
        power = st.button("Power", key="pow_btn")

    with col3:
        mul = st.button("Multiply", key="mul_btn")
        per = st.button("Percentage", key="per_btn")

    if add:
        result = num1 + num2
        st.success(f"Answer = {result}")

    elif sub:
        result = num1 - num2
        st.success(f"Answer = {result}")

    elif mul:
        result = num1 * num2
        st.success(f"Answer = {result}")

    elif div:

        if num2 != 0:
            result = num1 / num2
            st.success(f"Answer = {result}")

        else:
            st.error("Cannot divide by zero")

    elif power:
        result = num1 ** num2
        st.success(f"Answer = {result}")

    elif per:
        result = (num1 / 100) * num2
        st.success(f"Answer = {result}")

# ---------------- GAMES ---------------- #

elif st.session_state.menu == "games":

    st.subheader("Choose a Game")

    game = st.selectbox(
        "Select Game",
        ["Rock Paper Scissors", "Roll Dice"],
        key="game_select"
    )

    # ROCK PAPER SCISSORS
    if game == "Rock Paper Scissors":

        user = st.selectbox(
            "Choose",
            ["Rock", "Paper", "Scissors"],
            key="rps_choice"
        )

        if st.button("Play", key="play_rps"):

            computer = random.choice(
                ["Rock", "Paper", "Scissors"]
            )

            st.write(f"Computer chose: {computer}")

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

    # DICE GAME
    elif game == "Roll Dice":

        if st.button("Roll Dice", key="dice_roll"):

            dice = random.randint(1, 6)

            st.success(f"You got {dice}")

# ---------------- TABLE TELLER ---------------- #

elif st.session_state.menu == "table":

    st.subheader("Table Teller")

    num = st.number_input(
        "Enter Number",
        step=1,
        key="table_num"
    )

    if st.button("Show Table", key="show_table"):

        for i in range(1, 11):

            st.write(f"{num} × {i} = {num*i}")

# ---------------- TIME ---------------- #

elif st.session_state.menu == "time":

    st.subheader("Current Time")

    components.html(
        """
        <div id="clock" style="
            font-size:30px;
            font-weight:bold;
            color:lime;
            padding:20px;
            border-radius:10px;
            background-color:#0e402d;
            text-align:center;
        ">
        </div>

        <script>
        function updateClock() {

            const now = new Date();

            const time = now.toLocaleTimeString();

            document.getElementById("clock").innerHTML =
                "Current Time: " + time;
        }

        setInterval(updateClock, 1000);

        updateClock();
        </script>
        """,
        height=100
    )