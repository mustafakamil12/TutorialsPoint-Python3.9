import re

email = "sk@aol.com md@.com @seo.com dc@.com"

print("Email Matches: ", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",email)))
