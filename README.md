## empoWOMENt: Let’s break the glass ceiling!
=============

Motivation
----------
Did you know that statistically, women apologize more often than men do? According to a 2010 study in the US journal _Psychological Science_, women offer more apologies and believe they commit more offenses than men.

Women often downplay their successes and lose confidence for the sake of "being polite." And rather alarmingly, women who don't play by the rules are frequently labeled "bossy" or "conceited," whereas men would be labeled as "leaders." In an already incredibly underrepresented field, women in tech encounter obstacle after obstacle when trying to claim a seat at the table.

EmPower is a messaging tool that not only detects phrases that show a lack of confidence, but also suggests alternative ways to express ideas. By dropping unnecessary apologies and using clear and direct language, women will become more comfortable, confident, and proud when sharing ideas. And by changing the way women think about themselves, we can break the glass ceiling! Achieving women's equality isn't easy, but it starts from the grassroots.

How it Works
------------
**Who exactly is Em?** She’s an assistive bot aimed at helping women increase their confidence by providing suggestions to needlessly uncertain messages. When she detects uncertainty or sees you selling yourself short, she will encourage you to be more assertive.

**How does she work?** Em is a natural language processing automated assistant created using Dialogflow (previously known as api.ai), an AI/machine learning software that references Google Cloud API. She has the power to integrate with Facebook Messenger, Slack, and Google Assistant, among other platforms, and support both text and voice recognition. Trained to develop intelligent responses to key phrases as well as recognize sentiments and their lemmatizations, Em will continue to develop as she receives more exposure to user messages.

Not sure what to say? Try some of the following inputs to see Em in action!
>
>- “I’m not sure if I should submit the report.”
>- “Do you mind if I take the project lead?”
>- “#IAmRemarkable”
>- “How do you empower women?”
>- “What can I do to improve my confidence?”
>- “@didyouknow” - for some fun facts :)

You can talk to Em one-on-one on our website, or you can add her into a Facebook Messenger group chat, where she will interact with all the users involved and continue to make suggestions and motivations.

Data Analysis
----------------------
On the website, you’ll see two panels displaying analysis of the conversation history: sentiment and frequently used words. Thanks to Splunk’s NLP Analytics app, we were able to parse conversation data and thus offer users insight into their patterns of speech. Both the sentiment analysis and word frequency table are based on Em’s raining data over the past 24 hours.

Future Developments
----------------------
As this was our first time using many of the technologies present in this project, we ran into some challenges that we’ll attempt to address in the future:
>
>- Facebook Group Messaging with Em is not integrated into our web application. Currently, utilizing Em requires access to the Facebook Developer Test User Console, but we intend on making Em a public user so that everyone will have access to her services.
>- We hope to have Em generate live suggestion pop-ups as the user is typing a message, rather than having her provide feedback after the message has already been sent.
>- Data analytics currently does not display live data, but we hope to find a workaround to bypass this issue.


Technical Requirements
----------------------

**Instructions and platform specifications**

>**Languages and tools used:**
>
>- Python 2.7.15
>- apiai v. 1.2.3
>- json v. 2.0.9
>- requests v. 2.21.0
>- Javascript 
>- HTML5
>- CSS3
>- Google Cloud Dialogflow API
>- Splunk NLP Text Analytics v. 0.9.5
>
>**Instructions**
>
>0. Our web demo is hosted at https://self-empowoment.net, courtesy of Domain.com.
>1. Connect with Em Power on Facebook (she can’t friend real users, though, so you’ll have to create a test user).
>2. Run empowoment.py.
>3. Start chatting with your new friend Em Power!
>

tl;dr
-----
empOWOWOment 
