start_ab = int(input())
start_cd = int(input())
diff_ab = int(input())
diff_cd = int(input())
end_ab = diff_ab + start_ab
end_cd = diff_cd + start_cd

for ab in range(start_ab, end_ab + 1):
    for cd in range(start_cd, end_cd + 1):
        ab_is_prime = True
        cd_is_prime = True
        for i in range(2, ab):
            if ab % i == 0:
                ab_is_prime = False
                break
            for j in range(2, cd):
                if cd % j == 0:
                    cd_is_prime = False
                    break
        # if 9< ab< 91 and 9 <cd<91 and 0 <diff_cd<10 and 0<diff_ab<10:
        if ab_is_prime and cd_is_prime:
            print(f"{ab}{cd}")















