import streamlit as st
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

st.set_page_config(layout="wide")
todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo_local = st.session_state["new_todo"]
    todo_local = functions.cap_todo(functions.period_check(todo_local))
    todos.append(todo_local)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your <b>productivity</b>.",
         unsafe_allow_html=True)

for index, todo in enumerate(todos):
    key= f"{index}-todo"
    checkbox = st.checkbox(todo, key=key)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[key]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
