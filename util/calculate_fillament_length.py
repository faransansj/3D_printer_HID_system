import math

def calculate_filament_length(diameter_cm, filament_diameter_cm=1.75/10):
    # 원의 둘레 계산
    circumference_cm = math.pi * diameter_cm
    
    # 필라멘트 지름을 통한 레이어 당 둘레 증가
    filament_increase_per_layer = 2 * math.pi * (filament_diameter_cm / 2)
    
    # 필요한 레이어 수 계산
    layers_needed = (diameter_cm / 2) / (filament_diameter_cm / 2)
    
    # 전체 필요 길이 계산
    total_filament_length_cm = 0
    for layer in range(int(layers_needed)):
        total_filament_length_cm += circumference_cm + layer * filament_increase_per_layer
        
    return total_filament_length_cm
  
# 원의 지름설정
diameter = 50  
needed_filament_length = calculate_filament_length(diameter)
print(f"지름 {diameter}cm 원에 필요한 필라멘트 길이는 약 {needed_filament_length:.2f}cm 입니다.")
