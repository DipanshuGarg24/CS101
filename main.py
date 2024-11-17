# import streamlit as st
# import pandas as pd
# import altair as alt
# import statistics




# marks = [3,9,5.5,15.5,11.5,0,5.5,0,31,16,32.25,17.75,27,13,25.5,19,21.5,17,22.5,4.5,32.5,6,15.5,16.5,11.5,19,14.5,23.25,12.75,22.75,18.5,38,16.5,37,24,33.5,6,27.5,16,24.5,24,35,24.5,37.5,30,10,31,17.25,7,13,22,12,8.5,30.5,40,29.5,16.25,22.75,12,21.75,22.375,17.125,40,31.5,21.5,27,24.25,12,26,24,12,26.5,25.25,28,15.75,24.5,13.5,17.5,26.5,17.25,22.25,24,18,26,34.5,23,11.25,29,33,32,18.5,19.25,29.5,21.75,24,17.25,28.5,20.5,23.5,30.5,25.5,19.5,32.75,19.5,24.75,18.75,23.75,13.5,23.5,18,14.5,23.5,12.5,10.5,15,30.5,13,15.5,28.25,16.75,31.5,17.5,31,25,15.75,7,35.75,15,15,11.5,9.5,6.5,25,31.25,16.5,21,16.5,40,39,32.75,20,32.5,36.5,38.5,36.5,35,31.5,26,24,38.5,20,18.5,34.5,18,34.5,29.75,23.25,36.5,36,35.25,30,15,30.75,22.75,12.125,27,28.25,16.125,37,19,25.625,22.875,11,20,34.5,21.75,38.25,8.5,38.5,37.75,21.5,9,31,26,40,29.5,24.5,31.5,24.5,11.5,34,27.5,37,28.75,26.75,24,40,15.5,26,38,21,34,36.75,17.75,39,31.75,39.75,14,37.75,39.75,10.5,23.5,31.25,39,37,35,30.5,27,16.5,38,39,16,25.75,33,39.75,30.5,24,39,34.75,35.5,32.75,21,40,39.75,22.5,29.75,30.25,36,34,12.5,40,20.25,35,18,24.25,19.5,20.75,30.75,22.75,29.5,25.5,36.5,36,33.75,37.25,10,36.75,32.75,35.75,18.25,18,26.25,36.75,27.75,38.5,26.5,29.5,37.75,33.5,19.5,30.75,25.5,36,20,37,35.5,24.75,29.5,6,36,29,16,25,12,10,18.5,40,30.75,18,36,29,16.75,35.5,36.75,17,27.75,11.5,39.25,19,33,34.5,31.5,32,24.25,38.5,19.25,27.75,22,11.5,30,8.5,33.25,18,7,25.5,28.5,26.5,23,36.75,11,28.75,19.5,21,15.5,26.5,13.75,40,30,16,12.5,35.75,19,16.25,25,16,18.5,33.75,36,33,20,20.25,37,38,38.75,39.75,34.75,25,29.25,40,18.25,36.75,35.5,35.5,40,40,36,22.5,34.5,29.5,29,24.75,35,24,38.75,40,35,24.25,39.75,34.75,40,31.75,40,31.75,36,31,13.5,31,31.5,34,22.5,40,30.5,37,37,31.5,36.75,38.5,23.75,35.5,28.25,33.5,37.75,35,36.75,34,36.75,25.5,31.5,36.75,38.5,40,40,27.5,39,29.5,24.5,33,36,38,37.75,10.5,20.5,35.5,32,37,39,38.75,37.5,16.5,40,36,34.75,37.25,37.25,31.5,5.5,37.25,32.5,36.75,32.5,32,40,26,28.5,40,38.5,36,13.5,16,35.5,7.5,40,30,35.5,23.5,36,35.5,21.75,32,36.25,27.5,38.5,28.75,18.5,37.25,23.25,37.5,39.5,38.5,31,36.5,38.5,37,36.25,39.75,31.75,37,23,32.5,28,20,38.5,29.5,38,32.5,31.5,38.5,35.5,35.5,37.25,23.5,36.5,32,17,38.5,30.5,31.5,34.75,32.75,27.5,37.25,32,33,39.75,37.5,33.75,29,40,29.25,36,36.25,33.5,36.25,31.5,24.5,33,24.5,40,34,28,29,22.25,39.5,39.75,31.75,28.5,33.25,40,40,34.25,25,30.5,40,24.75,14.25,34.5,38,26.75,36.5,21.5,40,30.25,32,30.25,32,37,31.5,38.5,11.5,10.5,22,7,27.5,19,12.25,12.5,9,10,28.5,22.75,15,13,32,3.75,17.5,12.75,19.25,28.75,35.75,7,31.25,22.25,32.5,16.5,31.75,15.5,25,17.5,22.5,32,12,13.5,19.5,11,12,35.75,32.25,8.5,27.75,22,27,31.25,34.75,11.5,10.5,26,15.5,5.5,22,5.5,27.5,34.5,18.5,25,20.5,21.75,20,17,26.5,22,10,26.5,36,31.5,34,33.5,18.5,30.5,24.5,17,37,33.5,29,36,19.125,7.5,26.75,14.375,14.25,21.125,20.125,25.375,24.375,17.25,11.25,10.5,18.5,7.5,23.25,31.25,12,7.5,30.5,21,19,21,19.5,9,15.75,30,12.5,16.5,25,30,23,17.5,24.5,8,29.5,34.5,33.75,15.5,14.5,39.75,31.75,21.5,20.5,33.75,30,16.25,11,27.5,22.75,27.5,22.25,17.25,10.625,14.25,25.625,16.5,22.625,28.125,30.875,24.25,29,15,15,24.75,32.5,6,24.5,15.5,16.5,15.5,15,22.5,24.5,23.5]

