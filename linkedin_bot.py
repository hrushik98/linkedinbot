import streamlit as st
import openai
import pandas as pd
import os
import csv
import json
import requests
import time
import re
import wget


phantom_key = "BP8cVcWHckdQz2zKqwaYF6YYQSeX3JZgHAuR3O5yLFo"

st.title("Linkedin bot v1.1")

if st.button("Session Reset"):
    if os.path.exists("file.csv"):
        os.remove("file.csv")
        with open("file.csv", "a") as f:
                datai = csv.writer(f)
                col1 = "Post URL"
                col2 = "Profile URL"
                col3 = "Full Name"
                col4 = "Connection Degree"
                col5 = "title"
                col6 = "Post Date"
                col7 = "Like Count"
                col8 = "Comment Count"
                col9 = "Content"
                col10 = "score"
                col11 = "reply"
                datai.writerow([col1, col2, col3, col4, col5, col6, col7, col8, col9,col10, col11])
        st.text("Session Reset Complete!")
    if os.path.exists("result2.json"):
        os.remove("result2.json")
    else:
        with open("file.csv", "a") as f:
                
                datai = csv.writer(f)
                col1 = "Post URL"
                col2 = "Profile URL"
                col3 = "Full Name"
                col4 = "Connection Degree"
                col5 = "title"
                col6 = "Post Date"
                col7 = "Like Count"
                col8 = "Comment Count"
                col9 = "Content"
                col10 = "score"
                col11 = "reply"
                datai.writerow([col1, col2, col3, col4, col5, col6, col7, col8, col9,col10, col11])
        st.text("Session Reset Complete")

def score_75to100():
    lst1 = []
    data2 = pd.read_csv("file.csv", encoding='latin-1')
    for i in range(0, len(data2)):
        if str(data2['score'][i]) == "25-50":
            lst1.append(i)
        if str(data2['score'][i]) == "0-25":
            lst1.append(i)
        if str(data2['score'][i]) == "50-75":
            lst1.append(i)
        if len(str(data2['score'][i])) > 7:
            lst1.append(i)
    for i in range(0, len(data2)):
        if i in lst1:
            data2 = data2.drop(i)
    data2 = data2.reset_index()
    data3 = data2[['Post URL', 'Content','score', 'reply']]
    st.write(data3)
    output_file = data3
    st.download_button("Download", output_file.to_csv(), mime='text/csv')
session_cookie = st.text_input("Enter your session cookie...")
problem_statement = st.text_input("Enter the problem statement...")
product_description = st.text_input("Enter the product description...")
search_term = st.text_input("Enter search term/paste link")
no_of_searches = st.number_input('Enter number of posts:', value=10, min_value=10, step=10)

score_content = f""" You are a classifier that can generate a score between 0 and 100 to determine the relevancy of the linkedin post with a passage.
The passage: {problem_statement}

How to determine the score:
- Higher is a better answer 
- Don't be overconfident!
- Just return the score and nothing else.
- Only return values from '0-25' or '25-50' or '50-75' or '75-100'


Example #1
Passage: A conifer is a tree or shrub which produces distinctive cones as part of its sexual reproduction. These woody plants are classified among the gymnosperms, and they have a wide variety of uses, from trapping carbon in the environment to providing resins which can be used in the production of solvents. Several features beyond the cones set conifers apart from other types of woody plants. A conifer is typically evergreen, although some individuals are deciduous, and almost all conifers have needle or scale-like leaves.
LinkedIn Post: Conifers are also characterized by their tall and straight trunks, which often have a conical shape. This shape helps the tree to shed snow in colder climates and also helps to maximize light absorption in areas with limited sunlight. Conifers are found all over the world, from the Arctic tundra to the tropical rainforest, and they are an important part of many ecosystems. One of the main uses of conifers is as a source of lumber. Many species of conifers are grown in plantations specifically for their wood, which is used in the production of paper, furniture, and construction materials. Conifers are also an important source of food and shelter for wildlife, with many animals relying on the cones, bark, and needles of these trees for sustenance. In addition to their practical uses, conifers are also valued for their aesthetic qualities. They are often used in landscaping and gardening, with some species, such as the Christmas tree, being particularly popular during the holiday season. The distinctive cones and needles of conifers also make them popular subjects for artists and photographers. Overall, conifers are a diverse and important group of trees and shrubs, with a wide range of practical and aesthetic uses. Their distinctive cones and needles, along with their tall and straight trunks, set them apart from other types of woody plants and make them a fascinating and valuable part of many ecosystems around the world.
Score: 75-100

Example #2
Passage: In his younger years, Ronald Reagan was a member of the Democratic Party and campaigned for Democratic candidates; however, his views grew more conservative over time, and in the early 1960s he officially became a Republican. In November 1984, Ronald Reagan was reelected in a landslide, defeating Walter Mondale and his running mate Geraldine Ferraro (1935-), the first female vice presidential candidate from a major U.S. political party.
LinkedIn Post: The question of whether Ronald Reagan was a Democrat has been a subject of debate for a long time. Some people believe that Reagan was a Democrat in his early years, while others believe that he was always a Republican. There are also some who argue that Reagan switched from being a Democrat to a Republican at some point in his political career. However, regardless of whether Reagan was a Democrat or a Republican, he remains one of the most iconic and influential political figures in American history. His policies and ideas have had a lasting impact on American society and continue to shape political discourse to this day. Whether he was a Democrat or a Republican, Reagan's legacy remains a vital part of American political culture, and his presidency continues to be studied and analyzed by historians and political scientists alike.
Score: 50-75

Example #3
Passage: The amount of time needed to explore Sydney and its surrounding areas depends on individual interests and travel style. A few days may be enough to see the main highlights of Sydney and take a day trip to nearby attractions like the Blue Mountains or Hunter Valley. 
LinkedIn Post: On your right across College Street, in the sandstone building on the corner, is the Australian Museum [3] ($12 adult/$6 children, $30 family (2+2)). This museum, which focuses on natural history, is worth a visit in its own right if you have more time in Sydney and will take a couple of hours to explore. If you're up for exploring the area by bike (one of the best ways to do so as much of it is parkland), take the train to Concord West station on the Northern Line (red line on the Sydney Trains map-about 20-25 minutes from the city on a direct train).
Score: 25-50

Example #4
Passage: The cost to install tile in a shower can vary depending on a few factors, such as the size of the shower, the type of tile used, and the complexity of the design. On average, the cost to install tile in a shower can range from $1,000 to $3,000 or more. This cost may include the removal of any existing tile or fixtures, preparation of the shower walls and floor, and the installation of the new tile.
LinkedIn Post: In the context of adult body CT, the Computed Tomography Dose Index volume (CTDI vol) is commonly used to estimate the dose received by an organ that is fully encompassed by the primary radiation beam. A protocol-independent conversion coefficient is used for this purpose. However, research shows that fully encompassed organs only account for approximately 50% ± 19% of the k factor and 46% ± 24% of the q factor. This implies that the dose received by organs that are only partially encompassed by the primary radiation beam is also substantial and cannot be ignored when estimating the effective dose and risk index from the Dose Length Product (DLP). To accurately estimate the dose and risk associated with partial irradiation of organs, it is necessary to use conversion coefficients that are specific to the anatomical region being examined. In summary, the estimation of the effective dose and risk index in adult body CT requires a comprehensive understanding of the radiation dose received by both fully and partially encompassed organs and the use of appropriate conversion coefficients for the anatomical region under examination.
Score: 0-25
"""

reply_content = f"""You are a sales agent propsecting on LinkedIn for a product.
Your task is to generate replies to the given linkedin posts, that will help generate interest for your product. Don't mention that you're a sales agent. Your sales pitch should feel like a recommendation rather than a sales pitch.
Description of the product: {product_description}
"""

