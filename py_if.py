# 与えられた任意の整数を偶数か否か判定するプログラム

# 変数を設定
is_usr_even = False
usr = int(input('1から99のあいだで好きな整数を入力してください >> '))

# 偶数判定
if usr % 2 == 0:
    is_usr_even == True
else:
    is_usr_even == False

# 結果発表
print(f'入力された整数: {usr}')
print(f'偶数判定: {is_usr_even}')