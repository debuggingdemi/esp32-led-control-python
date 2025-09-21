#include <WiFi.h>

#define LED_PIN LED_BUILTIN

const char* ssid = "your wifi name"; // your wifi name (NOTE: see what GHz your MCU, eg. 2.4GHz or 5GHz)
const char* password = "your wifi password"; // your wifi password

WiFiServer server(80); // define web server/local IP address for ESP32 on port 80 (HTTP port)

void setup() {
  // put your setup code here, to run once:

  pinMode(LED_PIN,OUTPUT);
  digitalWrite(LED_PIN, LOW); // starts with LED off

  Serial.begin(115200);

  WiFi.mode(WIFI_STA);   // sets ESP32 as a station since it will be connected to another network
  WiFi.begin(ssid,password); // connects to Wifi network
  Serial.print("Connecting to WiFi...");
  while (WiFi.status() != WL_CONNECTED){  // while loop checks if connection is established 
    Serial.print('.');
    delay(1000);
    }
  Serial.println("");
  Serial.print("Wifi IP Adress:"); Serial.println(WiFi.localIP());

server.begin(); // starts server once Wifi conection is established 

}

void loop() {
  WiFiClient client = server.available();  // Check if a client is connected

  if (client) {
    Serial.println("Client connected");

    String request = client.readStringUntil('\r');  // Read HTTP request line
    Serial.print("Request: ");
    Serial.println(request);
    client.flush();  // Clear remaining input

    // Parse command from request
    if (request.indexOf("/on") != -1) {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("LED turned ON");
    }
    else if (request.indexOf("/off") != -1) {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("LED turned OFF");
    }

    // Send HTTP response
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");
    client.println("Connection: close");
    client.println();
    client.println("<!DOCTYPE HTML>");
    client.println("<html>");
    client.println("<h1>ESP32 LED Control</h1>");
    client.println("<p><a href=\"/on\">Turn ON</a></p>");
    client.println("<p><a href=\"/off\">Turn OFF</a></p>");
    client.println("</html>");

    delay(1);  // Give time for client to receive
    client.stop();  // Close the connection
    Serial.println("Client disconnected");
  }
}
