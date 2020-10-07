from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
import json,random
from . import forms
from . import models
def register(request):
    f1=forms.singininfo()
    if request.method == "POST":
        f1=forms.singininfo(data=request.POST)
        if f1.is_valid():
            print("\nPOST IS VALID\n")
            user = f1.save()
            user.set_password(user.password)
            user.save()
            a=models.Userinfo()
            a.user=user
            a.save()
            return HttpResponse("registered")#redirect("/")
    return render(request,"singin.html",{"f1":f1})
def login(request,username,password):
    #print('\n',username,password)
    urs=list(models.User.objects.filter(username=username))
    print(urs)
    if urs!=[]:
        user = authenticate(username=username,password=password)
        if user:
            return JsonResponse({"text":username})
        else:
            return JsonResponse({"text":"wpassword"})
    else:
        print('---',urs)
        return JsonResponse({"text":"wusername"})

def log_in(request):
    log=forms.loginform()
    if request.method == "POST":#
        log=forms.loginform(request.POST)
        if log.is_valid():
            print("\n\nlog.is_valid()\n\n")
            user = authenticate(username=log.cleaned_data["username"],password=log.cleaned_data["password"])
            if user:
                print("\n\nif user\n\n")
                if user.is_active:
                    print("\n\nuser.is_active\n\n")
                    login(request,user)
                    return redirect("/")#HttpResponseRedirect(reverse("index"))
                else:
                    HttpResponse("account is not active")
            else:
                print("user is not correct")
                return HttpResponse("details r not correct\n"+"username="+str(log.cleaned_data["username"])+"\npassword"+str(log.cleaned_data["password"]))

        else:
            print("login is not valid")
            return HttpResponse("account is not active")

    return render(request,"login.html",{"f1":log})

def create_room(request,username):
    print("\n\n",username)
    roomz=list(models.rooms.objects.filter(host=username))

    if roomz!=[]:
        roomz=roomz[0].delete()


    roomz=models.rooms(host=str(username),
    name=username+"'s_room",
    gamestart=False
    )
    roomz.save()
    game=models.game_state_op(room=roomz)
    game.save()
    a=models.Userinfo.objects.filter(user__username=username)[0]
    a.room=roomz
    a.save()
    return JsonResponse({"text":"done"})
    #location = UserLocation.objects.get_or_create(user=request.user)[0]
    #location.lat = request.POST.get("LAT") #lat is a field in the model see above
    #location.lon = request.POST.get("LON") #lon is a field in the model see above
    #location.point = lat (some operation) lon
    #location.save()
def wating_room(request,host):
    a=list(models.rooms.objects.filter(host=host))
    if a!=[]:
        a=a[0]
    #print(f'\n\n\n\n\na.gamestart={a.gamestart}, host={host}{a.players.all()}\n\n\n\n\n\n\n\n')
        if  a.gamestart==True:
            #print('\n\n\n\n\nwaithing\n\n\n\n\n\n\n\n')
            return JsonResponse({"text":"game start"})
        else:
            response={"text":"waiting...","players":[]}
            for i in a.players.all():
                response["players"].append(i.user.username)
            #print("yo",a.players.all(),username)
            return JsonResponse(response)
    #a.gamestart.game_state_op()???????????????????????
    else:
        return JsonResponse({"text":"waiting...","players":[]})
def update_status(request):
    return JsonResponse({'text':''})
def join_room(request,username,host):
    roomz=list(models.rooms.objects.filter(host=host))
    if roomz!=[]:
        plr=roomz[0].players.all()
        rplr=[]
        for it in plr:
            rplr.append(it.user.username)
        print(rplr)
        if roomz[0].gamestart==True and username not in rplr :
            return JsonResponse({"text":"Host Started Game For This Room"})
        else:
            if len(plr)<=6 or username in rplr :
                roomz=roomz[0]
                a=models.Userinfo.objects.filter(user__username=username)[0]
                a.room=roomz
                a.save()
                return JsonResponse({"text":"join done"})
            else:
                return JsonResponse({"text":"Players Are Full"})
    else:
        return JsonResponse({"text":"Host Id Is Incorrect"})

