image bg room30 = "images/bg/30.png"
image bg room31 = "images/bg/31.png"

image mom2 = "images/characters/others/mom2.png"
image me = "images/characters/others/me.png"

label l1_path:
    scene bg room30

    "候鸟向着家的方向飞行。"
    "越过山头，山脚是宁静的村庄。"

    "小酒馆的老板娘正在为晚上的酒局备货。"

    scene bg room31
    show mom2 at stand_center with dissolve
    "薇薇安""啊，你是......"
    "薇薇安""迷路的客人吗？"
    hide mom2 with dissolve

    show me at stand_center with dissolve
    "我""......"
    hide me with dissolve
    "不仅仅在王国的边境，也在生界边缘......"
    "魔兽，亡灵，都是这里的常客。"
    "和会伤害人类的魔兽不同，亡灵只是静静地路过前往下面的世界，人们甚至很难注意到亡灵的存在。"
    "“迷路的客人”，亡灵都是死后迷失了的灵魂，所以他们如此称呼我们。"

    show mom2 at stand_center with dissolve
    "薇薇安""有什么需要的吗，还是只是过来坐坐？"
    hide mom2 with dissolve
    
    show me at stand_center with dissolve
    "我""莉莉丝大人让我来和你聊聊......"
    hide me with dissolve

    show mom2 at stand_center with dissolve
    "薇薇安""女神大人吗......"
    "薇薇安""她想知道些什么呢？话说你一点也不惊讶啊，一般人类根本看不见亡灵更别说和你们交流了。"
    hide mom2 with dissolve

    show me at stand_center with dissolve
    "我""你看起来经常和亡灵打交道，就说说理由吧。"
    hide me with dissolve
    "女人沉思了片刻。"
    
    show mom2 at stand_center with dissolve
    "薇薇安""如果是莉莉丝大人想知道的话......"
    "薇薇安""我的父亲是一名强大的边境骑士，被莉莉丝大人祝福的，一往无前的骑士。"
    "薇薇安""虽然他本人极其低调，但是村子里还是流传着不少降临在他身上的奇迹的传闻。"
    "薇薇安""“莉莉丝的勇者”，大家都这样悄悄喊他。"
    "薇薇安""因为有这样的父亲，所以我也有一些神奇的力量吧。"
    "薇薇安""虽然不会魔法，但是我不仅很擅长和人类打交道，和你们也经常聊天哦！"
    hide mom2 with dissolve

    "为了显得自己很能干，女人撸起了袖子。"

    show mom2 at stand_center with dissolve
    "薇薇安""但你们之前都只是在这里徘徊，和你们聊天也只会说自己不知道要干什么。"
    "薇薇安""不知道去哪，也不知道自己是谁。"
    "薇薇安""好像都只是路过，放着不管过一会儿就消失了......"
    "薇薇安""你是第一个，有目的性前来的......"
    "薇薇安""你知道你是谁吗？"
    hide mom2 with dissolve

    show me at stand_center with dissolve
    "我""......"
    hide me with dissolve

    show mom2 at stand_center with dissolve
    "薇薇安""......没关系，等你不迷茫的时候，就会前往幸福的来生，预言里都是这么说的。"
    "薇薇安""这么说我是，和女神大人间接接触了啊，我的祈祷传达给女神大人了吗?"
    "薇薇安""五年前，失踪了六名骑士，至今生死未卜......"
    "薇薇安""你见过他们吗？"
    hide mom2 with dissolve

    show me at stand_center with dissolve
    "我""......我连自己的身份都不清楚，更别说别的亡灵的身份了。"
    hide me with dissolve

    show mom2 at stand_center with dissolve
    "薇薇安""这样......你给人一种熟悉的感觉......我还以为......"
    "薇薇安""不过我的女儿，应该是女神大人现任的圣女，她应该可以帮助很多亡灵......"
    "薇薇安""帮助你们前往有光的地方......"
    "薇薇安""而且！她的恋人还是女神大人的勇者耶！预言里不都说了吗勇者和圣女组合是特别特别好的事吗！"
    "薇薇安""我觉得她们一定可以把那六个人找到......"
    "薇薇安""我......没什么故事可以说......"
    "薇薇安""非常平凡的一个人......"
    "薇薇安""我只希望孩子们能幸福，那些帮助过我们的人能幸福......"
    "薇薇安""如果你是代表莉莉丝大人来的，能帮我传达我的问候吗？"
    "薇薇安""孩子们的未来，我父亲的过去，那六个人......"
    hide mom2 with dissolve

    show me at stand_center with dissolve
    "我""......"
    "我""我会帮你的。"
    hide me with dissolve

    "去找别人聊吧。"

    menu:

        "冷漠的女人":
            jump l2_path

        "悲伤的女人":
            jump l3_path


    return






    

