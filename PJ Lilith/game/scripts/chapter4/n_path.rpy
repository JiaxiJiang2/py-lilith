image 10 ="images/characters/8/zm.png"

transform stand_center2:
    anchor (0.5, 1.0)     # 锚点在底部中央
    align (0.5, 1.0)      # 对齐到底部中央（屏幕底）
    zoom 1     # 缩放50%，按需调整

label n_path:
    play music "audio/bgm/6.mp3" fadein 3.0
    "莉莉丝大人......这都是你安排的吗？"

    scene bg room2

    show lilith0 at stand_center with dissolve
    "莉莉丝""这就是你回忆完之后想问的吗？"
    "莉莉丝""......"
    "莉莉丝""是，那又怎样？"
    "莉莉丝""你们本就是罪人，得到了应有的结局不对吗？"
    "莉莉丝""和无数边境的骑士一样......死于魔物......没有任何意外不是吗？"
    "莉莉丝""我只是希望属于我的东西回到我身边。"
    "莉莉丝""亚当在你们之中......"
    hide lilith0 with dissolve

    "亚当......"
    "谁是亚当？"

    show lilith0 at stand_center with dissolve
    "莉莉丝""我不知道。"
    "莉莉丝""是你们人类蛊惑了亚当，让他切断了和我的联系。"
    "莉莉丝""......我用了上千年去找他，好不容易有了些线索......"
    "莉莉丝""只要献上祭品，让亚当回到我的怀抱......"
    "莉莉丝""为什么失败了？"
    "莉莉丝""有人将他从我身边偷走了。"
    "莉莉丝""小偷在这四个人之间......"
    "莉莉丝""而亚当在那八个人之间......"
    hide lilith0 with dissolve

    show 10 at stand_center2 with dissolve
    "亚当在我们之中。"
    "而其他人作为祭品......"
    "这么说来，答案已经很明显了啊。"
    hide 10 with dissolve

    show me at stand_center with dissolve
    "我""亚修和诺亚......你们活下来了。"
    "我""亚修......我不清楚，但我看见了————"
    "我""诺亚，你是第一个死的人。"
    "我""你在我面前......"
    hide me with dissolve

    show Noah at stand_center with dissolve
    "宰相""哼......就是说我已经死了吗？"
    "宰相""emmmmmmmmmm我也不好说我现在为什么还活着，不过你现在说的话还有别的线索吧。"
    "宰相""我是第一个出事的，而你是第二个......不过这都是一瞬间发生的事，顺序大差不差。"
    "宰相""倒是你，想起来自己是谁了吗？"
    "宰相""连那个时候的细节都想起来了不是吗？"
    hide Noah with dissolve

    show me at stand_center with dissolve
    "我""我？"
    "我""我是......"
    hide me with dissolve

    show Noah at stand_center with dissolve
    "宰相""一开始还在想你为什么和其他亡灵不一样，应该是和我们，和这件事有很紧密的联系。"
    "宰相""知道莉莉丝在寻找的东西我就比较清楚到底发生了什么事了。"
    "宰相""正所谓灯下黑，不是吗？"
    "宰相""还是没有想起来自己的身份吗？"
    "宰相""你什么时候变这么笨了，卢克索。"
    "宰相""还是说应该叫你，我亲爱的弟弟————"
    hide Noah with dissolve
    
    scene bg room0
    menu:
        "亚当-阿祖拉":
            jump n1_path

    return