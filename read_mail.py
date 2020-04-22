import re

import ezgmail

def read_mail():
    """
    Fetches your medium digest and emails you with tracking
    links removed.
    """
    resultThreads = ezgmail.search('from:noreply@medium.com', maxResults=25)
    text = resultThreads[0].messages[0].originalBody
    text = re.sub(
            r'(https://medium\.com/@[a-zA-z0-9]+/.*?)\?.*?&sectionName=.*?\)',
            r'\1)',
            text,
            )
    ezgmail.send(ezgmail.EMAIL_ADDRESS,'Your Medium Digest Tracking Free', text)

if __name__ == '__main__':
    text = read_mail()
