import requests
import os
import zipfile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    
]


def main():
    #create download folder
    os.makedirs('downloads',exist_ok=True)

    #pull the request
    # response= requests.get(download_uris[1])
    # with open('downloads/teste1.zip','wb') as r:
    #     r.write(response.content)

#download all files once
    for x in download_uris:                         
        if os.path.isfile('downloads' + '/' + x.split('/')[-1]):
            pass
        else:
            response= requests.get(x)
            with open('downloads' + '/' + x.split('/')[-1],'wb') as r:
                r.write(response.content)
# creade extract function
    def extract():
        for zip_file in os.listdir('downloads'):
            if zip_file.endswith('.zip'):
                with zipfile.ZipFile(os.path.join('downloads', zip_file), 'r') as z:
                    z.extractall('downloads')
            os.remove(os.path.join('downloads',zip_file))

    extract()
    pass
main()