input = ["a_an_example", "b_better_start_small", "c_collaboration", "d_dense_schedule", "e_exceptional_skills", "f_find_great_mentors"]
#, "b_better_start_small", "c_collaboration", "d_dense_schedule", "e_exceptional_skills", "f_find_great_mentors"

person = []
person_skill = []
skill = []
days = []
project = []
submission = []
reward = []
skill_req = []
count = 0
solution = []


for n in range(len(input)):
    person = []
    person_skill = []
    skill = []
    days = []
    project = []
    submission = []
    reward = []
    skill_req = []
    count = 0
    solution = []
    try:
        f = open(f"{input[n]}.in.txt", 'r')
        N, M = f.readline().split()
        print(M)
        print(N)
        for i in range(int(N)):
            line = f.readline().split()
            person.append(line[0])
            l1 = []
            for i in range(int(line[1])):
                
                skill_line = f.readline().split()
                l1.append(skill_line)
                
                if skill_line[0] not in skill:
                    skill.append(skill_line[0])
                    
            person_skill.append(l1)
            
        for i in range(int(M)):
            line = f.readline().split()
            project.append(line[0])
            days.append(line[1])
            reward.append(line[2])
            submission.append(line[3])
            l2 = []
            for i in range(int(line[4])):
                sk = f.readline().split()
                l2.append(sk)
            skill_req.append(l2)
        max_val = max(reward)
        max_index = reward.index(max_val)
        skill_req[max_index]
        
        needed_skill = skill_req[max_index]
        print(needed_skill)
#         for i in range(len(person_skill)):
#             for j in range(len(person_skill[i])):
        for l in range(len(needed_skill)):
            for i in range(len(person_skill)):
                for j in range(len(person_skill[i])):
                    if person_skill[i][j][0] == needed_skill[l][0] and person_skill[i][j][1] >= needed_skill[l][1]:
                        count = count + 1
                        solution.append(person[i])
        print(solution)
        if len(person_skill) >= count:
            with open(f"{input[n]}.out.txt",'w',encoding = 'utf-8') as w:
                w.write("1")
                w.write('\n')
                w.write(project[max_index])
                w.write('\n')
                for i in range(len(solution)):
                    w.write(f"{solution[i]} ")
            
        
                
    finally:
        f.close()