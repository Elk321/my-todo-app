import streamlit as st
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass


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
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
