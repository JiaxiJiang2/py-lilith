
image bg room26 = "images/bg/26.png"

image r1= "images/characters/relation1.png"
image r2= "images/characters/relation2.png"
image mom1= "images/characters/others/mom1.png"

transform stand_4:
    anchor (0.5, 1.0)
    align (0.5, 1.0)
    zoom 1.2

transform stand_5:
    anchor (0.5, 1.0)
    align (0.5, 1.0)
    zoom 1

label e_path:

    play music "audio/bgm/2.mp3" fadein 3

    scene bg room26

    "先来梳理一下现在知道的事情吧。"
    "搞清楚他们几个人之间的人际关系。"

    show r1 at stand_4 with dissolve
    "大致上是这样的。"
    hide r1 with dissolve

    "但是根据圣女和公主的说法似乎是这样。"
    show r2 at stand_5 with dissolve
    "他们之中似乎有人在说谎。"
    hide r2 with dissolve

    show mom1 at stand_center with dissolve
    "宰相的母亲究竟是谁？"
    "她......他们和莉莉丝大人到底有什么关系......"
    hide mom1 with dissolve
    "说到头来，如果是莉莉丝大人的话小偷不是一下就抓出来了吗，为什么要让他们......"

    "再看看四位嫌疑人呢？"
    "说谎的人是谁？"

    menu:
        "公主":
            jump f1_path

        "宰相":
            jump g_path

        "圣女":
            jump f1_path

        "侍卫":
            jump f1_path

    return

label f1_path:
    "问题应该不出在这个人身上。"
    menu:
        "公主":
            jump f1_path

        "宰相":
            jump g_path

        "圣女":
            jump f1_path

        "侍卫":
            jump f1_path

    return

label g_path:
    $ current_avatar = "images/characters/Noah/0.png"
    "这个人身上的谜团最多。"
    "明明是半精灵却没有一点魔力......"
    $ current_avatar = None
    "......"

    "隐瞒信息最多的人是谁？"
    menu:
        "公主":
            jump f2_path

        "宰相":
            jump f2_path

        "圣女":
            jump h_path

        "侍卫":
            jump f2_path

label f2_path:
    "问题应该不出在这个人身上。"
    menu:
        "公主":
            jump f1_path

        "宰相":
            jump f2_path

        "圣女":
            jump h_path

        "侍卫":
            jump f2_path

    return

label h_path:
    $ current_avatar = "images/characters/Isaiah/0.png"
    "圣女为什么会知道魔兽在哪里？"
    "明明使用光明的力量......"
    $ current_avatar = None
    "......"

    "比较无关紧要的人是谁？"
    menu:
        "公主":
            jump i_path

        "宰相":
            jump f3_path

        "圣女":
            jump f3_path

        "侍卫":
            jump f3_path

label f3_path:
    "问题应该不出在这个人身上。"
    menu:
        "公主":
            jump i_path

        "宰相":
            jump f3_path

        "圣女":
            jump f3_path

        "侍卫":
            jump f3_path

    return

label i_path:
    $ current_avatar = "images/characters/Nova/0.png"
    "公主殿下似乎什么都没干。"
    "新晋的勇者吗......"
    $ current_avatar = None
    "......"

    "亵渎神明的人是谁？"
    menu:
        "公主":
            jump f4_path

        "宰相":
            jump f4_path

        "圣女":
            jump f4_path

        "侍卫":
            jump j_path

label f4_path:
    "问题应该不出在这个人身上。"
    menu:
        "公主":
            jump f4_path

        "宰相":
            jump f4_path

        "圣女":
            jump f4_path

        "侍卫":
            jump j_path

    return

label j_path:
    $ current_avatar = "images/characters/Asche/0.png"
    "敢质疑莉莉丝大人的无礼之徒。"
    "但他说的话确实有些道理......"
    $ current_avatar = None
    "......"

    "试着和他们当面聊聊吧。"
    "先去找谁呢？"
    menu:
        "公主":
            jump k1_path

        "宰相":
            jump k2_path

        "圣女":
            jump k3_path

        "侍卫":
            jump k4_path

label k1_path:
    scene bg room2
    "公主殿下在亡灵之间穿行。"
    show Nova at stand_center with dissolve
    "公主""抱歉我......我赶着过去......"
    "公主""明明看见她就在那边，为什么怎么都走不过去呢？"
    "公主""麻烦你们让一下可以吗？或者谁可以带我过去？"
    "公主""对，你是......"
    "公主""你可以带我去找以赛亚或者诺亚吗？"
    "这个空间似乎是由莉莉丝大人隔开的，她不允许你们在这里自由行动。"
    "公主""那我只能在这里等着吗？"
    "公主""可以让我见一下莉莉丝大人吗？我到现在都一头雾水......"
    "你先在这里等着吧，我会去帮你带话。"
    "公主""谢谢。"
    hide Nova with dissolve
    "她看起来还是很紧张。"

    "下一步去找谁呢。"
    menu:
        "宰相":
            jump k2_path

        "圣女":
            jump k3_path

        "侍卫":
            jump k4_path

        "莉莉丝大人":
            jump l_path

label k2_path:
    scene bg room2
    "宰相坐在原地发呆。"
    show Noah at stand_center with dissolve
    "宰相""哎呀，你是......"
    "宰相""专门来见我吗？"
    "我们认识吗？"
    "宰相""看来你也迷失了，和那个女神一样。"
    "宰相""你还是去找莉莉丝吧。"
    "宰相""她欠我们所有人......"
    hide Noah with dissolve
    "他起身准备到处走走。"

    "下一步去找谁呢。"
    menu:
        "公主":
            jump k1_path

        "圣女":
            jump k3_path

        "侍卫":
            jump k4_path

        "莉莉丝大人":
            jump l_path

label k3_path:
    scene bg room2
    "她依然向着莉莉丝大人在的方向祈祷。"
    show Isaiah at stand_center with dissolve
    "圣女""你......"
    "圣女""你不应该来找我吧......"
    "圣女""你也有很多问题要问莉莉丝大人不是吗？"
    "圣女""你先去找她吧，我们之后还会有很多时间。"
    "圣女""在这里最不缺的就是时间......"
    hide Isaiah with dissolve
    "她继续祈祷。"

    "下一步去找谁呢。"
    menu:
        "公主":
            jump k1_path

        "宰相":
            jump k2_path

        "侍卫":
            jump k4_path

        "莉莉丝大人":
            jump l_path

label k4_path:
    scene bg room2
    "他在四处走动，抓着一个亡灵就问路。"
    show Asche at stand_3 with dissolve
    "侍卫""喂，你，知道怎么去诺亚那边吗？"
    "侍卫""你......你应该知道怎么去那边吧。"
    "侍卫""这种事你最清楚不过了不是吗？"
    "侍卫""......"
    "侍卫""你也搞不清楚状况啊......"
    "侍卫""你去和那个无良女神谈谈，让她放我们离开。"
    hide Asche with dissolve
    "没礼貌的人类......"
    "下一步去找谁呢？"

    menu:
        "公主":
            jump k1_path

        "宰相":
            jump k2_path

        "圣女":
            jump k3_path

        "莉莉丝大人":
            jump l_path








