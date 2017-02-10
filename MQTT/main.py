import network
from umqtt.simple import MQTTClient
import time

WLAN_SSID = 'WLAN_AP2'
WLAN_PSK = 'your password'
wlan = network.WLAN(network.STA_IF)
wlan.scan()
wlan.active(True)
wlan.connect(WLAN_SSID, WLAN_PSK)


MQTT_BROKER = '10.0.0.111'
MQTT_PORT = 1883
publisher = MQTTClient('publisher', MQTT_BROKER, MQTT_PORT)
publisher.connect()


for i in range(0, 10):
    publisher.publish(b'home/test', b'hello world')
    print(i)
    time.sleep(2)

publisher.disconnect()