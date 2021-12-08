# Mandatory config values

# START_URL -> the url that will act as the seed for the search engine db
# if left blank the scraper will look for the results in the first search
# page of major search engines and index results from that point forth
START_URL = ""

# connection uri for mongo db
MONGO_CONNECTION_URI = ""

# Optional Features -

# Virustotal SCANS
# Change to True if you want the links to be checked on virustotal for
# malicious checks
VIRUSTOTAL_SCANS = False
# Virus total API key that will be used to scan the urls for malicious intent
VIRUSTOTAL_API_KEY = ""
