from webserver import keep_alive
import requests

channelID = 1014412483345272832
headers = {
    "authorization":
    "MTAxNDU2NTExNDMyMzY2OTA3Mg.G0_Axp.1v1HqfoI5Nk8VvusquCC-aNYfHUbb-bLnDPg2Y"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
