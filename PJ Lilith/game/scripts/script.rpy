image bg room0 = "images/bg/b.png"
image bg room1 = "images/bg/1.png"
image bg room2 = "images/bg/2.png"

init python:
    current_avatar = None

transform stand_center:
    anchor (0.5, 1.0)     # 锚点在底部中央
    align (0.5, 1.0)      # 对齐到底部中央（屏幕底）
    zoom 0.50       # 缩放50%，按需调整
image lilith0 = "images/characters/lilith/03.png"

init:
    transform shake:
        linear 0.05 xoffset -10
        linear 0.05 xoffset 10
        linear 0.05 xoffset -10
        linear 0.05 xoffset 10
        linear 0.05 xoffset 0


#主菜单
define config.main_menu_music = "audio/bgm/1.mp3" 

#游戏开始第一幕
label start:

    scene bg room0
    "游玩前温馨提示"
    "本作为个人oc小游戏"
    "充满gl、bl、骨科等个人xp展现"
    "以及本人超绝小学生文笔"
    "没什么意见的话，游戏就开始了"

    play music "audio/bgm/0.mp3" fadein 3

    scene bg room1
    
    "——序章——"
    "亡灵们很躁动，似乎有不速之客闯入这里。"
    "大家都朝有光的地方前进。"

    show lilith0 at stand_center with dissolve
    "莉莉丝""这些闯入者需要受到惩罚。"
    "莉莉丝""请大家前往审判庭。"
    hide lilith0 with dissolve

    "过去多少年了，这里再次有了生者的气息。"
    "新来的亡灵们很兴奋，想看看是否是他们认识的人。"
    "大部分亡灵都很沉默，他们早已忘记过去的事，也对现在生者的世界没有一丝兴趣。"
    "我只是低头跟着他们前进。"
    "莉莉丝大人很生气，生者曾从这里带走了一样东西，现在是时候让他们偿还了。"

    scene bg room2
    "我从来没见过这么多亡灵集中在一起。"
    "我不敢想有那么多死者遗失了过去。"
    "我顺着他们的目光看去，找到了被包围的四位生者。"

    show lilith0 at stand_center with dissolve
    "莉莉丝""我并非是那种蛮不讲理的神明，但你们确实从我这里拿走过什么。"
    "莉莉丝""只要让我找到主犯，你们就可以平安无事地回去。"
    "莉莉丝""嫌疑人啊，你们可以自由地为自己发言。"
    hide lilith0 with dissolve

    "我向他们靠近，要先听听谁的发言呢。"

#选项跳转
    menu:
        "公主":
            jump a_path

        "宰相":
            jump b_path

        "圣女":
            jump c_path

        "侍卫":
            jump d_path

    return
