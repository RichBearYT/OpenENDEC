/*
 *  ArduinoENDEC.ino
 *  2020 Copyright (c) Nathan Sales. All righs reserved.
 *
 *  Author: Nate Sales (@nwsnate)
 *
 *  This is the main Arduino coprocessor code for the OpenENDEC project.
 *
*/

#include <Wire.h>
#include "rgb_lcd.h"

const int BUTTON_PIN = 8;
const int LED_PIN = 9;
const int PTT_CONTROL = 5;

rgb_lcd lcd;

void setFirstLine() {
  lcd.setCursor(0, 0);
}

void setSecondLine() {
  // set the cursor to column 0, line 1
  lcd.setCursor(0, 1);
}

void printFully(String text) {
  String _buffer = "";

  for (int i = 0; i < (16 - text.length()); i++) {
    _buffer += " ";
  }

  lcd.print(text + _buffer);
}

void key() {
  lcd.setRGB(255, 0, 0);
  setSecondLine();
  printFully("Transmitting...");
  digitalWrite(PTT_CONTROL, LOW);
}

void unkey() {
  lcd.setRGB(255, 255, 255);
  setSecondLine();
  printFully("Idle.");
  digitalWrite(PTT_CONTROL, HIGH);
}

void setButtonLight(boolean state) {
  if(state) {
    digitalWrite(LED_PIN, HIGH);
  } else {
    digitalWrite(LED_PIN, LOW);
  }

}

boolean buttonPressed() {
  return digitalRead(BUTTON_PIN) == 0;
}

void setup() {
  Serial.begin(9600);

  lcd.begin(16, 2);
  lcd.setRGB(255, 255, 255);

  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
  pinMode(PTT_CONTROL, OUTPUT);
  digitalWrite(PTT_CONTROL, HIGH);

  setFirstLine();
  lcd.print("No alerts.");

  setSecondLine();
  printFully("Idle.");
}

String serialInput = "";

void loop() {
  if (Serial.available() > 0) {
    serialInput = Serial.readString();
    serialInput.trim();

    if(serialInput.startsWith("#")) {
      setFirstLine();
      printFully(serialInput.substring(1, 17));
    } else if(serialInput == "CLEAR") {
      setFirstLine();
      printFully("No alerts.");
      setButtonLight(false);
    } else if(serialInput == "KEY") {
      key();
    } else if(serialInput == "UNKEY") {
      unkey();
    } else if(serialInput == "BUTTON_ON") {
      setButtonLight(true);
    } else if(serialInput == "BUTTON_OFF") {
      setButtonLight(false);
    }
  }
}