# st.header("CS 101 - Marks Analysis (Mid Sem)")
# st.divider()

# # Create a DataFrame to hold the frequency of marks
# marks_df = pd.DataFrame(marks, columns=['Marks'])
# frequency_df = marks_df['Marks'].value_counts().reset_index()
# frequency_df.columns = ['Marks', 'Frequency']

# # Create the interactive line graph using Altair
# line_chart = alt.Chart(frequency_df).mark_line(interpolate='linear').encode(
#     x='Marks:O',
#     y='Frequency:Q',
#     tooltip=['Marks:O', 'Frequency:Q']  # Add tooltip for interactivity
# ).properties(
#     title='Frequency Distribution of Marks',
#     width=700,
#     height=400
# )


# bar_chart = alt.Chart(frequency_df).mark_bar().encode(
#     x='Marks:O',
#     y='Frequency:Q',
#     tooltip=['Marks:O', 'Frequency:Q']  # Add tooltip for interactivity
# ).properties(
#     title='Frequency Distribution of Marks',
#     width=700,
#     height=400
# )


# tab1,tab2 = st.tabs(["Bar Graph","Line Graph"])
# with tab2:
#     # Streamlit heading
#     st.title('Marks Distribution Line Graph')
#     # Display the interactive line chart in Streamlit
#     st.altair_chart(line_chart, use_container_width=True)

# with tab1:
# # Streamlit heading
#     st.title('Marks Distribution Bar Graph')
#     # Display the interactive bar chart in Streamlit
#     st.altair_chart(bar_chart, use_container_width=True)


# # Calculating statistics
# max_marks = max(marks)
# min_marks = min(marks)
# mean_marks = statistics.mean(marks)
# median_marks = statistics.median(marks)
# mode_marks = statistics.mode(marks)

# # Displaying statistics using st.metric
# st.title('Marks Statistics')
# col = list(st.columns(3))
# with col[0]:
#     st.metric(label="Maximum Marks", value=max_marks)
#     st.metric(label="Minimum Marks", value=min_marks)
# with col[1]:
#     st.metric(label="Mean Marks", value=f"{mean_marks:.2f}")
#     st.metric(label="Median Marks", value=median_marks)
# with col[2]:
#     st.metric(label="Mode Marks", value=mode_marks)

# st.divider()
# st.markdown("<br><br><h4 style = 'text-align:center'>Made with 💝 By Dipanshu Garg</h4>", unsafe_allow_html=True)

# # making some social media buttons :)
# st.markdown("""
#         <div style="display: flex; justify-content: center;">
#         <div>
#             <a href='https://www.linkedin.com/in/dipanshu-garg24'><img src='https://img.icons8.com/fluent/48/000000/linkedin.png' width='30'></a>
#         </div>
#     </div>

#         """, unsafe_allow_html=True)


import streamlit as st
import asyncio
import telegram
import re

st.set_page_config(
    page_title="Increase Stipend",  # This title appears on the tab and when shared
    page_icon=":rocket:",            # Optional: add an emoji or image as the page icon
    layout="wide"                    # Optional: set layout to 'wide' or 'centered'
)

hide_streamlit_style = """
    <style>
    /* Hide the hamburger menu */
    #MainMenu {visibility: hidden;}
    /* Hide the "Manage app" button */
    footer {visibility: hidden;}
    </style>
"""

# Inject CSS with st.markdown
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

API_TOKEN = '7259751187:AAENuR_8zsJ1smrch0AW7mqAkAfmnX-kf40'  # Replace with your bot's API token
CHANNEL_ID = '-1002369094626'  # Replace with your actual channel ID



# Now start with your app content below



# Create a bot instance
bot = telegram.Bot(token=API_TOKEN)

flag = True
async def send_message(name,institue,email,branch,roll):
    message = f"Name : {name}\nEmail : {email}\nInstitue : {institue}\nbranch :{branch}\nroll : {roll}"
    await bot.send_message(chat_id=CHANNEL_ID, text=message)
    global flag
    flag = False

