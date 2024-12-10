bird_dict = {}
Cnt_bird = 0

f = open ('bird_names.txt', 'r')
data = f.readlines() #새 이름들 리스트
for bird_one in data:
    bird_one = bird_one.strip()
    Cnt_bird += 1
    
    if bird_one in bird_dict:
        bird_dict[bird_one] += 1
    
    else:
        bird_dict[bird_one] = 1

f.close()

sorted_keys = sorted(bird_dict.keys())

for key in sorted_keys:
    proportion = bird_dict[key]/Cnt_bird
    print(f"{key} {proportion:.3f}")


