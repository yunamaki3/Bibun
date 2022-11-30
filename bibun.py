#微分を行う
#入力値の想定:3x^2 +2x +2
#他の入力値の想定:4x^3 +2x +2
suusiki = input().split(" ")
kosuu = len(suusiki)
for i in range(kosuu):
  kou = suusiki[i]
  if 'x^' in kou:
    idx = kou.find('x')
    idx1 = idx
    kakarisuu = kou[:idx1]
    idx2 = idx + 2
    sisuu = kou[idx2:]
    kakarisuu = int(kakarisuu)*int(sisuu)
    sisuu = int(sisuu)-1
    if sisuu==1:
      print('{0}x'.format(kakarisuu),end=" ")
    else:
      print('{0}x^{1}'.format(kakarisuu,sisuu),end=" ")
  elif 'x' in kou:
    kou=kou.replace("x","")
    print(kou,end=" ")
