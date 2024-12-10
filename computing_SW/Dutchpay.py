cost = int(input("총 비용을 입력해주세요 : ")) 
people = int(input("총 인원을 입력해주세요 : ")) 
deliver = int(input("제외할 배달비를 입력해주세요 : ")) 
print("한 사람 당 지불할 비용은 ", (cost-deliver)/people,  "원 입니다.", sep='')
