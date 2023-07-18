import requests
import streamlit as st
from models.user import User

# Define the base URL for the FastAPI server
BASE_URL = 'http://localhost:8000'

# Function to make HTTP requests to the FastAPI server
def make_request(url, method='GET', payload=None):
    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, json=payload)
    elif method == 'PUT':
        response = requests.put(url, json=payload)
    elif method == 'DELETE':
        response = requests.delete(url)
    return response

# Streamlit app
def main():
    st.title('Student Data Management')

    # List all students
    st.header('All Students')
    #all_students_url = BASE_URL + '/user/'
    all_students_url = BASE_URL +'/'
    response = make_request(all_students_url)
    if response.status_code == 200:
        students = response.json()
        for student in students:
            st.write(f"Name: {student['name']}, Email: {student['email']}")

    # Create a new student
    st.header('Create Student')
    name = st.text_input('Name')
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    if st.button('Create'):
        new_student = User(name=name, email=email, password=password)
        create_student_url = BASE_URL + '/studentdata'
        response = make_request(create_student_url, method='POST', payload=new_student.dict())
        if response.status_code == 200:
            st.success('Student created successfully')

    # Find a single student
    # st.header('Find Student by ID')
    # student_id = st.text_input('Student ID')
    # if st.button('Find'):
    #     find_student_url = BASE_URL + f'/single_student/{student_id}'
    #     response = make_request(find_student_url)
    #     if response.status_code == 200:
    #         student = response.json()
    #         st.write(f"Name: {student['name']}, Email: {student['email']}")


    #find by name
    st.header("Find student by name")
    name = st.text_input("enter student name")
    if st.button('Find'):
        find_student_url = BASE_URL+f'/student/{name}'
        response = make_request(find_student_url)
        if response.status_code == 200:
            student = response.json()
            # st.write(f"Name:{student['name']},Email:{student['email']}")
            st.write(student)








    # Update a student
    st.header('Update Student')
    student_id = st.text_input('Student_ID')
    updated_name = st.text_input('Updated_Name')
    updated_email = st.text_input('Updated_Email')
    updated_password = st.text_input('Updated_Password', type='password')
    if st.button('Update'):
        updated_student = User(name=updated_name, email=updated_email, password=updated_password)
        update_student_url = BASE_URL + f'/user/update_data/{student_id}'
        response = make_request(update_student_url, method='PUT', payload=updated_student.dict())
        if response.status_code == 200:
            st.success('Student updated successfully')

    # Delete a student
    st.header('Delete Student')
    student_id = st.text_input('StudentID')
    if st.button('Delete'):
        delete_student_url = BASE_URL + f'/delete_data/{student_id}'
        response = make_request(delete_student_url, method='DELETE')
        if response.status_code == 200:
            st.success('Student deleted successfully')

if __name__ == '__main__':
    main()
