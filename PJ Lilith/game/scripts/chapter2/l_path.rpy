label l_path:
    scene bg room2
    show lilith0 at stand_center with dissolve
    "莉莉丝""你......"
    "莉莉丝""你不应该在这里。"
    "莉莉丝""你不应该和他们说话......"
    "莉莉丝""你......"
    "莉莉丝""你继续听吧，还有其他证人没来......"
    "莉莉丝""人类总是用花言巧语迷惑别人。"
    "莉莉丝""接下来的证人，她们有一些不会说谎。"
    "莉莉丝""亡灵不会对我们说谎。"
    "莉莉丝""去听听她们讲的吧......"
    hide lilith0 with dissolve

    
    
    scene bg room0
    ""
    "莉莉丝是光明的女儿，是所有生命的母亲。————《莉莉丝预言》"
    "第二章"
    "“她们”"
    "      "
    "似乎可以前往别的灵魂那里，要去和她们聊聊吗？"
    menu:

        "活泼的女人":
            jump l1_path

        "冷漠的女人":
            jump l2_path

        "悲伤的女人":
            jump l3_path


    return