def start_game(request,host):
    a=models.rooms.objects.filter(host=host)[0]
    #a.save()
    stad=a.gamestate.game_state_db.replace("'",'')

    game_state=json.loads(stad)
    game_state["current"]=["",""]
    load=json.loads(a.global_variabl.replace("'",''))
    load['username']=host

    tem=load['deck']
    print('\ntem=',tem,type(tem),'\n')
    random.shuffle(tem)
    load['shuffel_deck']=tem
    game_state["num_deck_card"]=len(load['shuffel_deck'])
    game_state["draw_break"]=True
    game_state["turnflag"]=0
    game_state["pile"]=0

    plyrs=[]
    for i in a.players.all():
        plyrs.append(i.user.username)
    game_state["num_of_players"]=len(plyrs)
    game_state["players"]=plyrs
    for player_index in plyrs:
        game_state[player_index] = {'turn':'false','guno':False,'name':player_index,'drawed':0,
                                         'hand_cards':load['shuffel_deck'][:5]}
        load['shuffel_deck']=load['shuffel_deck'][5:]
    try:
        game_state[plyrs[0]]['turn']='true'
    except:
        print('\n\nERROR=',plyrs)
    load['draw_num']=1
    load['winner']=''
    load['turn_num']=0
    load['pile']=0
    load['turnflag']=0


    #a.global_variabl['shuffel_deck']
    a.gamestart=True
    a.gamestate.game_state_db=json.dumps(game_state)
    a.global_variabl=json.dumps(load)
    a.gamestate.save()
    a.save()


    a=models.rooms.objects.filter(host=host)[0]

    print('game_state=',a.gamestate.game_state_db,a.global_variabl)
    #return JsonResponse(game_state)
    return JsonResponse({'game_state':str(a.gamestate.game_state_db),'a.global_variabl':str(a.global_variabl),'a.gamestart':a.gamestart})
def leave_waiting(request,username,host):
    if username==host:
        print('leave_waiting')
        roomz=models.rooms.objects.filter(host=host)[0].delete()

    a=models.Userinfo.objects.filter(user__username=username)[0]
    a.room=None
    a.save()

    return JsonResponse({"text":"wating leave"})

def leave_game(request,username,host):
    a=models.rooms.objects.filter(host=host)[0]
    stad=a.gamestate.game_state_db.replace("'",'')
    game_state=json.loads(stad)
    try:
        game_state['players'].remove(username)
    except:
        return JsonResponse({">":''})
    if len(game_state['players'])!=1 and username!=host:
        global_v=json.loads(a.global_variabl.replace("'",''))
        #a1,y=str(game_state),str(global_v)
        global_v['shuffel_deck']=global_v['shuffel_deck']+game_state[username]['hand_cards']
        game_state['num_deck_card']=len(global_v['shuffel_deck'])##############################
        del game_state[username]
        #global_v['turn_num']+=1
        """
        #set turn when delet a player
        """

        num_players=len(game_state['players'])
        print('num_players=',num_players)
        turn=game_state['players'][
        global_v['turn_num']
        ]
        '''
        if global_v['turnflag']==0:
            turn=game_state['players'][
            global_v['turn_num']+1
            ]
        else:
            turn=game_state['players'][#
            global_v['turn_num']-1
            ]#'''
        game_state[turn]['turn']='true'




        a.gamestate.game_state_db=json.dumps(game_state)
        a.global_variabl=json.dumps(global_v)
        #sendall(game_state)
        a.gamestate.save()
        a.save()
        a=models.Userinfo.objects.filter(user__username=username)[0]
        a.room=None
        a.save()
    else:
        roomz=models.rooms.objects.filter(host=host)[0].delete()

    return JsonResponse({">":''})#(a1,y),
    #"##############################text":game_state,'--------global_v':global_v})
    #a.gamestate=
def mod(n,m):
    a=n/m
    c=(a-int(a))*m
    return round(c)
