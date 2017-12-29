import pyspeedtest as pst

test = pst.SpeedTest()
#Get the current ping, rounded to 1 digit after the decimal point
ping = 'Current ping: {} ms'.format(round(test.ping(),1))
# print('Current ping:', round(test.ping(),1), 'ms')
# print(ping)
#Get the current download speed, converted from Kbps to Mbps, rounder to 2 digits after the decimal point
download = 'Current download speed: {} Mbps'.format(round(test.download()/1000/1000,2))
# print('Current download speed:', round(test.download()/1000/1000,2), 'Mbps')
# print(download)
#Get the current upload speed, converted from Kbps to Mbps, rounder to 2 digits after the decimal point
upload = 'Current upload speed: {} Mbps'.format(round((test.upload()/1000/1000), 2))
# print('Current upload speed:', round((test.upload()/1000/1000), 2), 'Mbps')
# print(upload)

if __name__ == "__main__":
    print("Ping:", ping)
    print("Download:", download)
    print("Upload:", upload)