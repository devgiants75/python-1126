### 도시 날씨 관리 시스템 ###

#! 프로젝트 개요
# : 사용자로부터 도시의 날씨 정보를 수집하여 csv 파일에 저장
# : 해당 파일의 데이터를 생성, 조회, 수정, 삭제하는 프로젝트
# : matplotlib 라이브러리를 사용하여 도시별 기온을 차트로 시각화

#! 프로젝트 데이터 구조

# 도시 이름(city name)
# 날짜(date)
# 최고 기온(max temperature)
# 최저 기온(min temperature)
# 강수량(rainfall)

#! 프로젝트 요구 사항
# 1. csv 파일 관리 클래스 생성
# : csv 파일을 생성, 조회, 수정, 삭제하는 기능을 포함

# 2. 사용자로부터 데이터를 입력받는 기능
# : 사용자로부터 데이터를 입력받아 csv 파일에 저장

# 3. 데이터를 차트로 시각화하는 기능
# : matplotlib 라이브러리를 사용해 csv 파일을 차트로 시각화
# : 도시별 최고 및 최저 기온을 선 그래프로 표시

# 4. 메인 함수
# : 프로그램의 실행을 관리하는 메인 함수를 작성
# : 사용자로부터 명령을 입력받아 해당 명령에 맞는 기능을 실행