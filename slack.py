import pycurl


def main():

    c = pycurl.Curl()
    c.setopt(c.URL, 'https://hooks.slack.com/services/xxxxxxxxxx')
    c.setopt(pycurl.CUSTOMREQUEST,"POST")
    c.setopt(pycurl.POSTFIELDS,'{"text":"Training Finished"}')
    c.perform()
    c.close()



if __name__ == '__main__':
    main()
