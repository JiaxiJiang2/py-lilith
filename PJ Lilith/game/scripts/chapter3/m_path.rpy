image d = "images/characters/others/dragon.png"
image A2 = "images/characters/Asche/2.png"
image I2 = "images/characters/Isaiah/2.png"
image V2 = "images/characters/Nova/2.png"

image 1 ="images/characters/8/Pride.png"
image 2 ="images/characters/8/Lust.png"
image 3 ="images/characters/8/Sloth.png"
image 4 ="images/characters/8/Wrath.png"
image 5 ="images/characters/8/Gluttony.png"
image 6 ="images/characters/8/Envy.png"
image 7 ="images/characters/8/Greed.png"
image 8 ="images/characters/8/Noah3.png"
image 9 ="images/characters/Isaiah/3.png"

image bg room00 = "images/bg/0.png"
image bg room33 = "images/bg/33.png"
image bg room34 = "images/bg/34.png"
image bg room35 = "images/bg/35.png"

label m_path:
    scene bg room0
    ""
    ""
    ""
    "......"
    "......"
    "......"
    "......"
    "你知道勇者和圣女的传说是怎么来的吗?"
    "很久很久以前，非常非常久，久到莉莉丝还没有成为女神，久到人类还非常弱小的那个时候。"
    show d with dissolve
    "有一头庞大的，可以覆盖住天空的黑龙。"
    "有人说，黑龙是保护人们的存在。"
    "有人说，黑龙会带来灾难。"
    "总之，人们敬畏黑龙。"
    hide d with dissolve

    scene bg room0
    "那个时候魔物肆虐，人类无法保护自己，所以他们试图寻求黑龙的帮助。"
    "黑龙不关心这些，毕竟魔物不是它带来的，灾难也不是它带来的。"
    "人类以为黑龙觉得他们诚意不够，于是为黑龙献上了祭品。"

    show A2 at stand_center with dissolve
    "“被诅咒的少年”，人们如此称呼着祭品。"
    "因为外貌上的一点不同，被认为和魔兽与黑龙有关系的，普通的少年。"
    "少年去了黑龙那里，再也没有别的消息。"
    hide A2 with dissolve

    "情况并没有好转，人类还是生活在魔物的压制之下。"
    show I2 at stand_center with dissolve
    "于是他们选出了一名圣女，一位纯洁美丽聪慧的女子，去和黑龙交流。"
    "少女独自前往黑龙的巢穴，也失去了所有音讯。"
    hide I2 with dissolve

    stop music fadeout 10.0

    scene bg room0
    "人们陷入了巨大的慌乱之中，他们开始不信任黑龙，开始憎恨，咒骂黑龙。"
    show V2 at stand_center with dissolve
    "他们派出了一名勇者，最强大的人类战士，前去讨伐黑龙。"
    "当然，这位也没回来。"
    hide V2 with dissolve

    scene bg room0
    "人们陷入了绝望，他们以为他们完蛋了。"
    "在抵抗和挣扎中过去了很多年......"
    scene bg room00
    "一名尖耳朵的少年出现了。"
    "少年带来了魔法与奇迹，在人类的世界种下了金色的树，树冠遮天蔽日，支起了巨大的结界。"
    "少年自称是勇者和圣女的孩子，相传他是莉莉丝的兄弟。"
    "而那为人类建立的庇护所，被称为伊甸园。"
    play music "audio/bgm/5.mp3" fadein 3.0
    "......"
    "......"
    scene bg room33

    show 3 at stand_center with dissolve
    "？？""你们真的信什么，什么黑龙啊，女神啊，那些有的没的吗？"
    hide 3 with dissolve

    show 7 at stand_center with dissolve
    "？？""信徒每年还要向教会上交一定的税，还不如信钱来得实在，女神和黑龙可不会莫名其妙给你钱。"
    hide 7 with dissolve

    show 5 at stand_center with dissolve
    "？？""埃瓦里就是因为活得太现实，现在才过得不幸福吧。"
    hide 5 with dissolve

    show 7 at stand_center with dissolve
    "埃瓦里""你们好不到哪里去，尤其是你，古拉，光靠吃就能把自己工作丢掉，还不如想想怎么多赚点钱能够过好下半辈子。"
    hide 7 with dissolve

    show 5 at stand_center with dissolve
    "古拉""“能吃的时候就多吃点”，有一位伟人曾经这样说过。"
    hide 5 with dissolve

    show 6 at stand_center with dissolve
    "？？""有这种传说吗，请务必和我讲讲细节。"
    hide 6 with dissolve

    show 5 at stand_center with dissolve
    "古拉""不要！和你关系太好担心我会有生命危险。"
    hide 5 with dissolve

    show 6 at stand_center with dissolve
    "？？""哎呀，被嫌弃了。"
    hide 6 with dissolve

    show 3 at stand_center with dissolve
    "？？""（打了个哈欠）因维迪亚只要好好地唱催眠曲就行了，队长，现在还不能回去吗？"
    hide 3 with dissolve

    show 8 at stand_center with dissolve
    "？？""如果你们能少闲聊一会儿，而你，我亲爱的阿西迪亚，如果能动一动自己开始干活，我相信我们一个小时之内就能回去了。"
    hide 8 with dissolve

    "第三章"
    "我们"

    show 5 at stand_center with dissolve
    "古拉""今天晚上吃什么？"
    hide 5 with dissolve

    show 6 at stand_center with dissolve
    "因维迪亚""我要减肥所以选沙拉。"
    hide 6 with dissolve

    show 7 at stand_center with dissolve
    "埃瓦里""随便。"
    hide 7 with dissolve

    show 3 at stand_center with dissolve
    "阿西迪亚""我要直接洗洗睡了，你们随便给我留点我饿醒了再吃。"
    hide 3 with dissolve

    show 4 at stand_center with dissolve
    "伊拉""吃肉。"
    hide 4 with dissolve

    show 2 at stand_center with dissolve
    "维利亚""......"
    hide 2 with dissolve

    show 1 at stand_center with dissolve
    "卢克索""西奥多吃什么我吃什么。"
    hide 1 with dissolve

    show 8 at stand_center with dissolve
    "西奥多""你们好烦啊，下次能不能统一一点，下馆子的话自己掏钱啊。"
    "西奥多""一起吃一样的，吃素的把肉给爱吃肉的，不爱吃菜的把菜给吃素的。"
    hide 8 with dissolve

    show 5 at stand_center with dissolve
    "古拉""反对！这是虐待队友！"
    hide 5 with dissolve

    show 8 at stand_center with dissolve
    "西奥多""吃最多的没有发言权，给你点两份你慢慢吃。"
    hide 8 with dissolve

    show 5 at stand_center with dissolve
    "古拉""队长万岁！！！"
    hide 5 with dissolve

    scene bg room0
    "......"
    
    scene bg room34
    show 8 at stand_center with dissolve
    "西奥多""姓名以及到这里来参军的理由。"
    hide 8 with dissolve

    show 1 at stand_center with dissolve
    "卢克索""明知故问。"
    hide 1 with dissolve

    show 8 at stand_center with dissolve
    "西奥多""你总该低调点，在这里还是给自己取一个假名吧。"
    hide 8 with dissolve

    show 1 at stand_center with dissolve
    "卢克索""......"
    "卢克索""看来你真不打算回去了。"
    "卢克索""......"
    "卢克索""叫我卢克索吧。"
    hide 1 with dissolve

    "......"
    show 3 at stand_center with dissolve
    "阿西迪亚""（打哈欠）"
    "阿西迪亚""阿西迪亚......本来是宪兵队的弓箭手......（打哈欠）"
    "阿西迪亚""因为太爱睡懒觉被炒了，感觉这个地方不会有太多活应该可以睡够......"
    "阿西迪亚""（打哈欠）如果没什么事我可以先去看看宿舍吗？"
    hide 3 with dissolve

    "......"
    show 4 at stand_center with dissolve
    "伊拉""伊拉，原自由冒险者。"
    "伊拉""因为在公会多次打架斗殴，被大部分公会和冒险者小队拉黑了。"
    "伊拉""接待员说我应该去军队调整一下。"
    "伊拉""于是就到这里来了。"
    "伊拉""你放心，我打架没输过。"
    hide 4 with dissolve

    "......"
    show 6 at stand_center with dissolve
    "因维迪亚""著名的吟游诗人因维迪亚，也是有名的花花公子。"
    "因维迪亚""第一次听人这么介绍自己吗，你貌似没听过我的传闻。"
    "因维迪亚""不是我多浪荡，是我交往过的女孩都被人杀害了。"
    "因维迪亚""别这个表请，这都是谣言，有人太嫉妒我的才华和美貌才散布的谣言。"
    "因维迪亚""不过这个谣言害得我没法在外边混口饭吃了，总之，军队应该不会有这些问题吧。"
    hide 6 with dissolve

    "......"
    show 5 at stand_center with dissolve
    "古拉""古拉！之前是超~级有名的那个舞团的舞者。"
    "古拉""什么？你没听说过，看来队长不近女色的传言是真的......"
    "古拉""总之因为快把舞团吃破产了，被开除了！"
    "古拉""军队应该会管饱的吧，我们国家应该还挺有钱的。"
    hide 5 with dissolve

    "......"
    show 7 at stand_center with dissolve
    "埃瓦里""埃瓦里，之前是主城的收税官。"
    "埃瓦里""......"
    "埃瓦里""因为贪污和受贿，被贬到这个鸟不拉屎的地方了。"
    "埃瓦里""我之前见过你们......"
    "埃瓦里""看来你们日子也不好受。"
    hide 7 with dissolve

    "......"
    show 8 at stand_center with dissolve
    "西奥多""总之我们小队的成员差不多就这样了。"
    "西奥多""我是西奥多，你们的队长，你们的老大，总之以后都听我指挥就行。"
    "西奥多""放轻松，我不是那种死板的人，像家人一样相处就行。"
    hide 8 with dissolve

    show 1 at stand_center with dissolve
    "卢克索""......"
    "卢克索""你身后那个家伙不需要自我介绍一下吗。"
    hide 1 with dissolve

    show 2 at stand_center with dissolve
    "维利亚""......"
    "维利亚""维利亚，西奥多的副官。"
    "维利亚""我的工作主要是辅助西奥多，所以你们好好听他的就行。"
    hide 2 with dissolve

    scene bg room35
    show 9 at stand_center with dissolve
    "？？？""今天也来了啊西奥多！"
    hide 9 with dissolve
    "一进入餐厅，金发的小女孩就扑向他们的队长，把大家都吓了一跳。"

    show 5 at stand_center with dissolve
    "古拉""萝莉！"
    "古拉""队长原来喜欢的是萝莉吗？"
    hide 5 with dissolve

    show 8 at stand_center with dissolve
    "西奥多""你不觉得我们长得很像吗......"
    "西奥多抱起了小女孩，两人的脸处在同一水平线，不仅耳朵都是尖尖的，瞳孔都是绿色的，连整体的五官都有几分相像。"
    hide 8 with dissolve

    show 1 at stand_center with dissolve
    "卢克索""你这么执着地要到边境生活不会是因为有这个私生子吧。"
    "卢克索""......我以为你......你原来是这种人吗。"
    hide 1 with dissolve

    show 2 at stand_center with dissolve
    "维利亚""是侄女。"
    "维利亚""妹妹的女儿。"
    hide 2 with dissolve

    show 1 at stand_center with dissolve
    "卢克索""妹妹？等等......你是说，妹妹？"
    hide 1 with dissolve

    show mom2 at stand_center with dissolve
    "？？？""欢迎......今天来了好多新面孔啊，都是新人吗。"
    hide mom2 with dissolve

    show 8 at stand_center with dissolve
    "西奥多""这是由我带领的全新的小队，以后就固定这个形式了。"
    "西奥多""四舍五入算我永久升官了，今天晚上我请客。"
    "西奥多""这是我妹妹，薇薇安，这家酒馆的老板。"
    "西奥多""还有这个小不点，以赛亚，我可爱的小侄女。"
    hide 8 with dissolve

    scene bg room0
    "和平的边境，热闹的酒馆，这是每个人都喜欢的环境。"
    "大家抛去了束缚着他们的过去，纷纷开始向前看。"
    "......"
    "即使是一开始和大家抱着不同目的来到这里的我......"
    "也许我也能放下......适应这里的一切......"
    "......"
    "西奥多......"
    "诺亚啊，如果这是你所期待的，我可以跟着你的步伐......"

    "还要继续回忆下去吗？"
    menu:
        "是":
            jump m1_path
return