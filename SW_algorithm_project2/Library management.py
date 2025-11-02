# 1. Node 클래스 : 단순 연결 리스트의 노드
# 노드의 데이터 필드는 도서(Book) 객체를 저장하는 역할

class Node:
    def __init__(self, elem, next = None):
        self.data = elem
        self.link = next

    def append(self, new):
        # 현재 노드 다음에 new 노드를 삽입
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self):
        # 현재 노드의 다음 노드를 삭제하고 반환
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
            deleted_node.link = None # 연결 해제
        return deleted_node


# 2. LinkedList 클래스 : 단순 연결 리스트 구조
"""
1. head: 리스트의 첫 번째 노드를 가리키는 포인터
2. 주요 메서드:
   - isEmpty(): 리스트가 비어있는지 확인
   - isFull(): 리스트가 가득 찼는지 확인
   - getNode(pos): 특정 위치의 노드를 반환
   - getEntry(pos): 특정 위치의 노드 데이터를 반환
   - replace(pos, elem): 특정 위치의 노드 데이터를 변경
   - size(): 리스트의 크기를 반환
   - display(msg): 리스트의 내용을 출력
   - insert(pos, elem): 특정 위치에 새 노드를 삽입
   - delete(pos): 특정 위치의 노드를 삭제
   - find_by_title(self, title): 책 제목으로 리스트에서 도서를 찾기
   - find_pos_by_title(self, title): 책 제목으로 리스트에서 도서의 위치를 찾기
"""
class LinkedList:
    def __init__(self):
        self.head = None # 비어있는 리스트의 초기 상태

    # 주요 기본 연산
    def isEmpty(self):
        # 리스트의 빈 상태 검사
        return self.head == None
    
    def isFull(self):
        # 리스트의 포화 상태 검사
        return False # 동적 노드 할당
    
    def getNode(self, pos): # pos 기반 연산
        # pos 위치에 있는 노드를 반환
        # pos는 리스트의 인덱스 0부터 시작
        if pos < 0: return None # pos는 유효하지않은 위치
        if self.head == None: # 리스트가 빈 상태
            return None
        else:
            ptr = self.head
            for _ in range(pos):
                if ptr == None: #pos가 리스트보다 크기가 큰 경우(유효하지 않은 위치)
                    return None
                ptr = ptr.link
            return ptr
        
    def getEntry(self, pos): # 인덱스 기반 연산
        # 리스트의 pos 위치에 있는 노드를 찾아 데이터값을 반환
        node = self.getNode(pos) # 해당 위치의 노드를 탐색
        if node == None: # 해당 노드가 없는 경우
            return None 
        else: # 해당 노드가 있는 경우
            return node.data
        
    def insert(self, pos, elem): # 인덱스 기반 연산
        # pos 위치에서 새 노드(elem) 삽입 연산
        if pos < 0:
            raise ValueError("잘못된 위치 값")
        new = Node(elem) # 1. 새 노드 생성
        before = self.getNode(pos - 1) # 2. pos-1 위치의 노드 탐색
        # 3. before 노드의 위치에 따라 구분
        if before is None :
            if pos == 0: # 1. 머리 노드로 삽입
                new.link = self.head
                self.head = new
                return
            else : # 2. pos가 리스트 범위에서 벗어남
                raise IndexError("삽입할 위치가 유효하지 않음")
        else : 
            before.append(new)

    def delete(self, pos): # 인덱스 기반 연산
        # pos 위치에서 해당 노드 삭제한 후 그 노드 반환
        if pos < 0:
            raise ValueError("잘못된 위치 값")
        
        before = self.getNode(pos - 1) # 1. 삭제 노드 이전의 노드 탐색
        # 2. before 노드의 위치에 따라 구분
        if before == None:
            if pos == 0: # 1. 머리 노드 삭제
                deleted = self.head
                self.head = deleted.link
                deleted.link = None # 연결 해제
                return deleted
            else: # 2. pos가 리스트 범위에서 벗어남
                raise IndexError("삭제할 위치가 유효하지 않음")
        else: # 3. 중간노드로 삭제
            return before.popNext()
        
    def size(self):
        # 리스트의 전체 노드의 개수
        if self.head is None: # 현재 리스트가 공백이면
            return 0
        else:
            ptr = self.head
            count = 0
            while ptr is not None:
                count += 1
                ptr = ptr.link
            return count
    
    def display(self, msg="LinkedList"):
        # 리스트의 내용을 출력
        print(msg, end= ' ')
        if self.head is None: # 현재 리스트가 공백이면
            return None
        else:
            ptr = self.head
            while ptr is not None:
                print(ptr.data, end=" \n ")
                ptr = ptr.link
            print("None")

    def replace(self, pos, elem): # 인덱스 기반 연산
        # 리스트의 pos 위치에 있는 노드의 데이터 필드를 수정
        node = self.getNode(pos)
        if node is not None: # 해당 노드가 있는 경우
            node.data = elem

    def find_by_title(self, title):
        # 책 제목으로 리스트에서 도서를 찾기
        ptr = self.head
        while ptr is not None:
            if ptr.data.title == title:
                return ptr.data
            ptr = ptr.link
        return None  # 찾지 못한 경우
    
    def find_pos_by_title(self, title):
        # 책 제목으로 리스트에서 도서의 위치를 찾기
        ptr = self.head
        index = 0
        while ptr is not None:
            if ptr.data.title == title:
                return index
            ptr = ptr.link
            index += 1
        return -1  # 찾지 못한 경우
    

