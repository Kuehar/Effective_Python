class ans_countNumber:
    def __init__(self,number,mn=0,mx=100):
        self.number = number
        self.ans_count  = 0
        self.min = mn
        self.max = mx

    def get_ans_count(self):
        ans_count = input(f"私の考えている数字を当ててみてください！（{self.min}~{self.max}の間の整数です。）:")
        if self.valid_number(ans_count):
            return int(ans_count)
        else:
            print("数字以外を入力しましたね？数字を入れてください！")
            return self.get_ans_count()

    def valid_number(self,str_number):
        try:
            number = int(str_number)
        except:
            return False
        return self.min <= number <= self.max

    def play(self):
        while True:
            self.ans_count += 1
            ans_count = self.get_ans_count()
            if ans_count > self.number:
                print("あなたの考えている数字よりも小さいです")
            elif ans_count < self.number:
                print("あなたの考えている数字よりも大きいです")
            else:
                break

        print(f"正解です！あなたは{self.ans_count}回で正解に辿り着きました！")


game = ans_countNumber(56,0,100)
game.play()

"""
クラスとか関数を決めずに作るとこんな感じ。
ただオブジェクト指向である時点できっちりとクラス分け、メソッドを分けて考え、適切な範囲に切り分けることでバグを減らしたり、仮に発生したとしても特定しやすくなる。
なにより再利用しやすい。
再利用できると楽ができる。楽なのは良いこと。


ans_count = 1

while True:
    num = input()
    try:
        num = int(num)
    except:
        print("数字以外を入力しましたね？数字を入れてください！")
        continue
    if num < 45:
        print("あなたの考えている数字よりも小さいです")
    elif num > 45:
        print("あなたの考えている数字よりも大きいです")
    else:
        break

    ans_count += 1

print(f"正解です！あなたは{ans_count}回で正解に辿り着きました！")
"""