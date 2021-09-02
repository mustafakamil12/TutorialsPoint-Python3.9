import os

wsi_user = "wsiinternal"
wsi_pass = "suninmarchfreezeinapril"
wsi_prof = "eric.mikula@weather.com"
ForecastRange =["1-5","6-10","11-15"]
remote_imageUrl = 'http://www.wsitrader.com/Services/CSVDownloadService.svc/GetForecastGraphics'
Region = ["NA"]
api_Creds = f"?Account={wsi_user}&profile={wsi_prof}&password={wsi_pass}&ForecastRange={ForecastRange[0]}&Region={Region[0]}"

print(f"{remote_imageUrl}{api_Creds}")
