import pygame,random,time
import _pickle as pickle
import threading,json
import requests
# Intialize the pygame
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
a=['black','+4']
deck={
'red':["['red','0'].png","['red','1'].png","['red','2'].png","['red','3'].png","['red','4'].png","['red','5'].png","['red','6'].png","['red','7'].png","['red','8'].png","['red','9'].png","['red','o'].png","['red','r'].png","['red','+2'].png","['red','+4'].png","['red','c'].png"]
,'yellow':["['yellow','0'].png","['yellow','1'].png","['yellow','2'].png","['yellow','3'].png","['yellow','4'].png","['yellow','5'].png","['yellow','6'].png","['yellow','7'].png","['yellow','8'].png","['yellow','9'].png","['yellow','o'].png","['yellow','r'].png","['yellow','+2'].png","['yellow','+4'].png","['yellow','c'].png"]
,'green':["['green','0'].png","['green','1'].png","['green','2'].png","['green','3'].png","['green','4'].png","['green','5'].png","['green','6'].png","['green','7'].png","['green','8'].png","['green','9'].png","['green','o'].png","['green','r'].png","['green','+2'].png","['green','+4'].png","['green','c'].png"]
,'blue':["['blue','0'].png","['blue','1'].png","['blue','2'].png","['blue','3'].png","['blue','4'].png","['blue','5'].png","['blue','6'].png","['blue','7'].png","['blue','8'].png","['blue','9'].png","['blue','o'].png","['blue','r'].png","['blue','+2'].png","['blue','+4'].png","['blue','c'].png"]
,'black':["['black','+4'].png","['black','c'].png"]}
ldeck={'red':[]
       ,'yellow':[]
       ,'green':[]
       ,'blue':[]
       ,'black':[]
       }
for c in ['red','yellow','green','black','blue']:
    for i in range(len(deck[c])): 
        ldeck[c].append(pygame.image.load(deck[c][i]))
        
# create the screen

screen = pygame.display.set_mode((1200,800), pygame.RESIZABLE)#,pygame.FULLSCREEN)#(1024,768))
print(pygame.display.Info())
pygame.display.set_caption("GU NO")
'''
tital_icon=pygame.image.load('uno back.png)
pygame.display.set_icon(tital_icon)
bg=pygame.image.load('uno back.png)
screen.blit(bg,(0,0))'''
hand_cards_list=[]
bg=[pygame.image.load('bg 0.png'),
    pygame.image.load('bg 1.png'),
    pygame.image.load('bg 1t.png'),
    pygame.image.load('bg 0t.png')
    ]
game_states={}
turnflag=0
num_of_players=0
TURN=False
guno=pygame.image.load('GUNO.png')
gunot=pygame.image.load('GUNOt.png')
guno_flag=False
deckpile=pygame.image.load('draw.png')
deckpilecards=pygame.image.load('drawdeckcards.png')
num_deck_card=64
pile_cards=pygame.image.load('pilecards.png')
color_selector=pygame.image.load('color.png')
pile_cards_number=64
current=['green', '1']
clickedcard=[-1,[]]
clickflag=0
action=[]
draw_break=False
choose_color_flag=False
color_pt=(0,0)
######CLIENT####################################################


pos='bhatt'


def uno():
    global TURN,current,pos,action,hand_cards_list,draw_break
    global guno_flag,turnflag,pile_cards_number,num_deck_card,num_of_players,game_states
    while True:
        source =json.loads( requests.get('''http://127.0.0.1:8000/bhatt_startgameview''').text)#.replace("\\",'')
        #print(source['text'])
        game_state=json.loads(source['text'].replace("\\",''))
        game_states=game_state
        #print(yo)
        current=game_state['current']
        #print('current=',current,'}}___UNO')
        hand_cards_list=game_state[str(pos)]['hand_cards']
        draw_break=game_state['draw_break']
        guno_flag=game_state[pos]['guno']
        turnflag=game_state['turnflag']
        num_deck_card=game_state['num_deck_card']
        pile_cards_number=game_state['pile']
        num_of_players=game_state['num_of_players']

        #print(pos,game_state[str(pos)]['turn'])
        if game_state[str(pos)]['turn']=='true':
            post={'action':('',''),'color':'','uno':False,'username':'bhatt'}
            TURN=True
            #print("post['action']=",action)
            while True:
                if action!=[]:
                    #'''
                    #if action[1][1]=='+4':
                        #input("post['action']=",action[1])#'''
                    post['action']=action[1]
                    print("uno_post['action']=",action)
                    
                    post['color']=action[1][0]
                    post['uno']=guno_flag
                    action=[]
                    TURN=False
                    #guno_flag=False
                    break
                #time.sleep(0.2)
            

            #send(post)
            
            requests.get('''http://127.0.0.1:8000/my'''+json.dumps(post))#.replace("\\",'')
        
            #a=int(client.recv(5).decode(str_format))
            #print(pickle.loads(client.recv(2048)))
