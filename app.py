# Bring in deps
import os 
import re
from apikey import apikey 

import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from youtube_transcript_api import YouTubeTranscriptApi

os.environ['OPENAI_API_KEY'] = apikey

# App framework
st.title('Crochet Pattern Writer')
prompt = st.text_input('Crochet Youtube Video Link:') 

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['transcript'], 
    template='I want you to act as a crochet pattern writer. I will provide you the transcript of the Youtube crochet tutorial video. The transcript is a list of dictionaries. You need to write me a crochet pattern in the professional language based on that transcript. Transcript is {transcript}'
)

# Llms
llm = OpenAI(temperature=0.9) 
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title')


# Show stuff to the screen if there's a prompt
if prompt: 
    # Extract video ID using regular expression
    match = re.search(r"v=([A-Za-z0-9_-]+)", prompt)
    if match:
        video_id = match.group(1)
    else:
        st.write("Invalid Youtube Video Link")
    list_of_dicts = YouTubeTranscriptApi.get_transcript(video_id)
    youtube_transcript = [item["text"] for item in list_of_dicts]
    title = title_chain.run(transcript=youtube_transcript)

    st.write(title) 
