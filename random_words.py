# -*- coding: SJIS -*-
import sys
import random


def random_words(m=10, n=10):
    # データセット作成
    digit = [d for d in range(ord(u"0"), ord(u"9")+1)]         # 数値
    l_letter = [l for l in range(ord(u"a"), ord(u"z")+1)]      # アルファベット小文字
    u_letter = [u for u in range(ord(u"A"), ord(u"Z")+1)]      # アルファベット大文字
    hiragana = [h for h in range(ord(u"ぁ"), ord(u"ん")+1)]      # ひらがな
    katakana = [k for k in range(ord(u"ァ"), ord(u"ヴ")+1)]      # カタカナ
    h_katakana = [h_k for h_k in range(ord(u"ｱ"), ord(u"ﾝ"))]   # 半角カタカナ
    cjk = [c for c in range(ord(u"一"), ord(u"龠")+1)]           # 漢字

    #dataset = digit + l_letter + u_letter + hiragana + katakana + h_katakana + cjk

    result = ""
    for col in range(m):
        for row in range(n):
            while True:
                flag = random.randrange(0,7)
                if flag == 0:
                    word = unichr(random.choice(digit))
                elif flag == 1:
                    word = unichr(random.choice(l_letter))
                elif flag == 2:
                    word = unichr(random.choice(u_letter))
                elif flag == 3:
                    word = unichr(random.choice(hiragana))
                elif flag == 4:
                    word = unichr(random.choice(katakana))
                elif flag == 5:
                    word = unichr(random.choice(h_katakana))
                elif flag == 6:
                    word = unichr(random.choice(cjk))

                try: # SJIS対応のチェック
                    word = word.encode("SJIS")
                    break
                except:
                    pass
            result += word
        result += "\n"
    return result


if __name__ == "__main__":    
    # 乱文ファイルの作成
    try:
        f = open(u"random_words.txt", "w")
        f.write(random_words(10,10))
        f.close()
    except IOError:
        print sys.exc_info[1]
        sys.exit()