def myturn(request,responce):
    print('\nresponce=',responce,'\n')
    #responce={'action': ['red', '2'], 'color': 'red', 'uno': True, 'username':bhatt}
    responce=json.loads(responce.replace("'",''))
    print(responce)
    try:
        a=models.rooms.objects.filter(host=responce['username'])[0]
    except:
        '2 player turn and host is removed'
        print(f'\n\n\n\n\n\n\n\n\n\n\nERROR{responce}\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        return JsonResponse({'text':'a.gamestate.game_state_db'})
    stad=a.gamestate.game_state_db.replace("'",'')
    game_state=json.loads(stad)
    print('\ngame_state=',game_state,'\n')
    action=responce['action']
    turn=''
    global_v=json.loads(a.global_variabl.replace("'",''))
    for i in game_state['players']:
        if game_state[i]['turn']=='true':
            turn=i
            break
    ####################################3setting variables^^^^
    #game_state['turn_flag']=turnflag
    game_state[str(turn)]['turn']='false'
    #game_state[str(turn)]['turn']='false'
    game_state[str(turn)]['guno']=responce['uno']
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #---------get suffel dec if main deck is low
    if len(global_v['shuffel_deck'])<=8:
        tem_deck=[]
        tem_deck+=global_v['shuffel_deck']
        for tem in game_state['players']:
            tem_deck+=game_state[str(tem)]['hand_cards']
            #print('\n\n',game_state[str(turn)]['hand_cards'])
        global_v['shuffel_deck']=[]
        if game_state['current'][1]=='+4'  :
            tem_deck.append(['black','+4'])
        elif game_state['current'][1]=='c'  :
            tem_deck.append(['black','c'])
        else:
            tem_deck+=[game_state['current']]
        b4=0
        bc=0
        for i in tem_deck :
            if i==['black','+4']:
                b4+=1
            if i==['black','c']:
                bc+=1
        print(tem_deck)
        for i in global_v['deck']:
            if i in tem_deck:
                pass
            else:
                global_v['shuffel_deck']+=[i]


        for i in range(2-b4):########
            global_v['shuffel_deck']+=[['black','+4']]
        for i in range(2-bc):########
            global_v['shuffel_deck']+=[['black','c']]
        random.shuffle(global_v['shuffel_deck'])
        #global_v['shuffel_deck']=shuffel(global_v['shuffel_deck'])
        global_v['pile']=0
        game_state['num_deck_card']=len(global_v['shuffel_deck'])
    print("global_v['shuffel_deck']=",global_v['shuffel_deck'],'\n\n')
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    #----not uno
    handnum=len(game_state[str(turn)]['hand_cards'])
    guno=game_state[str(turn)]['guno']
    if (
    (handnum==2 and guno==False) or
    (handnum>2 and guno==True)      ) and action!=['draw'] :
        print('''\n if (
        (handnum==2 and guno==False) or
        (handnum>2 and guno==True)      ) and action!=['draw'] :''',guno,handnum)

        #game_state[str(turn)]['hand_cards']=game_state[str(turn)]['hand_cards']+global_v['shuffel_deck'][:1]
        #global_v['shuffel_deck']=global_v['shuffel_deck'][1:]
        #game_state[str(turn)]['guno']=False
        action=['draw']
        global_v['draw_num']=1



    #^^^^^^^^^^^^^
    #--winner logic
    winner=[]
    if handnum==1 and responce['uno']==True and action!=['draw'] :
        print('\n\n##################\nwinner\n##################\n\n')
        #input('----------------------------------------------------')
        global_v['winner']=str(turn)
        a.gamestart=False
    #reset game_state['drawed']
    for plr in game_state['players']:
        game_state[plr]['drawed']=0
    #--action actioncution------------
    if action==['draw']:
        print("\nif action==['draw']:",action)
        game_state[str(turn)]['guno']=False
        #>draw action
        game_state['draw_break']=True
        print(  global_v['draw_num'],
                game_state[str(turn)]['hand_cards'],
                'draw=',global_v['shuffel_deck'][:global_v['draw_num']],
              '\n',
              game_state[str(turn)]['hand_cards']+global_v['shuffel_deck'][:global_v['draw_num']])

        game_state[str(turn)]['hand_cards']=game_state[str(turn)]['hand_cards']+global_v['shuffel_deck'][:global_v['draw_num']]
        global_v['shuffel_deck']=global_v['shuffel_deck'][global_v['draw_num']:]
        print(len(global_v['shuffel_deck']))
        #it add drawed
        game_state[str(turn)]['drawed']=global_v['draw_num']
        global_v['draw_num']=1

        print(game_state)
    else:
        #it reset drawed
        global_v['pile']=global_v['pile']+1
        #>action of cards
        print('\n\naction=',action,global_v['pile'])#type(action),game_state)
        try:
            if action[1]=='+4':
                game_state[str(turn)]['hand_cards'].remove(['black','+4'])
            elif action[1]=='c':
                game_state[str(turn)]['hand_cards'].remove(['black','c'])
            else:
                game_state[str(turn)]['hand_cards'].remove(action)
        except :
            print('str(turn)=',str(turn),'\naction=',action,
                  "\ngame_state[str(turn)]['hand_cards']=",
                  game_state[str(turn)]['hand_cards'])
            #input()
        print('\n\n\nelse')

        if action[1]=='+2':
            print('\n\n\n1')
            if global_v['draw_num'] ==1:
                global_v['draw_num']+=1
            else:
                global_v['draw_num']+=2
            game_state['draw_break']=False
            game_state['current']=action
        elif action[1]=='+4':
            print('2')
            if global_v['draw_num'] ==1:
                global_v['draw_num']+=3
            else:
                global_v['draw_num']+=4
            game_state['draw_break']=False
            game_state['current'][1]='+4'
            game_state['current'][0]=responce['color']
            print('+4',global_v['draw_num'])


        elif action[1]=='r':
            #print('INSIDE R \n\nstr(turn)=',str(turn),'\naction=',action,f"\n1 global_v['turn_num']={global_v['turn_num']}",
            #f"\n1 global_v['turnflag']={global_v['turnflag']}")
            global_v['turnflag']=1-(1*global_v['turnflag'])
            #print("\n2 global_v['turnflag']=",global_v['turnflag'])
            game_state['current']=action
            #print(f"\n1  global_v['pt']={global_v['pt']}")
            #print(f"\n2  global_v['pt']={global_v['pt']}")
            game_state['turnflag']=global_v['turnflag']

        elif action[1]=='c':
            print('4')
            print(action,responce['color'])
            game_state['current'][1]='c'
            game_state['current'][0]=responce['color']
        elif action[1]=='o':
            #print('5')
            game_state['current']=action
            if global_v['turnflag']==0:
                if global_v['turn_num']==num_players:
                    global_v['turn_num']=0
                else:
                    global_v['turn_num']+=1
            else:
                if global_v['turn_num']==0:
                    global_v['turn_num']=num_players
                else:
                    global_v['turn_num']-=1
        else:

            game_state['current']=action
            #print("----11\ngame_state['current']=",game_state['current'],action,'\n')
    num_players=len(game_state['players'])-1
    if global_v['turnflag']==0:
        if global_v['turn_num']==num_players:
            global_v['turn_num']=0
        else:
            global_v['turn_num']+=1
    else:
        if global_v['turn_num']==0:
            global_v['turn_num']=num_players
        else:
            global_v['turn_num']-=1
    #print(f"\n2 global_v['turn_num']={global_v['turn_num']}")
    #print('----\n1 turn=',turn,'\n')
    turn=game_state['players'][global_v['turn_num']]

    #global_v['turn_num']+=1

    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #-turn rotation flag---------


    #print('\n2  turn=',turn,'\n')
    game_state[str(turn)]['turn']='true'
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print('\n\ngame_state=',game_state)
    game_state['num_deck_card']=len(global_v['shuffel_deck'])
    game_state['pile']=global_v['pile']
    a.gamestate.game_state_db=json.dumps(game_state)
    a.global_variabl=json.dumps(global_v)
    #sendall(game_state)
    a.gamestate.save()
    a.save()
    print("----22\ngame_state['current']=",game_state['current'],'\n')
    return JsonResponse({'text':a.gamestate.game_state_db})

def is_joined(request,username):
    usr=list(models.Userinfo.objects.filter(user__username=username))
    if usr!=[]:
        print('\n\n\n\n',usr,'\n\n\n\n')
        usr=usr[0]
        print('\n\n\n\n',usr.room,'\n\n\n\n')
        if usr.room !=None:
            print('\n\n\n\n',usr.room.host,'\n\n\n\n')
            return JsonResponse({"text":str(usr.room.host)})
        else:
            return JsonResponse({"text":'False'})
    else:
        return JsonResponse({"text":'False'})


def game_state_view(request,username):
    try:
        a=models.rooms.objects.filter(host=username)[0]
        global_v=json.loads(a.global_variabl.replace("'",''))
        if global_v['winner']!='':
            return JsonResponse({'text':a.gamestate.game_state_db,'winner':global_v['winner']})
        else:
            return JsonResponse({'text':a.gamestate.game_state_db,'winner':''})
    except:
        print('error')
        #a='{"current": ["", ""], "num_deck_card": 56, "draw_break": true, "turn_flag": 0, "pile": 0, "num_of_players": 2, "turnflag": 0, "players": []'
        return JsonResponse({'text':'room close','winner':'winner'})


# Create your views here.
