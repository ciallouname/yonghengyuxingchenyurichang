


define third_choice = 0
default _route_9c = ""
default _blush_flag = True


label story_826_part1:

    play music bgm_14 fadein 1.0
    scene bg_office_1
    with Fade(0.5, 0.5, 0.5)
    show bg_office_1:
        zoom 1.06
        xalign 0.65
        yalign 1.0
    with dissolve

    tsa_ "小凑，到点了居然还不下班？真少见。"
    lxc_ "测试组的人说怕晚上做噩梦，测我们那个恐怖游戏时不敢开音效。"
    lxc_ "音频部分的功能就只好我自己验收了。"
    tsa_ "哈？音效都不敢开，请这帮人过来干嘛？"
    lxc_ "嘘，小声点，谁知道对方是怎么进来的。"
    lxc_ "要是不小心被听到，说不定你明天就『 因为左脚先进公司 』而被开除了。"
    tsa_ "……这倒也是，那我先溜了，你慢慢忙。"
    show bg_office_1:
        zoom 1.0
        xalign 0.5
        yalign 1.0
    with dissolve
    lxc_ "嗯，慢走。"


    scene bg_community_2
    with fade

    "回到家时，已经快十一点。"

    play music bgm_7 fadeout 1.0 fadein 1.0
    scene bg_living_room_2
    with fade
    show sy clothes2_front1 sigh kp20wl at left with dissolve
    show xm clothes2_front3_no smile at right with dissolve

    "时语正蜷在沙发上看烹饪节目，星弥则在厨房捣鼓着什么。"

    show sy sigh hide_fx with dissolve
    sy_ "终于回来了……你今天的生命力比昨天更低呢。"
    lxc_ "……这也能看出来？你是按什么标准判断的？"
    show sy clothes2_side1 focus at lean_in
    sy_ "简单来说，就是靠闻气味。"
    "她凑了过来，嗅了嗅鼻子。"
    show sy clothes2_side1 despise with dissolve
    sy_ "如果我还保持着吸血的习惯，你现在的血就是最难喝的那种，哪怕是免费送上门我都不想喝。"
    lxc_ "那还真是谢谢你啊。"
    show sy clothes2_front1 pout kp13wl at angry_stomp
    sy_ "哼，你也就反驳本小姐时有精神了。"
    show sy clothes2_front1 smile hide_fx with dissolve
    sy_ "快点去洗澡吧，热水我已经帮你开好了。"


    with dissolve
    show xm clothes2_front3_no bewilderment at lean_in
    xm_ "林先生，您看起来好累……先喝点牛奶吧？"
    lxc_ "谢谢你们。我待会还得写两个文档，你们先睡吧。"
    "虽然确实有点累，但一想到项目进度……还是先工作吧。"


    with dissolve
    show sy clothes2_side1 cat_mouth with dissolve
    sy_ "什么工作能把人折磨成这样子……星弥，你不觉得好奇吗？"


    with dissolve
    show xm clothes2_front2_no focus at nod_small
    xm_ "嗯……确实很在意。林先生每天都去的地方，到底是什么样的呢？"
    lxc_ "就是普通的公司而已……"


    with dissolve
    show sy clothes2_front2 cat_mouth kp17wl at excited_lean_forward
    sy_ "这样吧，我有个想法，我们明天——"
    show sy smile hide_fx at excited_lean_forward_undo
    "后来她们说了什么我没听清，只记得最后是时语催我去洗漱的。"
    "那天晚上，我做了个梦，梦见自己穿越进了游戏世界里——只不过，那个世界也充满了BUG。"

    scene black
    with ImageDissolve("rule/eyeclose.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)
    pause 0.5
    scene bg_living_room_1
    with ImageDissolve("rule/eyeopen.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)

    lxc_ "我出门了……"
    "第二天，我迷迷糊糊地洗漱完出门，完全没有注意到，时语已经早早起床了。"



    scene black with Fade(0.3, 0.3, 0.3)

    $ heroine = True
    $ heroine_name = "时语的视角"

    play music bgm_16 fadeout 1.0 fadein 1.0
    scene bg_living_room_1
    with fade

    show sy clothes2_front1 cat_mouth at left with dissolve
    show xm clothes2_front2_no smile at right with dissolve

    sy_ "好，人类他出门了，我们快跟上！"
    xm_ "嗯！"
    show xm clothes2_front2 focus kp17wl at emphasis_pop
    "星弥取出法杖，为我们施加上隐身魔法和静音魔法。"
    show xm clothes2_front2_no smile hide_fx with dissolve
    "这样一来，除了我们彼此，周围的人都无法察觉到我们的存在了。"

    scene bg_street_1
    with fade
    show sy clothes2_side1 smile at left with dissolve
    show xm clothes2_side1 smile at right with dissolve

    "隐身魔法让我们像两道透明的影子，不远不近地跟在他的身后。"
    "这家伙完全没发现我们，只顾低头往前走，真是毫无防备。"
    scene bg_subway_1
    with fade
    show bg_subway_1:
        zoom 1.08
        xalign 0.5
        yalign 1.0
    with dissolve
    show sy clothes2_front1 astonished at left with dissolve
    show xm clothes2_front2_no oo at right, shocked_step_back
    xm_ "好多人……！虽然听说过，但没想到地铁站里居然这么拥挤！"
    sy_ "是啊，据说这里每天的人流量至少有十万以上。"
    show xm astonished at emphasis_pop
    xm_ "十万……我一年都见不到这么多人呢。"
    show xm bewilderment with dissolve
    "地铁站里人群如潮水般涌动，推搡着向前。"
    show sy clothes2_front1 bewilderment with dissolve
    sy_ "这人流密度，比古堡天花板的蝙蝠群还要夸张啊。"
    "原来他每天都要面对这样的场面吗？"
    show sy clothes2_front2 focus at excited_lean_forward
    sy_ "他上地铁了，我们得跟上去！"

    scene bg_subway_2
    with Fade(0.5, 0.5, 0.5)

    show sy focus at left with dissolve
    show xm clothes2_front2_no oo at right, shocked_step_back
    xm_ "大家都在挤着上车……时、时语，我快要被挤成魔女饼干了！"

    "星弥紧紧抓着我的衣角，被人群推挤得声音发颤。"
    show sy bewilderment kp15wl with dissolve
    sy_ "魔女饼干是什么鬼啦！"
    show sy clothes2_front1 pout hide_fx at angry_stomp
    sy_ "你快点用屏障魔法不就好了！"
    show xm clothes2_front3_no focus with dissolve
    xm_ "对、对哦！"
    show xm at emphasis_pop
    "她立刻念出咒语，将我们笼罩在屏障中，隔绝了外界的拥挤。"

    show sy focus with dissolve
    "我看向林小凑，只见他早已熟练地缩在车厢角落，低头玩起了手机。"
    "每天早早来到地铁站，挤在人群里，躲在角落——这种事他恐怕早已习惯了。"
    show xm oo kp1wl at bounce_small
    xm_ "我刚刚好像踩到了谁的脚……对不起！对不起！"
    show xm hide_fx with dissolve
    "哪怕有屏障魔法，星弥还是踮起着脚，努力不与旁人接触。"
    "看着她慌慌张张道歉的样子，我觉得又好气又好笑。"
    "隐身和静音状态下，别人根本听不见好吧！"
    "地铁广播报出下一站的站名，更多乘客涌入车厢。"
    "为了避开人群，我们主动躲进角落里。"
    hide xm with dissolve
    show sy clothes2_side1 focus at center:
        zoom 1.2
    with dissolve
    play music bgm_6 fadeout 1.0 fadein 1.0
    "于是，我意外地来到了林小凑身旁。"

    "只见他对周围的拥挤毫无反应，仍专注盯着手机屏幕。"
    "我好奇地凑近一看，上面显示着「 经济实惠生活冷知识！ 」「 家里蹲也能做的线上兼职！ 」之类的内容。"
    show sy clothes2_side1 sigh at look_away_small
    sy_ "笨蛋……"
    "我忍不住轻轻戳了戳他的脸颊，哪怕可能被他察觉。"
    "车厢里地铁运行的声音很嘈杂，我却觉得这一刻格外安静。"
    "如果他知道我们在跟踪他，肯定会先大吃一惊，然后一本正经地开始说教。"
    "什么「 两个女孩子单独出门太危险 」「 外面的人可不会管你们是不是血族或魔女 」之类的。"
    "就算他不说出口，我也能想象出他那副严肃又担心的语气。"
    "……真是的，明明只是个比我和星弥还弱小的人类。"


    scene bg_office_4
    with Fade(0.5,0.5,0.5)
    play music bgm_14 fadeout 1.0 fadein 1.0
    show bg_office_4:
        zoom 1.08
        xalign 0.6
        yalign 1.0
    with dissolve
    show sy clothes2_front1 focus at left with dissolve
    show xm clothes2_front3_no focus at right with dissolve

    $ heroine_name = "星弥的视角"

    "下了地铁后，我和时语偷偷跟着林先生来到了他上班的地方。"
    "虽然一路上小吃摊飘来的香味很诱人，但现在有更重要的事要做。"
    "从环境上看，和林先生说的一样，只是一家普通的公司，和我在网上见过的图片差不多。"
    "在这样的公司工作也能让他这么疲惫，是不是说明这种现象很普遍呢？"
    "表世界的人类真不容易啊……"

    scene sd5
    with fade

    "林先生到了工位后，熟练地打开电脑上的工作软件。"
    "他是眯着眼睛完成这些动作的，看起来还没完全清醒。"
    "桌上除了必要的办公用品，几乎没太多别的东西，就和他家里一样简单干净。"
    sy_ clothes2_front1 focus "他和同事说话时好像挺严肃的，和我们相处时完全是两个人。" with dissolve

    xm_ clothes2_front1_no bewilderment "是啊，没有那么温柔，更像是……和我们初次见面时的样子。" with dissolve

    sy_ pout "他还真是不懂职场规矩呢，这样可没办法搞好同事关系。" with dissolve
    "虽然时语的语气像是在责备他，但从表情能看出来，她其实心里挺高兴的。"
    "毕竟这意味着，在林先生的眼里，我们是特别的。"
    show xm clothes2_front1_no shy skin_shy:
        ypos 5000
    with dissolve
    "……原来我们是特别的啊。"
    tsc_ "……你这个功能做起来太复杂了。"
    show bg_office_4:
        zoom 1.12
        xalign 0.55
        yalign 1.0
    with dissolve
    "正当我在观察办公室的人际关系时，一个同事走到了他的面前。"
    lxc_ "是吗？但据我了解，只要给文本加个变量，关闭开关时不显示变量就行。"
    lxc_ "哪怕表述不够精确，基础逻辑应该是类似的。"
    tsc_ "……到底你是程序还是我是程序啊。"
    lxc_ "还有个地方要提一下，内容回顾功能不要把没出现过的文本也显示出来。"
    lxc_ "正常游戏不会这么做的，而且需求文档上已经写清楚了。"
    lxc_ "哪怕字比较多，也麻烦你仔细看一下。"
    tsc_ "……知道了。"
    scene sd5
    with fade

    xm_ clothes2_front1_no pout "那个人的态度真差啊……" with dissolve

    sy_ clothes2_front1 pout "就是啊，什么意思嘛。" with dissolve
    sy_ "明明林小凑都讲明白了，他还一副不情愿的样子。"

    xm_ clothes2_front2_no focus "虽然两个人都板着脸，但至少我家的林先生说话还是很有礼貌的！" with dissolve

    sy_ astonished kp1wl "就是啊，林小凑可不会那么没教养……等等，我家的？" with dissolve

    xm_ clothes2_front1_no shy skin_shy kp8wl "唔……我们家的？" with dissolve
    sy_ oo skin_shy hide_fx "不对，重点好像不是这个吧！" with dissolve

    show bg_office_4:
        zoom 1.02
        xalign 0.45
        yalign 1.0
    with dissolve
    tsa_ "小凑，没事吧？"
    lxc_ "正常工作交接，能有什么事。"
    tsa_ "小冯那家伙拽得跟二五八万似的，水平不行还态度不好。"
    tsa_ "也就你脾气好，换做是我，哪会给他好脸色。"
    lxc_ "毕竟是新人，多包容一点吧。"
    lxc_ "准备开会了，老大最近出差了，会议我来主持。"
    tsa_ "行吧，又要开会啊。"
    "除了最初搭话的同事，还有几位同事也主动和林先生打了招呼，气氛轻松了不少。"

    scene sd5
    with fade

    sy_ clothes2_front1 smile "至少还是有正常同事的嘛。" with dissolve

    xm_ clothes2_front1_no smile skin_blush "嗯，说明林先生人缘还是很不错的。" with dissolve
    "如果换我遇上那种人，大概只会脸上假装微笑，然后心里默默祈祷对方摔个大跟头。"
    "但林先生不同，哪怕他一直板着脸，心里还是会为对方着想。"
    "他真厉害呢……"

    scene bg_street_4
    with fade
    play music bgm_20 fadeout 1.0 fadein 1.0
    show bg_street_4:
        zoom 1.04
        xalign 0.5
        yalign 0.0
    with dissolve
    show sy clothes2_side1 sigh at left with dissolve
    show xm clothes2_side1 bewilderment at right with dissolve

    xm_ "需求下达、工作对接、程序沟通、排期协商……原来林先生每天都要面对这么多麻烦事啊。"
    sy_ sigh "……比应付那些古板的老爷子麻烦多了。" with dissolve
    sy_ bewilderment "这个在家只会跟我斗嘴的人类，原来平时要面对这么多压力……" with dissolve
    sy_ sigh "虽然之前从房东那里已经知道他很不容易了，但远不如亲眼见到来得真实。" with dissolve
    xm_ sigh "嗯，我终于理解他为什么总是看起来很累，为什么有时候一回家就直接瘫在沙发上了。" with dissolve
    xm_ bewilderment "社会人还真不容易呢……" with dissolve
    scene bg_sky_5
    show bg_sky_5 at bg_pan_left
    with fade
    "落日的余晖洒在两人身上，拉出细长的影子。"
    "……我想对他更好一点。"

    call achievement (5) from _call_achievement_6
    "比之前、比现在，都要再温柔、再体贴一点。"
    "这一刻，两位少女的心里，不约而同地浮现出了同样的念头。"

    $ heroine = False

    scene bg_street_2
    with fade

    "今天又是加班到十点的一天，不过终于熬到周末了！"
    "最近为了赶项目都没怎么和她们好好聊天，也不知道她们会不会觉得寂寞。"
    "明天好好陪陪她们吧。"

    scene bg_living_room_3
    with fade

    "推开家门，发现里面已经关了灯。"
    lxc_ "都睡了吗——"

    play music bgm_13 fadeout 1.0 fadein 1.0
    scene bg_living_room_2
    with dissolve
    show bg_living_room_2:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve
    show sy clothes2_front1 shy at center with dissolve

    "话还没说完，周围忽然亮起了灯光。"
    "不过这灯光比平时的更柔和，更温暖。"
    "视线前方，时语正端坐在沙发上，脸上带着淡淡的红晕。"
    "她拍了拍自己的大腿。"
    show sy smile at look_away_small
    sy_ "……过来，躺下吧。"
    lxc_ "啊？搞什么，突然这么正经的……"
    show xm clothes2_side1 smile at char_enter_right
    with dissolve
    show xm clothes2_side1 smile at right
    show sy clothes2_front1 smile at left
    with dissolve
    xm_ "林先生今天工作了一天，一定很累了。"
    "星弥突然出现在我身后，轻轻把门关上。"
    xm_ smile_close "所以，今晚就好好交给我们吧。" with dissolve
    lxc_ "欸？什么情况？"

    show bg_living_room_2:
        zoom 1.08
        xalign 0.5
        yalign 1.0
    with dissolve

    "还没来得及询问，我就被一股看不见的力道轻轻推着向前走。"
    "……我懂了，是星弥用了魔法，包括灯光的效果，还有空气中那股好闻的香气。"
    lxc_ "请问……这是要做什么呢？"
    "连魔法都用上了，感觉有点不对劲。"
    xm_ cat_mouth "放心，对您没有坏处的~" with dissolve
    "……听你这么说我反而更紧张了。"
    show bg_living_room_2:
        zoom 1.14
        xalign 0.5
        yalign 1.0
    with dissolve
    "随着我和时语之间距离越来越近，我能更清楚地看到她脸上那害羞的红晕。"
    "不对劲，这氛围很不对劲……我不在的时候到底发生什么事了？！"
    show sy clothes2_front1 shy at shy_shrink
    sy_ "躺、躺上来吧！"
    lxc_ "……这样做是不是不太好？"
    show sy clothes2_front1 pout at angry_stomp
    sy_ "废话少说，躺上来就是了！"
    "时语扯住我的衣服，一把将我拉了过去。"


    scene black
    with ImageDissolve("rule/eyeclose.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)

    "诶？"

    scene cg1313
    with ImageDissolve("rule/eyeopen.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)

    "——然后把我的头放在她的大腿上。"


    lxc_ "不要乱来……嗯？什么情况？"

    show cg131 with dis_master

    sy_ pout "膝枕啊，你们人类不是最喜欢这样的事吗？" with dissolve

    show cg132 with dis_master

    sy_ shy "不然你以为是什么？" with dissolve
    lxc_ "……不，没什么。"
    "我刚刚脑海里闪过的奇怪想法，还是不要告诉她比较好。"

    show cg133 with dis_master

    xm_ clothes2_front3_no cat_mouth "嘻嘻，林先生感觉怎么样呢？" with dissolve
    lxc_ "……我能说没什么感觉吗？"

    show cg134 with dis_master

    sy_ pout "喂，你的意思是本小姐的膝盖很硬吗？！" with dissolve
    lxc_ "不是啊，主要是太意外了，一时间没反应过来。"
    lxc_ "怎么就突然间做这些事？"

    show cg135 with dis_master

    xm_ shy skin_shy "就……想着慰劳一下您啊？"

    show cg136 with dis_master

    xm_ smile skin_blush "毕竟您工作已经很辛苦了。" with dissolve

    show cg137 with dis_master

    xm_ cat_mouth "顺带一提，这个主意是时语出的哦？" with dissolve

    show cg138 with dis_master

    sy_ oo "星弥！不是说好了不说出来吗！"

    show cg139 with dis_master

    xm_ smile_close "不行哦，我可不能抢了你的功劳。" with dissolve
    lxc_ "……你不会是上网学回来的吧？？"
    show cg1310 with dis_master

    sy_ astonished "你、你怎么知道的？！"

    lxc_ "随便猜也能猜到吧。"

    show cg1311 with dis_master

    sy_ shy "……你不喜欢吗？" with dissolve
    lxc_ "没有啊？你们特意为我准备的，怎么会不喜欢。"
    lxc_ "只是太意外而已。"

    show cg1312 with dis_master
    sy_ smile skin_blush "哼，那就好。" with dissolve

    show cg1313 with dis_master

    xm_ smile "既然您喜欢，那我们就继续了。"
    "星弥跪坐在一旁，开始小心翼翼地按摩我的手。"
    "时语把我的头摆正，开始为我按摩头皮。"

    show cg1314 with dis_master

    sy_ shy skin_shy "那句台词怎么说来着……今、今天，请让我们为您缓解疲劳吧。"
    lxc_ "噗，其实你不用勉强说这种台词的……"
    show cg1315 with dis_master
    sy_ oo "你、你别笑啊！"
    "时语的手法并不专业，甚至有点笨拙，却让人觉得莫名温暖。"

    show cg1316 with dis_master
    sy_ pout "……哼！这可是特别的血族膝枕服务，按理说你应该感恩戴德！" with dissolve
    lxc_ "嗯，还是这样的时语更让人安心。"
    lxc_ "能享受到这样的服务，确实是我的荣幸，谢谢。"
    hide cg1314
    show cg1314 with dis_master
    sy_ shy "狡猾……净会说些好听的话。" with dissolve

    hide cg1313
    show cg1313 with dis_master
    sy_ smile skin_blush "算了，你就好好享受吧。" with dissolve
    "另一边，星弥按摩手法就熟练很多，手指在她的指法下变得松软舒适。"

    xm_ smile "以前有段时间替老师按摩过，后来她说这样会上瘾的，就没有再继续了。" with dissolve

    show cg1317 with dis_master
    xm_ focus "林先生觉得怎么样呢？" with dissolve
    lxc_ "很舒服啊，时间久了确实容易上瘾……我现在就觉得有点迷糊了……"


    show cg1318 with dis_master
    xm_ smile_close "我调整了安神魔法的效果……应该能让您放松下来。"

    "时语的大腿比想象中柔软，星弥的手指暖暖的。"
    "空气中飘着淡淡的、像是薰衣草的香气。"

    sy_ "不靠近点看，都不知道你的眼睫毛有点长呢。"
    hide cg1317
    show cg1317 with dis_master
    xm_ focus "您的手指虽然纤细却有力，是长期伏案工作的缘故吗……" with dissolve
    lxc_ "是吗……我自己都没怎么留意……"

    hide cg1318
    show cg1318 with dis_master

    xm_ smile_close "您已经很努力了，不用再勉强自己的。" with dissolve

    hide cg1311
    show cg1311 with dis_master

    sy_ shy skin_blush "是啊，我们都对你挺满意的……各种意义上。" with dissolve
    lxc_ "这样啊……谢谢……"

    hide cg1318
    show cg1318 with dis_master

    sy_ smile skin_blush "笨蛋，是我们谢谢你才对。" with dissolve

    xm_ "林先生就好好休息吧，在您睡着前，我们会一直陪在您身边的。"
    "星弥哼起轻柔的摇篮曲，时语在一旁轻轻和声相伴。"
    scene black
    with fade
    "在从未有过的安心感中，我沉沉睡去。"
    "那晚，我什么梦都没有做，是工作以来第一次睡得这么踏实。"

    call achievement (6) from _call_achievement_7

    play music bgm_19 fadeout 1.0 fadein 1.0
    scene bg_bedroom_1
    with fade
    show bg_bedroom_1:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve

    "清晨，阳光透过窗帘的缝隙把我唤醒。"
    "迷迷糊糊地睁开眼，发现自己正躺在房间的床上，身上盖着熟悉的被子。"
    "奇怪，我昨晚不是在沙发上……是她们把我搬进来的吧。"
    "记忆慢慢清晰起来，一想起昨晚的事，脸就微微发烫了。"
    "少女的膝枕，还有柔软的小手……真是如梦幻般的一晚。"
    "多亏了她们，好久没睡过这么舒服的觉了。"
    "我大大地伸了个懒腰，深呼吸的同时，被子上淡淡的香气也飘进了鼻腔。"

    show bg_bedroom_1:
        zoom 1.1
        xalign 0.5
        yalign 1.0
    with dissolve

    "对哦，之前都是她们睡我房间的……闻闻。"
    "……不对，怎么感觉好像变态一样？"
    "得赶紧出去，再在这里待久了，也不知道会冒出什么奇怪的想法。"
    show sy clothes2_side1 shy skin_shy at left with dissolve

    show sy clothes2_side1 shy at look_away_small
    sy_ "……咳咳，你终于醒了啊？"
    lxc_ "哇！怎、怎么不敲门？！"
    lxc_ "要是我在换衣服怎么办？"
    sy_ bewilderment "我们早上出去的时候哪有关房门……" with dissolve
    sy_ pout skin_blush "而且你平时都是在洗手间换衣服的吧？" with dissolve
    lxc_ "……哦，这样啊。"
    "不过……她们早上出去时是什么意思？"
    show xm clothes2_side1 shy skin_shy at right with dissolve
    xm_ "总、总之，您先起床吧。"
    show xm smile skin_blush at nod_small
    xm_ "我已经把早餐做好了。"
    "星弥从门旁探出身子，弱弱地说道。"
    lxc_ "好吧。"
    xm_ shy "还、还有，闻被子的事，下次不要再做了……" with dissolve
    show xm clothes2_side1 shy skin_shy kp8wl at shy_look_away
    xm_ "真的很让人害羞……！"
    show sy clothes2_side1 oo kp1wl at shocked_step_back
    "星弥尴尬地把视线偏向一边，时语已经用头发包住自己的脸，逃也似地跑出房间。"
    show sy at char_exit_left
    pause 0.4
    hide sy

    scene black
    with ImageDissolve("rule/eyeclose.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)

    "我向后一倒，闭上眼，永远不想再醒过来了。"

    with vpunch

    "……怎么枕头上也有香味啊。"

    scene bg_living_room_1
    with fade
    show sy clothes2_front1 smile at left with dissolve
    show xm clothes2_front2_no smile at right with dissolve

    "洗漱完，我回到客厅和她们一起吃早餐。"
    show xm smile at nod_small
    xm_ "我在今天的煎鸡蛋里面加了点火腿肠，是不是更好吃了呢？"
    lxc_ "嗯，嫩滑的鸡蛋和咸香的火腿肠配在一起，口感更有层次了。"
    lxc_ "继续锻炼下去，说不定哪天星弥的厨艺就超过我了。"
    xm_ shy skin_blush "也没那么厉害啦……不过我会加油的！" with dissolve

    show sy clothes2_front2 cat_mouth at emphasis_pop
    sy_ "……咳咳，鸡蛋可是我帮忙打的哦？"

    lxc_ "看你突然这么得意，我还以为鸡蛋是你生的呢。"
    show sy clothes2_front1 pout at angry_stomp
    sy_ "你！我又不是哈比那种生物！只有她们才会吃自己的蛋！"
    lxc_ "……还真有这种事？抱歉，刚刚我就随口胡扯而已。"
    "但你要吐槽的不应该是你根本不会下蛋吗……"
    xm_ focus "不过，也不是所有的哈比都会吃自己的蛋就是了。" with dissolve
    show xm clothes2_front2_no smile_close with dissolve
    xm_ "毕竟把蛋拿出去卖更划算嘛！"
    "把自己生的蛋拿出去卖……听起来更可怕了好吧。"
    lxc_ "所以，我们家的大小姐是受什么刺激了？"
    lxc_ "我还以为上次尝试过后，你就不想再下厨了呢。"
    show sy bewilderment at look_away_small
    sy_ "……总得做出点改变吧。"
    show sy clothes2_front1 sigh with dissolve
    sy_ "要是一直停在原地，就和以前待在古堡时没什么区别了。"
    lxc_ "是吗，挺好的。"
    lxc_ "期待哪天能吃到你亲手做的饭。"
    show sy smile_close at nod_small
    sy_ "哼，你就洗干净脖子给我等着吧。"
    "……这句话不是这么用的吧。"
    "希望之后厨房不会被她弄爆炸了。"

    scene bg_living_room_1
    with fade
    show sy clothes2_front1 smile_close at left with dissolve
    show xm clothes2_front2_no smile at right with dissolve

    "吃完早餐，看着正在收拾的时语和星弥，我不由自主地想起了昨晚的事。"
    "刚刚大家都对此闭口不谈，就像什么都没发生过一样。"
    "也不是不能理解，哪怕没什么越界的行为，但总归是亲密接触。"
    "换作是我，大概也不想主动提起这种让人心跳加速的事。"
    "但她们是为了我才特意做这种事的，既然被这样鼓励、被这样安慰，我觉得至少得好好说声谢谢。"
    lxc_ "昨晚的事……谢了。"
    lxc_ "虽然不知道你们为什么这么做，但我难得地睡了个特别安稳的觉。"
    lxc_ "真的挺感谢的，要知道对上班族来说，能睡个好觉实在太难得了——"
    show xm clothes2_front3_no pout skin_shy kp13wl at angry_stomp
    show sy clothes2_front1 shy skin_shy kp8wl at look_away_small
    xm_ clothes2_front3_no pout "……真是坏心眼呢。" with dissolve

    lxc_ "嗯？"
    xm_ pout "明明我们都特意闭口不谈了，您却还是故意把昨晚的事提了起来。" with dissolve
    lxc_ "我……"
    show xm oo hide_fx at emphasis_pop
    xm_ "您就这么想看我们害羞的样子吗？！"
    show sy hide_fx with dissolve
    "星弥突然气鼓鼓地开始埋怨，时语则满脸通红，低头说不出话。"

    lxc_ "冤枉啊……"
    "难道说，想道谢也有错吗？"
    lxc_ "我作为当事人，总不能当作什么事都没发生吧。"
    sy_ shy "……我去洗碗了！" with dissolve
    show sy at char_exit_left
    pause 0.4
    hide sy
    "时语立刻逃离了这个修罗场。"
    "喂，跑之前先带上我啊！"
    "错失最佳逃跑时机的我，只好老实留在原地，承受星弥的怒火。"
    show xm pout at excited_lean_forward
    "只见她鼓起脸颊，一副气势汹汹的样子走到我面前。"
    "正当我准备求饶时——"

    show xm cat_mouth with dissolve

    xm_ "嘻嘻，吓到了吗？"

    "星弥凑到了我的耳边，轻声说道。"
    lxc_ "欸？"
    xm_ cat_mouth "我是故意的啦，就是想假装生气一下，看看您会有什么反应？" with dissolve
    lxc_ "是、是这样吗？"
    xm_ shy "毕竟，您可是看到了我们害羞的一面哦？" with dissolve
    xm_ smile "那我想着，至少也得看一下您手足无措的样子才行。" with dissolve
    xm_ smile_close skin_blush "这样才能心理平衡嘛。" with dissolve
    "原来如此。"
    xm_ smile skin_blush "好了，就不继续捉弄您了，我去帮时语洗碗了！" with dissolve
    show xm smile at excited_lean_forward_undo
    "星弥的想法，倒也不是不能理解。"
    "但，这真的是她的全部想法吗？"
    "她微微泛红的脸颊和发烫的耳朵，印证了我的猜测。"
    lxc_ "如果你真是这么想的，那为什么你的耳朵会发红呢？"
    show xm oo skin_shy kp1wl at emphasis_pop
    xm_ "欸？这、这只是……"
    show xm hide_fx with dissolve
    lxc_ "刚刚的话，只是你用来遮掩害羞的方式，对吧？"
    xm_ "……！"
    lxc_ "一向温和的星弥因为害羞而假装生气，也不是不能理解。"
    lxc_ "毕竟昨晚的事确实很——啊！"
    with hpunch
    "擦桌子的布块精准地命中了我的头部。"

    show xm pout at angry_stomp
    xm_ "林先生是大笨蛋！一点都不懂得体贴少女心！"
    show xm at char_exit_right
    pause 0.4
    hide xm
    "星弥抛下这句话后，立刻逃进了厨房。"
    "……唉，我只是想道个谢而已，怎么就变成坏人了呢？"
    "我拿起丢过来的布块，只见它自动摊开，上面因为魔法浮现出几个小小的字："
    "【不用谢(/ /•/ω/•/ /)】"
    "哈，还真是不坦率呢。"

    play music bgm_7 fadeout 1.0 fadein 1.0
    scene bg_living_room_1
    with fade
    show bg_living_room_1:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve
    show sy clothes2_front1 smile at left with dissolve
    show xm clothes2_front3_no smile at right with dissolve

    lxc_ "来打游戏吧。"


    sy_ surprised_but "你居然会主动提议打游戏？还真是少见呢。" with dissolve
    lxc_ "心情好嘛，而且难得放假，不打游戏多可惜。"
    lxc_ "今天玩《猛汉》吧，星弥要一起玩吗？"


    show xm astonished at emphasis_pop
    xm_ "我？可以吗？"
    lxc_ "当然，大家一起玩更有意思。"
    show xm bewilderment with dissolve
    xm_ "但是，我现在开始玩，游戏进度什么的，也跟不上你们吧？"
    lxc_ "啊，进度你不用担心。"
    lxc_ "这个游戏宅家里蹲吸血鬼已经把几个平台的《猛汉》都给打通关了，所以我们的进度是一样的。"

    show sy pout at angry_stomp
    sy_ "谁是家里蹲吸血鬼啊！我这不是没新游戏玩，只好把旧游戏都给通关了嘛。"

    lxc_ "难道不是因为《猛汉》真的好玩吗？"
    show sy bewilderment at look_away_small
    sy_ "……也有这方面的原因就是了。"

    show xm focus at nod_small
    xm_ "好吧，那我会加油的，尽量不拖大家后腿！"

    lxc_ "嗯，放轻松就好。"
    lxc_ "打游戏嘛，开心最重要。"
    lxc_ "时语你开房间吧。"
    show sy clothes2_front2 laugh_open at celebrate_jump
    sy_ "开了开了！我想做鸭嘴兽的装备，我们来打它吧！"

    lxc_ "鸭嘴兽啊……那我选盾枪好了。"
    xm_ focus "我该选什么装备好呢？" with dissolve
    lxc_ "我想想……选这个御猫棍吧。"
    lxc_ "既可爱，操作也不复杂，重复按这个技能就行。"
    lxc_ "星弥你是魔女嘛，把这个武器想象成在远处使用猫咪魔法攻击敌人就好。"
    show xm clothes2_front2_no focus at emphasis_pop
    xm_ "把猫咪发射出去的魔法吗……嗯，我明白了！"
    show sy clothes2_front2 focus at excited_lean_forward
    sy_ "永恒星辰猎团，出击！全弹发射！"

    "一遇上鸭嘴兽，时语就开始疯狂射击。"
    "我负责在前面牵制怪物，星弥则是在后面慢慢摸索着操作方式。"
    show xm oo kp15wl at shocked_step_back
    xm_ "按这个键是发射猫咪来着……啊哇哇！对方朝我冲过来了！好大的火球！"

    "她激动地举起掌机，整个人都随着屏幕里的角色晃动了起来，甚至还晃到了我身上。"
    lxc_ "没事，有我在！"
    "我提起盾牌，挡住了袭向星弥的火球。"
    show xm smile hide_fx at bounce_small
    xm_ "哇，得救了！"

    lxc_ "趁现在继续进攻——糟了！被捕食了！"
    show sy clothes2_front1 cat_mouth at excited_lean_forward_undo
    sy_ "噗，我上个子弹的功夫，你就顶不住了？"

    sy_ smile_close "唉，人类就是弱小，没了本小姐就是不行啊。" with dissolve
    "时语一发导弹把怪物炸飞，随后给我补上了一颗治疗弹。"
    lxc_ "谢了！我来吸引注意，你们继续攻击吧！"
    show xm clothes2_front2_no focus at emphasis_pop
    xm_ "猫咪魔法猫咪魔法猫咪魔法！！！"

    "后方不断施法的星弥在持续提供火力压制。"
    show sy clothes2_front2 focus at emphasis_pop
    sy_ "该结束了！吃我超级无敌粉尘大爆炸！"

    with vpunch
    show sy clothes2_front2 laugh_open at celebrate_jump
    "时语把炸弹塞到鸭嘴兽的嘴中，随后绽放出一朵美丽的蘑菇云。"

    sy_ "哼哼，在本小姐的带领下，永恒星辰猎团又取得了一次伟大的胜利。"
    sy_ clothes2_front1 cat_mouth "作为被我救下的人类，是不是该说点什么呢？" with dissolve
    "她用右手臂蹭了蹭我，露出得意的小表情。"
    lxc_ "是是。多亏了时语大人的英明领导，我们才能战胜这次的强敌！"
    lxc_ "满意了吧？"
    sy_ smile_close "勉勉强强吧，下次得更有感情地赞美我才行。" with dissolve
    "再投入点感情，我怕你的嘴角都要翘到天上去了。"
    lxc_ "星弥觉得怎么样，第一次玩《猛汉》觉得有意思吗？"
    show xm clothes2_front2_no focus at emphasis_pop
    xm_ "猫咪魔法猫咪魔法猫咪魔法——！"
    lxc_ "呃，它已经倒下不用再攻击了！！！"
    show xm oo at shocked_step_back
    xm_ "欸，是这样吗？"
    "要是不知情的人看到刚刚那一幕，还以为她和鸭嘴兽有什么血海深仇呢……"
    show xm smile with dissolve
    xm_ "我觉得……还挺好玩的！虽然操作还不太熟，但大家一起合作讨伐怪物的氛围，我很喜欢！"
    xm_ bewilderment "如果我在里世界旅行时也能有伙伴一起的话……" with dissolve
    show xm bewilderment at deny_shake_small
    xm_ "不行不行，不要去设想没发生过的事！"
    show xm smile at bounce_small
    xm_ "我们继续玩吧！"
    lxc_ "嗯。"
    show sy clothes2_front2 cat_mouth with dissolve
    sy_ "那下一只我们来讨伐远古鹦鹉螺兽！"
    lxc_ "喂，那可是高难度的怪物啊。"
    sy_ smile "不试试怎么知道能不能打过嘛。" with dissolve
    "之后，我们不断讨伐各种各样的怪物，收获了许多素材和装备。"
    show xm focus at lean_in
    xm_ "说起来，林先生为什么会玩盾牌类型的武器呢？"
    xm_ bewilderment "一般来说，男生不都更喜欢进攻性强的武器吗？" with dissolve
    lxc_ "为什么要玩盾枪啊……"
    "我看了时语一眼。"
    show sy clothes2_front1 laugh_open at bounce_small
    sy_ "区区鹦鹉螺兽，在我们的合作下还不是手到擒来~"
    "在我和星弥闲聊的功夫，时语已经把怪物身上的素材挖得七七八八了。"
    lxc_ "……"
    lxc_ "咳咳，其实没什么特别的理由。"
    lxc_ "只是有位前辈，他是用盾枪，和一位用枪炮的女孩子组队玩的。"
    lxc_ "我有点羡慕他们玩游戏时的氛围，所以想模仿一下，看看会有什么感受。"
    show xm focus at excited_lean_forward
    xm_ "然后呢然后呢？"
    lxc_ "然后就发现……我根本不会用这武器啊！"
    lxc_ "要是换成其他更熟练的武器，早就打完了。"
    show xm astonished at excited_lean_forward_undo
    xm_ "啊，有点意外的现实发言呢……"
    lxc_ "但在这个过程中，不管是替她挡下危险攻击，还是被她的治疗弹及时救下，都让人觉得很开心。"
    lxc_ "最后我明白了，重点不在于用什么武器，也不在于武器熟不熟练，而在于和别人一起玩这个过程本身。"
    lxc_ "就像你说的一样，大家一起合作、一起打败怪物的那种氛围，真的很让人喜欢。"
    lxc_ "——啊，挖出宝玉了。"
    show sy clothes2_front1 pout kp13wl at angry_stomp
    sy_ "可恶，为什么你这么容易就挖出稀有素材啊！"
    show sy hide_fx with dissolve
    show xm clothes2_front2_no smile with dissolve
    xm_ "嘿嘿……我明白了，要是以后也有机会一起玩就好了。"
    sy_ smile "说什么呢，当然有机会啊。" with dissolve
    sy_ smile_close "反正两个人也是玩，三个人也是玩，那还是越多人玩越好。" with dissolve
    show sy clothes2_front2 focus at emphasis_pop
    sy_ "更何况我们队伍还缺一个输出手，这个位置非星弥你莫属！"
    show xm laugh_open at bounce_small
    xm_ "……嗯！我们继续开下一局吧！"
    lxc_ "好。"

    play sound sound_vibrate

    "嘀嘀嘀——"
    "手机不合时宜地响了。"
    lxc_ "啊，外卖到了，你们先玩。"
    sy_ clothes2_front1 surprised_but "你还点了外卖，今天不做饭了？" with dissolve
    lxc_ "偶尔也要偷下懒嘛。"
    lxc_ "你们先玩吧，我很快回来。"
    show xm smile at nod_small
    xm_ "嗯，那我们等你！"
    sy_ cat_mouth "你不快点回来，我们就要把素材全挖走了哦？" with dissolve
    "已经把素材差不多挖完的人还好意思说啊……"

    scene bg_community_4
    with fade
    play music bgm_8 fadeout 1.0 fadein 1.0
    show bg_community_4:
        zoom 1.04
        xalign 0.5
        yalign 0.0
    with dissolve

    "来到楼下，黄昏的晚风迎面缓缓吹来，远处的天空像被染开的橘红色水彩。"
    "不知不觉就玩了这么久的游戏，时间过得真快啊……不管是今天下午，还是最近两个月。"
    "好像有人说过，人越是感到快乐，时间就会过得越快。"
    "和她们一起生活的这段日子里，我确实过得很开心。"
    "真是神奇，明明不久前我还是个浑浑噩噩的普通上班族，过着重复又看不到尽头的生活。"
    "下班回到家，只有黑漆漆的房间迎接自己。"
    "而现在，因为来自里世界的她们，欢笑的日子不知不觉就变多了。"
    "多亏于此，我也开始有了停下脚步、抬头看看天空的闲心。"
    "橘红色的天空，意外地很好看。"

    scene bg_living_room_4
    with fade
    show bg_living_room_4:
        zoom 1.06
        xalign 0.5
        yalign 1.0
    with dissolve
    show sy clothes2_front1 pout at left with dissolve
    show xm clothes2_front2_no smile at right with dissolve

    "推开门回到家，两位少女立刻迎了上来。"


    show xm clothes2_front2_no focus at lean_in
    xm_ "您回来了！路上没出什么事吧？"


    show sy clothes2_front1 pout at look_away_small
    sy_ "怎么这么慢？我们等了你好久哦……"

    show xm smile_close with dissolve
    xm_ "时语刚刚还想出去找你呢，说怕你被什么奇怪的人抓走了……"

    xm_ smile "我倒觉得要相信林先生，在家乖乖等就好啦。" with dissolve
    show sy clothes2_front1 oo skin_shy kp1wl at emphasis_pop
    sy_ "星弥！不要每次都说多余的话啦……！"
    show sy hide_fx with dissolve
    show xm shy skin_shy with dissolve
    sy_ pout "而且你刚刚不也一脸担心的样子嘛！" with dissolve
    xm_ shy "我、我那只是……！" with dissolve
    "看着她们俩你一句我一句争辩的样子，我不禁笑了起来。"
    lxc_ "这样啊，抱歉抱歉，我稍微逛了一下，回来晚了点，哈哈。"

    show sy smile skin_blush with dissolve
    show xm smile_close skin_blush with dissolve

    sy_ bewilderment skin_blush "呜哇，这个人类道歉的时候居然还在偷笑……" with dissolve
    xm_ smile_close skin_blush "而且眼神还有点……温柔又宠溺的感觉？"
    lxc_ "有吗？"
    "我只是觉得，家里亮着灯，有人等你回来的感觉，真的还不错。"
    "不过要是说出来，时语恐怕要起鸡皮疙瘩了……"
    show xm smile at bounce_small
    xm_ "总之，欢迎回家！"
    show sy clothes2_front1 smile with dissolve
    sy_ "哼，回来了就好。"
    lxc_ "嗯，我回来了。"
    sy_ cat_mouth "所以，你买了什么外卖啊？" with dissolve
    lxc_ "新品蛋糕，晚饭时间吃点好的，换换心情。"
    show xm laugh_open kp4wl at celebrate_jump
    xm_ "哇，是『星空慕斯三重奏』！"
    show sy clothes2_front1 laugh_open kp4wl at bounce_small
    sy_ "哦哦，看起来就很好吃的样子……！"
    show xm hide_fx with dissolve
    show sy hide_fx with dissolve
    lxc_ "很不错吧？"
    lxc_ "可惜另外一份快递就没这么快送到了。"
    sy_ surprised_but "……你还点了两份外卖？" with dissolve
    lxc_ "虽然你说过我是笨蛋，但我看你也差不多嘛。"
    lxc_ "既然是快递，那送过来的肯定不是外卖啊？"
    sy_ pout "……哼，那送过来是什么？" with dissolve
    lxc_ "游戏卡带。"
    show sy clothes2_front1 astonished kp1wl at emphasis_pop
    sy_ "……欸？！真的假的？"
    show sy hide_fx with dissolve
    lxc_ "如假包换。"
    show xm smile_close at nod_small
    xm_ "林先生，时语，不要再聊天啦。"
    xm_ laugh_open "你们也快点吃吧，这个蛋糕好好吃！" with dissolve
    lxc_ "星弥，你嘴上都沾满奶油了……"
    show xm shy skin_shy at shy_look_away
    xm_ "……！不、不要看我啦……！"


    scene bg_office_1
    with Fade(0.5,0.5,0.5)
    play music bgm_14 fadeout 1.0 fadein 1.0
    show bg_office_1:
        zoom 1.05
        xalign 0.6
        yalign 1.0
    with dissolve
    "欢乐的时光总是过得很快，但现实不会因此而放慢脚步。"
    "今天又是加班的一天。"
    "原本计划两周前就该上线的游戏，因为测试期间冒出一堆奇怪的BUG，不得不延期。"
    "不过项目延期在我们公司也不算新鲜事，毕竟一开始规划的工期就很短，出什么状况都不意外，更何况这次安排的还是新人程序。"
    rszg_ "小林，今天也在加班啊？"
    show bg_office_1:
        zoom 1.10
        xalign 0.62
        yalign 1.0
    with dissolve
    "人事主管不知不觉地出现在我工位旁。"
    "他脸上挂着职业性的微笑，但我知道，这只是皮笑肉不笑。"
    lxc_ "冯主管，有什么事吗？"
    play music bgm_3 fadeout 1.0 fadein 1.0
    rszg_ "关于项目延期的事，我想和你聊聊。"
    rszg_ "测试部的同事反馈，这次延期主要是因为游戏里的BUG数量太多了。"
    show bg_office_1:
        zoom 1.13
        xalign 0.64
        yalign 1.0
    with dissolve
    rszg_ "我想问问，是不是因为你们策划案的需求描述，写得不够明确？"
    lxc_ "……"
    "测试部人太少，所以归人事管。"
    "他一上来就定性……是打算把锅甩给别人，好让自己免责？"
    "可出了这么多BUG，要甩锅也得找程序才对吧？"
    lxc_ "需求文档的每一版我都有保存，都是按照流程标准编写的，您可以随时查看。"
    rszg_ "哎，我当然不是说你写得不好。"
    rszg_ "只不过总得给上面一个交代，你说是不是？"
    lxc_ "那就应该找程……不，没什么。"
    "我忽然想明白，他为什么专挑晚上加班、而且公司人比较少的时候来找我。"
    "他在公司待了这么多年，不可能不知道问题出在哪儿。"
    "他是明知故问的。"
    "故意挑老大出差的这段时间找我发难。"
    "冯主管、程序员小冯……原来如此，是走后门进来的关系户吗？"
    "又是关系户……怪不得这种水平也能通过面试。"
    rszg_ "小林啊，我知道你加班很辛苦，也为项目付出了很多。"
    rszg_ "但一码归一码，你的表现啊……"
    "算了，他爱怎么说就怎么说吧，类似的事也不是第一次了。"
    rszg_ "虽然你负责过公司不少项目，但工作态度是不是有点问题呢？"
    rszg_ "我听说你总对新来的同事大呼小叫，提些不合理的要求……"
    show bg_office_1:
        zoom 1.16
        xalign 0.66
        yalign 1.0
    with dissolve
    "烦躁。"
    rszg_ "你在公司待了这么久，也没做出点成绩，都是因为……"
    rszg_ "要不是我力排众议，你早就——"
    "装模做样。"
    rszg_ "项目延期了，你作为执行主策总得负点责任吧？不然我也不好向上面交代。"
    rszg_ "你主动认错，受罚还能轻点。"
    rszg_ "而且测试部反馈，BUG多是因为需求描……"
    "我看着他滔滔不绝地说些有的没的，突然觉得特别没意思。"
    "恶心。"
    show bg_office_1:
        zoom 1.02
        xalign 0.5
        yalign 1.0
    with dissolve
    "看着时针分毫不差地指到「 10 」这个数字后，我立刻站了起来。"
    with hpunch
    lxc_ "不好意思，我到点该下班了。"
    rszg_ "哎，你这是什么态度啊？我好心为你着想，你还——"
    "我没有看他的表情，也没有听他最后说的废话，关上电脑后直接离开了公司。"

    scene bg_street_2
    show bg_street_2 at bg_pan_right
    with fade
    play music bgm_12 fadeout 1.0 fadein 1.0

    "经过街头的路灯，影子被拉长又压短。"
    "所以我这些天的加班到底是为了什么？"
    "为项目劳心劳力，最后换来一句「 这个锅由你来背 」？"
    "包容关系户、熬夜改方案、帮人擦屁股……原来认真干活的人活该吃亏。"
    lxc_ "真可笑……"
    show bg_street_2:
        zoom 1.12
        xalign 0.55
        yalign 1.0
    with dissolve
    "也许职场本来就不需要较真的人。"
    "就像那个新来的，能力差态度烂，但会甩锅会抱大腿，反而混得如鱼得水。"
    "而我这种埋头干活的，活该背锅。"
    with vpunch
    lxc_ "这种工作去他……！"
    "刚想开口，看到路边睡在大理石上的流浪汉，骂到嘴边的话又咽了回去。"
    lxc_ "冲动了啊……"
    show bg_street_2:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve
    "或许刚刚应该装模做样地道歉，这样等他发完脾气，事情说不定还有回转的余地。"
    "现在直接摆脸色，或许真的会「 因为左脚先进公司 」而被开除了。"
    lxc_ "唉。"
    "我这些天加班，也不全是为了项目，更多的是为了自己……还有家里的她们。"
    "加班有餐补，还有绩效奖金，虽然不多，但也是一份收入。"
    "要是丢了工作，该怎么办呢……"

    scene bg_living_room_2
    with fade
    play music bgm_13 fadeout 1.0 fadein 1.0
    show bg_living_room_2:
        zoom 1.06
        xalign 0.5
        yalign 1.0
    with dissolve
    show sy clothes2_front1 bewilderment at left with dissolve
    show xm clothes2_side1 bewilderment at right with dissolve



    xm_ "啊，您回来了！"


    sy_ "你回来了……今天比平时更晚呢。"
    lxc_ "……嗯，我回来了。"
    "虽然刚刚发生了很不愉快的事，但欣慰的是，回到家后还有她们会迎接我。"


    show xm clothes2_side1 bewilderment at lean_in
    xm_ "林先生，您还好吧？您的样子，好像有点……"
    lxc_ "……啊，没事，就是有点累而已。"
    "不好不好，可不能在她们面前表现得这么颓废。"


    show sy sigh at lean_in
    sy_ "本小姐不用闻味道都知道，你现在的样子可不像『 没事 』啊。"

    show sy focus at nod_small
    sy_ "如果遇到了什么麻烦，可以和我们说说看的。"
    "我深吸一口气，努力挤出笑容。"
    lxc_ "……真的没事，就是加班有点累了而已。我先去洗澡了。"
    "还没想好该怎么面对她们，我赶紧找了个借口，逃进了洗手间。"

    scene bg_living_room_3
    with fade
    show bg_living_room_3:
        zoom 1.06
        xalign 0.5
        yalign 1.0
    with dissolve

    "洗完澡，身体虽然清爽了一些，但心情却还是很郁闷。"
    "……明天还要上班，早点睡吧。"

    scene black
    with ImageDissolve("rule/eyeclose.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)

    window hide
    pause 0.5
    show text "{color=#FFFFFF}{size=+40}「 工作态度是不是有问题 」{/size}{/color}" as phrase1:
        xalign 0.25 yalign 0.12
    with dissolve
    pause 0.6
    show text "{color=#FFFFFF}{size=+40}「 没做出点成绩 」{/size}{/color}" as phrase2:
        xalign 0.72 yalign 0.38
    with dissolve
    pause 0.6
    show text "{color=#FFFFFF}{size=+40}「 主动认错，受罚还能轻点 」……{/size}{/color}" as phrase3:
        xalign 0.3 yalign 0.7
    with dissolve
    pause 1.2
    window show

    "一闭上眼，脑海里却浮现出那些恶心的话语。"

    pause 0.3
    scene bg_office_1
    show bg_office_1:
        zoom 1.18
        xalign 0.65
        yalign 1.0
    with ImageDissolve("rule/eyeopen.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)
    "本想强行无视它们，但在快要睡着时，周围的场景却变回了那个压抑的办公室，瞬间把我吓醒。"
    scene bg_living_room_3
    show bg_living_room_3:
        zoom 1.08
        xalign 0.5
        yalign 1.0
    with hpunch
    lxc_ "……睡不着啊。"

    menu:
        "或许找人说说话会好一点……"
        "找时语聊一聊":
            $ third_choice = 1
            jump choice_7_a_zhao_shi_yu_liao_yi_liao
        "找星弥聊一聊":
            $ third_choice = 2
            jump choice_8_b_zhao_xing_mi_liao_yi_liao
        "还是自己一个人静一静吧":
            $ third_choice = 3
            jump choice_9_c_hai_shi_zi_ji_yi_ge_ren_jing_yi_jing_ba

    return

label choice_7_a_zhao_shi_yu_liao_yi_liao:


    play music bgm_12 fadeout 1.0 fadein 1.0

    "要不找时语聊一聊吧。"
    "不过，这么晚她应该也睡了吧？"

    scene sd6
    with fade

    "我走出帐篷，只见黑暗中电视屏幕的光还在微微闪烁，时语和平时一样坐在沙发上，专注地操作着手柄。"
    "屏幕里她的角色正在暴揍一只体型庞大的水豚兽。"
    lxc_ "这么晚了还不睡，你也睡不着？"
    sy_ clothes2_front1 focus "……你忘了我是血族吗？" with dissolve
    lxc_ "对哦，血族都是夜猫子来着。"
    sy_ pout "才不是，这只是正常的作息而已。" with dissolve

    sy_ bewilderment "而且，看到你那个样子我怎么可能还睡得着嘛……" with dissolve
    "她暂停游戏，拍了拍身边的沙发。"
    sy_ "坐吧。"

    scene bg_living_room_3
    with fade

    show sy clothes2_front1 smile at center with dissolve

    "我犹豫着坐下，她突然凑近，仔细地盯着我的脸。"
    show sy focus at lean_in
    sy_ "眼睛里有血丝，眉头皱得能夹死蚊子……今天在公司发生了不好的事？"
    lxc_ "……您的视力还真好呢。"
    sy_ pout "别转移话题。" with dissolve
    lxc_ "很明显吗？"
    sy_ sigh "你平时回家虽然累，眼神就像死鱼一样，但今天就像那什么……『 仰望星空 』一样。" with dissolve
    lxc_ "这不还是死鱼眼嘛……"
    show sy cat_mouth at emphasis_pop
    sy_ "反正睡不着，来陪我打游戏吧。"
    lxc_ "……现在没什么心情啊。"
    show sy focus at emphasis_pop
    sy_ "就是没心情才要打！把水豚兽当成惹你生气的人，往死里揍！"
    "她强行把手柄塞到我手上。"
    play music bgm_15 fadeout 1.0 fadein 1.0
    lxc_ "水豚兽这么可爱，我怎么舍得下手啊。"

    scene bg_living_room_3
    with fade

    "半小时后，水豚兽被我们揍得趴在地上，无力地抽搐着。"
    show sy clothes2_front1 smile at center with dissolve
    sy_ "怎么样，解气了吧？"

    "我望着屏幕上「 任务完成 」的字样，视线忽然有点模糊了。"
    show sy oo at shocked_step_back
    sy_ "……喂，别这样啊。我本来是想让你开心才叫你打游戏的。"
    lxc_ "只是打得有点久，眼睛有点干而已。"
    "我用手擦了擦眼角，尽力掩盖自己的失态。"
    sy_ bewilderment "……" with dissolve
    sy_ sigh "真拿你没办法。" with dissolve
    show sy sigh with dissolve
    "忽然，脸上迎来了柔软的触感。"
    scene black
    with ImageDissolve("rule/eyeclose.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)
    scene bg_living_room_3
    show sy smile at center:
        zoom 1.5
        yoffset 1300


    with ImageDissolve("rule/eyeopen.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)

    "时语轻轻抱住我，把我的头靠在她肩上。"

    sy_ "这样会不会好受一点？"
    lxc_ "……嗯。"
    sy_ smile_close "那就好。" with dissolve
    "时语的身体小小的，但靠上去却很温暖。"
    lxc_ "……我明明已经尽力把事做好了。"
    sy_ smile "我知道，你已经做得很好了。" with dissolve
    lxc_ "但是，却还是受到了责备，为什么？"
    sy_ sigh "……有些事，就是这么不讲理吧。" with dissolve
    lxc_ "……真不公平啊。"
    sy_ bewilderment "……" with dissolve

    sy_ "我一直觉得，你太勉强自己了。"
    "时语一边摸着我的头，一边慢慢说道。"
    sy_ sigh "每天看你一脸疲惫地回家……我心里就有点不舒服。" with dissolve
    sy_ bewilderment "但一想到自己也是让你变得这么累的原因之一，就什么话也说不出口了。" with dissolve
    show sy sigh at look_away_small
    sy_ "要是我没给你添麻烦，或许你就不会这么辛苦和难受了……我时不时会这么想。"
    lxc_ "……不是这样的。"
    "我抬起头 ，看着她的双眼。"
    show sy astonished with dissolve
    lxc_ "哪怕没有你和星弥，今天的事也还是会发生，那些让人痛苦的事也还是一样存在。"
    show sy calm at look_away_small

    "我把公司里发生的事，断断续续地告诉了时语。"
    "时语一直安静地听着，直到我说完才开口。"
    show sy clothes2_side1 sigh with dissolve
    sy_ "……不管去到哪，和那些贵族一样装模作样、表里不一的人，也还是到处都有呢。"
    lxc_ "你也遇到过类似的事吗？"
    sy_ sigh "是啊。" with dissolve
    sy_ calm "我在逃到表世界前，经常要去参加贵族间的交流会。" with dissolve
    sy_ sigh "在那里，许多人为了利益和面子，戴上不同的面具，伪装出同一副样子。" with dissolve
    sy_ bewilderment "……我也一样，为了附和她们，不得不装出一副顺从、乖巧的模样。" with dissolve
    sy_ despise "现在想起来，还真是恶心呢。" with dissolve
    lxc_ "但你最后还是离开了那里。"
    sy_ focus "对啊，我实在受不了那种气氛，所以才逃了出来。" with dissolve
    sy_ smile "这么看，我们也算是同病相怜呢。" with dissolve
    lxc_ "……是啊。"
    show sy clothes2_front1 smile kp10wl at look_away_small
    sy_ "所以，你不是孤独一人的。至少，在这件事上我是你的同伴。"
    show sy hide_fx with dissolve
    "时语把我抱得更紧了一些，像是想用这种方式传达她的心意。"
    sy_ smile "在你家住的这段时间里，我真的过得很开心。" with dissolve
    sy_ smile_close "彼此之间能互相理解，不用伪装，不用设防，可以完完全全地做自己。" with dissolve
    sy_ shy skin_shy "在这件事上，我真的，真的很谢谢你收留了我和星弥。" with dissolve
    lxc_ "……嗯。"
    sy_ focus skin_blush "所以，你要是不开心的话，不要硬撑，不要把我们当外人，好吗？" with dissolve
    lxc_ "……我知道了。"
    $ route_sy_score = (1 if first_choice in (1, 3) else 0) + (1 if second_choice in (1, 3) else 0) + (1 if third_choice in (1, 3) else 0)
    $ route_xm_score = (1 if first_choice in (2, 3) else 0) + (1 if second_choice in (2, 3) else 0) + (1 if third_choice in (2, 3) else 0)

    if route_sy_score >= route_xm_score:
        "她是认真的。"
        "她的真心，不仅通过对话，还通过那清晰、有力的心跳声，真切地传达了过来。"
        "我那一直封闭、压抑的内心，似乎也因此裂开了一道小小的缝隙。"

    lxc_ "谢谢你，时语。"
    show sy clothes2_front1 shy skin_blush at look_away_small
    sy_ "……这还差不多。"
    show sy smile_close with dissolve
    "昏暗的灯光下，少女那带着温柔笑意的侧脸，深深烙印在了我的心里。"

    if route_sy_score > route_xm_score:
        jump choice_7_a_route_shiyu
    elif route_xm_score > route_sy_score:
        jump choice_7_a_route_xingmi
    else:
        jump choice_7_a_route_harem

label branch_a_rooftop_common(name):
    scene bg_community_5
    with Fade(0.5,0.5,0.5)

    pause 0.5

    if name == "第三人称视角":
        scene bg_sky_3
        show bg_sky_3 at bg_pan_right
        with fade
        pause 0.8

    scene cg1001
    with Fade(0.5,0.5,0.5)

    $ heroine = True
    $ heroine_name = name

    play music bgm_21 fadeout 1.0 fadein 1.0
    xm_ clothes1_side1 smile "林先生睡了吗？"
    sy_ clothes1_side1 smile "睡了，哄了他好一会儿才睡着呢。"
    return

label choice_7_a_route_shiyu:

    call branch_a_rooftop_common ("星弥的视角") from _call_branch_a_rooftop_common
    show cg1002 with dis_master
    sy_ pout "哼，真是没个大人样。" with dissolve
    show cg1003 with dis_master
    xm_ cat_mouth "虽然嘴上在吐槽，但时语的表情却在笑呢。" with dissolve
    show cg1004 with dis_master
    sy_ oo "有、有吗？肯定是你看错了啦！" with dissolve
    show cg1005 with dis_master
    xm_ smile_close "呵呵。" with dissolve

    "是这样啊，原来时语她对林先生……"
    jump route_003_shiyu_common

label choice_7_a_route_xingmi:

    call branch_a_rooftop_common ("时语的视角") from _call_branch_a_rooftop_common_1
    sy_ smile "哼，真是没个大人样。" with dissolve
    show cg10018 with dis_master
    xm_ pout "这样啊，真羡慕呢……明明他也可以找我商量的。" with dissolve
    show cg10019 with dis_master
    xm_ cat_mouth "……要不等下直接夜袭他帐篷好了，呵呵。"
    show cg10020 with dis_master
    sy_ oo "呃，星弥你冷静点！他好不容易才睡着的哦？"
    show cg10021 with dis_master
    xm_ smile skin_blush "……开玩笑的啦！我怎么会做那种事呢？" with dissolve
    "怎么看都不像是在开玩笑吧……"
    "不过，原来是这样啊，星弥她对林小凑……"
    show cg10022 with dis_master
    sy_ bewilderment "……" with dissolve

    jump route_003_xingmi_common

label choice_7_a_route_harem:

    call branch_a_rooftop_common ("第三人称视角") from _call_branch_a_rooftop_common_2
    sy_ smile "哼，真是没个大人样。" with dissolve
    show cg10018 with dis_master
    xm_ pout "这样啊，真羡慕呢……明明他也可以找我商量的。" with dissolve
    show cg10019 with dis_master
    xm_ cat_mouth "……要不等下直接夜袭他帐篷好了，呵呵。"
    show cg10020 with dis_master
    sy_ oo "呃，星弥你冷静点！他好不容易才睡着的哦？"
    show cg10021 with dis_master
    xm_ smile skin_blush "……开玩笑的啦！我怎么会做那种事呢？" with dissolve
    show cg10040 with dis_master
    sy_ shy skin_shy "难道说，星弥你也……" with dissolve
    show cg10052 with dis_master
    xm_ astonished "嗯？" with dissolve
    sy_ shy "没、没什么。" with dissolve
    "银发少女微微偏过微微发红的脸，迅速转移了话题。"
    jump route_003_harem_common

label route_003_parting_words:

    "夜风吹过天台，两位少女做出了不同的选择。"
    "一位选择回归原本的世界，另一位选择为重要的人停留。"
    "虽然前方的道路不同，但这份共同生活过的回忆，会永远留在彼此心中。"
    return

label route_003_shiyu_common:
    hide cg1001
    show cg1001 with dis_master
    xm_ smile "说起来，我们在这边已经待了三个月了。" with dissolve
    sy_ smile skin_blush "是啊。"
    "她望着城市的灯火，银发在夜风中轻轻飘动。"
    sy_ smile "这三个月，感觉比在古堡里三年经历的事情都还要多。" with dissolve
    sy_ smile skin_blush "定居、打游戏、看电影、和你一起挤地铁……还有每天和某个人类斗嘴。" with dissolve
    xm_ smile "但很开心，不是吗？" with dissolve
    sy_ smile skin_blush "……或许吧。" with dissolve

    show cg1006 with dis_master

    sy_ sigh "只是有时候会忍不住想，这样的日子能持续到什么时候呢？" with dissolve
    sy_ sigh "人类的寿命不过百年，对血族来说，只是漫长岁月里很短的一段时光。" with dissolve
    show cg1007 with dis_master
    xm_ bewilderment "……" with dissolve
    "我明白她的意思，林先生会慢慢老去，而我们……不会。"
    "看着她忧愁的样子，或许她在犹豫到底要不要留下来吧。"
    "既然如此……"
    show cg1008 with dis_master
    xm_ focus "时语，你有没有想过回去？" with dissolve
    show cg1009 with dis_master
    sy_ bewilderment "回里世界吗？" with dissolve
    show cg10010 with dis_master
    xm_ sigh "嗯。毕竟这里……不是我们原本的世界嘛。" with dissolve

    sy_ bewilderment "我，我的话——" with dissolve
    show cg10011 with dis_master
    xm_ focus "我会回去的。" with dissolve
    show cg10012 with dis_master
    sy_ astonished "欸？" with dissolve
    xm_ focus "在里世界，我是魔女会新生代里最出色的一位，老师说过我有机会成为下一任茶话会的管理者。" with dissolve
    show cg10013 with dis_master
    xm_ bewilderment "但在这里，我连煮饭都会烧糊电饭煲……" with dissolve
    show cg10014 with dis_master
    sy_ sigh "……" with dissolve
    show cg10015 with dis_master
    xm_ sigh "而且，如果继续留在这里，说不定会给林先生带来更多麻烦。" with dissolve
    xm_ sigh "既然约定的时间快到了，还是离开比较好。" with dissolve
    sy_ sigh "……是吗。" with dissolve
    "她沉默了片刻，目光望向远方的星空。"
    sy_ sigh "既然这是你的决定……我尊重你。" with dissolve
    show cg10016 with dis_master
    sy_ smile "毕竟每个人都有自己必须走的路。" with dissolve
    sy_ "——但我要留下来。" with dissolve
    sy_ "人类的生活，比我想象中要有趣得多……至于家族那边的事，管他呢。" with dissolve
    sy_ "留下来，至少在他需要的时候，我可以陪在他身边。" with dissolve
    show cg10017 with dis_master
    xm_ smile "这样啊……嗯，很有时语的风格呢。" with dissolve
    "嗯，这样就好。"
    call route_003_parting_words from _call_route_003_parting_words

    jump after_menu_3

label route_003_xingmi_common:
    hide cg1001
    show cg1001 with dis_master
    sy_ smile skin_blush "说起来，不知不觉已经过去三个月了。"
    xm_ smile "嗯……总感觉发生了好多事呢。" with dissolve
    "她抬头仰望着夜空的星光，棕色的长发在晚风中轻轻飘动。"
    show cg10023 with dis_master
    xm_ focus "以前在里世界到处旅行时，也会遇到很多有趣的人和事。" with dissolve
    xm_ "只是我觉得自己像个过客，从不会在任何一个地方停留太久。" with dissolve
    show cg10024 with dis_master
    xm_ bewilderment "所以，最初我也只打算在这里暂住一段时间。" with dissolve
    show cg10025 with dis_master
    xm_ sigh "毕竟彼此之间都只是陌生人，我和林先生的初次见面甚至争吵了起来……" with dissolve
    show cg10026 with dis_master
    xm_ smile skin_blush "可随着朝夕相处，我却有了……不一样的想法。" with dissolve
    xm_ smile "和大家一起相处的日子，我总会莫名其妙地觉得开心。" with dissolve
    show cg10027 with dis_master
    xm_ shy skin_blush "特别是做菜时，每次想象林先生吃下时会露出什么样的表情，心里就会变得很温暖。" with dissolve
    show cg10028 with dis_master
    xm_ smile skin_blush "我很喜欢这样的生活。" with dissolve
    show cg10029 with dis_master
    xm_ sigh "只是，这样的日子还能持续多久呢……" with dissolve
    "她话里的意思，不只是之前约定的时间快到了，还有……我们和他之间不可逾越的寿命差距。"
    "看她那失落的样子，一定是想留在他身边吧。"
    "既然如此。"

    sy_ smile "我要回去了。" with dissolve
    show cg10030 with dis_master
    xm_ astonished "欸？" with dissolve
    sy_ smile "这几月玩得够疯了，是时候回去了。" with dissolve
    show cg10031 with dis_master
    sy_ sigh "再不回去，家里那些老头子肯定要唠叨个没完。" with dissolve
    show cg10032 with dis_master
    sy_ smile "而且，也是时候该把家族的事务正式接手到自己手上了。" with dissolve
    show cg10033 with dis_master
    xm_ sigh "这样啊……" with dissolve
    sy_ "这是我自己的决定，不会后悔的。" with dissolve
    sy_ "你也不要后悔。" with dissolve
    show cg10034 with dis_master
    xm_ smile "……我明白了。" with dissolve
    show cg10035 with dis_master
    xm_ smile_close "如果这是时语的决定……我会支持你的。" with dissolve
    sy_ "谢谢。" with dissolve
    sy_ "那你呢？要回去吗？" with dissolve
    show cg10036 with dis_master
    xm_ bewilderment "我……" with dissolve
    "她低下头，犹豫了一会儿。"
    show cg10037 with dis_master
    xm_ smile_close "……我想留下来。"
    show cg10038 with dis_master
    xm_ smile "茶话会那边本来就很随意，不用经常露面的。" with dissolve
    xm_ smile skin_blush "我至少……想陪林先生走完这段路。" with dissolve
    show cg10039 with dis_master
    xm_ smile_close skin_blush "想一直留在他身边，就像家人一样。" with dissolve
    sy_ smile "是吗，不也挺好嘛。" with dissolve
    "嗯，这样就好。"
    call route_003_parting_words from _call_route_003_parting_words_1

    jump xingmi_route

label route_003_harem_common:
    show cg10048 with dis_master
    sy_ smile skin_blush "说起来，自从在这里住下后，发生了好多事呢。" with dissolve
    xm_ smile "是啊，没想到我会在一个地方停留这么久……" with dissolve
    "棕发少女轻轻撩起耳边的发丝，望着远处城市的灯火，思绪却飘向了更远的地方。"

    jump route_003_harem_common_end

label route_003_harem_common_end:
    sy_ "大家一起出门买衣服、做饭、打游戏……" with dissolve
    xm_ "也发生过争吵、互相怀疑和误解……" with dissolve
    show cg10051 with dis_master
    sy_ "有开心、害羞的事。" with dissolve
    xm_ calm "也有难过、痛苦的事。" with dissolve
    "也许，人类的生活就是这样吧。"
    "也许，这就是所谓的日常吧。"
    show cg1005000000 with dis_master
    xm_ sigh "虽然只是短短几个月，却感觉已经过去很久、很久了。" with dissolve
    sy_ sigh "是啊，但时间要是能再慢一点，就更好了。" with dissolve
    "两人沉默片刻，不约而同地望向繁星闪烁的夜空。"
    show cg10051 with dis_master
    xm_ calm "和永恒不变的星辰相比，其他的一切都显得好短暂呢。" with dissolve
    sy_ smile "嗯……但不管过去多久，月亮总会在夜空升起，明天也总会到来。" with dissolve
    "夜风轻轻地吹着，拂过她们的发梢。"

    show cg1001 with dis_master

    "两位少女相视一笑，谁都没有再开口多说。"
    "她们默契地没有提及那个即将到期的约定，也没有点破彼此心中那日渐清晰的情感。"
    "珍惜之后每一秒的共处时光，对她们来说，才是此刻最重要的事。"

    jump hougong_route

label choice_8_b_zhao_xing_mi_liao_yi_liao:


    play music bgm_12 fadeout 1.0 fadein 1.0

    "要不……去找星弥聊聊吧。"
    "不过这么晚，她应该已经睡了吧？"

    scene bg_kitchen_2
    with fade
    show bg_kitchen_2:
        zoom 1.06
        xalign 0.55
        yalign 1.0
    with dissolve
    show xm clothes2_side1 smile at center with dissolve

    "走出帐篷，黑暗的客厅里只有厨房的灯还亮着。"
    show xm clothes2_side1 oo kp1wl at emphasis_pop
    xm_ "啊，林先生您怎么醒了？"
    show xm hide_fx with dissolve
    "星弥正对着微波炉，手忙脚乱地调整着温度。"
    lxc_ "睡不着……你呢？这么晚在做什么？"
    show xm clothes2_side1 shy skin_shy at look_away_small
    xm_ "我、我也睡不着，就想热杯蜂蜜牛奶，看能不能好睡一点……"
    "微波炉「 叮 」的一声，她小心翼翼地端出冒着热气的马克杯。"
    show xm clothes2_side1 smile skin_blush with dissolve
    xm_ "要一起喝吗？"
    lxc_ "……好。"

    scene bg_living_room_2
    with fade
    show bg_living_room_2:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve
    show xm clothes2_front3_no bewilderment at center with dissolve

    "我们在餐桌前坐下，热牛奶的甜香味弥漫在空气里。"
    show xm bewilderment at lean_in
    xm_ "您今天……是不是在公司里遇到不开心的事了？"
    lxc_ "为什么这么问？"
    xm_ bewilderment "您的表情，和平时不太一样。" with dissolve
    xm_ focus "加上之前在公司看到的……就有点担心。" with dissolve
    show xm oo at emphasis_pop
    lxc_ "……嗯？你什么时候去过我公司？"
    show xm shy skin_shy at look_away_small
    xm_ "啊……这、这个，只是稍微打个比喻啦！"

    xm_ shy skin_blush "总之就是觉得，您是不是在公司遇到了什么！" with dissolve
    lxc_ "……"
    "我沉默地喝了口牛奶。"
    "好甜，但对于此时的我来说却恰到好处。"
    "牛奶明显是两个人的量，她不只是因为自己睡不着才加热牛奶的。"
    "是在担心我吧……"
    show xm bewilderment with dissolve
    xm_ "啊，当然，要是您不想说的话，我……"
    lxc_ "不是这样的，我只是……在想该怎么说而已。"
    lxc_ "事情是这样的——"

    scene bg_living_room_2
    with fade
    play music bgm_5 fadeout 1.0 fadein 1.0
    show xm clothes2_front3_no astonished kp1wl at center with dissolve
    "把公司发生的事告诉她后，星弥激动地瞪圆了眼睛。"

    show xm clothes2_front3_no pout kp13wl at angry_stomp

    xm_ "好过分……怎么可以这样啊。"

    show xm clothes2_front3_no pout at emphasis_pop
    xm_ "明明您都那么努力了……我、我要用诅咒魔法让那些坏蛋都摔倒！"
    lxc_ "别冲动。"
    show xm clothes2_front3_no pout hide_fx with dissolve
    "我连忙阻止她摸向法杖的动作。"
    "虽然她平时总是一幅温和的样子，但一旦生气起来，行动力比谁都强。"
    "就像我们最初见面时那样。"
    show xm cry skin_cry with dissolve
    xm_ "可是……看到您这么难过，我心里就觉得好难受。"
    xm_ cry skin_cry "更难过的是，自己却什么忙都帮不上……" with dissolve
    "星弥的眼角滑下泪珠。"
    "眼前的女孩，因为无法帮到我而难过地落泪。"
    "明明是我的事，她却表现得比谁都伤心。"
    "真是善良得让人心疼啊。"
    "我轻轻擦去她眼角的泪水。"
    show xm cry skin_cry at shy_shrink
    lxc_ "不是这样的。"
    lxc_ "星弥你愿意听我说这些，就已经帮了我很多。"
    lxc_ "要是让我一直憋在心里，我肯定比现在还要难受一百倍。"
    lxc_ "所以，你不是什么都没做到。"
    "我轻轻握住她的手。"
    show xm shy skin_blush with dissolve

    lxc_ "谢谢你，替我流下了眼泪。"
    xm_ shy skin_blush "……嗯。" with dissolve

    xm_ smile_close "我、我很喜欢在这里生活，不用风吹日晒，也不必勉强自己做到什么。" with dissolve
    xm_ smile "而这一切，都是您提供给我们的。" with dissolve
    xm_ focus "所以，我不希望像您这样温柔的人，受到不公平的对待。" with dissolve

    xm_ smile "我希望林先生，每天都能过得开开心心的。" with dissolve
    "她轻轻回握我的手，温暖的体温传递了过来。"
    lxc_ "我明白的。"
    $ route_sy_score = (1 if first_choice in (1, 3) else 0) + (1 if second_choice in (1, 3) else 0) + (1 if third_choice in (1, 3) else 0)
    $ route_xm_score = (1 if first_choice in (2, 3) else 0) + (1 if second_choice in (2, 3) else 0) + (1 if third_choice in (2, 3) else 0)

    if route_xm_score >= route_sy_score:
        "她的真心，通过行动清清楚楚地传达给了我。"
        "正因为她如此关心我，才会为我难过，替我落泪。"

    lxc_ "谢谢你，星弥。"
    if route_xm_score >= route_sy_score:
        "马克杯里的牛奶渐渐凉了。"
        "但我心里某个一直冰凉的地方，正被这点点温暖慢慢化开。"
    show xm smile skin_blush at bounce_small
    xm_ "嗯！"
    "少女破涕为笑，眼角的泪光在灯光下闪烁如星。"

    if route_sy_score > route_xm_score:
        jump choice_8_b_route_shiyu
    elif route_xm_score > route_sy_score:
        jump choice_8_b_route_xingmi
    else:
        jump choice_8_b_route_harem

label sy_xm_he_sleeping(variant="shiyu"):
    sy_ clothes1_side1 smile "他睡了吗？"

    if variant == "shiyu" or variant == "harem":
        xm_ clothes1_side1 smile "嗯，牛奶的效果很好，我还加了一点点催眠魔法，肯定能睡得很香的。"
    elif variant == "xingmi":
        show cg10019 with dis_master
        xm_ clothes1_side1 cat_mouth "嗯，牛奶的效果很好，我还加了一点点催眠魔法，肯定能睡得很香……呵呵。" with dissolve

    return

label choice_8_b_route_shiyu:

    scene bg_community_5
    with Fade(0.5,0.5,0.5)

    pause 0.5

    scene cg1001
    with Fade(0.5,0.5,0.5)

    play music bgm_21 fadeout 1.0 fadein 1.0

    $ heroine = True
    $ heroine_name = "星弥的视角"

    call sy_xm_he_sleeping ("shiyu") from _call_sy_xm_he_sleeping
    show cg1002 with dis_master
    sy_ pout "哼，他倒是睡得着……明明也可以找我商量的。" with dissolve
    sy_ pout "啊啊，越想越气，我下次要给他来一份血族特制安眠套餐！" with dissolve
    show cg10053 with dis_master
    xm_ bewilderment "欸欸，时语，冷静点啦……" with dissolve
    sy_ pout skin_shy "我很冷静！我才没有羡慕呢！" with dissolve
    "你的表情明明就是一脸不甘心嘛……"
    "不过，原来是这样啊，时语她对林先生……"
    xm_ smile "……" with dissolve
    jump route_003_shiyu_common

label choice_8_b_route_xingmi:


    scene bg_community_5
    with Fade(0.5,0.5,0.5)

    pause 0.5

    scene cg1001
    with Fade(0.5,0.5,0.5)

    play music bgm_21 fadeout 1.0 fadein 1.0

    $ heroine = True
    $ heroine_name = "时语的视角"

    call sy_xm_he_sleeping ("xingmi") from _call_sy_xm_he_sleeping_1
    show cg10020 with dis_master
    sy_ clothes1_side1 oo "呜哇，这个魔女有时候真可怕呢……"
    show cg10021 with dis_master
    xm_ smile "毕竟明天林先生还要上班，我希望他能好好休息嘛。" with dissolve
    xm_ smile "至少在睡梦中，希望他能过得幸福一点。" with dissolve
    show cg1006 with dis_master
    sy_ sigh "……是吗。" with dissolve
    "虽然她自己可能没意识到，但星弥说起林小凑时的表情，明显是……"
    jump route_003_xingmi_common

label choice_8_b_route_harem:

    scene bg_community_5
    with Fade(0.5,0.5,0.5)

    pause 0.5

    scene bg_sky_3
    show bg_sky_3 at bg_pan_right
    with fade
    pause 0.8

    scene cg1001
    with Fade(0.5,0.5,0.5)

    play music bgm_21 fadeout 1.0 fadein 1.0

    $ heroine = True
    $ heroine_name = "第三人称视角"

    show cg1002 with dis_master
    call sy_xm_he_sleeping ("harem") from _call_sy_xm_he_sleeping_2
    sy_ pout "哼，他倒是睡得着……明明也可以找我商量的。" with dissolve
    sy_ pout "啊啊，越想越气，我下次要给他来一份血族特制安眠套餐！" with dissolve
    show cg10053 with dis_master
    xm_ bewilderment "欸欸，时语，冷静点啦……" with dissolve
    sy_ pout skin_shy "我很冷静！我才没有羡慕呢！" with dissolve
    show cg10054 with dis_master
    xm_ cat_mouth "但你表情明明……" with dissolve
    show cg10020 with dis_master
    sy_ oo "我一点！也！不！羡！慕！" with dissolve
    show cg1005 with dis_master
    xm_ smile_close "这样啊，原来时语也……" with dissolve
    show cg10055 with dis_master
    sy_ astonished "我也什么？" with dissolve
    show cg10056 with dis_master
    xm_ shy skin_blush "没、没有啦！我随便乱说的！" with dissolve
    "棕发少女偏过微微发红的脸，慌忙转移话题。"
    show cg10048 with dis_master
    xm_ shy skin_blush "说、说起来，在这里住下之后，发生了好多事呢。" with dissolve
    sy_ smile skin_blush "是啊，不知不觉就和那家伙经历了这么多。" with dissolve
    "银发少女望向房间里那个小小的帐篷，眼神变得柔和。"
    jump route_003_harem_common_end

label choice_9_c_hai_shi_zi_ji_yi_ge_ren_jing_yi_jing_ba:



    "……这么晚，她们应该都睡了，还是别打扰比较好。"
    "工作上的烦心事，说出来也只会让她们白白担心。"
    "早点睡吧，明天还要上班呢。"
    "我再次闭上眼，可那些刺耳的话语仍在脑海里挥之不去。"
    "但为了休息，我还是努力强迫自己进入睡眠状态。"
    "……据说人有一种「 穴居本能 」，心情低落的时候就想躲在狭小、封闭的空间里。"
    "我现在躲在这个帐篷里，是否也在无意识地寻求这种安全感呢？"
    "……有点怀念之前时语的膝枕，还有星弥的按摩了。"
    "在这样漫无边际的胡思乱想中，我蜷缩成一团，逐渐沉入昏暗的梦乡。"
    "……"
    scene black
    with ImageDissolve("rule/eyeclose.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)
    temp_2 clothes2_side1 shy "……我们这样偷偷进来，是不是不太好啊？"
    temp_ clothes2_front1 "来都来了，总不能现在打退堂鼓吧？"
    temp_2 "但……林先生好像已经睡着了。"
    "在半梦半醒间，我隐约听见窸窸窣窣的声响，随后感觉身边的空间变得有些拥挤。"
    scene bg_living_room_3
    show bg_living_room_3:
        zoom 1.08
        xalign 0.5
        yalign 1.0
    show sy clothes2_front1 shy skin_shy at left
    show xm clothes2_side1 shy skin_shy at right
    with ImageDissolve("rule/eyeopen.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)
    "微微睁开眼，在朦胧的视野里，看到的银发少女那近在咫尺的、可爱的脸蛋。"
    lxc_ "……时语？"
    show sy shy at shy_shrink
    sy_ "……！"
    "哪怕在黑暗中，我也能看清她脸颊上渐渐泛起的红晕。"
    "这算是日有所思，夜有所梦吗？"
    "没做恶梦，倒也不算坏。"
    "翻过身，另一侧映入眼帘的，是棕发少女同样通红的脸庞。"
    lxc_ "……星弥？"
    show xm shy at shy_shrink
    xm_ "……！！"
    "……居然一次梦到两个？"
    "我不禁为自己这夸张的幻想感到一丝惊讶。"
    "……不过，反正是梦，偶尔任性一下也没关系吧？"

    scene black
    with ImageDissolve("rule/eyeclose.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)


    "我揉了揉眼睛，打算再次闭上眼。"
    "随后，一股熟悉的、淡淡的香味飘来——那是少女身上特有的、好闻的体香。"
    "……这梦未免真实得过分了吧？"

    scene bg_living_room_3
    show bg_living_room_3:
        zoom 1.08
        xalign 0.5
        yalign 1.0
    show sy clothes2_front1 oo skin_blush kp1wl at left, emphasis_pop
    show xm clothes2_side1 oo skin_blush kp1wl at right, emphasis_pop
    with ImageDissolve("rule/eyeopen.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)
    "再次睁眼，眼前是时语和星弥羞红的脸。"
    sy_ "晚、晚上好啊，人类？"
    xm_ "……您还没睡着啊。"
    with hpunch
    lxc_ "——不是？！你们怎么会在这里啊？"



    show sy hide_fx with dissolve
    show xm hide_fx with dissolve
    sy_ bewilderment "你今天状态很不对劲嘛，我就想找机会和你聊聊。" with dissolve
    show sy clothes2_front1 sigh with dissolve
    sy_ "但在外面等了半天也不见你从帐篷里出来……"
    show xm shy at look_away_small
    xm_ "我也是，本来想给您冲杯牛奶，谁知您这么快就进帐篷了。"
    xm_ smile "于是我们就决定，一起进来这里了……" with dissolve
    lxc_ "但也没必要都挤进来吧？帐篷太小了，装不下三个人。"
    xm_ cat_mouth "只要挤一挤，总会有办法的，不是吗？" with dissolve

    xm_ smile "而且，总觉得不能放任您一个人不管嘛。" with dissolve

    sy_ pout "就是啊，你回家时的表情就像被雨淋湿的小狗一样。" with dissolve
    sy_ bewilderment skin_blush "刚才睡觉时还缩成一团……一不留神，说不定就弄丢了。" with dissolve
    lxc_ "……"
    lxc_ "……我又不是小孩子。"
    xm_ smile "但从年龄上来说，您对我们而言确实是小孩子呀？" with dissolve
    lxc_ "……行吧，真是说不过你们。"
    show sy cat_mouth at bounce_small
    sy_ "哦，他笑了他笑了！"
    lxc_ "喂，为什么这么黑你也能看到啊！"
    sy_ smile_close "哼哼，本小姐可是高贵的血族，区区夜视不在话下！" with dissolve

    xm_ smile "嘻嘻，感觉有点像大家一起在野营呢。" with dissolve
    "时语轻轻踢了下我的脚，星弥则往我身边靠了靠，我们之间的距离变得越来越近。"
    lxc_ "……谢谢你们，心情突然好多了。"
    sy_ focus "所以，到底是什么事让你这么不开心？" with dissolve
    xm_ focus "肯定是公司领导又提了什么过分的要求吧！" with dissolve
    lxc_ "嗯……其实就是今天在公司里——"
    "我把公司里发生的事一五一十地告诉了她们。"

    scene bg_living_room_3
    with fade

    show sy clothes2_front1 despise at left with dissolve
    show xm clothes2_side1 shy at right with dissolve

    sy_ "哇，这主管简直比下水道的老鼠还惹人厌！"

    show xm pout at angry_stomp
    xm_ "就是啊，太可恶了！我要画个圈圈诅咒他！"
    lxc_ "冷静点，这种事在职场其实还挺常见的……"
    xm_ focus "但是，常见不代表就能轻易接受呀，不是吗？" with dissolve
    lxc_ "是啊，就算知道难免会发生，真遇上了还是难受。"
    lxc_ "可恶啊……"
    "一想到这，手里的拳头不自觉地握紧了。"

    syxm_ "……"
    "她们不约而同地对视了一眼。"
    show sy at look_at_right
    show xm at look_at_left
    with dissolve

    play music bgm_20 fadeout 1.0 fadein 1.0
    show sy shy skin_shy kp17wl at shy_shrink
    sy_ "……我倒是知道一个缓解难受的办法。"
    show xm shy skin_shy kp17wl at shy_shrink
    xm_ "嘻嘻，我也想到了。"
    "星弥轻轻握住我的右手，时语则是抓住了我的左手，甚至还把我的拳头掰开，把自己的手指滑入了我的掌心。"
    show sy hide_fx with dissolve
    show xm hide_fx with dissolve
    syxm_ "这样的话，会不会好一点？"
    lxc_ "你们……"
    xm_ smile "据说在没有魔法的地方，人们就是通过彼此靠近来取暖的呢。" with dissolve
    sy_ smile skin_blush "不管是人类、血族还是魔女，只要身体变暖，心也会变得安定吧。" with dissolve
    "……真奇怪啊，明明她们是血族和魔女，但手心的温度却如此温暖。"
    "里世界的真相，和传说故事里写的完全不一样呢。"
    "哪怕身份特殊，她们也是活生生的人。"
    "是因为各种机缘留在我身边、真心待我的人。"
    "我却一直以「 保护她们 」为借口，几乎没对她们敞开心扉，甚至还打算把今天的事也藏在心里。"
    "这是不是……也是一种傲慢呢？"
    show xm smile skin_blush at nod_small
    xm_ "之后要是再觉得难受，就和我们倾诉吧。"
    xm_ focus "我和时语，会像今天一样认真听的。" with dissolve
    sy_ pout skin_blush "是啊，有事还藏着掖着的话，我会生气的……" with dissolve
    sy_ focus skin_blush "我们都相处这么久了，还不值得你信任吗？" with dissolve
    "两位少女慢慢地、轻轻地靠在了我的肩膀上。"
    scene black
    with ImageDissolve("rule/eyeclose.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)
    scene bg_living_room_3
    show bg_living_room_3:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    show sy clothes2_front1 shy skin_shy at left
    show xm clothes2_side1 shy skin_shy at right
    with ImageDissolve("rule/eyeopen.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)
    lxc_ "……"
    "我一直觉得，遇到问题要自己承担，才算是合格的大人。"
    "但现在，我有了新的想法。"
    lxc_ "我知道了，以后我会试着多依赖你们一点的。"
    lxc_ "谢谢你们，我……想通了一些事。"

    xm_ "嘻嘻，不客气，这也是我们自己想做的。"

    show sy shy at look_away_small
    sy_ "……哼，要是你一直颓废下去，我可是会很困扰的。"
    show xm smile skin_blush with dissolve
    xm_ "时间不早了，林先生早点休息吧。"
    sy_ smile skin_blush "在你睡着前，我们都会陪着你的。" with dissolve
    "星弥轻轻哼起那首熟悉的摇篮曲，时语也在旁低声应和。"

    "此刻的场景，和那一晚如出一辙。"
    "我深深觉得，能遇到她们，是多么幸运。"
    "怀着这份感激，我渐渐沉入了甜美的梦乡。"

    scene black
    with ImageDissolve("rule/eyeclose.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)

    $ route_sy_score = (1 if first_choice in (1, 3) else 0) + (1 if second_choice in (1, 3) else 0) + (1 if third_choice in (1, 3) else 0)
    $ route_xm_score = (1 if first_choice in (2, 3) else 0) + (1 if second_choice in (2, 3) else 0) + (1 if third_choice in (2, 3) else 0)

    if route_sy_score > route_xm_score:
        jump choice_9_c_route_shiyu
    elif route_xm_score > route_sy_score:
        jump choice_9_c_route_xingmi
    else:
        jump choice_9_c_route_harem

label choice_9_c_embarrassment_common:

    scene bg_community_5
    with Fade(0.5,0.5,0.5)

    pause 0.5

    scene cg1001
    with Fade(0.5,0.5,0.5)

    play music bgm_21 fadeout 1.0 fadein 1.0

    $ heroine = True

    sy_ clothes1_side1 smile "终于睡着了呢。"
    xm_ clothes1_side1 smile "是啊，他睡着时的样子，像只温顺的小动物，还挺可爱的。"
    show cg10040 with dis_master
    sy_ shy skin_shy "……做了那种事之后，星弥居然还能这么平静啊。" with dissolve
    show cg10041 with dis_master
    xm_ oo skin_blush "不、不要说出来嘛！其实我也很害羞的……！！" with dissolve
    show cg10042 with dis_master
    sy_ cat_mouth skin_blush "欸——原来不是只有我一个人在害羞啊。" with dissolve
    show cg10043 with dis_master
    sy_ shy "不过上次就算了，这次居然又冲动做了这样的事……" with dissolve
    sy_ "啊啊，现在想起来都想找个枕头把脸埋进去了！" with dissolve
    return

label choice_9_c_post_embarrassment:


    if _route_9c == "xingmi":
        "为什么我会同意星弥做这种事啊……！"
    elif _route_9c == "shiyu":
        "虽然是我提议的，但现在想想，还真是让人害羞啊……"

    xm_ shy "嗯，直到现在，我的心跳还是好快呢……呜呜。" with dissolve

    if _route_9c == "harem":
        "冲动的后劲渐渐消退，两位少女才后知后觉地意识到，自己刚才做出了多么令人脸红心跳的事。"

    show cg10044 with dis_master


    sy_ pout skin_blush "哈，可恶，都怪林小凑！看到他露出那种让人没法放心的样子，我怎么可能不管嘛！" with dissolve

    if _route_9c == "xingmi":
        "毕竟……受过他那么多的照顾，哪有不回报的道理！"
        "礼尚往来，才是真正的血族应有的礼仪！"
        "没错，我这么做，只是因为要报答他而已！"

    show cg10045 with dis_master


    xm_ pout skin_blush "就是！林先生太坏了，还想把心事一个人憋着不说！" with dissolve

    if _route_9c == "shiyu":
        "明明我们都很想帮上忙的！"
    elif _route_9c == "harem":
        "两人小声互相吐槽着，直到夜晚的微风轻轻吹过，才让她们渐渐平复下来。"

    return

label choice_9_c_route_shiyu:

    $ heroine_name = "星弥的视角"
    call choice_9_c_embarrassment_common from _call_choice_9_c_embarrassment_common
    $ _route_9c = "shiyu"
    $ _blush_flag = True
    call choice_9_c_post_embarrassment from _call_choice_9_c_post_embarrassment
    show cg10057 with dis_master
    sy_ sigh "他这人老是这样，自己的事就想独自承担，不想给别人添麻烦。" with dissolve
    sy_ pout "但我明明又不是外人……" with dissolve
    "时语嘟囔着嘴，一脸气鼓鼓的样子。"
    "啊，原来时语她对林先生……"
    show cg1002 with dis_master
    xm_ smile "……" with dissolve
    jump route_003_shiyu_common

label choice_9_c_route_xingmi:

    $ heroine_name = "时语的视角"
    call choice_9_c_embarrassment_common from _call_choice_9_c_embarrassment_common_1
    $ _route_9c = "xingmi"
    $ _blush_flag = True
    call choice_9_c_post_embarrassment from _call_choice_9_c_post_embarrassment_1
    show cg10058 with dis_master
    xm_ focus skin_blush "明明只要他开口说一声，我就会安慰他的！" with dissolve
    show cg10045 with dis_master
    xm_ pout skin_blush "哪怕帮不上什么忙，我也能陪他说说话、聊聊天嘛！" with dissolve
    "星弥一口气说了一大串话，脸颊都变得有点气鼓鼓的。"
    show cg10059 with dis_master
    xm_ sigh "自己一个人生闷气、把什么都藏在心里的滋味，我最清楚了……那种感觉，真的很不好受……" with dissolve
    show cg10010 with dis_master
    sy_ bewilderment "……" with dissolve
    "虽然星弥自己可能没意识到，但她其实对林小凑……"
    jump route_003_xingmi_common

label choice_9_c_route_harem:

    $ heroine_name = "第三人称视角"
    scene bg_sky_3
    show bg_sky_3 at bg_pan_right
    with fade
    pause 0.8
    call choice_9_c_embarrassment_common from _call_choice_9_c_embarrassment_common_2
    $ _route_9c = "harem"
    $ _blush_flag = False
    call choice_9_c_post_embarrassment from _call_choice_9_c_post_embarrassment_2
    show cg10046 with dis_master
    xm_ smile "不过，看到他那么失落的样子，任谁都会忍不住想去安慰他吧。" with dissolve
    show cg10047 with dis_master
    sy_ smile "是啊，现在后悔也来不及了。无论是刚刚的事，还是……" with dissolve
    sy_ "我们最初决定留下来的这件事。" with dissolve
    "银发少女望向远方的星空，眼神变得柔和。"
    xm_ "嗯，不知不觉间，已经一起经历了这么多事啊。" with dissolve
    "棕发少女轻轻撩起耳边的发丝，望着远处城市的灯火，思绪却飘向了更远的地方。"
    jump route_003_harem_common_end
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
