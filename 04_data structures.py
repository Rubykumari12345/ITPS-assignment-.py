# 04. Marks ke basis par students ko pass/fail classify karo:

marks = {"Ruby": 47, "Neha": 65, "Riya": 60, "Roshni": 70, "Dipshikha": 80, "Anjali": 45, "Sanya": 30}
for name, m in marks.items():
    status = "pass" if m >= 50 else "fail"
    print(f"{name}: {status}")