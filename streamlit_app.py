import streamlit as st
from langchain_openai import ChatOpenAI


st.set_page_config(page_title="SEO Keyword Generator")
st.title('SEO Keyword Generator')

# Sidebar for API key input
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_keywords(topic):

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9, openai_api_key=openai_api_key)
    # Customizing the prompt for SEO keyword generation
    prompt = f"Generate a list of SEO keywords for content related to {topic}. Provide a broad range of keywords, including long-tail keywords."
    response = llm.invoke(input=prompt)
    return response

with st.form("keyword_form"):
    topic_text = st.text_input('Enter the main topic:', '')
    submitted = st.form_submit_button('Generate Keywords')
    if submitted:
        if not openai_api_key.startswith('sk-'):
            st.error('Invalid OpenAI API key. Please check your key!')
        else:
            keywords_response = generate_keywords(topic_text)
            if keywords_response:
                st.success('Generated Keywords:')
                # Ensure the response is formatted correctly for display
                st.write(keywords_response)
            else:
                st.error('Could not generate keywords. Please try again.')


# Instructions for getting an OpenAI API key
st.subheader("Get an OpenAI API key")
st.write("You can get your own OpenAI API key by following the instructions:")
st.write("""
1. Go to [OpenAI API Keys](https://platform.openai.com/account/api-keys).
2. Click on the `+ Create new secret key` button.
3. Next, enter an identifier name (optional) and click on the `Create secret key` button.
""")