if st.button("Scrape"):

      
      
      
    url = "https://api.phantombuster.com/api/v2/agents/launch"
    payload = {
    "id": "1317260686753160",
    "argument": f""" 
    {{ 	
      \"connectionDegreesToScrape\": [ \"2\", \"3+\" ],

      \"category\": \"Content\", 	\"numberOfLinesPerLaunch\": 10, 	

      \"sessionCookie\": \"{session_cookie}\", 	
      
      \"search\": \"{search_term}\", 	
      
      \"numberOfResultsPerLaunch\": {no_of_searches}, 	
      
      \"removeDuplicateProfiles\": true }} """
}
    headers = {
      "content-type": "application/json",
      "X-Phantombuster-Key": f"{phantom_key}"
  }

    response1 = requests.post(url, json=payload, headers=headers)

    text1 =  response1.text
    time.sleep(no_of_searches+30)
    container_id = re.search(r'"containerId":"(\d+)"', text1).group(1)

    url = f"https://api.phantombuster.com/api/v2/containers/fetch-output?id={container_id}"

    headers = {
        "accept": "application/json",
        "X-Phantombuster-Key": f"{phantom_key}"
    }

    response2 = requests.get(url, headers=headers)

    text = response2.text
    try:
        json_link = re.search(r'https:\/\/[^\s]+result\.json', text).group()
        url = json_link
        wget.download(url,"result2.json")
        with open('result2.json', 'rb') as file:

            contents = file.read()
            decoded_contents = contents.decode('latin-1') # or the appropriate encoding
            data = json.loads(decoded_contents)
        for i in range(0, len(data)):

    
       
            with open("file.csv", "a", encoding="utf-8") as f:

                dataii = csv.writer(f)

                col1 = str(data[i]['postUrl'])
                try:
                    
                    col2 = str(data[i]['profileUrl'])
                except:
                    col2 = str(data[i]['companyUrl'])
                try:
                    
                    col3 = str(data[i]['fullName'])
                except:
                    col3 = str(data[i]['companyName'])
                try:
                    
                    col4 = str(data[i]['connectionDegree'])
                except:
                    col4 = "None"
                try:
                    
                    col5 = str(data[i]['title'])
                except:

                    col5 = "None"
                try:

                    col6 = str(data[i]['postDate'])
                except:

                    col6 = "None"
                try:

                    col7 = str(data[i]['likeCount'])
                except:

                    col7 = "None"
                try:

                    col8 = str(data[i]['commentCount'])
                except:

                    col8 = "None"
                try:

                    col9 = str(data[i]['textContent'])
                except:

                    col9 = "None"
                try:
                    openai.api_key =  st.secrets['API_KEY'] 
                   
                    
                    m = [{"role": "system", "content": f"{score_content}"},
                    {"role": "user", "content": f"Linkedin post:\n {data[i]['textContent']} \nScore:\n"}]

                    result = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    max_tokens = 4,
                    messages=m)
                    score=result["choices"][0]['message']['content']
                    col10 = str(score)
                    time.sleep(3)
                    try:


                        result = re.search(r'(?<=Score: ).*', score).group(0)
                        col10 = str(result)
                    except:
                        col10 = str(score)
                except:
                    col10 = "None"
                if str(col10) == "75-100":
                    openai.api_key = st.secrets['API_KEY']
                    

                    m = [{"role": "system", "content": f"{reply_content}"},
                {"role": "user", "content": f"{data[i]['textContent']} \nLinkedin reply:\n"}]
                    result = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    max_tokens = 500,
                    messages=m)
                    reply=result["choices"][0]['message']['content']
                    col11 = str(reply)
                    time.sleep(3)
                else:
                    col11 = 'None'
                dataii.writerow([col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11])
    except:
        st.write(text)
data = pd.read_csv("file.csv", encoding='latin-1')[['Content','score','reply']]
st.write(data)

if st.button("Filter"):
    score_75to100()
    
st.write('---')

# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# If a file was uploaded, display its contents
# if uploaded_file is not None:
#     # Load the CSV file into a pandas DataFrame
#     df = pd.read_csv(uploaded_file)
    
#     # Display the DataFrame
#     st.write(df)
spreadsheetUrl = st.text_input("Enter Spreadsheet Url...")
if st.button('Post Reply'):
    
    # st.write(spreadsheetUrl)
    # if st.button("Go"):
    
    url = "https://api.phantombuster.com/api/v2/agents/launch"
    payload = {
        "id": "6722836923161351",
        "argument": f"""{{
        "sessionCookie": "{session_cookie}",
        "spreadsheetUrl": "{spreadsheetUrl}"

    }}"""
    }
    headers = {
        "content-type": "application/json",
        "X-Phantombuster-Key": "X6M9h7iZOr6O6ZfSCax35IaCmMenHjNNcFSGNjjc2N8"
    }

    response1 = requests.post(url, json=payload, headers=headers)
    

    # text1 =  response1.text

    # time.sleep(16*())

    # container_id = re.search(r'"containerId":"(\d+)"', text1).group(1)

    # url = f"https://api.phantombuster.com/api/v2/containers/fetch-output?id={container_id}"

    # headers = {
    #     "accept": "application/json",
    #     "X-Phantombuster-Key": "X6M9h7iZOr6O6ZfSCax35IaCmMenHjNNcFSGNjjc2N8"
    # }

    # response2 = requests.get(url, headers=headers)

    # text = response2.text
    # st.text("comments posted successfully!")

    st.write("Comments are being posted....")
    st.write("each comment takes about 20 seconds.")









            


            
