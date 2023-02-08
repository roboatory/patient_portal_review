from app_store_scraper import AppStore
from google_play_scraper import Sort, reviews_all
import pandas as pd
from pprint import pprint

def extract_from_apple_store(app_name, app_id):
    # scrape reviews from apple store
    app = AppStore(country = "us", app_name = app_name, app_id = app_id)
    app.review(sleep = 30)
    df = pd.DataFrame(app.reviews)
    
    # unpack developer response into three distinct columns
    if "developerResponse" in df.columns.values:
        developer_response = df["developerResponse"].apply(pd.Series)
        df = pd.concat([df, developer_response], axis = 1)
        df.drop(["developerResponse", 0], axis = 1, inplace = True)
    
    df.to_csv(app_name + "_apple.csv", index = False)

def extract_from_google_play(app_name, app_id):
    result = reviews_all(
        app_id,
        sleep_milliseconds = 0,
        lang = "en",
        country = "us",
        sort = Sort.NEWEST
    )
    
    df = pd.DataFrame(result)
    df.to_csv(app_name + "_google.csv", index = False)

def main():
    # extract_from_apple_store("FollowMyHealth", 502147249)
    # extract_from_apple_store("MyChart", 382952264)
    # extract_from_apple_store("healow", 595012291)
    # extract_from_apple_store("MyUPMC", 1365606965)
    # extract_from_apple_store("MyHealthONE", 1493014954)
    # extract_from_apple_store("UnitedHealthcare", 1348316600)
    # extract_from_apple_store("Mayo Clinic", 523220194)
    # extract_from_apple_store("Sydney Health", 1463423283)
    # extract_from_apple_store("VA: Health and Benefits", 1559609596)

    # extract_from_google_play("FollowMyHealth", "com.jardogs.fmhmobile")
    # extract_from_google_play("MyChart", "epic.mychart.android")
    # extract_from_google_play("MyUPMC", "com.upmc.enterprises.myupmc")
    # extract_from_google_play("MyHealthONE", "com.hcahealthcare.mhom")
    # extract_from_google_play("healow", "com.ecw.healow")
    # extract_from_google_play("UnitedHealthcare", "com.mobile.uhc")
    # extract_from_google_play("MayoClinic", "com.mayoclinic.patient")
    # extract_from_google_play("Syndey Health", "com.anthem.sydney")
    # extract_from_google_play("VA: Health and Benefits", "gov.va.mobileapp")

main()