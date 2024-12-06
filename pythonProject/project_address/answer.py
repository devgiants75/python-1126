import sys

#! Person 클래스 생성
# : 각 개인의 정보를 저장할 클래스
# : 이름(name), 전화번호(phone), 주소(address)

class Person:
    # 생성자를 사용하여 해당 정보를 전달
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
        
    # 저장된 개인 정보를 출력
    def info(self):
        print(f'{self.name}, {self.phone}, {self.address}')
        
#! AddressBook 클래스
# : 주소록 프로젝트의 모든 기능을 구현하는 클래스
# : Person 클래스의 객체를 여러 개 저장할 수 있는 address_list 배열을 포함
# 기능
# - CSV 파일 읽기/쓰기
# - 신규 주소록 등록, 삭제, 수정, 검색, 전체 출력

class AddressBook:
    # 생성자
    # : csv 파일을 읽어서 address_list 배열(리스트)에 저장
    # : 리스트 생성 후 csv 파일을 읽어오는 file_reader() 메서드를 호출
    def __init__(self):
        self.address_list = []
        # file_reader() 메서드(리더기)를 실행하여 csv 파일로부터 데이터를 로드
        self.file_reader()
        
    # csv 파일 읽기
    # : csv 파일의 정보를 address_list 에 저장하는 메서드
    def file_reader(self):
        try:
            # 예외의 가능성이 있는 코드 블럭을 작성
            # : 예외 발생 시 except문 실행, 발생하지 않으면 else 문 실행
            
            # 'addressBook.csv' 파일을 읽기 모드로 열기
            file = open('addressBook.csv', 'rt', encoding='utf-8', errors='replace')
        except:
            # csv 파일이 없을 때
            print('addressBook 파일이 없습니다.')
        else:
            # csv 파일이 있을 때
            
            # 파일의 각 줄을 순회하여 공백을 제거하고 콤마로 분리
            for buffer in file:
                if buffer.strip(): # 공백 라인 건너뛰기
                    # 쉼표로 데이터 분리
                    name, phone, address = buffer.strip().split(',')
                    # 리스트에 추가
                    self.address_list.append(Person(name, phone, address))
            print('addressBook.csv 파일을 로드했습니다.')
            file.close()
            
    # csv 파일 생성
    # : address_list의 모든 데이터를 사용하여 csv 파일을 생성
    def file_generator(self):
        try:
            # 'addressBook.csv' 파일을 쓰기 모드로 열기
            file = open('addressBook.csv', 'wt', encoding='utf-8')
        except:
            # 파일 생성 실패 시 예외 처리
            print('addressBook.csv 파일을 생성할 수 없습니다.')
        else:
            # 파일 생성 완료 시
            for person in self.address_list:
                # '이름, 전화번호, 주소' 형식으로 파일에 작성
                file.write(f'{person.name},{person.phone},{person.address}\n')
            file.close() # 파일 닫기
            
    # 수행 메뉴 소개 및 입력
    # : 프로그램의 동작을 안내하는 출력문으로 구성
    # : 어떤 동작을 수행할 것인지 사용자로부터 입력받아서 그 값을 반환
    @staticmethod # 모든 객체에서 공통된 값을 공유하는 메서드
    def menu():
        print('-' * 30)
        print('1. 신규 주소록 등록')
        print('2. 기존 주소록 삭제')
        print('3. 기존 주소록 수정')
        print('4. 주소록 검색')
        print('5. 전체 주소록 출력')
        print('0. 프로그램 종료')
        print('-' * 30)
        choice = int(input('수행할 작업을 숫자로 입력하세요 : '))
        return choice
    
    # 프로그램 종료
    # : sys 모듈의 exit() 메서드를 호출하여 종료
    def exit(self):
        print('프로그램을 종료합니다.')
        sys.exit()
        
    # 프로그램 실행
    # : 사용자로부터 입력받은 값으로 작업할 해당 메서드를 호출
    def run(self):
        # 무한 루프: 프로그램을 종료 시키는 0번 동작 이전까지는 프로그램이 반복적으로 실행
        
        while True:
            # menu(): 정적 메서드 - 클래스명으로 호출
            choice = AddressBook.menu()
            if choice == 0: self.exit()
            elif choice == 1: self.insert()
            elif choice == 2: self.delete()
            elif choice == 3: self.update()
            elif choice == 4: self.search()
            elif choice == 5: self.print_all()
            else: print('없는 번호입니다. 확인 후 다시 입력해주세요.')
        
    # insert()
    # : 사용자로 부터 새로 등록할 이름, 전화번호, 주소를 입력받고 Person 객체를 생성하여
    #   , address_list에 저장
    def insert(self):
        print('== 신규 주소록 생성 ==')
        name = input('등록할 이름 입력: ')
        phone = input('등록할 전화번호 입력: ')
        address = input('등록할 주소 입력')

        # and 논리 연산자
        # : 모든 값이 true 여야 true를 반환
        if name and phone and address:
            # 모두 입력이 되었을 경우
            self.address_list.append(Person(name, phone, address)) # 삽입
            
            # 변경된 address_list 내용으로 csv 파일을 새로 생성
            self.file_generator()
            print('신규 주소록이 정상적으로 생성되었습니다.')
        else:
            # 누락된 입력이 하나라도 있는 경우 - 삽입 실패
            print('입력값이 부족하여 주소록이 생성되지 않습니다.')
            
    # delete()
    # : 사용자로부터 삭제하고자 하는 데이터의 이름을 입력받아 address_list에서 제거
    
    # update()
    # : 사용자로부터 수정할 사용자 정보를 입력 받아서 address_list에서 해당 사용자 정보를 수정
    
    # search()
    # : 특정 주소록 정보를 검색해서 출력하는 메서드
    # : 사용자로부터 이름을 입력 받아서 동일한 정보를 찾아 모두 출력
    # - 같은 이름으로 등록된 경우 모두 출력
    # - 검색된 사람이 없으면 메시지 출력
    
    # print_all()
    # : 전체 주소록 정보를 출력하는 메서드
    
my_app = AddressBook() # 클래스로 객체 생성(인스턴스화)
my_app.run() # 메서드(함수) 실행