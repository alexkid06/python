import requests

issue = 1
url = "https://www.digitalwhisper.co.il/issue{}".format(issue)
source_code = requests.get(url)
while (requests.status_codes == 200):
    for line in source_code.text.split("\n"):
        if "herf" in line:
            for brick in line.split():
                if ".pdf" in brick and "http" in brick and "DW" in brick:
                    start = brick.index("http")
                    end = brick.index(".pdf")
                    name = brick.index("DW")
                    link = brick[start:end + 4]
                    pdf = brick[name:end + 4]
                    f = open(r"C:\Users\ak06\Desktop\DigitalWhisper\pdf\{}".format(pdf), "wb")
                    f.write(requests.get(link).content)
                    f.close()
    issue += 1
    url = "https://www.digitalwhisper.co.il/issue{}".format(issue)
    source_code = requests.get(url)

#####################################################################################################
# the point of this exercise is to "crawl" to this specific web page and gather all the 109 issued###
# articles.                                                                                       ###
#####################################################################################################