def sleep():
    time.sleep(5)
    print('uthgya')
def socket():
    thread=threading.Thread(target=uno)
    thread.daemon=True
    thread.start()
socket()
##########################################################
def clickcheck(c=''):
    global clickflag
    x=pygame.mouse.get_pressed()
    '''
    if c!='':
        print(x)'''
    if (x==(1,0,0)) and clickflag==0:
        clickflag=2
        #print(c)
        return True
    elif clickflag>0 and clickflag<=2:
        if (x==(1,0,0)) :
            clickflag=2
        clickflag-=1
        
def clickchecks(c=''):
    #print('in')
    for event in pygame.event.get(): 
        if event.type == pygame.MOUSEBUTTONDOWN:
            return True
def hand_cards():
    global hand_cards_list,clickedcard,choose_color_flag
    xalpha=0
    if hand_cards_list!=[]:
        a=hand_cards_list
        
        l=len(a)
        spacing=round(1200/l)
        if spacing>110:
            spacing=110
            xalpha=int(600-(l/2)*110)
        for i in range(l):
            x0=(spacing*i)+xalpha
            if i==clickedcard[0]:#clicked card logic
                y0=651-90
            else:
                y0=651
                
                    
            x1=x0+110
            y1=y0+143
            color=a[i][0]
            actn=a[i][1]
            if actn=='o':
                actn=10
            elif actn=='r':
                actn=11
            elif actn=='+2':
                actn=12
            elif actn=='+4':
                actn=0
            elif actn=='c':
                actn=1
            else:
                try:
                    actn=int(actn)
                except:
                    print('hands_cards__hands_cards_list=',a)
                    
            screen.blit(ldeck[color][actn],(x0,y0))
            x,y=pygame.mouse.get_pos()
            '''
            if clickcheck('i')==True:
                print(clickedcard[1])
                print((x>x0 and y>y0) , (x<x1 and y<y1) , (x<spacing*(i+1)))
                print(('x>x0',x>x0 ,'y>y0', y>y0) , ('\nx<x1',x<x1 ,'y<y1', y<y1) )
                print(x0,y0)
                print(x,y)
                print(x1,y1)#'''
            
   
            if (x>x0 and y>y0) and (x<x1 and y<y1) and (x<(spacing*(i+1))+xalpha) :
                
                if clickcheck()==True:
                    
                    #print('lol')
                    if clickedcard[0]==i:
                        if a[i][1]=='+4':
                            choose_color_flag=False
                        if a[i][1]=='c':
                            choose_color_flag=False
                            print('hand_cards__yo',a[i])
                        clickedcard=[-1,[]]
                    else:
                        clickedcard[0]=i
                        clickedcard[1]=a[i]
def choose_color():
    global color_pt,choose_color_flag,clickedcard,action
    selected_color=''
    if choose_color_flag==True:
        #print('\n\n\n oo bhaimaaro')
        screen.blit(color_selector,color_pt)
        x,y=pygame.mouse.get_pos()
        x0,y0=color_pt
        x1,y1=color_pt[0]+110,color_pt[1]+143
        xp,yp=color_pt[0]+53,color_pt[1]+69
        if (x>x0 and y>y0) and (x<x1 and y<y1):
        
            a=clickchecks()
            if a==True:            
                if x<xp and y<yp:
                    selected_color='red'
                if x>xp and y<yp:
                    selected_color='yellow'
                if x>xp and y>yp:
                    selected_color='blue'
                if x<xp and y>yp:
                    selected_color='green'
                action=[-1,[selected_color,clickedcard[1][1]]]
                choose_color_flag=False
                clickedcard=[-1,[]]
                #print('\n\n\n\n\naction sent\n\n',action)
            '''
            else:
                print("\n\n\n\n\clickcheck('choose')=False \n\n")'''
        
