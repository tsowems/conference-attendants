#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
                 Idenify delegates that attended During the Virtual event and logged in after the event
          Did anyone attend in-person and then log on later to view the information and or network?
       
       Note: You are required to have preinstalled the needed third party libraries as stated in the documentation
"""
#LIbraries importation
import mysql.connector
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from IPython.display import display, HTML

dbConnect=mysql.connector.connect(host="localhost",user="root",password="password",database="BookMeIn2", auth_plugin='mysql_native_password')
mycursor=dbConnect.cursor()


display(HTML("<h1 style='color:red;text-align:center; font-size:40px;'> Virtual Attendees & After Event Viewers</h1><h3 style='color:blue;text-align:center; font-size:25px;'>Chart showing those attended in-person and then log on later to view the information and or network?</h5>"))

#Select Query counting delegates inperson during event
mycursor.execute("SELECT COUNT(*) FROM `registrations` INNER JOIN `attendee_log` ON `registrations`.`attendee_id` = `attendee_log`.`attendeeid` WHERE `event_id`=4114 AND `date_visited` BETWEEN '2021-12-09 09:00:00' AND '2021-12-09 15:30:00' AND `reftype`='login' AND `registered`=1")
duringEvent = mycursor.fetchone()

#Select Query counting delegates inperson after event
mycursor.execute("SELECT COUNT(*) FROM `registrations` INNER JOIN `attendee_log` ON `registrations`.`attendee_id` = `attendee_log`.`attendeeid` WHERE `event_id`=4114 AND `date_visited` > '2021-12-09 15:30:00' AND `reftype`='login' AND `registered`=1")
afterEvent = mycursor.fetchone()


print('Delegates Who Attended In-Person and Logged In During Event: ', duringEvent[0])
print('Delegates Who Attended In-Person and Logged In To Delegate Site After Event: ', afterEvent[0])

display(HTML("<p>If the login time was between 9:00 and 15:30 on the day of the event, they were considered to have been online during the event. If a login was made by a user after 15:30 on the day of the event or thereafter, they were considered to have logged in after the event.</p>"))

#----------Footer Section for report generation navigation -----------------#
footer = "</br></br></br><div style='width:100%; text-align:center;'><a href='3-duration_on_live_session.html' style='color:blue;'>Previous</a> <a href='Question6.html' style='color:blue;'>Next</a></div>"
display(HTML(footer))


# In[ ]:




