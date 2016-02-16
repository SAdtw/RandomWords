# -*- coding: SJIS -*-
import sys
import random


def random_words(m=10, n=10):
    # �f�[�^�Z�b�g�쐬
    digit = [d for d in range(ord(u"0"), ord(u"9")+1)]         # ���l
    l_letter = [l for l in range(ord(u"a"), ord(u"z")+1)]      # �A���t�@�x�b�g������
    u_letter = [u for u in range(ord(u"A"), ord(u"Z")+1)]      # �A���t�@�x�b�g�啶��
    hiragana = [h for h in range(ord(u"��"), ord(u"��")+1)]      # �Ђ炪��
    katakana = [k for k in range(ord(u"�@"), ord(u"��")+1)]      # �J�^�J�i
    h_katakana = [h_k for h_k in range(ord(u"�"), ord(u"�"))]   # ���p�J�^�J�i
    cjk = [c for c in range(ord(u"��"), ord(u"�")+1)]           # ����

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

                try: # SJIS�Ή��̃`�F�b�N
                    word = word.encode("SJIS")
                    break
                except:
                    pass
            result += word
        result += "\n"
    return result


if __name__ == "__main__":    
    # �����t�@�C���̍쐬
    try:
        f = open(u"random_words.txt", "w")
        f.write(random_words(10,10))
        f.close()
    except IOError:
        print sys.exc_info[1]
        sys.exit()
