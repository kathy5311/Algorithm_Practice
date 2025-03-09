from collections import Counter

participant=["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(list((Counter(participant)-Counter(completion)).keys())[0])