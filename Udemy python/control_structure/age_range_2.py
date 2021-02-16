# Age range using if-else conditional

def age_range(age):
    if 0 <= age < 18:
        return "Underage"
    elif age in range (18,64):
        return "Adult"
    elif age in range (65, 100):
        return " Golden age"
    elif age >= 100:
        return "Kicked the bucket"

if __name__== "__main__":
    for age in (17,35,90,123,68):
        print(f'{age}:{age_range(age)}')