# Function to validate email format
def is_valid_email(email):
    # Check if there is exactly one "@" symbol
    if email.count("@") != 1:
        return False

    # Split the email into username and domain parts
    username, domain = email.split("@")

    # Check basic length requirements
    if len(username) < 1 or len(domain) < 3:
        return False

    # Ensure domain contains at least one "." and it's not the first/last character
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False

    return True

def func(x):
    result = ""
    for i in x:
        if i == ' ':
            result += "%20"
        elif i == '\n':
            result+="%0A"
        else:
            result+=i
    return result
def genratedata(n,i,b,e):
    subject = func("Urgent Appeal for Revision of M.Tech and MS Stipend of GATE qualified students.")
    body = func(f'''Respected Sir,
   
We, the M.Tech and MS students across NITs and IITs who have qualified GATE exam, respectfully request an urgent revision of our stipend, which has remained unchanged since 2015. We are currently receiving a mere amount of Rs12400 since 2015 which is currently insufficient in 2024 as  the tuition fees and the cost of living have risen significantly over these years , placing a substantial financial burden on us. While the stipend for Ph.D. students has seen multiple adjustments over the same period of time. M.Tech/MS stipends have not, leaving many students struggling to meet basic expenses.

In support of this request, with reference the AICTE Act (1987) and UGC Act (1956), which provide for periodic stipend reviews. Guidelines issued by the Ministry of Education (MoE) and Seventh Central Pay Commission (2015), alongside provisions for Cost of Living Adjustment (COLA) and Dearness Allowance (DA), further establish the need for regular updates to stipends based on inflation and cost of living.

We kindly urge you to consider a prompt increase in the M.Tech/MS stipend of GATE qualified students.This support would alleviate financial pressures, enabling us to focus fully on our academic and research commitments and contribute meaningfully to national advancements in science and technology.

Thank you for your attention to this pressing matter.

Sincerely,
{n}
{b}
Enrollment : {e}
({i})
''')
    emails = '''chairman@aicte-india.org
cmoffice@aicte-india.org
vcm@aicte-india.org
ea.vcm@aicte-india.org
ms@aicte-india.org
director@nitagartala.in
director@nitp.ac.in
director@nitandhra.ac.in
director@manit.ac.in
director@nitc.ac.in
director@nitdelhi.ac.in
director@nitdgp.ac.in
director@nitgoa.ac.in
director@mnit.ac.in
director@nitj.ac.in
director@nitk.ac.in
director@nitm.ac.in
director@nitnagaland.ac.in
director@nitrr.ac.in
director@nitsikkim.ac.in
director@nitt.edu
director@nitw.ac.in
director@iitbhilai.ac.in
director@iitbbs.ac.in
director@iitb.ac.in
director@iitd.ac.in
director@iitdh.ac.in
director@iitgn.ac.in
director@iitgoa.ac.in
director@iitg.ac.in
director@iith.ac.in
director@iiti.ac.in
director@iitjammu.ac.in
director@iitj.ac.in
director@iitk.ac.in
director@iitkgp.ac.in
director@iitm.ac.in
director@iitmandi.ac.in
director@iitpkd.ac.in
director@iitp.ac.in
director@iitr.ac.in
director@iitrpr.ac.in
director@iitbhu.ac.in
minister.sm@gov.in
minister.hrd@gov.in
'''

    x = emails.split("\n")
    mail = ",".join(x)
    print(mail.count(','))
    link = "mailto:"+mail+"?subject="+subject+"&body="+body
    return link

z = st.columns((1,5,1))

with z[1]:
    st.title("#Increase Stipend 🔥")
    # Set the title of the app
    st.subheader("Make your contribution count by reaching out to the government today to support an increase in our stipend!")

    st.success("This Website is no longer supporting now for contributions :)\nThankyou for visiting")
    
    # Create a form
    # with st.form(key='student_info_form'):
    #     # Create text inputs for the form
    #     name = st.text_input("Name")
    #     institute_name = st.text_input("Institute Name")
    #     branch = st.text_input("Course + Branch")
    #     st.caption("Example : Mtech CSE")
    #     roll_number = st.text_input("Roll Number")
    #     email = st.text_input("Email Address")
    
    #     # Check if all inputs are filled and if the email is valid
    #     all_filled = all([name, institute_name, email,branch,roll_number])
    #     email_valid = is_valid_email(email)
    
    #     # Create a submit button that is active only if all fields are filled and email is valid
    
    #     # If the form is submitted and valid, display the entered information
    #     if st.form_submit_button("Generate Email"):
    #         if (all_filled and email_valid):
    #             asyncio.run(send_message(name,institute_name,email,branch,roll_number))
    #             link = genratedata(name,institute_name,branch,roll_number)
    #             with st.spinner("Generating Email ..."):
    #                 while flag:
    #                     pass
    #             st.success("Email Generated Successfully!")
    #             st.link_button("Click to send Email",link,type="primary")
    #         else:
    #             st.error("Please Fill all the details Properly")
    
    st.text("")
    x = st.columns((1,2,1))
    x[1].text("Thankyou for contributing :) 🙏🏻")
