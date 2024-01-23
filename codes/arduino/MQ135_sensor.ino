const int mq135Pin = A0;  // MQ135의 아날로그 출력 핀을 아날로그 0번 핀에 연결

void setup() 
{
    Serial.begin(9600);  // 시리얼 통신을 9600 baud로 시작
}

void loop() 
{
    int sensorValue = analogRead(mq135Pin);  // MQ135 센서로부터 아날로그 값 읽기
    float voltage = sensorValue * (5.0 / 1023.0);  // 아날로그 값을 전압으로 변환

    // 여기서는 간단한 변환 공식을 사용합니다. 실제 응용에서는 더 정교한 보정이 필요할 수 있습니다.
    // 이 코드는 대략적인 값만을 제공합니다.
    float approximateCO2 = (voltage - 0.4) * 1000;  // 대략적인 CO2 수준 계산

    Serial.print("Sensor Value: ");
    Serial.print(sensorValue);
    Serial.print(", Voltage: ");
    Serial.print(voltage);
    Serial.print(", Approx. CO2 Level: ");
    Serial.println(approximateCO2);

  

    delay(100);  // 1초 딜레이
}
