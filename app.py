# -*- coding: utf-8 -*-
"""1)LLM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UuYB7TDA32gjtuchTY7p4HTIDdOMGX6l
"""

!pip cache purge

!pip install openai

!pip install LangChain

!pip install streamlit

!pip install  langchain==0.0.148

!pip install pydantic==1.10.6
!pip install typing-inspect==0.8.0

!pip install langchain_community

import sys
print(sys.version)

import streamlit as st
from langchain import OpenAI,LLMChain
from langchain.prompts import PromptTemplate
import os


#set your OpenAI API Key
os.environ["OPENAI_API_KEY"] = "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"

#Define your LangChain App
prompt_template = "You are ahelpful assistant . Answer the question:{question}"
prompt = PromptTemplate(template=prompt_template, input_variables=["question"])

#llm = OpenAI(model ="text-davinci-003")
llm = OpenAI(model="gpt-3.5-turbo")

#llm = OpenAI(model_kwargs={"model": "gpt-3.5-turbo"})
llm_chain = LLMChain(llm=llm, prompt=prompt)

st.title("LangChain App")
question = st.text_input("Enter your question:")
if question:
    response = llm_chain.run({"question" : question})
    st.write(f"Response: {response}")

