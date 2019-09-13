
# Created at 2019.06.02
# bit全探索アルゴリズム
# n個の要素からなる集合 {0,1,…,n−10,1,…,n−1} の部分集合をすべて調べ上げるアルゴリズム
# 引用：「 n個の選択肢それぞれに Yes or No の二択があるが、その部分集合（選択できるパターン）の全てを
#       網羅的にチェックしたい 」といった場合に使えます。 - Python de アルゴリズム（bit全探索）| Qiita

# MARK:- データがソート済であることが条件→バラバラであればデータをソートする必要がある→ソートアルゴリズム
#最大探索回数は 2^n となる。
# →20個のデータからなる集合から部分集合を全探索する場合、最大探索回数は 約2000万回となるので、
# 計算量の爆発には十分注意が必要。


#問題：みかん（100円）りんご（200円）ぶどう（300円）がそれぞれ1つずつ果物屋さんにありました。
#     財布の中には300円ありますが、考え得るすべての買い物パターンを列挙しなさい。

#解放：全ての買い物パターン（部分集合）で合計金額を計算し、その中から300円以下に収まったものを列挙する。

#indexと買い物パターンの判別方法：
# 部分集合を全て探索して列挙することができるのがbit全探索だが、
# では、各ループでチェックしている部分集合（買い物パターン）はどう判別すれば良いのだろう？
#      例）「 i=5の時の買い物パターン」（=答えは「みかん＋ぶどう」）

# ➡️ここで「 bit 」を用いる！
#  すなわち、「　2進数表記のそれぞれの桁が０であるか１であるか 」を見る
# i=5を2進数に直すと「101」。

if __name__ == '__main__':
    money = 300
    fruits = (("みかん", 100), ("りんご", 200), ("ぶどう", 300)) #タプル内タプル=重複不可の配列
    count = len(fruits)

    for pattern_i in range(2 ** count):
        # ここで必要なチェックを行う
        bag = [] #今回のパターンに含まれるフルーツの組み合わせ
        total = 0 #今回の買い物の合計金額
        # 全てのフルーツでbitのチェック
        for fruit_i in range(count):
            #2進数の下からfruit_i桁目は、fruits[i]がそのパターンに含まれているかどうかを示している。
            #　→pattern_iをfruit_i桁右にシフトさせた時の最下位の桁が...
            #  １ = パターンに含まれている / 0 = 含まれていない
            if ((pattern_i >> fruit_i) & 1):
                bag.append(fruits[fruit_i][0])  # 含まれていたら bag に果物を詰める
                total += fruits[fruit_i][1] # 会計金額に計上する
        #買い物金額が300円以下の時だけ出力する
        if (total <= money):
            print(total,bag)