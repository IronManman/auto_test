#一个回合制游戏，每个角色都有hp和power，hp代表血量，
#power代表攻击力，hp初始值为1000，power初始值为200

def game():
    enemy_hp = 1000
    enemy_power = 200
    my_hp = 1000
    my_power = 15
    while True:
        my_hp=my_hp-enemy_power
        enemy_hp=enemy_hp-my_power

        if my_hp<=0:
            print("敌人获胜")
            break
        elif enemy_hp<=0:
            print("我获胜了")
            break

game()