def ID(line):
    ID = None
    if "INDI" in line:
        ID = line[3:10]
    if ID is not None:
        return ID

def Sex(line):
    Sex = None
    if "SEX" in line:
        Sex = line[6]
    if Sex is not None:
        return Sex

def Name(line):
    Name = None
    if "GIVN" in line:
        Name = line[7:]
        Name = Name.rstrip()
    if Name is not None:
        return Name

def Surname(line):
    Surname = None
    if "SURN" in line:
        Surname = line[7:]
        Surname = Surname.rstrip()
    if Surname is not None:
        return Surname

def FName(line):
    FName = None
    if "NAME" in line:
        if " MyHeritage" in line:
            return
        FName = line[7:]
        if "/" in FName:
            FName = FName.replace("/", " ")
            FName = FName.rstrip()
    if FName is not None:
        return FName

f = open('Tree.txt')

file_temp = []

for line in f:
    file_temp.append(line)


IDs = list(filter(None, map(ID, file_temp)))
Names = list(filter(None, map(FName, file_temp)))
Sex = list(filter(None, map(Sex, file_temp)))

familyMembersIDNames = dict(zip(IDs, Names))
familyMembersSexNames = dict(zip(Names, Sex))

children = []

for line in file_temp:
        if "FAM" in line:
            FAMILY = line[3:10]
            if FAMILY is not None:
                father = None
                mother = None
                continue
        if "HUSB" in line:
            father = line[8:15]
            continue
        if "WIFE" in line:
            mother = line[8:15]
            continue
        if "CHIL" in line:
            child = line[8:15]
            if father is not None:
                fact = (familyMembersIDNames[child], familyMembersIDNames[father])
                children.append(fact)
            if mother is not None:
                fact = (familyMembersIDNames[child], familyMembersIDNames[mother])
                children.append(fact)
                continue

res = open('res.txt', 'w')

for fact in children:
	child, parent = fact
	res.write("child({}, {}).\n".format(child, parent))

res.write("\n")

line = ""
for key in familyMembersSexNames:
    if familyMembersSexNames[key] == 'M':
        line+= 'Male('+key+')\n'

line_=""
for key in familyMembersSexNames:
    if familyMembersSexNames[key] == 'F':
        line_+= 'Female('+key+')\n'

lines = line+ "\n" + line_
res.write(lines)





