import streamlit as st
from supabase import create_client, Client
#Configurar Supabase
SUPABASE_URL = "https://peioqwvlxrgujotcuazt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBlaW9xd3ZseHJndWpvdGN1YXp0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjQwMzM0MDUsImV4cCI6MjAzOTYwOTQwNX0.fLmClBVIcVGr_iKYTw79kPJUb12Iem7beooWfesNiXE"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


﻿
def get_students():
response= supabase.table('students').select('*').execute()
return response.data

def count_students():
response = supabase.table('students').select('*', 'count="exact').execute()
return response.count

def add_student (name, age):
supabase.table('students').insert({"name": name, "age": age}).execute()

st.title("CRUD con Streamlit y Supabase")

menu = ["Ver", "Agregar"]
choice = st.sidebar.selectbox("Menu", menu)
