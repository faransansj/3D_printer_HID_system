#include <Keyboard.h>

const int endstopPin = 2;  // Optical endstop의 신호 핀을 디지털 2번 핀에 연결

void setup() 
{
    pinMode(endstopPin, INPUT);
    Serial.begin(9600);  // 시리얼 통신을 9600 baud로 시작
    Keyboard.begin();    // 키보드 기능을 초기화
}

void loop() 
{
    int endstopState = digitalRead(endstopPin);  // Endstop 상태 읽기

    if (endstopState == LOW) {  // Optical endstop이 활성화 되었을 때 (0)
        Serial.println("no fillament!");
        Keyboard.print("0");    // PC로 키보드 "0" 입력을 보냄
    }

    Serial.println(endstopState);  // 시리얼 모니터에 상태 출력

    delay(100);  // 100ms의 딜레이
}
