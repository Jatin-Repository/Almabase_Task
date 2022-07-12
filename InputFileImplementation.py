from Profile import *
import re
from fuzzywuzzy import fuzz


class InputFileImplementation:

    def __init__(self):
        self.entries = dict()
        self.list1 = []

    def read_input_file(self, file):
        my_file = open(file, "rt")
        s = ""
        for txt in my_file:
            s += txt.rstrip()
        self.list1 = re.split(r"profile", s)
        del self.list1[0]

    def extract_profile(self):
        length = len(self.list1)
        for i in range(0, length):
            x = self.list1[i].strip()
            temp = x.strip().split("-", 1)
            temp[1] = temp[1].replace("â€˜", "'")
            temp[1] = temp[1].replace("â€™", "'")
            number = temp[0].strip()  # Profile Number
            details = temp[1].strip()  # Profile Details
            self.entries[number] = details  # Mapping id with details

    def assign_details_to_profile(self):
        for num, det in self.entries.items():
            profile = dict()
            details = str(det)
            details = details.replace("{", ",")
            details = details.replace("}", ",")
            values = details.split(",")
            for z in values:
                if z == '':
                    continue
                else:
                    _id = email = first_name = last_name = date_of_birth = class_year = ""
                    z = z.strip()
                    if re.match("id:", z):
                        _id = re.split("id:", z)[1].strip()
                        profile['id'] = _id
                    if re.match("email:", z):
                        email = re.split("email: ", z)[1].strip()
                        profile['email'] = email
                    if re.match("first_name:", z):
                        first_name = re.split("first_name:", z)[1].strip()
                        profile['first_name'] = first_name
                    if re.match("last_name:", z):
                        last_name = re.split("last_name:", z)[1].strip()
                        profile['last_name'] = last_name
                    if re.match("class_year:", z):
                        class_year = str(re.split("class_year:", z)[1].strip())
                        profile['class_year'] = class_year
                    if re.match("date_of_birth:", z):
                        date_of_birth = re.split("date_of_birth:", z)[1].strip()
                        profile['date_of_birth'] = date_of_birth
                    self.entries[num] = profile

    def Display_Profiles(self):
        entry = dict()
        self.read_input_file("input")
        self.extract_profile()
        self.assign_details_to_profile()
        entry = self.entries
        return entry

    def check_duplicate(self, a, b):
        duplicate = []
        matching_attribute = []
        non_matching_attribute = []
        ignored_attribute = []
        score = 0
        f = fuzz.ratio(a.first_name, b.first_name)
        if f >= 80:
            matching_attribute.append("first_name")
        else:
            non_matching_attribute.append("first_name")
        l = fuzz.ratio(a.last_name, b.last_name)
        if l >= 80:
            matching_attribute.append("last_name")
        else:
            non_matching_attribute.append("last_name")
        e = fuzz.ratio(a.email, b.email)
        if e >= 80:
            pass
        else:
            non_matching_attribute.append("email")
        name1 = a.first_name+a.last_name+a.email
        name2 = b.first_name+b.last_name+b.email
        ratio_name = fuzz.ratio(name1, name2)
        if ratio_name > 80:
            score += 1
        class_year_a = a.class_year
        class_year_b = b.class_year
        if class_year_a or class_year_b:
            ignored_attribute.append("class_year")
        else:
            if class_year_a == class_year_b:
                score += 1
                matching_attribute.append("class_year")
            else:
                score -= 1
        dob_a = a.date_of_birth
        dob_b = b.date_of_birth
        if dob_a or dob_b:
            ignored_attribute.append("date_of_birth")
        else:
            date_a = dob_a.split("-")
            date_b = dob_a.split("-")
            if date_a[0] == date_b[0] and date_a[1] == date_b[1] and date_a[2] == date_b[2]:
                matching_attribute.append("date_of_birth")
                score += 1
            else:
                score -= 1
        duplicate.append(score)
        duplicate.append(matching_attribute)
        duplicate.append(non_matching_attribute)
        duplicate.append(ignored_attribute)
        return duplicate


profiles = dict()
res = []
count = 0
profiles = InputFileImplementation().Display_Profiles()
list2 = list(profiles.keys())
length = len(profiles)
a = b = dict()
e = g = f = h = l = ""
for i in range(0, length):
    list3 = []
    c = list2[i]
    a = profiles[c]
    x = Profile(a['id'], a['email'], a['first_name'], a['last_name'], a['class_year'], a['date_of_birth'])
    list1 = []
    for j in range(i+1, length):
        l = c
        d = list2[j]
        b = profiles[d]
        y = Profile(b['id'], b['email'], b['first_name'], b['last_name'], b['class_year'], b['date_of_birth'])
        list3 = InputFileImplementation().check_duplicate(x, y)
        for k in range(0, len(list3)):
            z = list3[k]
            if isinstance(z, list) and len(z) == 0:
                del list3[k]
                list3.insert(k, "None")
        e, f, g, h = list3
        output = "profile {}, profile {}, total match score : {}, matching_attributes:{}, non_matching_attributes: {}, ignored_attributes: {}".format(l, d, e, f, g, h)
        res.append(output)
for m in res:
    print(m)