def pile():
    global action,pile_cards_number,current,clickedcard,color_pt,choose_color_flag
    x0=552
    y0=530
    xm=0
    ym=0
    if current!=['',''] :
        for i in range(pile_cards_number):
            screen.blit(pile_cards,(x0+xm,y0+ym))
            ym-=2
        
        actn=current[1]
        if actn=='o':
            actn=10
        elif actn=='r':
            actn=11
        elif actn=='+2':
            actn=12
        elif actn=='+4':
            actn=13
        elif actn=='c':
            actn=14
        else:
            try:
                actn=int(actn)
            except Exception as e:
                print('1)pile_error=',actn,current,str(e))
            
        try:
        
            screen.blit(ldeck[current[0]][actn],(x0+xm,y0+ym-143))
        except Exception as e:
            print('pile_error=',actn,current,str(e))
        color_pt=(x0+xm+110,y0+ym-143)##############################
        
        
        x1=x0+110
        y1=y0
        y0=y0+ym-147
    else:
        x0,y0=548,376
        x1,y1=674,524

    
    x,y=pygame.mouse.get_pos()
    '''
    if clickcheck()==True:
        print(x0,y0)
        print(x,y)
        print(x1,y1)'''
    if (x>x0 and y>y0) and (x<x1 and y<y1) and TURN==True and clickedcard!=[-1, []]:
        if clickcheck()==True:
            print('pile=',clickedcard)
            try:
                if draw_break==False:
                    if current[1]=='+4'and ((current[1]==clickedcard[1][1])):
                        choose_color_flag=True
                        
                        print('action=',action)
                    if current[1]=='+2' and ((current[1]==clickedcard[1][1])):
                        action=clickedcard
                        print('action=',action)
                    '''
                    elif current[1]!='+2' and (clickedcard[1][0]==current[0] or clickedcard[1][1]==current[1] or current==['','']):
                        action=clickedcard
                        print('action=',action)'''
                
                elif clickedcard[1][1]=='+4':
                    choose_color_flag=True
                elif clickedcard[1][1]=='c':
                    choose_color_flag=True
                    
                    print('\n\n\n\ninnnnnnnn\n\n\n\n')
                    
                elif clickedcard!=[-1,[]] and ((clickedcard[1][0]==current[0] or clickedcard[1][1]==current[1] or current==['',''])) :
                        action=clickedcard
                        print('action=',action)
                        clickedcard=[-1,[]]
                else:
                    print(clickedcard)
            except Exception as e:
                print('pile__clickedcard=',clickedcard,e)
                
def drawer():
    global num_deck_card,action    
    x0=400
    y0=390
    
    xm=0
    ym=0
    
    for i in range(num_deck_card):
        if i%3==0:
            screen.blit(deckpilecards,(x0+xm,y0+ym))
            xm+=1
            ym-=1
    
    screen.blit(deckpile,(x0+xm,y0+ym))
    x1=x0+xm+110
    y1=y0+ym+119
    x,y=pygame.mouse.get_pos()
    if (x>x0 and y>y0) and (x<x1 and y<y1) and TURN==True :
        if clickcheck()==True:
            action=[-1,['draw']]
            print('draw=',clickedcard)
    
    
                    
def gunoset():
    global guno_flag
    x0=772
    y0=421
    x1,y1=x0+47,y0+47
    if guno_flag==False:
        screen.blit(guno,(x0,y0))
    else:
        screen.blit(gunot,(x0,y0))
    x,y=pygame.mouse.get_pos()
    if (x>x0 and y>y0) and (x<x1 and y<y1):
        if clickcheck()==True:
            who_say_gu_no()
            print('guno button')
            if guno_flag==False:
                guno_flag=True
            else:
                guno_flag=False
                
            
def backgroung():
    global bg,turnflag,TURN,pos
    #print(turnflag, TURN)
    if turnflag==0 and TURN==True:
        screen.blit(bg[3],(0,0))
    if turnflag==1 and TURN==True:
        screen.blit(bg[2],(0,0))
    if turnflag==0 and TURN==False:
        screen.blit(bg[0],(0,0))
    if turnflag==1 and TURN==False:
        screen.blit(bg[1],(0,0))
def who_say_gu_no():
    #print('inside')
    global game_states,num_of_players,pos
    #print(pos,type(pos))
    a=[]
    b=[]#[['turn','no of cards']]
    #print(pos,num_of_players)
    for i in range(num_of_players):
        if str(i) !=pos:
            #print('inside --')
            a.append(game_states['players'][i])
    for i in a:
        s=[]
        #print(i)
        s.append(game_states[str(i)]['turn'])
        s.append(len(game_states[str(i)]['hand_cards']))
        s.append(game_states[str(i)]['guno'])
        b.append(s)
    print(b)
    
    
def yo ():
    screen.blit(ldeck['black'][1],(random.randint(0,1000),random.randint(100,1000)))


###################################################################################

pygame.init()
running=True
while running:#main loop
    screen.fill((100,100,0))#it is leare one
    backgroung()
    #screen.blit(ldeck['black'][1],(random.randint(0,1000),random.randint(100,1000)))
    #yo()
    gunoset()

    hand_cards()
    pile()
    drawer()
    choose_color()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            #exit()
    #print(pygame.mouse.get_pos())#give mouse position
    #print(pygame.mouse.get_pressed())#show clicks
    #time.sleep(.03)
    #print(clickedcard[1])
                    
    pygame.display.update()
