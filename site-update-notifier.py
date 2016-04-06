# sends a text when a website's content changes.
from bs4 import BeautifulSoup
from urllib.request import urlopen
from lxml.html.clean import clean_html
import lxml
import time
from twilio.rest import TwilioRestClient

sensitive_list = []
sensitive = open('sun-sensitive', 'r')
for line in sensitive:
	sensitive_list.append(line.rstrip())
# important fields
url = sensitive_list[0]
# enter the number the text is being sent to in the "to" field and your twilio number in the "from_" field
# number are preceded with '+' and then the country code, for example all numbers in the US are precede by '+1'
personal_number = sensitive_list[1]
twilio_number = sensitive_list[2]
# enter your twilio sid and token below (you can sign up for an account here: https://www.twilio.com/)
account_sid = sensitive_list[3]
auth_token = sensitive_list[4]


client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(to=personal_number, from_=twilio_number, body="You will recieve a text when %s is updated." % url)

init_response = urlopen(url)
init_html = init_response.read()
init_document = lxml.html.document_fromstring(init_html)
init_raw = init_document.text_content()

while (True):
	new_response = urlopen(url)
	new_html = new_response.read()
	new_document = lxml.html.document_fromstring(new_html)
	new_raw = new_document.text_content()
	if (init_raw != new_raw):
		message = client.messages.create(to=personal_number, from_=twilio_number, body="%s was updated!" % url)
		break
	time.sleep(60)