# 3. Book 클래스 : 도서의 객체 정보를 저장하는 클래스 (책 번호, 책 제목, 저자, 출판연도)
class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"[책 번호: {self.book_id}] 제목: '{self.title}' 저자: {self.author} 출판 연도: ({self.year})"
    

# 4. BookManagement 클래스 : 인터페이스 기능을 구현하는 클래스
"""
- 주요메소드:
    - add_book(self, book_id, title, author, year): 새로운 도서를 리스트에 추가
    - remove_book(self, title): 주어진 책 제목에 해당하는 도서를 리스트에서 삭제
    - search_book(self, title): 주어진 책 제목에 해당하는 도서를 리스트에서 조회 후 해당 도서 정보 출력
    - display_books(self): 현재 리스트에 등록된 모든 도서를 출력
    - run(self): 프로그램이 종료될 때까지 메뉴를 출력 후 사용자가 선택한 작업을 수행
"""
class BookManagement:
    def __init__(self):
        self.book_list = LinkedList()

    def add_book(self, book_id, title, author, year):
        ptr = self.book_list.head
        while ptr is not None:
            if ptr.data.book_id == book_id:
                print(f" 책 번호 '{book_id}'는 이미 존재합니다.")
                return 
            ptr = ptr.link
        new_book = Book(book_id, title, author, year)
        self.book_list.insert(self.book_list.size(), new_book)
        print(f"도서' {new_book} '가 추가되었습니다.")

    def remove_book(self, title):
        pos = self.book_list.find_pos_by_title(title)
        if pos != -1:
            deleted_node = self.book_list.delete(pos)
            print(f"도서 삭제: {deleted_node.data}")
        else:
            print(f"도서 '{title}'를 찾을 수 없습니다.")

    def search_book(self, title):
        book = self.book_list.find_by_title(title)
        if book:
            print(f"도서 조회: {book}")
        else:
            print(f"도서 '{title}'를 찾을 수 없습니다.")

    def display_books(self):
        self.book_list.display("전체 도서 목록:")

    def run(self):
        while True:
            print("\n=== 도서관리 프로그램 ===")
            print("1. 도서 추가")
            print("2. 도서 삭제(책 제목으로 삭제)")
            print("3. 도서 조회(책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 종료")
            choice = input("메뉴를 선택하세요: ")

            if choice == '1':
                book_id = input("책 번호를 입력하세요: ")
                title = input("책 제목을 입력하세요: ")
                author = input("저자를 입력하세요: ")
                year = input("출판연도를 입력하세요: ")
                self.add_book(book_id, title, author, year)
            elif choice == '2':
                title = input("삭제할 책 제목: ")
                self.remove_book(title)
            elif choice == '3':
                title = input("조회할 책 제목: ")
                self.search_book(title)
            elif choice == '4':
                self.display_books()
            elif choice == '5':
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 선택입니다. 다시 시도하세요.")
    

#=========================================================
# 도서관리 프로그램
# 1. 도서추가 기능(책 번호, 책 제목, 저자, 출판연도)
# 2. 도서삭제 기능(책 제목으로 삭제)
# 3. 도서 조회 (책 제목으로 조회)
# 4. 전체 도서 목록 출력
# 5. 프로그램 종료
#=========================================================
if __name__ == "__main__":
    manager = BookManagement()
    manager.run()