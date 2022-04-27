/*
* This is the testing file for Arduino / ESP8266 interface with DHT11 Temperature and Humidity sensor.
*/

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <DHT.h>

#define DHTPIN 2 //D4
#define DHTTYPE DHT11

// WiFi SSID & Password
const char* ssid = "ssid";
const char* password = "password";

// server setting=
const char* serverName = "http://ip_address/supremeproject/post-sql-data.php";
String apiKeyValue = "tPmAT5Ab3j7F9";

String sensorName = "DHT11";
String sensorLocation = "Electronics Lab";

DHT dht(DHTPIN, DHTTYPE);
HTTPClient http;
WiFiClient wifiClient;

int i = 1;

void setup() {
  // put your setup code here, to run once:

  //WiFi connection
  Serial.begin(115200);
  dht.begin();
  http.begin(wifiClient, serverName);
  WiFi.begin(ssid, password);
  while(WiFi.status() != WL_CONNECTED) {
    //Serial.print(".");
    delay(500);
    }
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());
  Serial.print("Client IP Address: ");
  Serial.println(WiFi.localIP());
  delay(5000);

  //sensor initialization
  //Serial.println(F("DHT11 test!"));
}

void loop() {
  // put your main code here, to run repeatedly:
  
  //sensor reading
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  //float f = dht.readHumidity(true); //bool isFahrenheit = true;
  //float hif = dht.computeHeatIndex(f,h);
  //float hic = dht.computeHeatIndex(t,h,false);
  if(isnan(h) || isnan(t) /*|| isnan(f)*/){
    //Serial.println("Failed to read from sensor!");
    delay(500);
    return;
    }

  //sensor reading result
  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print("% ");
  Serial.print(F("Temperature: "));
  Serial.print(t);
  Serial.print("\xc2\xb0");
  Serial.print("C");
  Serial.println("");
  delay(1000);

  //http client setting and data posting
  if(WiFi.status() == WL_CONNECTED && (!isnan(h) || !isnan(t))){
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    String request = "api_key=" + apiKeyValue + "&sensor=" + sensorName + "&location=" + sensorLocation + "&value1=" + String(t) + "&value2=" + String(h) + "&value3=" + "<a href=\"specified_result.php?id=" + i++ + "\">Preview</a>" + "";
    Serial.print("HTTP Request Data: ");
    Serial.println(request);
    int response = http.POST(request);
    if(response > 0) {
      Serial.print("HTTP Response Code: ");
      Serial.println(response);
      }
    else {
      Serial.print("Error Code: ");
      Serial.println(response);
      }
    http.end();
    delay(10000);
    }
  else {
    Serial.println("WiFi Disconnected");
    }
}
