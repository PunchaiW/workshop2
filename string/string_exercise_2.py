# จงเขียนคำสั่งเพื่อแสดงความยาวของตัวอักษร "I am the best programmer"
print(len("I am the best programmer"))
# จงเขียนคำสั่งเพื่อแสดงอักษรแรกของข้อความ "I am the best programmer"
print("I am the best programmer"[0])
# จงเขียนคำสั่งเพื่อแสดง "best" ของข้อความ "I am the best programmer"
print("I am the best programmer"[9:14])
# จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ที่ไม่มี space
print("I am the best programmer".replace(" ", ""))
# จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ให้เป็นตัวพิมใหญ่ทั้งหมด
print("I am the best programmer".upper())
# จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ให้เป็นตัวพิมเล็กทั้งหมด
print("I am the best programmer".lower())
# จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ที่ถูกแทนที่อักษร e ด้วย z ทั้งหมด
print("I am the best programmer".replace("e", "z"))
# จงเติมคำในช่องว่าเพื่อแสดงชื่อ
myname = "ถ้าเค้าจะไปก็ปล่อยเขาไป"
txt = "{} is the best programmer"
print(txt.format(myname))