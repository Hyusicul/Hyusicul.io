"""
programmer : 박현
Date : 2022.11.10
File name : py3-r8 박현.py
Description: 애스터로이드 게임
"""
import turtle       #터틀문
import random       #랜덤문
import math         #함수
player_speed=2              #플레이어 스피드2
player=turtle.Turtle()
player.color("blue")        
player.shape("turtle")
player.up()
player.speed(0)
screen=player.getscreen()   #스크린상에서 움직이게하기

asteroids=[]            #행성만들기
for i in range(10):
    a=turtle.Turtle()
    a.color("red")
    a.shape("circle")
    a.up()
    a.speed(0)
    a.goto(random.randint(-300,300),random.randint(-300,300))
    asteroids.append(a)
distance = [0]*10

area=turtle.Turtle()        #경계선 800x800만들기
area.speed(0)
area.hideturtle()
area.up()
area.goto(-400,400)
area.down()
area.goto(400,400)
area.goto(400,-400)
area.goto(-400,-400)
area.goto(-400,400)

def turnleft():
	player.left(30)     # 왼쪽으로 30도 회전한다.

def turnright():
	player.right(30)    # 오른쪽으로 30도 회전한다.
def up():
    global player_speed
    player_speed += 1

def down():
    global player_speed
    player_speed -= 1
 
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.listen()

def play():
	player.forward(2)   # 2픽셀 전진
	screen.ontimer(play, 10)    # 10ms가 지나면 play()를 다시 호출
screen.ontimer(play, 10)

while True:             
    size= len(asteroids)
    ai_hide =asteroids

    for i in range(size):               #행성 나오는 위치 설정하기
        asteroids[i].fd(random.randint(3,10))
        asteroids[i].lt(random.randint(0,359))
        if asteroids[i].xcor() >= 400 or  asteroids[i].ycor() >= 400:
            asteroids[i].goto(-400, random.randint(-400,400))
        elif asteroids[i].xcor() <= -400 or asteroids[i].ycor()<= -400:
            asteroids[i].goto(-400, random.randint(-400,400))

    if player.xcor() >= 300:            #플레이어가 밖으로 나가면 반대편으로 나오게 하기
        player.goto(player.xcor() - 800,player.ycor())
    elif player.xcor() <=-400:
        player.goto(player.xcor() + 800,player.ycor())
    if player.ycor() >= 400:
        player.goto(player.xcor(), player.ycor() - 800)
    elif player.ycor() <=-400:
        player.goto(player.xcor(), player.ycor() + 800)
    player.fd(player_speed)

    for i in range(size):       #distance를 이용하여 플레이어와 행성이 부딪히면 사라지게 하기
        distance[i] = math.sqrt(math.pow(player.xcor()-asteroids[i].xcor(),2)+math.pow(player.ycor()-asteroids[i].ycor(),2))
        if distance[i]<=20:
            asteroids[i].hideturtle()
            player.write("kill!", font=('Times New Roman',10,'bold'))
            del asteroids[i]
            del distance[i]
            break
        
        





                                
