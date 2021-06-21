def main():
    def find_cont_skill(skill_tree, skl):
        _cont_skill = []
        for st in skill_tree:
            if st[0] == skl:
                _cont_skill.append(sk)

        if not st:
            return skl
        else :
            for _cs in _cont_skill:
                cst = _cs[0] + find_cont_skill(skill_tree, _cs[1])

    skills = input().split(' ')
    n_cont_skill = int(input())
    skill_tree = []
    for _ in range(n_cont_skill):
        skill = input().split(' ')
        skill_tree.append(skill)
    for cont_skill in skill_tree:

    print(x)

if __name__=="__main__":
    main()
