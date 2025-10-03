from talaba.models import Talaba

def add_students():
    Talaba.objects.create(ismi="Ali", yoshi=19, kursi=1, guruhi="101A", universiteti="TATU")
    Talaba.objects.create(ismi="Vali", yoshi=20, kursi=2, guruhi="202B", universiteti="SamDU")
    Talaba.objects.create(ismi="Dilshod", yoshi=17, kursi=1, guruhi="103C", universiteti="NamDU")
    print("3 talaba qoshildi!")

def first_course_students():
    return Talaba.objects.filter(kursi=1)

def change_name():
    Talaba.objects.filter(ismi="Ali").update(ismi="Alijon")

def upgrade_students():
    Talaba.objects.filter(kursi=2).update(kursi=3)

def delete_underage_students():
    Talaba.objects.filter(yoshi=18).delete()

from talaba.models import Talaba