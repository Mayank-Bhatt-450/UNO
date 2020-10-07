import random
def prn(*a,**k):
    colors=['red','green','yellow','blue','pink','light_blue','white']
    try:
        color=k['color']
        for i in range(7):
            if color==colors[i]:
                print(f"\x1b[{0};{30};{41+i}m",str(a).replace('(','').replace(')','')[:-1],'\x1b[0m')
                break
    except:
        #print('\x1b[6;35;42m' + 'except!' + '\x1b[0m')
        print(f"\x1b[{0};{30};{random.randint(43,48)}m",str(a).replace('(','').replace(')','')[:-1] ,'\x1b[0m')
def mod(n,m):
    a=n/m
    c=(a-int(a))*m
    return round(c)
game_state={'players':['A','B','C','D']}
global_v={'turnflag':0,'turn_num':4,'pt':3}
num_players=len(game_state['players'])
print()
if global_v['turnflag']==0:
    turn=game_state['players'][
    mod(global_v['turn_num'],num_players)
    ]
else:
    prn(f"global_v['pt']={global_v['pt']},num_players={num_players},global_v['turn_num']={global_v['turn_num']}",color='light_blue')

    a0=mod(
                                                global_v['turn_num'],
                                                num_players)
    a=mod(
    num_players+(global_v['pt']+(global_v['pt']-a0))
    ,num_players)
    prn(f'a={a},a0={a0}')
    turn=game_state['players'][#
    a
    ]#
prn(f"players={['A','B','C','D']}")
prn(f'turn= {turn}')


print(f"\x1b[{0};{30};{41}m")
#print(game_state['players'][turn])
