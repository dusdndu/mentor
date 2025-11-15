import pandas as pd

# 1. 파이썬 딕셔너리로 데이터 생성 (Numpy와 비슷)
raw_data = {
    'timestamp' : ['2025-11-13 10:00:00', '2025-11-13 10:00:01', '2025-11-13 10:00:02', '2025-11-13 10:00:03'],
    'Sensor_X' : [10, 12, 11, 15],
    'Sensor_Y' : [5, 6, 8, 7],
    'Sensor_Z' : [102, 101, 103, 100]
}

# 2. DataFrame 생성 (엑실 시트와 유사)
df = pd.DataFrame(raw_data)

# 3. [과제] 'Sensor_Z' 열의 데이터만 선택해서 출력하기
# 힌트: df['컬럼이름']
print(df['Sensor_Z'])

# 4. [과제] 'timestamp' 열을 '시간 인덱스'로 변환하기 (시계열의 핵심)
# 이 작업을 해야 시간 기반 분석이 가능해진다.
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.set_index('timestamp') ##################### 0, 1, 2, 3, ... >> 시간 timestamp를 인덱스로 변환

# 5. [과제] 변환된 df를 print() 해보고, 2번에서 출력한 df와 무엇이 달라졌는지 관찰하기
print(df)

# 인덱스가 timestamp로 바뀜