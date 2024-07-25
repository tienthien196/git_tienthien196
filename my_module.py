import random 
import time
import sys
import os 
from pathlib import Path
from datetime import datetime

# thực hiện thao tác với thời gian 
class Nowerday:
    def __init__(self) -> None:
        pass
    def d_m_y():
        return datetime.now() 
# Thực hiện thao tác ghi dữ liệu 
class Load_file:
    def __init__(self,dc,dsdir):
        self.dc = dc
        self.dsdir = dsdir

    # Địa chỉ thư mục hiện tại
    def dc_cr():
        return os.getcwd()

    # Thay đổi địa chỉ file hiện tại 
    def changefile(self):
        os.chdir(self.dc)

    # Viết hàm tạo folder
    def creat_folder(name_folder):
        if not os.path.exists(name_folder):
            os.mkdir(name_folder)
            print(f"đã tạo folder{name_folder} ")
        else:
            print("folder này đã có rồi")

    # Hiện danh sách thư mục file
    def show_file_folder(self):
        for it in self.dsdir:
            content_it = os.path.join(self.dc,it)
            content_it = Path(content_it)
            if content_it.is_file():
                print(f"tệp :{content_it}")
            elif content_it.is_dir():
                print(f"thư mục :{content_it}")
    
    # Viết kq game vào file kq.txt:
    def w_kq_game(ket_qua,n,mode):
        try:        
            with open("kq.txt",mode, encoding = "utf-8") as file:
                file.write(f"kết quả ván {n} là : {ket_qua}\n ")
                print("kq đã được lưu vào file")
                file.close()            
        except Exception as e:
                print(" đã  gặp lỗi ",e)
    
    # Đọc kết quả game
    
    def r_kq_game():
        try:        
            with open("kq.txt","r") as file:
                print(file.read())
                file.close()      
        except Exception as e:
                print(f" đã  gặp lỗi {e}")
    
class Player:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age 
        self.money = money
    
    def check_age(self):
        if self.age >= 18:
            print("Người chơi đủ tuổi")
            return True
        else:
            print("Bạn chưa đủ tuổi")
            return False

class Robot:
    def __init__(self, name, msg, age, money):
        self.name = name
        self.age = age
        self.money = money
        self.msg = msg

    def answer(self):
        print(f"Hi! Tôi tên là {self.name}")
        print(f"{self.msg}")
    
    def ai_play(self):
        choices = ["bua", "keo", "bao"]
        return random.choice(choices)

class Gaming:
    def __init__(self, name, kq_game):
        self.name = name
        self.kq_game = kq_game

    @staticmethod
    def play():
        print("Trò chơi sẽ bắt đầu sau 3s ...")
        time.sleep(3)
        player_choice = input("Bạn lựa chọn (bua/keo/bao) or thoat: ")
        return player_choice

    @staticmethod
    def check_input(player_choice, robot_choice, mn_player):
        valid_inputs = ["bua", "keo", "bao"]
        while player_choice not in valid_inputs:
            player_choice = input("Nhập lại lựa chọn hợp lệ: ")

        print(f"Máy chọn: {robot_choice}")

        result = {
            ("bua", "keo") :("ban win", 1000),
            ("keo", "bao") :("ban win", 1000),
            ("bao", "bua") :("ban win", 1000),
            ("bua", "bao") :("ban thua", -1000),
            ("keo", "bua") :("ban thua", -1000),
            ("bao", "keo") :("ban thua", -1000),
            ("bua", "bua") :("ban hoa", 0),
            ("keo", "keo") :("ban hoa", 0),
            ("bao", "bao") :("ban hoa", 0),
        }

        ket_qua, change = result.get((player_choice, robot_choice), ("Kết quả không hợp lệ", 0))
        mn_player += change
        print(f"Kết quả: {ket_qua}")
        print(f"Số tiền của người chơi: {mn_player}")

        return ket_qua, mn_player


if __name__ == "__main__":
    age_pl = True
    while age_pl:
        age_player = int(input("nhập vào số tuổi của bạn"))
        if age_player >= 18:
            break

    player1 = Player("bin", age_player, 10000)
    robot1 = Robot("alanin", "Dứt thôi nào!", 20, 2000000)
    game1 = Gaming("Oẳn tù tì", "Thắng hay bại")

    kq_game = ""
    dolar = player1.money
    van_game = 0

    name_dc = "C:/Users/THIỆN"
    ds_tm = os.listdir(name_dc)
    file_r = Load_file

    if player1.check_age():
        robot1.answer()
        time.sleep(2)
        print(game1.name)
        time.sleep(1)

    while dolar >= 0:
        player_choice = game1.play()
        if player_choice == "thoat":
            break
        print("loading...")
        time.sleep(3)
        robot_choice = robot1.ai_play()   
        
        kq_game, dolar = game1.check_input(player_choice,robot_choice, dolar)
        van_game += 1
        file_r.w_kq_game(kq_game, van_game,"a")

    file_r.r_kq_game()
