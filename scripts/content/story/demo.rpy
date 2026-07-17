


define first_choice = 0
define second_choice = 0


label story_7761:
    $ heroine = False


    play music bgm_14 fadein 1.0
    scene bg_office_1
    with dissolve

    lxc_ "我先下班了。"
    "和同事打过招呼后，像往常一样，我头也不回地离开了公司。"

    scene bg_street_2
    with fade

    "踏出公司的那一刻，时针分毫不差地指在「 10 」这个数字上。"
    "放在平时，此刻自己应该刚洗完热水澡，舒服地躺在沙发上玩平板吧。"
    "但——"


    scene bg_sky_3
    show bg_sky_3 at bg_pan_down
    with fade

    lxc_ "今天也要加班啊。"
    "连续的项目赶工，以及上司那高压锅般的性格，压得自己有点喘不过气。"
    "长叹一声，呼出的白气瞬间消散在夜色中，什么也看不到。"
    "就像我自己的未来一样。"
    "经济下行，找到一份称心如意的工作并不容易。"
    "我这份工作说不上多好，但至少，名义上是份双休的工作。"
    "工资刚刚够维持生活，每个月日常开销之后，还能攒下一点积蓄。"
    "比起生活在水深火热的其他人来说，要体面太多。"


    scene bg_street_2
    with fade

    "算了，下班就不要再想工作的事。"
    "明天是周末，终于能尽情地睡个懒觉了。"
    "一想到这，心情总算稍微轻松了一点。"

    show bg_street_2:
        zoom 1.5
        xalign 1.0
        yalign 0.5
    with dissolve

    "「 成年人的选择，XX纯生——今晚，为自己干杯！ 」"
    "路边新竖起的啤酒广告牌映入眼帘，「 成年人 」三个字在夜色里显得格外醒目。"
    "……我承认，这广告词确实有点吸引到我了。"

    scene bg_community_2
    with Fade(0.5,0.5,0.5)

    lxc_ "好难喝……"
    "从挤满人的地铁下来，我拖着疲惫的身躯回到了家门前。"
    "刚刚试喝的那一小口，味道苦涩得让我瞬间清醒了不少。"
    "也许是因为连续加班，脑子真的有点迷糊了。"
    "明明自己并不喜欢酒的味道，但还是天真地相信「 喝了酒就是大人了 」这种鬼话。"
    "我开始嫌弃一个小时前愚蠢的自己。"



    lxc_ "……唉。"
    "我摇摇头，把这些乱七八糟的念头甩开，凭本能掏出钥匙，打开了门。"




    play music bgm_7 fadeout 1.0 fadein 1.0
    scene bg_living_room_2
    with fade

    lxc_ "……？灯怎么开了？"
    lxc_ "早上忘记关了吗……"

    show bg_living_room_2:
        zoom 1.5
        yalign 1.0
        xalign 1.0
    with dissolve

    "「 电费又要多交了 」的念头在脑中一闪而过，双腿已经不由自主地被沙发吸引了过去。"
    lxc_ "嗯……还是家里的沙发躺起来最舒服啊……"

    show bg_living_room_2:
        zoom 2.0
        yalign 1.0
        xalign 1.0
    with dissolve

    "我闭着眼，右手习惯性地朝平时放平板的位置摸去——却落了个空。"

    show bg_living_room_2:
        zoom 3.0
        yalign 1.0
        xalign 1.0
    with dissolve

    lxc_ "嗯？是放在左边吗？"
    "没有。"
    "奇怪，我记得应该是放在这里才对啊？"
    "那应该是放在前面——"



    scene cg400:
        zoom 2.0
        yalign 1.0
        xalign 1.0
    with dissolve

    show sy clothes1_front1 calm:
        yalign -3.0

    temp_ "喂，人类。你的手再往前就要碰到我了。"
    "娇小的声音在耳边响起，十分悦耳。"

    show cg400:
        zoom 1.5
        yalign 1.0
        xalign 1.0
    with dis_master

    "那不是我认识的人的声音，当然也不是自己的声音。"
    "更像是，来自异世界的——也就是游戏中的角色的声音。"
    lxc_ "没想到我居然连游戏也忘了关——？！"

    show cg400:
        zoom 1.0
    with dis_master

    "睁开眼，抬起头，映入眼帘的，并非预想中的游戏画面。"
    "不，平板上的游戏确实开着。"
    show cg403 with dis_master
    "但拿着平板的，却是位素未谋面的少女。"
    "银发红瞳，周围散发着遮掩不住的高贵与傲气。"
    "黑白相间的连衣裙又让这份高傲束之高阁，留下优雅端庄的印象。"
    "我和眼前的少女互相凝视了三秒后，得出了结论。"
    lxc_ "哈哈，二次元看多了，终于出现幻觉了吗？"
    "一定是加班把人加傻了。"


    show sy pout:
        yalign -3.0
    show cg401 with dis_master
    yfsn_ "喂，人类，这一关游戏要怎么过啊？"
    lxc_ "……"


    show sy despise
    show cg402 with dis_master
    yfsn_ "本小姐在和你说话呢！"

    show sy at char_exit_left
    pause 0.5
    hide sy


    scene bg_kitchen_2
    with fade

    "无视少女的呼唤声，我来到厨房。"
    lxc_ "肯定是又饿又困导致的，吃点东西就好——？！？！"
    "正当我打算打开冰箱时，我的注意力却被另外一样东西吸引住了。"

    scene sd0
    with fade


    show xm clothes1_side1 oo:
        ypos 5000

    temp_2 "看不到我看不到我看不到我……"
    "不，不是那个在地上瑟瑟发抖，抱头蹲防的黑紫色帽子。"
    "而是粘稠的黄色与白色混合，如凶案现场般凌乱的"
    "——我的微波炉。"
    "无暇顾及在脚边不断发抖的黑紫色帽子，我颤颤巍巍地来到微波炉前。"
    "颤抖的手缓缓揭开了微波炉的门。"

    "尽管已经有了心理准备，但在见到惨案的那一刻，我还是忍不住叫了出声。"
    with vpunch
    lxc_ "我在超市半价抢回来的鸡蛋啊啊啊！！！"

    call achievement (21) from _call_achievement


    scene bg_living_room_2
    with Fade(0.5,1.0,0.5)


    show xm clothes1_side1 bewilderment at right with dissolve
    show sy clothes1_front1 smile at left with dissolve

    "确认了眼前发生的事并不是幻觉后，我为我的半价鸡蛋默哀了三秒钟。"
    "然后，我把在厨房里瑟瑟发抖的棕发少女「 请 」到了沙发上，并倒好三杯水回到了客厅。"
    "此时，棕发少女已经端端正正地坐在了沙发上。"
    "棕色长发与细长的披风为她增添了几分不符合外表的成熟气质。"
    "然而那双裹在白短袜里、紧张得不知该往哪放的小脚，却彻底暴露了她此刻的真实心情。"
    "另一边，那位一直坐在沙发上的银发少女则是气势不减，和刚才一样，大大方方地靠在沙发里玩着我的平板。"
    "被白色裤袜包裹的小腿优雅地交叠翘起，与身旁那只无处安放、微微扭动的白袜小脚形成了鲜明对比。"

    lxc_ "所以，你为什么要把鸡蛋放进微波炉？"

    zfsn_ "唔……因为微波炉上写着，『 把食物放进去就可以加热 』？"
    lxc_ "不不不，我问的不是这个。"
    lxc_ "我问的是，为·什·么，要把那么多个鸡蛋一起放进微波炉？"


    show xm surprised_but with dissolve
    zfsn_ "……因为老师说过，量变引起质变？"
    lxc_ "量变引起质变是这么用的吗？！"


    show xm cry skin_cry at shy_shrink
    zfsn_ "对、对不起！"



    "她立刻把整张脸藏进黑紫色的宽大帽檐下。"
    show xm shy skin_blush with dissolve
    "过了一会儿，又像只小心翼翼的小动物般，微微抬起帽檐，偷瞄我是不是真的在生气。"

    lxc_ "……算了，也不是什么大问题。"


    show sy clothes1_front1 smile with dis_master
    show xm smile with dis_master
    yfsn_ "不就是几个鸡蛋嘛，本小姐替她赔你就是……呃，不过我身上的钱好像花光了。"
    show xm oo with dis_master

    yfsn_ not_good kp8wl "看来最后还是得你自己赔咯。" with dissolve



    "不得不说，棕发少女此刻的表情变化堪称精彩。"
    lxc_ "……先不说这个，你为什么会这么自然地玩起我的平板啊？"
    "我从银发少女手中轻轻抽回平板。"
    "检查了一下——还好，她只是点开了游戏界面，没乱翻别的应用。"

    show sy pout kp13wl with dis_master
    show xm shy with dis_master
    yfsn_ "切，小气。让我玩一下也不会怎么样嘛。"



    show sy cat_mouth hide_fx with dissolve
    "她鼓起了脸颊，顺手抓起桌上那只买奶茶送的小黄鸭，捏得吱吱作响。"





    show xm shy with dissolve
    "而棕发少女则睁大眼睛，满眼写着羡慕，却又不敢伸手，只是远远地看着那只被捏扁的小黄鸭，一副想碰又不敢吭声的模样。"


    show sy smile with dissolve
    "看着她们两个像小孩子一样的行为，我原本就没剩多少的火气，也逐渐消散了。"

    lxc_ "所以，你们是谁？怎么进到我家的？"
    yfsn_ "哼，听了可不要吓一跳。"

    show sy clothes1_side1 with dissolve

    "她站起身来，扬起下巴，摆出一个颇具威严的姿势。"
    yfsn_ "本小姐名为时语·布莱菲特，来自血族最古老的家族之一。"
    sy_ "放在平时，普通人可没那么容易见到我。"
    sy_ "至于为什么来到你家，是因为本小姐在这里感受到了异常的魔力波动。"

    "魔力波动……？这是什么最新的Cosplay设定吗？"


    show sy bewilderment at look_away_small
    sy_ "啊，这个好像不能说出来的……家族那些规定真烦。"

    "似乎是察觉到我怀疑的目光，她立刻改口，语气却依旧从容。"

    show sy smile with dissolve
    sy_ "人类，你就当没听过刚才那段话吧。"
    sy_ "当然了，本小姐的名字你可得好好记住。"

    "时语拂了拂银发，丝毫没有因为刚刚的失误而慌乱。"
    lxc_ "……哪怕你身份再高贵，也不应该随便闯进别人家吧？"
    sy_ "那当然，我在进来之前可是有好好敲门的。"
    lxc_ "那是谁给你开的门？"
    sy_ "她啊。"
    "她指了指身旁一直躲在帽子后面的棕发少女。"
    lxc_ "但她也不是这个家的主人啊？"
    "一个误闯进来的人，给另一个敲门的人开了门，然后两人都以为对方是这里的主人……"
    "我已经能想象到当时的情景了。"
    sy_ not_good "……我、我这不是后面才知道嘛。" with dissolve
    "她心虚地低下头。"
    sy_ shy "还有……刚才没经过你同意就玩了你的平板，对不起……" with dissolve
    sy_ "我第一次接触到能联网的设备，有点太兴奋了……"
    sy_ "但我只玩了那个游戏，其他东西都没有乱碰。"
    lxc_ "……行吧。"
    lxc_ "那你是怎么进来的？刚刚像只受惊的松鼠般不断发抖的魔女小姐？"



    show xm clothes1_side1 oo kp1wl at emphasis_pop
    zfsn_ "欸，轮到我了吗？！我、我叫星弥，本来是在找甜品的路上，结果传送魔法出错，不小心闯进你家，引发的魔力波动还把时语给吸引了过来……然后看到冰箱里有好吃的，就忍不住尝了一块，后来在研究那个叫『 微波炉 』的东西时，不小心弄爆炸了……"
    xm_ "不对！您怎么会知道我是魔女？!"

    lxc_ "这位大小姐自称血族，我看你这身打扮，就猜你大概也是扮演魔女之类的吧。"
    "说实话，血族，魔女，精灵，矮人……都是奇幻游戏里常见的设定。"
    "不过，现在的新游戏已经越来越少采用这类设定了。"


    show xm pout hide_fx with dissolve
    xm_ "……我不是在扮演。星弥我，是魔女会的正式成员。"


    show xm focus at lean_in
    xm_ "那些很难很难的考核……我也都一一通过了。"

    lxc_ "设定完整，连考核细节都有……现在玩Cosplay的都这么讲究吗？"
    lxc_ "说真的，虽然你看起来年纪小，但演技可比漫展上大多数Coser都好太多了，连发抖都像真的一样。"
    lxc_ "还是说，这也是角色设定的一部分？"

    "感叹于她始终如一的演技，我伸手打算去拿桌上的水杯。"


    show xm bewilderment with dissolve
    xm_ "……酒馆里的人是这样，公会的冒险者也是这样……"
    xm_ "明明我递出的是魔女会的正式徽章，他们却总笑着说『 小妹妹扮得真像 』，连我调配的魔药都被当成『 过家家 』……"
    xm_ "……你也一定是觉得我看起来太年轻，才不相信我是魔女吧。"


    show xm clothes1_front3_no bewilderment with dissolve
    "眼前棕发少女的身体微微发颤，却不再是先前那种畏缩的害怕。"
    "更像是，委屈与决心交织的颤动。"


    show xm clothes1_front3 pout with dissolve
    xm_ "既然言语解释不清……那我就用魔法证明给你看！"

    scene sd1
    with fade

    "伴随着一段迅速却难以理解的咒语，我正要伸手去拿的水杯瞬间冻结成冰——"
    "冰块的形状甚至凝成了一只栩栩如生的小黄鸭，和桌上那只赠品一模一样。"

    lxc_ "……？"
    "什么情况？"
    "特效？全息投影？混合现实？"
    "各种猜测在我脑海中飞速闪过，又一个个被否定。"
    "迅速，精准，过于逼真——"
    "我甚至能清晰地感受到冰面散发出的寒气。"


    show sy clothes1_side2 smile:
        ypos 5000
    sy_ "你在普通人面前用魔法，可违反了规定哦？"


    show xm clothes1_front3 pout:
        ypos 5000
    xm_ "唔，有什么关系嘛！时语你自己不也说漏嘴了！"


    show sy astonished:
        ypos 5000
    sy_ "我！我那只是意外……！"

    "不，说不定一切都只是幻觉。"
    "我的理性仍在拒绝那个最荒谬的答案。"
    "俗话说，加班加多了，都会见鬼的。"
    "魔法什么的，根本不可能存在的。"
    "只要伸手碰一下，那些名为冰的假象就会烟消云散。"
    "来吧，我的幻想●手——！"
    with vpunch
    lxc_ "好冰！"
    "指尖传来的刺骨寒冷让我猛地缩回手。"
    "杯子里的冰，是货真价实的。"

    call achievement (1) from _call_achievement_1

    lxc_ "两位，这……到底是什么？真的是魔法？"

    scene bg_living_room_2
    with Fade(0.5,1.0,0.5)


    show xm clothes1_front3 bewilderment at right with dissolve
    show sy clothes1_side2 smile at left with dissolve


    show sy smile with dissolve
    sy_ "对啊，她刚刚用的不过是最基础的冰魔法，只是把水凝结成冰而已。"

    lxc_ "……那为什么偏偏是小黄鸭造型？"


    show xm smile at emphasis_pop
    xm_ "我只是想证明，自己真的是魔女而已！"


    xm_ clothes1_front2 focus "魔女对魔力的操控，可是非常精细的！" with dissolve

    "她握紧法杖，气鼓鼓地挺起胸。"

    show xm smile with dissolve
    xm_ "像这样塑造具象的冰晶形态，普通的魔法师根本做不到！"

    lxc_ "……我明白了，刚才是我失礼了。"
    "如此超现实的场面摆在眼前，就算再不愿相信，我也只能接受了。"

    show xm clothes1_front3_no with dissolve


    show xm shy with dissolve
    "星弥似乎没料到我会这么说，一下子又变回先前那副弱气的模样。"
    xm_ "我、我也不是真的很生气啦，只是希望您不要小看魔女而已……"
    xm_ "而且，该道歉的是我才对……不仅擅自闯入了你家，还乱动了厨房里的东西！"
    xm_ "真的很抱歉！我会想办法赔偿的！"
    "她站起身，很用力地弯下腰道歉，魔女帽都差点掉下来。"
    lxc_ "嗯，我接受你的道歉。"
    lxc_ "既然你们没有恶意，那这次就算了。"
    lxc_ "不过，以后可不能再乱碰别人家里的东西哦？"
    xm_ "嗯……"
    "我看看眼前这两位并非普通人的少女，思绪有点混乱。"
    "既然她们不是普通人类，或许我不能用常规的目光去看待她们了。"

    lxc_ "既然星弥是真的魔女，那时语你就是……"


    show sy smile with dis_master
    sy_ "血族。"
    sy_ "不过，对于人类来说，我们有个更广泛的名字……"

    lxc_ "……吸血鬼。"


    show sy cat_mouth with dis_master
    sy_ "没错，看来你也很懂嘛。"
    "她微微一笑，隐约露出唇边的虎牙。"
    "牙齿露出的寒光细微却致命——正如她本人一样，美丽且危险。"


    show sy clothes1_front1 cat_mouth with dis_master
    sy_ "说起来，你身上似乎散发着很好闻的味道呢。"


    show xm oo with dis_master
    show sy clothes1_front1 cat_mouth:
        zoom 1.2 yalign 0.7 xalign -0.2
    with dis_master
    "她忽然起身，一步步向我靠近。"
    show sy:
        zoom 1.5 yalign 0.5 xalign -1.0
    with dis_master
    sy_ "如果刚才的事没有目击者的话……"
    sy_ "那我们所做的事，是不是就可以当做没发生过了呢？"
    "我不自觉地咽了下口水，下意识想向后躲，却被沙发靠背挡住了。"
    "真是见鬼了。"
    "她迅速地俯身凑近，小巧的嘴唇微微张开——"


    show sy laugh_open kp4wl at bounce_small
    sy_ "哈哈，逗你的啦。"


    show sy clothes1_side2 wink hide_fx with dissolve
    sy_ "真正古老的纯粹血族，早就不靠吸血为生啦。"

    sy_ "而且，我要是真的做出那种事，不就变得和那些讨厌的贵族一样了吗？"
    sy_ "今天给你添的麻烦，我回到家族后会想办法给你补偿的。"
    show sy clothes1_front1 smile_close at left:
        zoom 1.0
    with dissolve
    "她退后一步，轻轻提起裙摆，行了一个优雅的礼。"
    show sy smile with dis_master
    lxc_ "这、这样啊……"


    show xm bewilderment with dissolve
    xm_ "时语，不要突然吓人啦……我刚刚都差点当真了。"

    sy_ "抱歉抱歉，我就想着逗逗他嘛。"
    "这个调皮的小鬼……等等。"
    "看着眼前银发与棕发的少女，我突然意识到一个极其严重的问题。"
    lxc_ "说起来，你们两位的年龄究竟是……？"
    "从外表上看，她们毫无疑问是属于少女的范畴。"
    "然后，深更半夜，她们突然出现在一个独居男性的家中。"
    "不管怎么想，这个状况都有点不太妙吧？！"
    "手止不住地颤抖，耳边仿佛已经开始幻听警笛的悲鸣。"
    "说实话，这可比被吸血鬼吸血要恐怖千万倍。"


    show sy pout kp13wl at angry_stomp
    sy_ "你这问题……可是很失礼的哦？"
    sy_ "怎么能随意问一位淑女的年龄呢？"


    show xm bewilderment at look_away_small with dissolve
    xm_ "我是不介意啦……但您这样问确实有点失礼……"


    lxc_ "拜托了，请一定、务必、绝对要告诉我！"


    show sy clothes1_front1 smile hide_fx at left with dissolve
    sy_ "好吧，既然你这么诚恳，本小姐就勉为其难告诉你。"


    show sy bewilderment with dissolve
    sy_ "我想想……大概是三百零七，还是零八来着？"


    show sy cat_mouth with dissolve
    sy_ "嗯，总之就是这个岁数吧。"


    show xm shy with dissolve
    xm_ "我没时语那么年长，只有一百一十多岁……"


    "Safe！！！万岁，永远娘万岁！！！"
    "我在心中高举双拳，摆出胜利的姿势，向那不存在的假想敌宣告着我的清白。"

    call achievement (2) from _call_achievement_2


    show sy bewilderment with dissolve
    sy_ "虽然不知道发生了什么，总之问题好像解决了？"


    show xm smile with dissolve

    "没错，我已经打败那不知名的社会性死亡恶魔了。"



    "既然最麻烦的部分解决了，剩下的就是……"
    lxc_ "……你们今天晚上打算在哪里过夜？"

    show sy calm with dissolve
    sy_ "我？大概会找个安全的地方待着吧。"


    sy_ "反正晚上不睡觉也没什么关系。"


    show xm bewilderment at shy_shrink
    xm_ "我、我才刚来到这边不久，暂时还没想好要去哪里……"
    "……"
    "这个时间点，要是把她们赶出去时被别人看到了，说不定会惹来很多麻烦。"
    "又不能去麻烦房东……啧。"
    lxc_ "……大晚上的就别在外面乱跑了。"
    lxc_ "我把房间借给你们，今天就先在我这里住下吧。"


    show xm astonished at emphasis_pop
    xm_ "欸？这不太好吧？和刚认识的人住在同一个房子里什么的……"


    show sy clothes1_side1 with dissolve
    sy_ "星弥说得对，我们才刚认识没多久吧？"
    sy_ smile "虽然这话由我来说不太合适，但随便让陌生人进自己家里可是很危险的哦？" with dissolve
    lxc_ "……我有自己的考量。"
    lxc_ "而且，古老血族的大小姐和很厉害的魔女小姐，应该不会做出趁人之危的事吧？"


    show sy smile at nod_small
    sy_ "那当然。"

    show xm smile at nod_small
    xm_ "……我不会那么做的。"
    lxc_ "那就行——"
    "悬在心头的问题解决后，强烈的困意忽然就涌了上来。"


    scene black
    with ImageDissolve("rule/eyeclose.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)
    scene bg_living_room_2
    show sy clothes1_side1 at left
    show xm clothes1_front3_no at right
    with ImageDissolve("rule/eyeopen.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)
    pause 0.5
    scene black
    with ImageDissolve("rule/eyeclose.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)
    scene bg_living_room_2
    show sy clothes1_side1 at left
    show xm clothes1_front3_no at right
    with ImageDissolve("rule/eyeopen.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)

    "……毕竟已经是深夜嘛。"


    show sy astonished at emphasis_pop
    sy_ "喂，人类，你没事吧？"


    show xm oo at shocked_step_back
    xm_ "他，他好像要倒下了！"

    show xm:
        zoom 1.2
        yoffset 700

    with dissolve
    "在我失去意识前的最后一刻，感觉自己的身体被轻轻地扶住了。"


    hide sy
    hide xm
    with dissolve

    play music bgm_6 fadeout 1.0 fadein 1.0
    scene bg_living_room_1
    with Fade(0.5, 1.0, 0.5)

    "再次醒来时，眼前的是陌生的——不，是熟悉的天花板。"
    "家里客厅的天花板。"
    lxc_ "疼疼疼……"
    "昨晚太累，竟然直接在这里睡着了吗？"
    lxc_ "……我就试喝了一小口，后劲有这么大吗？"
    "我努力回想睡着前发生的事，但脑海一片浆糊，只是隐约记得似乎遇到了两个很有趣的人，好像是……啊。"

    lxc_ "她们人呢？"

    show bg_living_room_1:
        zoom 1.5
        xalign 0.0
    with dissolve
    pause 0.5
    show bg_living_room_1:
        zoom 1.5
        xalign 1.0
    with dissolve
    pause 0.5
    show bg_living_room_1:
        zoom 1.0
        xalign 0.5
    with dissolve
    "我坐起身，环视四周，客厅里空荡荡的，只有我一个人。"
    "安静得能清楚地听见自己的呼吸声。"
    "难道说，她们只是我做的一场梦？"
    "想到家中其实并没有被陌生人闯入，我不由得松了口气——"

    lxc_ "……"

    "但是，比起那一点点安心，更多的却是……一种说不上来的失落。"
    "难道我是在期待什么吗？"
    "突然闯进我的生活，又悄无声息地消失。"
    "我讨厌这种感觉。"
    "哪怕只是一场梦。"


    "我伸手去拿桌上的水杯，指尖却碰到一小滩还没有完全干的水渍。"
    "……水？"


    scene bg_living_room_2

    show sy clothes1_side2 cat_mouth at left
    show xm clothes1_front3_no shy skin_blush at right
    show expression Solid("#ffa200") as yellow_tint:
        alpha 0.12
    with fade
    pause 0.4


    show sy smile with dissolve
    show xm smile with dissolve
    pause 0.4

    show sd0
    hide yellow_tint
    show expression Solid("#ffa200") as yellow_tint:
        alpha 0.12
    with dissolve
    pause 0.4

    scene bg_living_room_1
    with fade

    "不，那不是梦。"
    "我想起来了，自己在睡着之前说过的话。"
    lxc_ "她们是真实存在的。"

    call achievement (3) from _call_achievement_4


    "我立刻起身，快步走向自己的卧室。"

    scene bg_bedroom_1 with Fade(0.3, 0.3, 0.5)
    pause 0.5


    "推开门——"

    scene cg2
    with dissolve

    "映入眼帘的，是两位少女安稳睡在床上的样子。"


    show sy clothes3_front1 sigh:
        yalign -2.0
    sy_ "唔……谁呀，竟敢打扰本小姐睡觉……"


    show xm clothes3_front1 smile_close:
        yalign -2.0
    xm_ "再一会……再让星弥我睡一会儿就好……"

    pause 0.5

    "不得不承认，她们在梦中呓语的模样，才更贴近她们外表所显示的年纪。"
    "什么血族和魔女，对于我来说都太过遥远。"
    "看着她们毫无防备的睡颜，我感觉一整晚积累的疲惫，好像瞬间就被治愈了。"


    "让她们再多睡一会儿吧。"
    "我轻轻地、小心地关上了房门。"


    scene bg_kitchen_1 with Fade(0.5, 0.5, 1.0)

    "洗完澡后，在厨房准备早餐时，她们两个也揉着眼睛、迷迷糊糊地醒来了。"


    show sy clothes1_front1 calm at left with dissolve
    pause 0.3
    show xm clothes1_front3_no smile_close at right with dissolve
    pause 0.3


    show sy smile with dissolve
    show xm smile with dissolve

    lxc_ "醒了？去刷个牙然后准备吃早餐吧，牙刷和毛巾都放在洗手台上了。"


    show sy bewilderment at look_away_small
    sy_ "……怎么感觉过了一晚，你整个人的态度都变了？"


    show xm smile at lean_in
    xm_ "突然变得好温柔……明明刚见面时还是一副凶巴巴的样子！"
    lxc_ "还不是因为某个人把我的微波炉搞炸了……"


    lxc_ "快点去刷牙。"


    show sy astonished kp1wl at shocked_step_back
    show xm oo kp1wl at shocked_step_back

    "我竖起手中的锅铲，摆出要敲她们脑袋的样子。"


    show sy hide_fx at char_exit_left
    show xm hide_fx at char_exit_right
    pause 0.3

    "两位少女像受惊的小动物一样，飞快地跑进了洗手间。"
    "真是的，说到底不还是小孩子嘛。"


    scene bg_kitchen_1 with Fade(0.5, 0.3, 0.5)


    show sy clothes1_front1 smile at left with dissolve
    show xm clothes1_front3_no smile at right with dissolve

    lxc_ "做好了，吃吧。"

    "我把最后一份煎饼端上餐桌，与蒸好的包子和馒头摆在一起。"
    "作为临时准备的早餐，还算过得去吧。"


    show sy smile at nod_small
    sy_ "噢，以人类的食物来说，还算不错嘛。"
    sy_ "没想到你居然会下厨。"

    lxc_ "煎个饼而已，没什么大不了的。"
    "等有机会，再给你们露一手真正的厨艺吧。"
    lxc_ "趁热吃吧。"


    show sy clothes1_side1 smile with dissolve
    sy_ "等等。人类，你是不是忘了什么很重要的东西？"



    xm_ focus "对哦，最重要的事您还没说呢。" with dissolve

    lxc_ "什么？忘记加盐了？还是酱油？"
    lxc_ "吃个煎饼和包子，不需要这么重口味吧？"


    show xm smile_close at bounce_small
    xm_ "不是，是名字，名字啦！"



    xm_ smile_close "您还没有告诉我们名字哦？" with dissolve


    show sy clothes1_side2 cat_mouth at left with dissolve
    sy_ "只有你知道本小姐的名字，太不公平了吧。"

    "啊。"
    "原来是指这个。"
    "成年以后，几乎只在工作场合，或那些不得不自我介绍的尴尬时刻，才会说出自己的名字。"
    "像这样，能够轻松地和别人交换姓名，竟让我感到一种久违的温暖。"

    lxc_ "我……"
    lxc_ "我叫林小凑，很高兴认识你们。"


    show sy clothes1_side1 smile_close at look_away_small
    sy_ "……哼，作为人类的名字来说，还不错嘛。"


    show xm clothes1_front2_no laugh_open kp4wl at bounce_small
    xm_ "林小凑，林小凑……嗯，真是个不错的名字呢！"

    lxc_ "好了，快点吃吧。"
    "我挠了挠脸颊，试图掩饰自己害羞的心情。"


    show sy clothes1_front1 smile with dissolve
    show xm smile hide_fx with dissolve
    pause 0.5

    "时语用餐巾纸包起煎饼，轻轻地吹了吹才送入口中。"
    "她的动作虽然看起来很随意，但举手投足间还是能看出良好的教养。"
    "星弥的姿势则更为端正，就像守规矩的小孩一样，拿起包子时还不忘用碗接着，生怕掉地上。"
    "我啃了几口馒头，等大家都吃得差不多后，开始进入正题。"


    show sy calm with dissolve
    show xm calm with dissolve

    lxc_ "说起来，你们之后有什么打算？"
    lxc_ "星弥是因为传送魔法失误才来到这边，时语则是被那阵魔力波动吸引过来的。"
    lxc_ "你们原本应该都有自己的计划吧？"
    lxc_ "如果有什么我能做的，我很乐意帮忙。"
    "俗话说，来者皆是客，哪怕是从异世界来的客人也一样。"
    "虽然昨晚她们给我的初印象并不算好，但至少现在，我们是能心平气和坐在一起吃早餐的伙伴了。"



    show sy at look_at_right
    show xm at look_at_left
    pause 0.5


    show sy smile at nod_small
    show xm smile at nod_small
    pause 0.3


    show sy at left with dissolve
    show xm at right with dissolve


    show xm shy skin_blush with dissolve
    xm_ "在那之前……请您先听我们讲一个故事，可以吗？"

    lxc_ "当然。"

    hide sy with dis_master
    show xm clothes1_side1 smile at center
    with dis_master

    xm_ "……在遥远的异界，有一位名为时语·布莱菲特的少女。"

    "星弥轻轻托着下巴，语气变得温柔而平缓，像在讲述睡前故事。"


    show xm calm with dissolve
    xm_ "她身为古老血族的千金，每日都被无数的礼仪课程和茶会包围。"
    xm_ "但她早已对此感到厌倦。"
    xm_ "比起家族中那些无聊透顶的贵族社交，时语更向往人类社会那些新奇有趣的事物——"



    xm_ smile "电影与游戏里的世界，让她深深着迷。" with dissolve
    xm_ "于是，她选择了离家出走，只身来到了人类世界。"



    xm_ bewilderment "只不过，这个过程……很快就遇上了麻烦。" with dissolve

    lxc_ "……钱花光了。"


    show xm shy at nod_small
    xm_ "是的，您还记得呢。"



    sy_ clothes1_front1 pout "……本小姐随口一提的事，你居然还记得啊。" with dissolve

    "不谙世事的大小姐逃到陌生的社会中，很快就花光积蓄，最后只能含泪回家……"
    "这种桥段在不少故事里还挺常见的。"


    xm_ calm "就在她走投无路时，突然感应到某处传来异常的魔力波动……" with dissolve

    xm_ bewilderment "而引发这波动的元凶正是——" with dissolve


    hide xm with dis_master
    show sy clothes1_side1 cat_mouth at center
    with dis_master

    sy_ "一位来自魔女会的魔女。"

    "不知道为什么，讲述的主导权很自然地交到了时语手中。"
    "星弥则悄悄松了口气，小脸微微泛红。"


    show sy clothes1_front1 smile with dissolve
    sy_ "魔女星弥，身为大魔女的现役弟子，天赋非凡却总被意外眷顾。"

    "时语不知从哪里拿出一本书，像舞台剧演员般讲述了起来。"


    show sy calm with dissolve
    sy_ "原本在里世界旅行的她，因为传送魔法失误，意外地来到了表世界。"


    show sy smile at lean_in
    sy_ "她对这里的一切都充满好奇——"
    sy_ "电灯、冰箱、微波炉……这小小房间里竟塞满了那么多她从未见过的新奇事物。"


    show sy cat_mouth at bounce_small
    sy_ "最重要的是，她还在这里找到了旅途的终极目标——美味的甜点！"


    sy_ clothes1_side1 smile "正当她享用完甜点，打算深入研究那名为『 微波炉 』的神奇方盒时——" with dissolve


    show sy clothes1_front1 astonished at emphasis_pop
    sy_ "房间的男主人回来了！"


    sy_ cat_mouth "嗯，接下来的部分，就轮到你自己来讲了！" with dissolve
    lxc_ "啊，好，我叫林小凑，某天回家发现家里突然多了两个——"
    lxc_ "……不对！为什么突然就变成故事接龙了啊！"


    show sy despise at look_away_small
    sy_ "切，居然没骗到你。"


    show sy clothes1_front1 calm at left with dissolve
    show xm clothes1_front3_no skin_blush calm at right with dissolve
    lxc_ "言归正题，你们刚刚讲的，就是来我家之前发生的事吧？"
    lxc_ "但为什么非要两个人换着讲？"


    show xm shy at shy_shrink
    xm_ "……因为自己说自己的事，实在太让人害羞了。"

    "星弥拽了拽魔女帽的帽檐，试图遮住发烫的脸颊。"


    show sy shy with dissolve

    "我看你讲别人的事时，也没好到哪里去嘛……"


    show sy smile with dissolve
    show xm smile with dissolve

    lxc_ "我现在知道你们一个是游戏宅，一位是甜点爱好者了。"
    lxc_ "但这和你们接下来的计划有什么关系？"
    lxc_ "我好像也帮不上什么忙。"


    show sy clothes1_side1 cat_mouth at emphasis_pop
    sy_ "不对，不如说你正是计划中最关键的一环"


    sy_ "我们昨晚商量后，发现彼此的目的并不冲突，所以……"

    lxc_ "所以？"


    show sy clothes1_front1 smile_close at left with dissolve
    pause 0.3
    show sy smile at bounce_small
    sy_ "所以我们决定——留在这里。"

    lxc_ "……嗯，什么？？？"


    show sy clothes1_side1 cachinnation kp4wl at celebrate_jump
    sy_ "哼哼~感到荣幸吧，人类！本小姐可是决定屈尊住在你这小房子里哦？"


    show sy smile hide_fx with dissolve
    sy_ "虽然面积远比不上家族的古堡，但胜在麻雀虽小，五脏俱全。"
    sy_ "安全，舒适，最重要的是——居然还通了互联网！"


    show sy laugh_open at bounce_small
    sy_ "这可比藏书室里那些老古董有趣多了！"


    show xm smile_close with dissolve
    xm_ "这里的一切对我而言都充满未知，我真的很想好好研究一下！"


    show xm oo at shocked_step_back
    xm_ "啊，当然！我们也不是要永远留在这里……半年，不，三个月就好！"


    show xm shy skin_blush at shy_shrink
    xm_ "只要让我们暂住三个月，等我们熟悉了表世界的基本规则，我们就会离开的！"


    show sy at left
    show xm skin_blush at right
    with dissolve

    lxc_ "……等等，让我想想。"


    show sy calm with dissolve
    show xm calm with dissolve
    pause 0.5

    "说实话，这个请求完全出乎我的意料。"
    "职业习惯让我立刻开始思考，快速分析各种可能性。"
    "日常开销、水电费用、潜在风险……"
    "让两个陌生，而且不是人类的少女住在自己家，怎么想都不是一件「 稳妥 」的事。"
    "可是，「 稳妥 」就一定是正确的选择吗？"
    "不知道为什么，了解到她们的处境之后，我就想起了自己刚来到这座城市时的情形。"
    "那时候的我，也是个需要被帮助的、有点狼狈的陌生人。"


    show xm bewilderment at disappointed_droop
    xm_ "不……不行吗？"

    "见我沉思许久，星弥的脸上写满了不安。"


    show xm sigh with dissolve
    xm_ "……也是呢。突然有两个陌生人说要住在家里，怎么想都很奇怪吧。"
    xm_ "您拒绝也是理所当然的……"

    "她低下头，声音渐渐变小。"


    show sy astonished at emphasis_pop
    sy_ "欸？人类你不愿意吗？"

    sy_ bewilderment "我还以为你肯定会答应呢……" with dissolve

    "听到时语叫我，我下意识地看向她。"


    show sy clothes1_side1 bewilderment at shocked_step_back
    "或许是我思考时的表情过于严肃，她甚至被吓得往后缩了缩。"


    show sy clothes1_front1 bewilderment with dissolve
    sy_ "……真的不行吗？我知道这要求有些强人所难……"


    show sy shy at shy_shrink
    sy_ "但好歹……本小姐也是第一次主动想住在别人家哎？"
    sy_ skin_shy "更何况还是男孩子的家……" with dissolve
    sy_ "我是觉得你人很好，身上的气味也很不错，值得让人信赖……"

    "就在气氛即将滑向更奇怪的方向时，我终于回过神。"


    show sy clothes1_front1 skin_blush bewilderment at left with dissolve
    show xm bewilderment at right with dissolve

    lxc_ "啊，抱歉。"
    lxc_ "我有个坏习惯，一开始认真思考就容易忽略周围。"
    lxc_ "说实话，刚听到你们想留下时，我其实还——"
    lxc_ "挺开心的。"


    show sy astonished with dis_master
    show xm astonished with dissolve

    lxc_ "平淡的生活里突然闯入了新的人和事，迎来了意想不到的变化……这是我心里一直隐隐期待着的。"
    lxc_ "但另一方面，让你们住在这里，就意味着我要对你们负起责任。"

    "像我这样的普通人，真的能做好吗？"


    show xm smile with dissolve
    xm_ "也就是说……您是因为担心我们，才犹豫的吗？"

    lxc_ "可以这么说。"


    show sy clothes1_side1 despise at look_away_small
    sy_ "……什么嘛，原来是这样。"


    show sy smile with dissolve
    sy_ "那有什么好担心的？"
    sy_ "站在你面前的，可是尊贵的血族和天才魔女哦？"


    show sy cachinnation at bounce_small
    sy_ "即便在里世界，我们也绝非等闲之辈，更别说在没有魔法的表世界了。"


    show xm clothes1_front2_no laugh_open at celebrate_jump
    xm_ "没错，而且从年龄上来说，我们可是你的姐姐哦！"
    xm_ "真要担心，也应该是我们担心你才对吧！"

    "不，按实际年龄算，你们恐怕不止是姐姐辈了吧……"


    show sy smile with dissolve
    show xm clothes1_front3_no smile with dissolve

    lxc_ "好吧，是我想太多了。"
    "虽然我担心的不是人身安全就是了。"

    lxc_ "既然你们决定住下来，那有件事就得马上做了。"


    show sy astonished at emphasis_pop
    show xm astonished at emphasis_pop
    syxm_ "是什么？"

    lxc_ "买·衣·服。"

    "我指了指她们身上与这个世界格格不入的装扮。"
    "总不能让她们一直穿着这身显眼的行头出门吧。"


    show sy oo with dis_master
    show xm oo with dissolve
    pause 0.5

    play music bgm_11 fadeout 1.0 fadein 1.0
    scene bg_street_1 with Fade(0.5, 0.5, 0.5)
    pause 0.5
    scene bg_shop_1 with Fade(0.5, 0.5, 0.5)
    pause 0.3


    show sy clothes1_front1 astonished at left with dissolve
    show xm clothes1_front3_no astonished at right with dissolve


    show sy laugh_open kp4wl at excited_lean_forward
    sy_ "人类的世界真厉害，居然还有专门售卖游戏的店铺！"
    show sy laugh_open hide_fx at excited_lean_forward_undo


    show xm smile at excited_lean_forward
    xm_ "林先生，那边的机器到底是什么？居然能轻易地变出一个雪糕！"
    show xm smile at excited_lean_forward_undo

    lxc_ "那个是雪糕机，专门现场做雪糕的。"

    show sy clothes1_side1 laugh_open at char_exit_left
    lxc_ "还有，好奇归好奇，时语你别那么自然地就往游戏店里面走……"





    show sy clothes1_front1 pout at left with dissolve

    lxc_ "我们今天出门的首要任务是买衣服，其他事情等结束了再说。"


    show sy pout at angry_stomp

    "现在的社会越来越开放，在商场里看到两位穿着略显奇特的少女，倒也不会特别引人注目。"
    "别人最多只会觉得，这些人的爱好有点特别而已。"
    "就像那个有名的表情包：「 我这个人物比较特殊.jpg 」"
    "嗯，完全没问题。"


    hide sy
    hide xm
    with dissolve

    scene bg_shop_2 with Fade(0.5, 0.5, 0.5)

    "来到商城三楼，整层都是卖衣服的。"
    "适合她们体型的衣服……好像主要集中在童装区和少女服饰区。"
    "一想到要和店员交流，手就不自觉地微微发抖。"


    show bg_shop_2:
        zoom 1.06
        xalign 0.55
        yalign 1.0
    with dissolve


    fwy_ "先生您好，请问有什么能帮到您？"

    show bg_shop_2:
        zoom 1.08
        xalign 0.35
        yalign 1.0
    with dissolve

    lxc_ "呃，我……来买衣服。"

    fwy_ "是给身后这两位小姑娘选吗？"

    lxc_ "对……"


    show bg_shop_2:
        zoom 1.1
        xalign 0.45
        yalign 1.0
    with dissolve
    fwy_ "两位都好可爱啊！是刚刚参加完节目表演回来吗？"

    show sy clothes1_front1 smile at left with dissolve

    show xm clothes1_front3_no shy at right with dissolve

    "该说不愧是专业的销售人员吗，能如此自然地与陌生人开启对话。"


    show xm shy skin_blush at shy_shrink
    "只不过，被搭话的星弥悄悄拽住了我的衣角，一下子躲到我身后。"

    "嗯？怎么了？"
    "我用眼神向她传达了疑问。"


    show xm bewilderment skin_blush with dissolve
    "星弥露出疑惑的表情，仿佛在说「 不是你让我们不要随便和陌生人说话吗？ 」。"

    "……我出门前确实这么叮嘱过，但也没必要遵守到这种程度吧。"


    show sy clothes1_front1 smile with dissolve
    "另一边的时语虽然脸上还挂着礼貌的微笑，但也只是安静地站在我身旁，一声不吭。"
    "估计她的心思早就飘回刚才的游戏店里，正脑补着自己游玩时的场面吧。"



    show bg_shop_2:
        zoom 1.06
        xalign 0.55
        yalign 1.0
    with dissolve
    fwy_ "呵呵，看来两位小姑娘都有点怕生呢。"

    "不，其实真正怕生的人是我才对。"

    lxc_ "……麻烦你帮她们挑几件居家穿的休闲服。"
    lxc_ "啊，还有……那个，贴身衣物也是，拜托了。"

    "……明明是她们要穿的衣服，为什么非得由我来开口说明啊！"


    fwy_ "好的，您还真是个细心贴心的好哥哥呢。"

    lxc_ "啊哈哈……"

    hide sy
    hide xm
    with dissolve
    pause 0.5

    "最终，在服务员热情又专业的引导下，她们总算选定了各自心仪的衣服。"


    scene black with dissolve
    pause 0.5
    scene cg30 with dissolve
    pause 0.3

    "当服务员把她们从更衣室带到我面前时，我不由得微微一愣。"
    "时语选了一条简单的白色连衣裙，外面套了件宽松的粉色棉质外套，头发上系了个和外套同色系的蝴蝶结发带，整个人看起来清爽又大方，带着一点自然的优雅。"
    "星弥则选了一件浅蓝色的半身外套，里面是一件印着可爱小猫图案的白色T恤，下身搭配深蓝色带点小花边的短裙，整体风格温柔恬静，又隐约透着活泼。"



    show xm at turn_around
    pause 1.0

    "明明是再寻常不过的日常装扮，穿在她们身上，却有种说不出来的、格外适合的感觉。"



    show xm shy skin_blush:
        yalign -3.0
    xm_ "林、林先生，怎么样？"


    show sy clothes2_front1 cat_mouth:
        yalign -3.0

    show cg31 with dissolve
    sy_ "哼哼，本小姐亲自挑选的这件，还不错吧？"


    show cg32 with dissolve

    menu:
        "我觉得"
        "时语的衣服更好看":
            $ first_choice = 1
            jump choice_1_a_shi_yu_de_yi_fu_geng_hao_kan
        "星弥的衣服更好看":
            $ first_choice = 2
            jump choice_2_b_xing_mi_de_yi_fu_geng_hao_kan
        "两人的衣服都好看":
            $ first_choice = 3
            jump choice_3_c_liang_ren_de_yi_fu_dou_hao_kan

    return

label choice_1_a_shi_yu_de_yi_fu_geng_hao_kan:
    call AutoAfterChoicesCheckReset () from _call_AutoAfterChoicesCheckReset

    lxc_ "嗯，都很适合你们。"
    lxc_ "不过时语这身搭配，既有气质又贴近生活，像是微服私访的大小姐一样。"


    show sy clothes2_front1 shy at shy_shrink:
        yalign -2.0
    show cg33 with dis_master
    sy_ "……哼，我本来就是大小姐啊。"


    show xm clothes2_front1 sigh at disappointed_droop:
        yalign -2.0

    lxc_ "也是，难怪这么有品味。"


    show sy clothes2_front1 smile_close with dissolve

    lxc_ "虽然都选好了，但机会难得，要不要再逛逛？"

    show cg34 with dis_master
    syxm_ "好！"

    "果然，女孩子都是天生喜欢逛服装店的。"
    jump after_menu_1

label choice_2_b_xing_mi_de_yi_fu_geng_hao_kan:
    call AutoAfterChoicesCheckReset () from _call_AutoAfterChoicesCheckReset_1

    lxc_ "嗯，都很适合你们。"
    lxc_ "不过星弥这一身格外清新有活力，说你是住在隔壁的邻家少女，也没人会怀疑。"


    show xm clothes2_front1 smile_close:
        yalign -2.0
    show cg35 with dis_master
    xm_ "嘻嘻，我挑的时候就在想，要穿得轻松日常一点。"


    show sy clothes2_front1 pout with dissolve:
        yalign -2.0

    lxc_ "这样穿很好看，很有新鲜感。"


    show xm clothes2_front1 laugh_open at bounce_small
    show sy clothes2_front1 pout at look_away_small

    lxc_ "虽然都选好了，但机会难得，要不要再逛逛？"
    show cg34 with dis_master
    syxm_ "好！"

    "果然，女孩子都是天生喜欢逛服装店的。"
    jump after_menu_1

label choice_3_c_liang_ren_de_yi_fu_dou_hao_kan:
    call AutoAfterChoicesCheckReset () from _call_AutoAfterChoicesCheckReset_2

    lxc_ "说实话，两套都挺好看的。"
    lxc_ "时语是有气质又日常的休闲风，星弥是温柔恬静的邻家女孩风——风格完全不同，但都特别适合你们。"
    lxc_ "自然又有生活感，很好看。"


    show sy clothes2_front1 smile at bounce_small:
        yalign -2.0
    show xm clothes2_front1 smile_close at bounce_small:
        yalign -2.0
    show cg33 with dis_master
    "她们本来就出众的外貌，在合适衣服的衬托下，显得更加明亮动人了。"


    show cg36 with dis_master
    show sy clothes2_front1 cat_mouth
    sy_ "是吧，本小姐的审美还不赖吧？"


    xm_ clothes2_front1 smile_close "嗯……能听到您这么说，真的很开心。" with dissolve

    lxc_ "虽然都选好了，但机会难得，要不要再逛逛？"
    show cg34 with dis_master
    syxm_ "好！"

    "果然，女孩子都是天生喜欢逛服装店的。"
    jump after_menu_1

label after_menu_1:

    hide sy
    hide xm
    with dissolve


    call achievement (4) from _call_achievement_5

    scene bg_shop_1 with Fade(0.5, 0.5, 0.5)

    show xm clothes2_front2_no calm at right with dissolve

    show sy clothes2_front1 pout at left with dissolve
    "之后，我们一起在服装店里逛了一圈。"
    sy_ "——所以，为什么不买那件猫耳睡衣啊？"



    lxc_ "那件太贵了，而且实用性不高。"


    show sy pout at angry_stomp
    sy_ "但明明很可爱啊？"

    lxc_ "世界上可爱的事情太多了，我总不能全都买下来吧。"


    show sy bewilderment at emphasis_pop
    sy_ "林小凑，难道你……工资其实并不高？"

    lxc_ "……不要问社会人这么扎心的问题。"


    show sy oo with vpunch
    "我用食指轻轻弹了一下时语的额头。"


    show sy pout with dissolve

    "比起网络上那些挥金如土的人，我的收入确实不算特别高，但偶尔让自己过得更舒服一点还是没问题的。"

    lxc_ "『 好钱花在刀刃上 』是我的宗旨。"
    lxc_ "把钱用在合适的地方，不是更好吗？"
    lxc_ "来，这个给你。"


    show sy calm with dissolve
    "我从口袋里掏出一盒东西，递给了时语。"


    show sy astonished kp1wl at emphasis_pop
    sy_ "！这不是刚刚店里的《公主传说-流泪之国》吗！"


    show sy laugh_open hide_fx at celebrate_jump
    "时语双眼发亮，小心翼翼地捧起游戏卡带，开心得像个收到生日礼物的小孩子。"

    lxc_ "还有，这个是给星弥的。"


    show xm astonished kp1wl at emphasis_pop
    xm_ "提、提拉米苏冰淇淋！"


    xm_ bewilderment hide_fx "但我记得这个挺贵的吧？" with dissolve

    lxc_ "还好，就当是庆祝你们来我家的小礼物。"


    show xm focus with dissolve
    lxc_ "呃，你快吃吧，我看你口水都要滴到包装盒上了。"


    show xm smile_close at bounce_small
    xm_ "嗯！"


    show xm clothes2_front3_no smile_close with dissolve
    xm_ "唔姆~不过，您是什么时候去买的？"

    lxc_ "趁你们换衣服的时候。"


    show xm smile with dissolve
    xm_ "可我们换衣服也没花很长时间呀……"

    lxc_ "是啊，所以我不得快去快回，就怕被你们发现。"

    "其实是怕离开太久，这边出什么幺蛾子……"
    "那位店员实在太热情了，不知是职业素养还是真心喜欢，不停地说「 这件超适合她们！ 」「 那件也很可爱！ 」，一副恨不得把整家店都推荐给我们的样子。"
    "一不留神，她们就要变成店里的真人换装模特了。"


    show sy clothes2_front1 cat_mouth at emphasis_pop
    sy_ "作为人类，你还挺能干的嘛！"
    sy_ "不枉本小姐屈尊住在你家！"


    show sy smile with dissolve
    "她带着些许嚣张的笑意，十分珍惜地把卡带抱在怀里。"

    lxc_ "是是是。"


    show sy clothes2_front1 laugh_open kp4wl at bounce_small
    sy_ "那我们赶紧回去吧！我好想立刻开始玩！"

    lxc_ "别急，回去前还得买今晚的晚饭。"


    show sy clothes2_front1 pout hide_fx at angry_stomp
    sy_ "哎，怎么这么麻烦啊。"

    lxc_ "是啊，人类的生活就是这么麻烦。"


    show sy calm with dis_master
    show xm calm with dis_master

    "呼吸，进食，睡眠。"
    "日复一日，重复着相似却必需，甚至有点无趣的事。"
    "不如说，每个活着的生命都在重复这样的循环——哪怕来自「 里世界 」的她们，应该也不例外。"


    show xm clothes2_side1 smile with dissolve
    "我看向一旁安静的星弥，却发现她已经把冰淇淋重新盖好，放回了盒子。"

    lxc_ "不吃了吗？"


    show xm shy skin_blush at shy_shrink
    xm_ "已经吃掉一半啦，我想留着另一半晚上再享受……"

    "这么快就吃一半了？明明刚刚我和时语才说了几句话……"

    lxc_ "带回家的话，可能会化掉哦？"


    show xm clothes2_front2_no smile_close skin_blush with dissolve
    xm_ "没关系的，我已经用冰魔法把它完美保存好了！"


    show xm cat_mouth at bounce_small
    xm_ "哪怕有顶级火魔法来袭，我也敢保证它不会融化！"

    lxc_ "……这里应该不会出现什么顶级火魔法吧。"


    show sy clothes2_front1 pout at angry_stomp
    sy_ "快点走吧人类，赶紧去买菜然后回家！"


    show sy at char_exit_left

    "时语催促着，一个劲地把我往某个方向推。"

    hide sy
    hide xm
    with dissolve

    lxc_ "不是，菜市场不在那边啊。"


    play music bgm_18 fadeout 1.0 fadein 1.0
    scene bg_sky_5
    show bg_sky_5 at bg_pan_left
    with Fade(0.5, 0.5, 0.5)
    pause 0.5

    "夕阳缓缓落下，夜幕悄然降临。"


    scene bg_kitchen_2 with Fade(0.5, 0.5, 0.5)

    "小小的厨房里飘散着清甜的香气，夹杂着温暖的烟火气。"

    lxc_ "呼，总算做好了。"

    "可乐鸡翅、苦瓜炒蛋、红烧焖肉，蒜蓉生菜……准备了三个人的分量，应该差不多了。"
    "一个人生活的时候，常常因为太累就随便点个外卖应付一下。"
    "现在家里多了两个人，从各方面来看，还是自己做饭更划算，也更健康。"


    scene bg_living_room_2 with dissolve


    show xm clothes2_front2_no focus at center with dissolve

    "摘下围裙回到客厅，看到星弥正一脸专注地盯着平板。"
    "做饭前怕她无聊，我顺手点开网站上的视频给她看。"
    "只见她两只小手规规矩矩地扶着屏幕，指尖轻触时也特别小心，像是对待什么易碎的宝物。"

    "让我瞧瞧她在看什么……《论微波炉的加热原理》？"
    "妹啊，看这个也学不会用微波炉的……"


    scene cg415 with dissolve

    "相比之下，沙发另一侧的时语就吵闹许多。"
    "她一回到家，就非常自觉地拿起了桌上的游戏机。"
    "真是的，到底谁才是这个家的主人啊……"

    "我给她买的是一款很有名的角色扮演游戏。"
    "凭借强大的交互系统，玩家经常能实现各种离谱却又合理的操作。"


    show cg418 with dis_master
    sy_ clothes2_front1 oo "啊！这雪山还会扣血的！好冷！我的角色要冻死啦！" with dissolve

    "不过对于像她这样的新手来说，当务之急是先活下去。"

    lxc_ "去山脚下摘几个辣椒，做成辣味料理就能取暖了。"


    show cg411 with dis_master
    sy_ pout "山脚太远啦！而且我已经发现举火把也可以取暖！" with dissolve

    lxc_ "……等会儿遇到怪物你就知道惨了。"


    hide cg418
    show cg418 with dis_master
    sy_ oo "被怪物围殴了！赶紧换武器……可这样又没法取暖了！" with dissolve


    hide cg411
    show cg411 with dis_master
    sy_ pout "可恶！" with dissolve

    "你看，我说什么来着。"

    scene bg_living_room_2 with dissolve


    show sy clothes2_front1 calm at left with dissolve
    show xm clothes2_front2_no calm at right with dissolve

    lxc_ "饭做好了，先去厨房吃饭吧。"


    show sy smile at nod_small
    show xm smile at nod_small
    syxm_ "好~"

    "两位少女几乎是同时应声。"
    "星弥回应得快我不意外，但时语也这么干脆，倒是有点出乎意料。"
    "该说不愧是大小姐吗？或许她家的规矩比我想象的还要严格。"


    show sy despise at look_away_small
    sy_ "……总觉得你在想什么很失礼的事情。"

    lxc_ "没有没有，我怎么敢。"

    scene bg_kitchen_2
    with fade


    show sy smile at left with dissolve
    show xm clothes2_front2_no smile at right with dissolve

    lxc_ "说起来，有件事忘记问了。"
    lxc_ "……你们会用筷子吗？"

    "一位是血族大小姐，一位是魔女。"
    "从「 人设 」上看，都不像是会用筷子的类型。"


    show sy clothes2_front2 smile at emphasis_pop
    sy_ "当然。"


    show xm clothes2_front2_no smile_close at nod_small
    xm_ "我也会哦。"


    lxc_ "啊？真的假的。"
    lxc_ "我还以为你们只会用刀叉之类的。"


    show sy clothes2_side1 calm with dissolve
    sy_ "家里常接待世界各地的访客和商人。"
    sy_ "在餐桌上打交道多了，自然就学会各种餐具的用法。"


    show xm smile_close at bounce_small
    xm_ "我是在各地旅行时，偶然在美食街上学会的~嘻嘻。"


    show sy clothes2_front1 smile with dissolve
    show xm clothes2_front2_no smile with dissolve

    lxc_ "原来如此。"
    "看来对于里世界的认知，还真不能全靠刻板印象去判断。"


    show xm calm with dissolve
    xm_ "林先生……平时都是一个人住吗？"

    "星弥对着碗里的红烧肉轻轻吹了口气，小声问道。"

    lxc_ "嗯，出来工作后就一直自己住。"
    lxc_ "要是和别人合租，恐怕也没办法让你们住进来了。"


    show sy cat_mouth at emphasis_pop
    sy_ "这么说，我们是不是该感谢你是自己一个人住？"


    show sy smile with dissolve
    "时语慢条斯理地夹起鸡翅，像猫咪般在试探性地品尝人类的佳肴。"

    lxc_ "这好像不是什么值得夸奖的事吧……"


    show xm clothes2_front3_no smile with dissolve
    xm_ "但我和时语真的很幸运呢。"
    xm_ "虽然是意外才来到你家，却恰好遇到独居又善良的您。"


    xm_ calm "如果这两个条件缺了任何一个，我们可能就无处可去了。" with dissolve


    xm_ smile_close "这么一想，简直像是命运特意安排的一样。" with dissolve

    "命运吗……"
    "我并不太喜欢这个词。"


    show sy calm with dissolve
    show xm calm with dissolve

    lxc_ "我反而觉得，这更像是一次普普通通、却又刚刚好的偶遇。"
    lxc_ "因为不是被谁安排好的，才显得更难得，更让人想珍惜。"
    lxc_ "也因为发生在最平常的日子里——才让我觉得特别真实。"


    show xm laugh_open at celebrate_jump
    xm_ "不是必然的命运，而是偶然的日常吗……"
    xm_ "嗯，我很喜欢您这个说法！"


    show sy clothes2_side1 shy at look_away_small
    sy_ "……真没想到，人类——不，林小凑你也会说出这么感性的话呢。"

    lxc_ "总感觉，我在你眼里的形象是不是有点奇怪？"


    show sy clothes2_front1 smile with dissolve
    sy_ "没有啊，不如说……我觉得还意外地可靠？"

    "时语轻笑一声，微微地抿了下筷子尖，眼里带着狡黠的光。"


    show sy cat_mouth clothes2_side2 at emphasis_pop
    sy_ "作为得到本小姐赏识的奖励，这些苦瓜就都给你吃了！"

    lxc_ "我说你啊……挑食可不是好习惯哦？"


    show sy clothes2_side1 despise at look_away_small
    sy_ "高贵的血族不需要吃软弱的蔬菜！"

    lxc_ "挑食的孩子可没资格在我家吃饭！"


    show sy clothes2_front1 cry skin_cry at shy_shrink
    sy_ "呜……你这是虐待贵族！"


    show xm clothes2_front2_no smile with dissolve
    xm_ "好啦好啦，您就别欺负她了。"

    "星弥悄悄伸出筷子，语气温和地打圆场。"


    show xm smile_close with dissolve
    xm_ "时语，要不我帮你分一些？"

    lxc_ "不行，星弥！别惯着她——她至少得吃掉一半才行！"


    show sy oo skin_blush at shocked_step_back
    sy_ "一半？！你、你这是要谋杀贵族吗？！"


    hide sy
    hide xm
    with dissolve
    pause 0.3

    "最后，在时语强烈抗议和讨价还价下，剩下的苦瓜还是由我们三人平分了。"


    scene bg_sky_3 at bg_pan_right
    with dissolve
    pause 0.5

    "夜空渐深，永恒的明月悄然升起，星光零星点缀其间，而屋内的灯光却愈发温暖明亮。"


    scene bg_kitchen_2 with dissolve
    pause 0.3

    "餐桌上回荡着轻松的氛围，三人嬉笑打闹的声音此起彼伏——"
    "时语不满的嘟囔、星弥温柔的劝解，还有我那假装严肃却藏不住笑意的要求。"
    "这份偶然交织的日常，正在悄悄变成我们彼此最温暖、也最特别的礼物。"

    stop music
    scene cg100000 with fade

    $ renpy.block_rollback()
    if persistent.op_watched:
        $ renpy.movie_cutscene("images/op.webm")
    else:
        $ _skipping = False
        $ _rollback = False
        show expression Movie(play="images/op.webm", size=(2560, 1440),loop=False) as op_movie
        $ renpy.pause(113.5, hard=True)
        scene black
        hide op_movie
        $ _rollback = True
        $ persistent.op_watched = True
        $ _skipping = True



    scene bg_office_4 with dissolve
    pause 0.3


    show bg_office_4:
        zoom 1.08
        xalign 0.35
        yalign 1.0
    with dissolve

    tsa_ "小凑，最近气色不错啊。"


    tsa_ "上班都会偷笑了。"

    lxc_ "……有这么明显吗？"


    tsa_ "超——明显的！你之前上班那表情，像上坟一样！"
    tsa_ "现在简直是坟头长出了花，还是带闪光特效的那种！"

    lxc_ "……你这比喻能不能稍微吉利点？"


    show bg_office_4:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve

    lxc_ "不跟你扯了，我还得赶新项目的案子。"
    lxc_ "你也是，有空和我闲聊，还不如赶紧把活干完。"


    show bg_office_4:
        zoom 1.08
        xalign 0.35
        yalign 1.0
    with dissolve
    tsa_ "哎，别急嘛，灵感来了我马上立刻下一秒就能写完！"


    with vpunch
    tsb_ "老张，我要的东西好了没？！催三次了！"


    with hpunch
    pause 0.2
    tsa_ "立刻马上！"

    show bg_office_4:
        zoom 1.0
        xalign 0.5
        yalign 1.0
    with dissolve


    "我们公司是一家规模不大的游戏开发工作室。"
    "主要做一些老板喜好的，风格奇奇怪怪的游戏。"
    "作为执行策划，我每天的任务就是：完成上级的需求，给其他同事下达需求，再跟他们来回扯皮、验收反馈。"
    "除了偶尔和同事互相调侃几句外，大多数时候都不是什么开心的事。"
    "真希望能快点到周末……"


    play music bgm_10 fadeout 1.0 fadein 1.0
    scene bg_sky_4
    show bg_sky_4 at bg_zoom_in
    with Fade(0.5, 0.5, 0.5)
    pause 0.5

    "在和公司比命长的日子里又熬过一周，终于迎来了周末。"


    scene bg_living_room_1:
        zoom 1.5
        xalign 0.0
        yalign 1.0
    with Fade(0.5, 0.5, 0.5)
    pause 0.5

    "阳光穿过阳台，照进帐篷的小窗，把我晒醒了。"
    "自从把房间让给那两位里世界的「 客人 」后，我就一直睡在客厅的沙发上。"
    "不过昨晚整理储物柜时，意外翻出了这个被遗忘在箱底的帐篷。"
    "那是毕业时买的，本来满怀期待想用在毕业旅行上，结果连着下了好几天大雨，计划彻底泡汤。"
    "之后忙着投简历、找工作、碰壁、再投简历再碰壁……这件事也就渐渐被忘了。"
    "真没想到，时隔这么久，最后居然是在自己家里用上了。"
    "不过说实话，在帐篷里醒来的感觉还挺有意思的，有点像小时候梦寐以求的「 秘密基地 」。"

    scene bg_living_room_1
    with dissolve

    show xm clothes2_front2 calm at center with dissolve
    pause 0.3

    "我拉开帘子，发现星弥早已坐在沙发上，手上握着她的法杖，正悄悄地盯着我这边看。"


    show xm astonished at emphasis_pop
    xm_ "啊，早上好！"

    lxc_ "早上好。"


    show xm clothes2_front2_no smile with dissolve

    "醒来后有人可以打招呼的感觉，真不错。"

    lxc_ "刚才凑那么近，是在看什么？"


    show xm oo at shocked_step_back
    xm_ "！没、没有啊，我怎么会偷看您起床呢！"


    show xm shy skin_blush at shy_shrink
    xm_ "我只是……对帐篷的结构有点好奇……"

    "……我也没说你偷看啊。"


    show xm clothes2_front3_no calm skin_blush with dissolve

    lxc_ "我要去刷牙了，你想看的话可以进去。"


    show xm bewilderment with dissolve
    xm_ "哦……但我真的没有偷看喔？"

    lxc_ "……"
    "行吧。"


    hide xm hide_fx with dissolve

    "我起身走向洗手间，身后还不时传来「 哇~原来里面长这样！ 」之类充满惊叹的嘀咕声。"


    pause 0.5

    scene bg_living_room_1
    with fade


    show xm clothes2_front3_no smile at center with dissolve

    "等我洗漱回来，星弥已经考察完毕，端端正正地坐回沙发上。"

    lxc_ "平时都起这么早吗？"

    "我从零食箱里拿出两片早餐饼干递给她。"


    show xm smile_close at bounce_small
    xm_ "唔姆~睡醒就起来啦。以前养成的习惯，天亮了就不想赖床。"


    show xm cat_mouth with dissolve
    "她像只小松鼠似的，小口小口地嚼着食物。"


    show xm smile with dissolve

    lxc_ "这样啊。"
    lxc_ "时语又在睡懒觉？"


    show xm calm at nod_small
    xm_ "血族嘛，晚起也很正常。"

    lxc_ "也是。"

    "放在以前，我大概也会像时语一样，周末狠狠地睡个懒觉。"
    "但不知怎么的，最近醒来时总觉得精神还不错……明明工作还是一样忙啊。"


    show xm clothes2_side1 focus with dissolve
    xm_ "其实今天起这么早，还有一个原因是……有件事想拜托您！"

    lxc_ "什么事？"


    show xm laugh_open at emphasis_pop
    xm_ "请、请教我做饭吧！"


    show xm smile with dissolve
    xm_ "如果我学会了，我和时语就不用天天吃外卖了。"


    show xm shy skin_shy at shy_shrink
    xm_ "晚上还可以给您做点宵夜什么的……"
    xm_ focus skin_blush "……可以吗？" with dissolve

    lxc_ "……当然可以，只是有点意外。"


    show xm laugh_open skin_blush at emphasis_pop

    lxc_ "没想到，你和我的想法一样。"

    "她们住进我家也有一周了。我下班晚，只能让她们凑合吃外卖，心里总有点过意不去。"

    lxc_ "要是你能学会做饭，确实帮大忙了。"


    show xm smile at nod_small
    xm_ "嗯！"


    show xm smile_close at bounce_small
    xm_ "嘻嘻，没想到我和您想到一起去了。"


    show xm smile with dissolve

    lxc_ "是啊。"
    "这算不算是某种默契呢？"

    lxc_ "那事不宜迟，我们现在就开始吧？"


    show xm laugh_open at celebrate_jump
    xm_ "好的！我准备好了！"


    hide xm with dissolve
    scene bg_kitchen_1 with dissolve


    show xm clothes2_front3_no focus at center with dissolve

    lxc_ "俗话说万事开头难，我们就从最基础的煮饭开始。"
    lxc_ "把适量的米倒进内锅，加水没过米面，用手轻轻搅动直到水变浑浊。"
    lxc_ "然后把水倒掉，重新加入比米面略高一点的水就行了。"
    lxc_ "想洗得干净点可以多重复几次，不过偷懒的话，洗一次也没关系。"


    show xm smile at nod_small

    lxc_ "你先试试看，按我刚才的步骤洗一次米。"


    show xm smile_close at emphasis_pop
    xm_ "好！"


    show xm clothes2_front2_no focus with dissolve
    xm_ "首先把米倒进锅里……三个人的话，两杯米就够啦。"
    xm_ "然后加水，轻轻画圈搅拌……"
    xm_ "倒掉后再重复几次，最后再加入比米高一点点的水……"

    "她就像在进行一项严谨的实验，一边小声复述步骤，一边小心翼翼地操作着。"

    lxc_ "做得很好，最后记得把锅外面的水珠擦干净就行。"


    show xm smile with dissolve
    xm_ "这样就可以了吗？"

    lxc_ "没错，接下来只要把内锅放回电饭煲，按下『 煮饭 』键，等它自己完成就好。"


    show xm astonished at emphasis_pop
    xm_ "人类的科技好厉害，比调配魔药简单好多！"


    show xm smile with dissolve

    lxc_ "是啊。有了这些电器，只要掌握方法，谁都能做出不错的饭菜。"

    "网络上就有很多视频，专门教人只用电饭煲就做出各种各样的美食。"


    show xm focus with dissolve
    xm_ "饭大概要煮多久呀？"

    lxc_ "嗯……大概二十到三十分钟吧。"
    lxc_ "我先去楼下丢个垃圾，回来再教你做菜的部分。"


    show xm smile at nod_small
    xm_ "嗯！"


    hide xm with dissolve


    scene bg_community_1 with Fade(0.5, 0.3, 0.5)

    "微风轻轻拂过脸颊，连带着心情也愉悦起来。"
    "即便是教人做饭这样简单的小事，也能带来小小的成就感。"
    "我把垃圾丢到指定位置，脚步轻快地返回公寓。"

    pause 0.3

    "正要深吸一口清新的空气——却隐约嗅到一股焦糊的味道。"
    "嗯？哪来的烧焦味？"
    "好像是……从我家传来的？"


    show bg_community_1:
        zoom 1.08
        xalign 0.2
        yalign 1.0
    with dissolve


    fd_ "小林啊，你是不是把菜炒糊了？"

    "连在楼下散步的房东都闻到味，轻声询问我。"

    lxc_ "……应该没有吧。"
    lxc_ "我回去看看。"


    "只是煮个饭而已，没理由会出问题吧？"


    scene bg_living_room_1 with dissolve


    show xm clothes2_side1 bewilderment at center with dissolve

    xm_ "您、您回来啦，丢垃圾辛苦了。"

    lxc_ "丢个垃圾而已，没什么。"
    lxc_ "话说，厨房里是不是有东西烧焦了？"


    show xm smile_close kp8wl with dissolve
    xm_ "没、没有啊，怎么会呢……"

    "虽然她尽力保持平静，但脸颊旁的汗珠却出卖了她。"

    lxc_ "……你出了好多汗喔？要不要擦一擦？"


    show xm astonished kp29wl at emphasis_pop
    xm_ "欸？真的吗？"

    "趁她低头擦汗，我侧身绕过她走向厨房。"


    show xm oo hide_fx at shocked_step_back
    xm_ "……！不、不行啦，林先生，现在还不能进去！"

    "虽然她立刻反应过来，像只小鸭子般急急忙忙追过来，但我还是抢先一步进了厨房。"


    hide xm with dissolve
    scene bg_kitchen_1 with dissolve

    "乍一看没什么问题。"
    "那么焦味的来源是——"

    lxc_ "我靠！"


    scene bg_kitchen_1 at Shake((0, 0, 0, 0), 0.5, dist=15)
    pause 0.5

    scene sd3
    with fade

    "原本白色的电饭煲半边焦黑，还冒着缕缕黑烟。"
    "我赶紧打开窗户通风。"
    "检查了一圈，其他电器看起来没什么问题。不过为了安全起见，我还是先把它们的插头都拔了。"
    "家里也没因为电线短路而停电，看来只是电饭煲出问题了。"
    "可正常电饭煲坏了也不会这样吧？我才离开了几分钟啊。"

    scene bg_kitchen_1
    with fade


    show xm clothes2_side1 cry skin_cry at center with dissolve
    xm_ "T-T"


    show xm cry skin_cry at shy_shrink
    xm_ "呜呜……"

    lxc_ "刚刚发生了什么事吗？"
    lxc_ "比如插座冒火花，或者听到奇怪的声响之类的？"


    show xm bewilderment skin_blush with dissolve
    xm_ "刚刚的话，我在好奇地观察电饭煲运作，然后……"

    lxc_ "然后？"


    show xm shy at shy_shrink
    xm_ "然后我就想，既然能用魔力加快熬魔药的速度，那是不是也能用魔力加快电饭煲煮饭的速度呢……"


    xm_ bewilderment "……然后电饭煲就冒出火花了。" with dissolve

    lxc_ "原来如此。"
    lxc_ "你没受伤吧？"


    show xm at deny_shake_small
    xm_ "没、没有。"


    show xm bewilderment at disappointed_droop
    xm_ "我还以为您会像上次那样生气……"
    xm_ "毕竟我弄坏了电饭煲。"

    "她低下头不敢看我，像个做错事的小孩。"

    lxc_ "这个嘛……"


    show xm calm with dissolve

    "微波炉那次，主要是太反常识了。"
    "没想到真的有人会把鸡蛋放进微波炉，而且还是一次放好几个……"
    "但这次情况不同——魔力运作的原理我根本不懂，也不可能未卜先知地提醒她「 不要对电器使用魔法 」。"

    lxc_ "电饭煲坏了是有点麻烦，不过也不是什么大问题"
    lxc_ "这是我从老家带过来的，已经用了好几年了。"


    show xm astonished at emphasis_pop
    xm_ "真、真的吗？"


    show xm sigh at disappointed_droop
    xm_ "但不管怎么说，都是我弄坏了您的电饭煲。"
    xm_ "以前也是这样，每次我想帮老师的忙，总会搞砸……"

    lxc_ "……"
    lxc_ "我问一下，你为什么想用魔力加快电饭煲煮饭的速度呢？"


    show xm shy skin_blush at shy_shrink
    xm_ "我想着，如果能快点做好饭的话，您和时语就能更快吃上饭了……"

    lxc_ "原来如此。"


    show xm bewilderment skin_blush with dissolve

    "真是个善良的孩子。"

    lxc_ "虽然结果不太理想，但你的心意是好的，不是吗？"


    show xm shy skin_blush with dissolve
    xm_ "林先生……"

    lxc_ "而且没有人受伤，已经是不幸中的万幸了。"
    lxc_ "所以别这么沮丧啦。"
    lxc_ "下次做类似的事情之前，先和我商量一下就好。"


    show xm smile at nod_small
    xm_ "我、我知道了！"


    show xm laugh_open at bounce_small
    xm_ "下次我一定会做好的！"


    show xm smile with dissolve

    lxc_ "很好，保持积极的心态最重要。"

    "虽然这话从一个社畜嘴里说出来，好像没什么说服力就是了。"


    show xm clothes2_front3_no at right with dissolve
    show sy clothes2_front1 astonished kp1wl at left with dissolve
    sy_ "呜哇，你们在厨房搞什么？"


    sy_ not_good hide_fx "在研究希卡炸弹吗？" with dissolve

    lxc_ "真有希卡炸弹的话，厨房早就被炸飞了。"
    lxc_ "大小姐，懒觉睡醒了？"


    show sy pout at angry_stomp
    sy_ "才不是睡懒觉！这是血族正常的作息！"


    show sy sigh with dissolve
    sy_ "而且我是被焦味熏醒的……"

    lxc_ "是吗，那还真是抱歉。"


    show sy calm with dissolve
    sy_ "看这样子，是电饭煲炸了？"

    lxc_ "是啊。"


    show xm cry skin_cry at disappointed_droop
    xm_ "呜呜……"


    show sy astonished at emphasis_pop
    sy_ "这个损毁情况……该不会是星弥对它用魔力了吧？"

    lxc_ "是……等等，你怎么知道？"


    show sy clothes2_side1 calm with dissolve
    sy_ "类似的情况我见过很多次了。"
    sy_ "以前商人从表世界带来的电器里，好多都是这么坏掉的。"


    show xm smile clothes2_front2_no skin_blush with dissolve
    xm_ "时语知道为什么会这样吗？"


    show sy clothes2_front1 bewilderment with dissolve
    sy_ "一开始本小姐也不清楚，还以为表世界的物品都特别容易坏。"


    show sy focus at excited_lean_forward
    sy_ "后来才发现，原来这个世界的电力和魔力是相斥的。"
    sy_ "当两种不同属性的能量作用于同一个物体时，就会互相排斥。"


    show sy calm at excited_lean_forward_undo
    sy_ "轻则无事发生，重则……像这个电饭煲一样。"


    show sy smile with dissolve
    sy_ "从那之后，我用电器时都特别小心。"


    show xm smile at nod_small
    xm_ "原来是这样……"


    show sy smile_close with dissolve
    sy_ smile_close "魔女会的人不怎么接触这边的东西，不知道也很正常。" with dissolve


    show sy smile at left with dissolve
    show xm smile at right with dissolve

    lxc_ "还有这种说法啊……"
    lxc_ "你要是早点告诉我们就好了。"


    show sy despise at look_away_small
    sy_ "哼，那还不是因为你们没问。"

    "时语撇了撇嘴，一副「 我才不会主动说呢 」的傲娇模样。"


    show sy clothes2_front1 bewilderment with dissolve
    sy_ "我饿了。"


    show sy smile with dissolve
    sy_ "既然电饭煲坏了，我们出去吃吧？"


    show sy pout with dissolve
    sy_ "最近天天吃外卖，我都吃腻了。"


    show sy laugh_open with dissolve
    sy_ "好想去商场五楼那家看起来就超~级香的肥牛店！"

    lxc_ "没必要，今天就在家吃吧。"


    show sy sigh with dissolve
    sy_ "欸——怎么这样嘛……"

    lxc_ "经常出去吃，我的钱包可撑不住。"


    show sy clothes2_side1 shy with dissolve
    sy_ "就一次嘛~那家店看起来真的很好吃！"

    "时语轻轻地拽住我的衣角，眨着大眼睛，一副可怜巴巴的样子。"

    lxc_ "……装可爱这招对我可没用哦。"


    show sy clothes2_front1 pout with dissolve
    sy_ "切，居然不上当。"


    show sy sigh with dissolve
    sy_ "以前我这样做，家里人什么都会答应我的……"

    "虽然我不会一直宠着她，不过，不得不承认——时语撒娇的样子，确实挺可爱的。"


    hide sy
    hide xm
    with dissolve


    scene bg_sky_4 at bg_pan_left with fade
    pause 0.5

    "提问，在没有电的时代，人类是如何做饭的？"
    "答案很简单，也很无聊——用火就好。"
    "和普通套房不同，这栋独立公寓并没有禁止使用明火的规定。"
    "既然可以用火，那做饭就不成问题了。"


    scene bg_kitchen_1 with fade

    lxc_ "煎两块牛排，配上生菜和煎蛋……"
    lxc_ "盖在热腾腾的米饭上——简易版牛排饭完成！"

    "最近的冷冻包装牛排性价比很高，只要选对品牌，肉质和口感都相当不错。"


    show sy clothes2_front1 astonished at left with dissolve
    show xm clothes2_front2_no focus at right with dissolve

    sy_ "哦哦……！"


    show sy smile with dissolve
    sy_ "虽然没能出去吃是有点遗憾。"
    sy_ "但时隔一周能再次尝到你做的饭，倒也不错。"


    show xm focus at nod_small
    xm_ "冒着热气的牛排和米饭……！"
    xm_ "看起来就很好吃！"



    show sy smile with dissolve
    show xm smile with dissolve

    lxc_ "吃吧，别光顾着感叹了。"


    show xm clothes2_front3_no shy with dissolve
    xm_ "啊，明明本来是想替您分担厨房的工作，结果最后还是全交给您来做了……"
    xm_ "好不甘心……！"


    "星弥一脸不甘，嘴里的动静却没有停下来。"


    show xm calm with dissolve

    lxc_ "毕竟今天出意外了。"
    lxc_ "安全起见，还是我来做饭吧。"
    lxc_ "反正机会很多，下次再教你就好。"


    show xm smile at nod_small
    xm_ "嗯嗯！"

    lxc_ "做饭这种事，本来就不是一朝一夕就能学会的。"
    lxc_ "我反而觉得，星弥你有点太着急了。"
    lxc_ "总感觉你好像什么事都想靠魔法解决……"

    "第一次见面时是这样，保存冰淇淋时是这样，就连刚才煮饭时也是这样。"


    show sy bewilderment at nod_small
    sy_ "好像是哦。"

    lxc_ "魔女会的魔女都这么热衷于用魔法吗？"


    show xm sigh at disappointed_droop
    xm_ "毕竟我唯一擅长的，也就只有魔法了……"


    show xm not_good with dissolve
    xm_ "啊哈哈……"

    "她的笑声里带着一丝不易察觉的落寞。"
    "总觉得，这背后似乎有什么隐情。"
    "不过，再追问下去，就有点不识趣了。"


    show sy clothes2_front1 astonished at emphasis_pop
    sy_ "人类，今天晚上我们去吃肥牛吧！"

    lxc_ "我们现在不是已经在吃了吗？"
    lxc_ "而且，我之前说过今天在家吃吧？"


    show sy smile with dissolve
    sy_ "我当然知道啦。"


    show sy laugh_open at excited_lean_forward
    sy_ "可你做的牛排饭都这么好吃，不就让我更想尝尝外面专业大厨的手艺了嘛！"

    show sy laugh_open at excited_lean_forward_undo

    lxc_ "这算什么逻辑啊……"


    show sy pout at angry_stomp
    sy_ "我不管，我就要去吃嘛！"


    show sy pout with dissolve
    "时语鼓起脸颊，气呼呼地瞪着我。"


    show sy clothes2_side1 despise with dissolve
    sy_ "我以前在家里，可是经常能吃到顶级牛肉的！"

    lxc_ "但你现在不是离家出走了吗？"


    show sy clothes2_front1 shy skin_shy at shy_shrink
    sy_ "唔……！"

    "她一下子语塞，小脸涨得通红。"
    "明明理亏却还强撑着不肯认输的模样，实在让人想好好捏上一把。"
    "虽然她总自称是高贵的血族大小姐，但闹起脾气来，其实也跟普通女孩没什么两样。"


    show sy skin_blush at look_at_right
    sy_ "星弥呢？你就不想去外面吃吗？"


    show xm bewilderment with dissolve
    xm_ "我？我其实也挺想尝尝看的……"


    xm_ smile_close "不过，能在家吃到林先生亲手做的饭菜，也挺满足的！" with dissolve


    show sy pout at emphasis_pop
    sy_ "虽然我也觉得好吃，但这种时候星弥你应该站在我这边嘛！"


    show sy focus at excited_lean_forward
    sy_ "这样我们二对一，他说不定就妥协了！"
    show sy focus at excited_lean_forward_undo

    "喂喂，哪有当着当事人的面大声密谋的啊。"


    show xm smile with dissolve
    xm_ "可、可是林先生做的饭真的很香呀……"


    xm_ smile "诚实面对自己的味觉，才是对食物最大的尊重哦？" with dissolve


    show sy oo at glare_shake
    sy_ "现在不是在讨论美食家的自我修养啦！"


    hide sy
    hide xm
    with dissolve

    "最后，我和时语达成协议，答应以后偶尔会带她去吃顿好的，她才乖乖听话。"
    "毕竟我自己偶尔也会想去外面吃一顿，她的心情我倒是能理解。"
    "只不过，这个「 偶尔 」具体是多久一次嘛……那就得看我的心情了。"


    play music bgm_19 fadeout 1.0 fadein 1.0
    scene bg_living_room_2 with Fade(0.5, 0.5, 0.5)


    show sy clothes2_front1 laugh_open at center with dissolve

    sy_ "人类，来打游戏吧！"
    show sy cat_mouth at bounce_small
    sy_ "我最近学会玩网络游戏了！"

    "周末的夜晚，时语刚从浴室出来后就兴冲冲地朝我喊道。"


    show sy astonished at excited_lean_forward
    sy_ "你不是在游戏公司里上班吗？那打游戏一定很厉害吧？"
    show sy astonished at excited_lean_forward_undo
    lxc_ "……你这是典型的刻板印象啊。"
    lxc_ "在游戏公司上班，和打游戏厉不厉害之间可没有必然联系。"


    show sy oo at emphasis_pop
    sy_ "欸，真的假的？"


    show sy calm with dissolve

    lxc_ "因为工种细分，很多人不懂游戏也一样能胜任工作。"
    lxc_ "这种情况在美术部门特别常见。"


    show sy bewilderment with dissolve
    sy_ "不懂游戏也能做游戏设计，感觉好矛盾啊……"

    lxc_ "一般来说，只要负责领导的人有足够专业知识就行了。"
    lxc_ "不过作为策划的话，肯定还是得懂游戏才行。"


    show sy smile with dissolve
    sy_ "不管了，总之你会打游戏就行。"


    show sy cat_mouth at bounce_small with dissolve
    sy_ "来陪我玩嘛？"

    lxc_ "好吧，我也好久没玩了。你想玩什么？"


    show sy laugh_open at celebrate_jump
    sy_ "《巅峰争夺战》！那个最近很出名的大逃杀射击游戏！"

    lxc_ "嗯？这个游戏最火的时候都是几年前的事了吧……"



    show sy bewilderment with dissolve
    sy_ "才几年前而已，不就是最近吗？"
    lxc_ "……几年前怎么也算不上最近吧。"

    "不是很懂你们血族的时间观念。"


    show sy smile at emphasis_pop
    sy_ "总之一起来玩啦！"

    lxc_ "……行吧，我先去房间把旧电脑拿出来。"



    lxc_ "你先开一局热热身。"


    show sy eyes_closed with dissolve
    sy_ "已经在打啦~"


    scene cg410
    with fade


    show sy clothes2_front1:
        yalign -3.0

    "等我从房间抱着笔记本出来，时语的屏幕已经显示阵亡画面了。"

    lxc_ "这么快就结束了？"


    show sy bewilderment at look_away_small
    sy_ "我、我没拿到武器，被人打死了……"

    lxc_ "懂了。和别人跳同一个降落点，结果对方先捡到枪。"


    show cg411 with dis_master
    show sy pout
    sy_ "他、他只是运气好而已！"


    show cg412 with dis_master
    show sy clothes2_front2 astonished
    sy_ "你快点上游戏和我一起玩！"

    lxc_ "别急，刚更新完。"
    lxc_ "上号了，我看看你ID叫——『 高贵优雅残酷美丽的神秘千金 』？"


    show cg413 with dis_master
    show sy clothes2_front1 cachinnation
    sy_ "哼哼，怎么样？很有本小姐的风格吧？"

    lxc_ "……挺好的。"

    "就是别人会以为你是个中二病的学生。"
    "不过，因为这游戏能随便改名，玩家ID倒是一个比一个整蛊。"
    "比如「 转生成为飞天意面之王 」「 从隔壁转游，这里有能成为我母亲的女人吗 」之类的。"
    "某种意义上，时语这名字还算正常。"


    show cg410 zorder 100 with dis_master
    sy_ bewilderment "让我看看你的……『 路过的蒙面武者 』？"


    show cg414 zorder 100 with dis_master
    sy_ despise "哼，太短了！一点气势都没有！还是本小姐的名字好听！" with dissolve

    lxc_ "又不是名字越长就越好听……"


    show cg415 zorder 101 with dis_master
    show sy smile

    lxc_ "开游戏吧，我进房间了。"


    show cg410 zorder 102 with dis_master
    show sy bewilderment
    sy_ "好吧……不过，你坐那么远干嘛？"

    lxc_ "桌子又不小，没必要挤这么近吧？"


    show cg416 zorder 103 with dis_master
    show sy cat_mouth
    sy_ "靠近一点才有打游戏的氛围嘛~"

    "时语往我的身旁挪近了一点。"
    "刚洗完澡的她，身上散发出一股好闻的香气，像是淡淡的玫瑰花香。"
    "不知道是沐浴露的味道，还是她身上自带的芬芳。"


    show cg415 zorder 105 with dis_master
    show sy clothes2_side2 smile
    sy_ "我一直很想这样和别人一起打游戏。"
    sy_ "以前在家里，都没人对这些感兴趣，只能自己玩。"


    show cg417 zorder 106 with dis_master
    sy_ smile_close "嘻嘻。" with dissolve

    "她挨在我身边，笑得特别开心。"

    lxc_ "……是吗，你不介意就行。"


    show cg412 zorder 107 with dis_master
    show sy clothes2_front2 astonished
    sy_ "发现敌人！我上了！"

    lxc_ "等等！别冲那么快——"


    show cg418 zorder 108 with dis_master
    show sy oo
    sy_ "啊！我被打倒了！"


    show cg411 zorder 109 with dis_master
    show sy pout
    sy_ "对面怎么这么坏！三个人一起行动！"

    lxc_ "所以说了别那么急……"

    "谈话间，队友趁机打倒一个，局面变成二对二。"


    show cg419 zorder 110 with dis_master
    show sy calm

    lxc_ "时语，爬到那个箱子后面。"
    lxc_ "我找机会救你。"


    show cg410 zorder 111 with dis_master
    show sy bewilderment
    sy_ "好吧……但他们会放过我吗？"

    lxc_ "我猜他们会先救人。"
    lxc_ "然后再让队友开枪牵制……好，我赶到了！"


    show cg413 zorder 112 with dis_master
    show sy cachinnation
    sy_ "被救起来了！好哎！"


    show cg410 zorder 113 with dis_master
    sy_ bewilderment "但为什么你的角色是用拳头救人啊！" with dissolve

    lxc_ "愚人节特效皮肤是这样的！"


    show cg411 zorder 114 with dis_master
    show sy pout
    sy_ "明明被你救了，为什么还是感觉好不爽……"

    lxc_ "活下来就算不错了，还这么多要求。"


    show cg412 zorder 115 with dis_master
    show sy focus
    sy_ "哼，等本小姐恢复好状态就要他们好看！"

    "我和重回战场的时语互相配合，对手很快就被击溃了。"

    lxc_ "差一枪！"


    show cg415 zorder 116 with dis_master
    show sy smile
    sy_ "交给本小姐吧！"
    "她一个位移冲脸，顺利击杀对方。"


    show cg413 zorder 117 with dis_master
    show sy cachinnation at celebrate_jump
    sy_ "哼哼，不愧是我！"


    show cg415 zorder 118 with dis_master
    show sy smile

    lxc_ "下次看到人别急着冲啊，先观察。"


    show cg416 zorder 119 with dis_master
    show sy clothes2_front1 cat_mouth
    sy_ "知道啦，赢了不就行了嘛！"

    scene bg_living_room_2
    with fade


    show sy at left with dissolve
    show xm clothes2_front3_no smile at right with dissolve
    xm_ "嗯？林先生是在和时语玩游戏吗？"

    "星弥刚洗完澡出来，身上还微微散发着热气。"


    show xm smile with dissolve
    xm_ "明明您在游戏公司工作，但在家却很少见您玩游戏呢。"

    lxc_ "平时下班太累，没动力玩，只想躺着玩手机。"


    show xm focus at excited_lean_forward

    "她走到我身边，仔细地看着我屏幕上的画面。"
    "眼角的余光能瞥见她湿润的头发，细小的水珠粘在上面闪闪发光，随后沿着发丝滑到脖颈。"
    "同样的，她身上也散发着好闻的味道。"
    "和时语的玫瑰香不同，是淡淡的奶香，如同铃兰一般清新。"

    lxc_ "……"
    show xm smile at excited_lean_forward_undo

    "我自觉地往另外一边靠了靠，结果碰到了时语的外套。"
    "再靠近就要碰到时语了，我只好在左右为难的状态下继续游戏。"


    show sy oo at emphasis_pop
    sy_ "人类，别发呆了，我被打倒了快救我！"

    "两边的香气不断飘来，让我的注意力有些分散。"

    lxc_ "哦哦，抱歉抱歉……"

    "但我还没赶到她身边，我和队友都被陆续击倒了。"

    lxc_ "？"


    show sy bewilderment with dissolve
    sy_ "你怎么也被打倒了？"

    lxc_ "遇到高手了，没办法。"

    "这游戏的匹配机制还真是一如既往的烂……"


    show sy pout at emphasis_pop
    sy_ "再开一局！"

    scene bg_living_room_2
    with fade

    show sy clothes2_front1 pout at left with dissolve
    show xm clothes2_front3_no smile at right with dissolve


    show sy oo at shocked_step_back
    sy_ "啊，你又死了！"

    lxc_ "笔记本屏幕太小了，我根本看不清人。"
    lxc_ "别搜我的遗产了，隔离区要过来了。"


    show sy bewilderment with dissolve
    sy_ "但我想多拿点东西再进去嘛……哎？我怎么倒了！"

    lxc_ "游戏后期就是这样，所以我叫你快跑。"
    lxc_ "开新一局吧。"

    scene bg_living_room_2
    with fade

    show sy clothes2_front1 astonished at left with dissolve
    show xm clothes2_front3_no smile at right with dissolve


    sy_ "这次对面好像只有一个人，我们一起上！"

    lxc_ "……不对劲，对面水平好像有点高。"


    show sy sigh at disappointed_droop
    sy_ "啊，又输了。"


    show sy cry skin_cry at shy_shrink
    sy_ "呜呜……"

    lxc_ "被炸鱼了啊……"


    show xm focus clothes2_front2_no at emphasis_pop
    xm_ "林先生，这黑白的游戏画面是正常现象吗？"

    lxc_ "……"

    "要不是星弥一脸好奇地问我，我都要怀疑是不是被阴阳怪气了。"
    "但她这么可爱，怎么也不可能是腹黑吧……"


    show xm calm with dissolve

    lxc_ "不正常。虽然我们的水平不高，但这次是因为遇上高手了。"
    lxc_ "打个比方……就像在新人魔女的比赛里，突然出现了像星弥你这样经验丰富的魔女。"


    show xm shy skin_blush at shy_shrink
    xm_ "经验丰富……其实我也不是啦。"


    show xm smile skin_blush at nod_small
    xm_ "不过游戏的事我明白了。"

    xm_ bewilderment "但您刚才说的『 炸鱼 』是什么意思？" with dissolve


    show xm focus at excited_lean_forward
    xm_ "是指什么好吃的东西吗？"
    show xm focus at excited_lean_forward_undo

    "和刚才好奇的眼神不同，现在的星弥属于两眼发光的状态。"

    lxc_ "此『 炸鱼 』非彼『 炸鱼 』啦。"
    lxc_ "不过，下次确实可以找机会试着做炸鱼给你们吃。"


    show xm laugh_open at celebrate_jump
    xm_ "好哎！"


    show sy bewilderment skin_blush with dissolve
    sy_ "……听你们聊吃的都把我说饿了。"


    show sy cat_mouth at bounce_small
    sy_ "人类，喂我吃薯片。"

    lxc_ "薯片就放在那儿，你自己拿不就好了？"


    show sy smile with dissolve
    sy_ "别人喂的比较香嘛。"

    lxc_ "……真拿你没办法。"


    show sy smile_close with dissolve
    sy_ "啊~"

    lxc_ "大小姐，在下亲手喂您的这片香浓红烩味薯片如何？"


    show sy despise with dissolve
    sy_ "还可以，要是味道再淡一点就更好了。"

    lxc_ "……你还挑上了。"
    lxc_ "星弥要吃吗？"


    show xm smile with dissolve

    "喂完时语后，我下意识地也拿了一块递到星弥嘴边。"
    "但我立刻想到，她并没有让我喂她。"

    lxc_ "呃，抱歉。"


    show xm shy skin_shy at shy_shrink

    "她的小脸顿时染上红晕。"

    "我刚要把薯片收回来自己吃，她却凑过来轻轻咬住了薯片。"


    show xm eyes_closed at emphasis_pop
    xm_ "好、好赤！！！"

    "或许是因为激动，她的说话声变得有些含糊，让我也有点不好意思。"

    lxc_ "……是我失礼了。"


    show xm shy skin_shy at deny_shake_small
    xm_ "没、没关系的！我不介意……"

    "空气中弥漫着一种微妙的尴尬。"
    "明明喂时语的时候那么自然，可面对星弥……却莫名让人心跳加速，甚至有点脸红。"
    "这究竟是怎么回事呢？"


    show sy cat_mouth at bounce_small
    show xm shy skin_blush with dissolve
    sy_ "人类，再喂我一块嘛。"

    lxc_ "遵命，大小姐！"


    show sy bewilderment with dissolve
    sy_ "怎么还学起了管家的说话语气……"


    show sy focus with dissolve

    "多亏了时语，我才从那有点奇怪的氛围中脱离出来。"
    "为什么同样是喂食，对象不同，感觉就完全不一样？"
    "我下意识地看向时语——"
    "她正随意地靠在沙发上，两只手在狂按手柄，打得入神时还会不自觉地嘟囔两句。"
    "这副模样，任谁看了，都只会觉得是个彻头彻尾的宅女。"
    "根本不会有人想到，她其实是血族中的贵族，贵族中的大小姐。"
    "原来是这样。"
    "是因为时语的这份随意感，才让一切都显得那么自然吧。"


    show sy sigh at disappointed_droop
    sy_ "我们今天晚上打了这么久，好像没赢几局呢。"


    show sy smile with dissolve

    lxc_ "毕竟是竞技网游，输多赢少也很正常，开心就好。"


    show sy pout with dissolve
    sy_ "但输了怎么开心得起来啊？"

    lxc_ "你是想要赢，还是想要开心？"


    show sy cat_mouth at bounce_small
    sy_ "我两个都想要嘛~"

    lxc_ "全都要……还真是任性啊。"
    lxc_ "那你去玩单机不就好了？"
    lxc_ "之前的《公主传说》打完了吗？"


    show sy laugh_open at celebrate_jump
    sy_ "打完了！是个好游戏！"

    lxc_ "这么快？"

    "不用上班就是好啊，能天天打游戏。"


    show sy shy skin_shy with dissolve
    sy_ "而且，难得周末，玩单机的话就……"

    "时语撇了我一眼，扭过头去。"


    show sy despise skin_blush at look_away_small
    sy_ "哼！没什么！"

    "……这是怎么了？"


    show xm smile_close at bounce_small
    xm_ "毕竟是难得的周末，还是想和您一起过嘛。"
    xm_ "平时您工作这么忙，回家都很累了，时语她也不好意思缠着你。"

    lxc_ "是这样吗？"


    show xm smile with dissolve
    xm_ "嗯，不光是时语，其实我也是这么想的。"


    xm_ cat_mouth "嘻嘻。" with dissolve

    "在周末的休闲时光里，大家一起开开心心地度过吗……"
    "我确实也曾幻想过这样的生活，没想到近在咫尺时，反而没能立刻察觉。"


    show sy smile with dissolve

    lxc_ "来吧时语，再开一把。"
    lxc_ "这次我教你一个有意思的打法。"


    show sy smile_close at look_away_small
    sy_ "……哼，真拿你没办法。"

    "她虽然还是一副高傲的样子，但语气里却藏着些许笑意。"


    show sy calm with dissolve

    lxc_ "你先选这个大招是护盾的角色。"


    show sy bewilderment with dissolve
    sy_ "然后呢？"

    lxc_ "然后正常打就行……等等！发现敌人了！快开盾！"


    show sy astonished at emphasis_pop
    sy_ "开啦开啦！"

    lxc_ "很好！我要把炸弹到装你身上……搞定！"

    "时语冲到敌人脸上，身上的炸弹随后把对方全部炸倒了——但她自己也因此而被炸翻在地。"

    lxc_ "哎，没想到这远古BUG还没修复……不过战术成功，司令部会记住你的牺牲的！"


    show sy pout at angry_stomp
    sy_ "喂，我连枪都没开就被炸死了啊？！"

    lxc_ "欸？是这样吗？"
    lxc_ "没关系啦，反正赢了嘛，结局好一切都好。"


    show sy black skin_black at glare_shake
    sy_ "林·小·凑！下次换你当炸弹！"

    lxc_ "好好好~"


    show xm smile_close at bounce_small
    xm_ "呵呵，两位玩得真开心呢。"

    scene bg_sky_3 with Fade(0.5, 0.5, 0.5)

    "最后时语用同样的套路成功收割残局，我们吵吵闹闹地度过了一个充满欢笑的夜晚。"


    play music bgm_6 fadeout 1.0 fadein 1.0
    scene bg_kitchen_1 with Fade(0.5, 0.5, 0.5)

    pause 0.5

    scene cg6 with fade

    xm_ "……呼。"

    show cg61 with dis_master
    xm_ astonished "集中精神，想象它是邪恶的怪物！"

    "星弥拿着菜刀，全神贯注地盯着眼前的「 敌人 」。"


    xm_ "……嘿呀！"

    with vpunch
    "她以惊人的气势挥刀而下，「 敌人 」瞬间被劈成两半，其中一半「 啪嗒 」一声飞进了水槽里。"
    "事先声明，我们只是在切土豆而已。"
    "今天是星弥正式开始学习做饭的日子。"

    lxc_ "星弥……我们只是在准备炖咖喱的食材，不是讨伐魔王。"
    lxc_ "放心吧，它是不会跳起来咬你的。"

    "我捡起水槽里的土豆，把它切成相对规整的方块状。"


    show cg62 with dis_master

    lxc_ "放在砧板上，轻轻扶稳，慢慢切下去就好。"
    lxc_ "你也来试一下吧。"


    show cg63 with dis_master
    xm_ focus "好、好的！用手扶着，慢慢切……"

    lxc_ "对，就是这样。看，这不是做得很好吗？"

    "虽然动作还有些笨拙，土豆也被切得大小不一，但总算顺利完成了。"


    show cg64 with dis_master
    xm_ laugh_open "成功了！它看起来变得像真正的食物了！"

    lxc_ "……土豆本来就是食物吧？"


    show cg65 with dis_master

    xm_ bewilderment "唔，我的意思是，它看起来像餐桌上的食物啦！"



    xm_ "我又不是笨蛋！"

    lxc_ "说的也是，至少比某个血族大小姐聪明很多。"


    show sy clothes2_front1 pout:
        yalign -3.0
    sy_ "臭人类，我可是听得到的！"

    "时语的怒吼立刻从客厅传了过来。"

    lxc_ "是吗？那要不大小姐你也来下厨试试？"


    show sy pout skin_blush at glare_shake
    sy_ "你你你……欺负人！！！"
    sy_ "你明知道我不擅长的！"


    hide sy with dissolve


    show cg6 with dis_master

    lxc_ "哈哈。"

    "在此之前，时语也曾说过要一起学做饭。"
    "但在她展现出灾难级别的厨艺后，我觉得还是不要让她下厨为妙。"

    lxc_ "不过，星弥的心情我也能理解。"
    lxc_ "看到原始的食材逐渐变成餐桌上的样子，确实很有成就感。"


    show cg65 with dis_master

    xm_ bewilderment "说起来，您是怎么学会做饭的？"

    lxc_ "最初是跟着网上的教程一点点学的，后来练习多了，慢慢地也就像样了。"


    hide cg62
    show cg62 with dis_master

    xm_ calm "原来是这样。"

    scene bg_kitchen_1 with fade

    lxc_ "接下来该处理洋葱了。"


    show xm clothes2_front2_no oo kp29wl at center, shocked_step_back
    xm_ "！"

    "一听到「 洋葱 」两个字，星弥立刻像只受惊的小动物般躲到了我身后。"

    lxc_ "怎么了？"


    show xm bewilderment hide_fx at shy_shrink
    xm_ "老师说过，洋葱里蕴含着会让人流泪的魔法。"
    xm_ "虽然没有危害，但一不小心就会中招……"
    xm_ "传说中有个女子就是因为被洋葱刺激到，流泪哭倒了一座城……"

    lxc_ "什么翻版孟姜女哭长城……那只是一种夸张的说法吧。"
    lxc_ "处理不当的话，确实容易流眼泪。"
    lxc_ "但只要像这样……放在清水里切，就不会刺激到眼睛了。"


    show xm bewilderment with dis_master
    xm_ "真的吗？"

    lxc_ "是啊。你看，我现在切它也不会流眼泪啊？"


    show xm astonished at emphasis_pop
    xm_ "真的呢！剩下的就交给我吧！"


    show xm focus at lean_in

    "清水中的洋葱最终被切得东一块西一块，但至少安全地处理完了。"
    "接着把其他准备好的食材放进锅里，咖喱的准备工作就完成大半了。"


    show xm smile with dissolve
    xm_ "咖喱的做法真的好简单呢。"
    xm_ "感觉比起您之前做的可乐鸡翅、红烧肉什么的要简单好多。"

    lxc_ "虽然我也想过教你别的菜，比如番茄炒蛋、红烧排骨之类的。"
    lxc_ "但综合考虑后，还是觉得咖喱是最适合新手的入门菜式。"


    show xm smile_close at nod_small
    xm_ "嗯！"

    "看着锅里「 咕嘟咕嘟 」冒着热气的咖喱，星弥的脸上洋溢着前所未有的满足感。"
    "她拿起大勺子，小心翼翼地搅拌着。"


    show xm astonished at emphasis_pop
    xm_ "哇，林先生您看！颜色变深了，香味也飘出来了！"


    show xm calm at lean_in
    xm_ "感觉和熬制魔药的过程有点像呢……都要控制火候，注意材料的变化。"


    show xm smile_close at excited_lean_forward_undo
    xm_ "不过，做饭给人的感觉更温暖，更让人安心。"

    lxc_ "这就是美食最大的特点吧。"
    lxc_ "不需要复杂的咒语，只要用心，就能让人感到温暖。"


    show xm calm with dissolve
    xm_ "……是啊。我好像有点明白，自己为什么这么喜欢美食了。"


    show xm cat_mouth at bounce_small
    xm_ "特别是甜品！"

    lxc_ "因为你是个小吃货吗？"


    show xm black skin_black with dissolve
    xm_ "……"


    show xm at look_away_small
    xm_ "林先生平时肯定不受欢迎吧。"

    lxc_ "……欸？突然人身攻击是怎么回事？！"
    lxc_ "而且你笑着说出这种话更可怕了啊！"


    xm_ "这个嘛，您就自己慢慢猜吧，呵呵。"


    hide xm with dissolve


    scene bg_living_room_1 with dissolve

    "炖好咖喱，回到客厅，发现时语正抱着膝盖，蜷缩在沙发中间，眼睛紧紧地盯着电视屏幕。"
    "电视上正在放一部动画电影——一根穿着宇航服的香蕉，正孤零零地飘在宇宙里，深情地望着远处那颗像荷包蛋一样的地球。"


    show sy clothes2_front1 calm at left with dissolve

    sy_ "……明明只是宇宙中的一颗尘埃，却承载了无数生命的重量。"
    sy_ "永恒的孤独与守望，这就是你的使命吗？"

    "屏幕里的香蕉伸出天线，轻轻碰了碰一颗漂浮的太空草莓，背景音乐变得悠扬而伤感。"


    show sy sigh with dissolve
    sy_ "哪怕近在咫尺，却还是无法触碰吗……"


    show xm clothes2_front2_no astonished at right with dissolve
    xm_ "好厉害……"

    "也许是星弥情不自禁的感叹声惊动了她，时语猛地转过头——"
    "看到我们俩站在沙发后面，她整个人瞬间僵住，脸唰地一下就红了，眼神也从刚才那种软软的样子，一下子变得慌乱起来。"


    show sy shy skin_shy at shy_shrink
    sy_ "咳！你、你们什么时候出来的？！竟然偷看！太失礼了！"

    lxc_ "这里是我家哎，哪有什么偷看不偷看的。"
    lxc_ "而且我们是正大光明走过来的，是某人看得太投入了没发现而已。"
    lxc_ "怎么样，这部电影？"

    "听到我这么问，时语回过神，恢复成平时那副有点高傲的表情。"


    show sy despise skin_blush at look_away_small
    sy_ "哼，马马虎虎吧。作为娱乐消遣而言，还算不错。"

    lxc_ "是吗？原来刚刚的『 永恒的孤独与守望 』『 近在咫尺却无法触碰 』之类的话，是我听错了啊。"


    show sy pout skin_blush at angry_stomp
    sy_ "无、无礼之徒！本小姐那只是……只是在客观地进行艺术鉴赏！"

    with vpunch
    "她的脸更红了，像被踩到尾巴的猫一样，抓起手边的抱枕就朝我扔过来。"

    lxc_ "喂，别乱丢东西啊。"

    "我轻松接住抱枕，抱在怀里。"


    show sy despise at glare_shake
    sy_ "那不是普通的香蕉，那是承载了孤独使命的勇敢宇航员！"


    show xm smile_close with dissolve
    xm_ "它和那颗草莓的感情，真的好感人啊……"


    show sy astonished at emphasis_pop
    sy_ "没错！这是关于勇气与牺牲的宏大叙事！"


    show sy pout at excited_lean_forward
    sy_ "你这个只关注表象的人类根本不懂！"
    show sy pout at excited_lean_forward_undo

    lxc_ "别瞎说，这电影我看过好多次了，基本内核还是明白的。"
    lxc_ "与其吐槽我，我劝你们还是关心一下快被外星猩猩吃掉的宇航员吧。"


    show sy oo at shocked_step_back
    show xm oo at shocked_step_back
    syxm_ "啊！不要啊！"

    "两人的注意力立刻被吸回屏幕，表情同步紧张起来，时语还不自觉地握紧了小拳头。"

    "一番有惊无险的逃脱戏后，香蕉宇航员总算安全了。"

    "时语松了口气，随即又板起脸。"


    show sy despise at look_away_small
    sy_ "咳哼！算、算它逃过一劫。"
    sy_ "这部作品虽然制作粗陋，但内核的表达……嗯，勉强还算有点深度吧。"
    sy_ "值得本小姐花费些许时间品鉴。"

    lxc_ "总体上确实是部好电影。"
    lxc_ "说起来，其实我以前参与过这部电影的改编游戏项目。"


    show xm astonished at emphasis_pop
    xm_ "真的吗？林先生好厉害！"


    sy_ bewilderment "……真的假的？" with dissolve

    lxc_ "我说的是实话，不信拉倒。"


    show xm smile_close at bounce_small
    xm_ "我信哦！毕竟林先生的气质，和这部电影有点像嘛……"

    "不，一点也不像好吧……她该不会觉得我是某种食物的拟人化吧？"


    show sy despise at look_away_small
    sy_ "哼……本小姐又没说不信。"


    sy_ bewilderment "然后呢？那个游戏怎么样？能玩一下吗？" with dissolve

    lxc_ "不行，那游戏到最后都没做完。"


    show sy pout with dissolve
    sy_ "为什么啊？"

    lxc_ "有很多原因。一开始是老板一拍脑袋想合作，然后开发初期版本各方都不满意，最后就中止了。"
    lxc_ "电影改编游戏哪有那么简单。"


    show sy sigh with dissolve
    sy_ "这样啊……"


    show xm sigh with dissolve
    xm_ "好可惜……"

    lxc_ "还好啦，也过去很久了。"
    lxc_ "星弥的咖喱做好了，先吃饭吧！"

    scene bg_kitchen_1 with fade


    show xm clothes2_front3_no laugh_open at right with dis_master
    show sy smile at left with dis_master
    xm_ "嗯嗯！我特意选了微辣口味！"


    xm_ smile_close "应该大家都会喜欢吃的！" with dissolve


    show sy oo at shocked_step_back
    sy_ "欸……微辣吗？"


    show xm bewilderment with dissolve
    xm_ "怎么了？有什么问题吗？"


    show sy shy at shy_shrink
    sy_ "没、没有！本小姐只是确认一下！"

    lxc_ "喂，你该不会是……"

    "我凑到时语身边小声问道。"


    show sy pout at angry_stomp
    sy_ "不准说！哪怕猜到了也不准说！"

    lxc_ "行吧，可别勉强哦？"


    show sy despise at look_away_small
    sy_ "要你管……本小姐自有分寸。"


    show xm shy at shy_shrink
    xm_ "怎、怎么样？"


    hide sy
    hide xm
    with dissolve

    "我舀起一勺咖喱送进嘴里，米饭软硬适中，咖喱的浓淡也恰到好处。"

    lxc_ "不错。"
    lxc_ "土豆炖得软烂，鸡肉也很入味，火候掌握得刚好。"

    "虽然咖喱算是入门菜式，但对初学者来说，能精准控制火候已经非常不容易了。"


    show sy clothes2_front1 smile at left with dissolve
    sy_ "看来星弥很有下厨的天赋啊。"


    show xm clothes2_front2_no cat_mouth at right with dissolve
    xm_ "嘻嘻，其实是我以前熬魔药的经验帮上忙啦！"


    show xm smile_close at bounce_small
    xm_ "虽然切菜还要多练习，但对火候的控制我可很有自信！"

    lxc_ "是啊。"
    lxc_ "不过光听我一个人的评价可能不够客观，也得问问时语觉得怎么样。"


    show xm focus at lean_in
    xm_ "嗯！时语觉得合口味吗？"

    "另一边，时语的表情就比较精彩了——嘴角忍不住上扬，可眉头又微微皱着，一副「 好吃但不得不忍耐 」的纠结样子。"


    show sy bewilderment skin_blush with dissolve

    xm_ "怎么样？"


    show sy not_good skin_blush with dissolve
    sy_ "……嗯，很好吃。"
    sy_ "就是，就是有点……"

    lxc_ "行了，别硬撑啦。"

    "我忍住笑意，转身从冰箱拿出一瓶牛奶，递到她面前。"

    lxc_ "这种事告诉星弥也没关系吧？"


    show xm bewilderment with dissolve
    xm_ "欸，怎么了？"

    lxc_ "其实……她不是很能吃辣。"


    show sy shy skin_shy at shy_shrink
    sy_ "但这毕竟是星弥第一次做的菜，我不想让你失望嘛……"

    "她像小猫舔牛奶似的，小口小口地喝着，罕见地没用「 本小姐 」自称——看来是真的被辣到了。"


    show xm cry skin_blush at disappointed_droop
    xm_ "时语……你不用勉强自己的！你能这么想，我就已经很开心了！"


    show sy skin_blush calm with dissolve
    sy_ "没关系的……至少，让我把碗里的吃完吧。"

    scene bg_kitchen_1 with fade

    show sy clothes2_front1 smile_close at left with dissolve
    show xm clothes2_front2_no calm at right with dissolve

    "她挤掉眼角被辣出的泪花，坚持把剩下的咖喱吃完了。"

    sy_ "我吃完了！真的……很好吃！"


    show xm smile_close at nod_small
    xm_ "嗯！下次我一定会把口味调得更轻的！"

    "看到她们俩和睦的样子，我也不自觉地笑了起来。"
    "不过，真没想到时语会怕辣啊。"
    "难道是因为吸血鬼怕大蒜，而大蒜是辣的，所以产生了连带反应？"


    show sy black skin_black with dissolve
    sy_ "……你这个奇怪的眼神，总感觉在想什么很失礼的事。"

    lxc_ "怎么会呢。"

    "她直觉还真是准得可怕啊。"


    play music bgm_7 fadeout 1.0 fadein 1.0
    scene bg_office_4 with Fade(0.5, 0.5, 0.5)


    show bg_office_4:
        zoom 1.08
        xalign 0.65
        yalign 1.0
    with dissolve

    lxc_ "总之你先按案子上写的测试反馈，把BUG修一下吧。"


    tsc_ "……好。"


    show bg_office_4:
        zoom 1.0
        xalign 0.5
        yalign 1.0
    with dissolve

    "把问题反馈给程序员后，我回到自己的工位。"
    "最近的项目跟进压力不小，新来的程序员经验不足，代码上出现了很多问题。"
    "按他的工作效率，估计修复又要花上大半天……"
    "有点怀念之前的程序员了……算了，人已经离开了，再想这些也没用。"
    "但愿新人别拖慢整体项目进度就好。"


    show bg_office_4:
        zoom 1.08
        xalign 0.3
        yalign 1.0
    with dissolve
    tsa_ "喔喔喔——！"

    lxc_ "……怎么这么兴奋？"


    tsa_ "今天可是发工资的日子，能不兴奋吗？"


    with vpunch
    tsa_ "终于能买那款限量版机甲模型了！"

    lxc_ "发工资啊……"


    show bg_office_4:
        zoom 1.0
        xalign 0.5
        yalign 1.0
    with dissolve

    "不知不觉已经到月中了。"

    menu:
        "看着短信里到账的提示，要拿这笔钱做什么好呢？"
        "给时语买新游戏":
            $ second_choice = 1
            jump choice_4_a_gei_shi_yu_mai_xin_you_xi
        "给星弥买新甜品":
            $ second_choice = 2
            jump choice_5_b_gei_xing_mi_mai_xin_tian_pin
        "和她们去游乐园":
            $ second_choice = 3
            jump choice_6_c_he_ta_men_qu_you_le_yuan

    return

label choice_4_a_gei_shi_yu_mai_xin_you_xi:
    call AutoAfterChoicesCheckReset () from _call_AutoAfterChoicesCheckReset_3


    scene bg_living_room_2 with Fade(0.5, 0.5, 0.5)

    lxc_ "我回来了。"
    lxc_ "…………"

    "推开门，居然看到时语正趴在地上，拿着扫把认真清扫沙发底下的灰尘，活脱脱一副专业家政员的样子。"


    show sy clothes2_front1 focus at center with dissolve
    sy_ "……"

    lxc_ "不好意思走错地方了——"


    show sy pout at angry_stomp
    sy_ "没走错！别装看不见！"

    lxc_ "看到你在做清洁什么的，我都怀疑自己是不是走入什么异空间了……"


    show sy despise at look_away_small
    sy_ "……本小姐也是会做家务的好吗？"
    sy_ "真是的，在你眼里我到底是什么形象啊。"

    lxc_ "嗯……贪玩，慵懒，偶尔还有点爱撒娇吧。"


    show sy black skin_black with dissolve
    sy_ "……你确定没把心里话和玩笑说反吗？"

    lxc_ "啊，不小心说漏嘴了。"


    show sy pout skin_blush kp13wl at glare_shake
    sy_ "林·小·凑！！！"

    with vpunch

    lxc_ "抱歉抱歉，开个玩笑。"
    lxc_ "作为赔礼，这个给你。"


    show sy despise hide_fx at look_away_small
    sy_ "哼，肯定又是随手买的东西吧，本小姐才没这么容易……这是，《猛汉狩猎传·黎明》？！"


    show sy oo at shocked_step_back
    sy_ "而且还是豪华版！"

    lxc_ "怎么样，作为赔礼足够有诚意了吧？"

    "时语一把接过卡带，开心地抱在怀里，但马上又轻咳一声，摆出高傲的样子。"


    show sy despise at look_away_small
    sy_ "……算你识相。"


    show sy bewilderment with dissolve
    sy_ "不过，这个应该很贵吧。"

    lxc_ "还好，刚发工资。而且我是那家店的熟客，用了折扣券。"
    lxc_ "最重要的是，这游戏可以联机组队玩。"
    lxc_ "刚好符合你之前说过的，既能赢，又能玩得开心，还能和我一起玩。"


    show sy shy skin_shy at shy_shrink
    sy_ "我随口说的话你还记得啊……不对不对！本小姐可没说过想和你一起玩！"

    lxc_ "啧，这都没把你骗到。"


    show sy pout skin_blush at look_away_small
    sy_ "哼，臭人类，总是捉弄我……"

    "明明最初见面的时候，是你在捉弄我才对吧……"


    show sy shy skin_blush at shy_shrink
    sy_ "……总、总之，谢谢你了。"

    lxc_ "不客气，反正本来就是送你的礼物。"
    lxc_ "只要你卡关的时候别气得咬手柄就行了。"


    show sy pout skin_blush at angry_stomp
    sy_ "本小姐才不会这么做呢！"

    "之后，我们窝在沙发上，畅玩了一晚上的《猛汉》。"

    jump after_menu_2

label choice_5_b_gei_xing_mi_mai_xin_tian_pin:
    call AutoAfterChoicesCheckReset () from _call_AutoAfterChoicesCheckReset_4


    scene bg_kitchen_2 with Fade(0.5, 0.5, 0.5)

    lxc_ "我回来了。"

    "推开门，一股熟悉的炒蛋香气飘来，是星弥在厨房里做菜吗？"


    show xm clothes2_front3_no smile at center with dissolve

    xm_ "啊！林先生，您回来了！"


    xm_ smile_close "请再稍等一下，蛋炒饭马上就好了……" with dissolve

    lxc_ "这么晚还在做饭？"


    show xm smile with dissolve
    xm_ "因为您说今天会加班到很晚嘛……我担心您饿着。"
    xm_ "就想试试把冰箱里的剩饭做成蛋炒饭。"


    show xm astonished at emphasis_pop
    xm_ "嗯？这个味道是……"

    "她注意到了我手上提着的纸袋。"

    lxc_ "路过那家你喜欢的甜品店时买的。正好今天发工资，就给你带了块草莓奶油蛋糕。"


    show xm oo at shocked_step_back
    xm_ "真的吗？！是上次我们看到的新品吗？"

    lxc_ "是啊。不过……"

    "我指了指灶台。"

    lxc_ "你的饭好像要糊了。"


    show xm cry skin_cry at shy_shrink
    xm_ "哇！我的黄金蛋炒饭！"


    show xm sigh skin_blush at disappointed_droop
    xm_ "都怪林先生突然拿出甜品，让我分心了……"

    lxc_ "看起来还好，只是有一点点焦。"


    show xm bewilderment with dissolve
    xm_ "本来想做得完美一点的……"

    lxc_ "能吃就行，没必要要求那么高嘛。"
    lxc_ "忙了一天我也饿了，先吃宵夜吧。"


    show xm smile at bounce_small
    xm_ "嗯！我帮您拿筷子！"


    show xm focus at lean_in
    xm_ "您尝尝看味道怎么样？"

    "我吃了一口。米饭炒得粒粒分明，鸡蛋也很嫩滑。"

    lxc_ "好吃，火候掌握得正好。"


    show xm laugh_open at celebrate_jump
    xm_ "真的吗？太好了！"


    xm_ smile_close "其实我练习了好几次呢，之前不是太咸就是炒得太老……" with dissolve

    lxc_ "现在的水平已经很好了。"
    lxc_ "来，一起吃吧。"

    "我把蛋糕以及勺子推到她面前。"


    show xm cat_mouth at bounce_small
    xm_ "好！嗯——！好好吃！"

    lxc_ "慢点吃，没人跟你抢。"

    "看到她嘴角沾到了奶油，我递了张纸巾过去。"

    lxc_ "看，都吃到脸上了。"


    show xm smile_close with dissolve
    xm_ "因为真的很好吃嘛……"


    xm_ smile "林先生也尝尝？" with dissolve

    "她挖了一勺，递到我面前。"

    lxc_ "嗯，甜而不腻，确实不错……"


    show xm shy skin_shy at shy_shrink

    lxcxm_ "啊。"

    "我们两人不约而同地喊了出声。"
    "刚刚一不留神，很自然地用了她递过来的勺子。"
    "星弥​​的脸一下子红了，耳朵尖也染上淡淡的粉色。"


    lxc_ "抱歉，我该用自己的勺子的。"


    show xm bewilderment skin_blush with dissolve
    xm_ "没、没关系的，毕竟是我主动递给您的嘛……"


    show xm shy skin_shy at shy_shrink
    xm_ "而且，作为比你年长的大姐姐，间、间接接吻什么的，我完全不在意哦……！"

    "不管怎么看都很在意吧……"

    lxc_ "……总之，下次我们都注意点就好。"


    show xm shy at nod_small
    xm_ "嗯……"

    "就这样，在有点微妙的气氛中，我们结束了这顿宵夜。"

    jump after_menu_2

label choice_6_c_he_ta_men_qu_you_le_yuan:
    call AutoAfterChoicesCheckReset () from _call_AutoAfterChoicesCheckReset_5


    scene bg_amusement_park_1 at bg_pan_right with Fade(0.5, 0.5, 0.5)

    "午后的阳光透过树叶的缝隙，在我们身上投下斑驳的光点。"
    "我们三个人并排坐在树荫下的长椅上，慢慢地喝着刚买的饮料。"


    show sy clothes2_front1 laugh_open at left with dissolve
    sy_ "那个叫『 疯狂旋风 』的大转盘！下次我还要玩！虽然转得头晕，但那种快要飞起来的感觉……真的很刺激！"

    "时语轻轻踢着腿，银发随着动作微微晃动。"


    show xm clothes2_front2_no smile_close at right with dissolve
    xm_ "我还是更喜欢旋转咖啡杯，大家一起坐在上面，慢慢地转，会有种莫名的安心感。"

    "星弥仔细地吸着饮料里的小果粒，还在回味着刚刚游玩的感觉。"

    lxc_ "我、我选择再休息一下，好累……"

    "我整个人瘫在长椅上，贪婪地享受着这来之不易的喘息机会。"


    show sy despise at look_away_small
    sy_ "什么嘛，明明才玩了五六个设施，人类你还真是不行啊。"

    "「 老了，哪有你们年轻人这么好体力 」——刚想这么说，转念一想，好像我才是年轻人……"

    lxc_ "我只是个普通小朋友，没您这位大姐姐这么能折腾。"


    show sy black skin_black with dissolve
    sy_ "……你是不是在暗搓搓说我年纪大？"

    lxc_ "哪敢。"


    show sy smile skin_blush with dissolve
    show xm bewilderment with dissolve
    xm_ "林先生……是不习惯玩这类设施吗？"

    lxc_ "只要是出门的活动，大部分我都不习惯。"

    "时语这丫头，平时一副资深宅女样，一出门玩倒是活跃得不行，拉着我连玩好几个项目都不带停的……"

    lxc_ "倒是星弥你，玩海盗船之前还挺害怕的，下来后怎么跟没事人一样？"


    show xm smile with dissolve
    xm_ "玩之前确实有点怕，但上去之后感觉还好啦。"


    show xm cry at shy_shrink
    xm_ "至少没升降机那么恐怖……呜，那种一下子掉下去的感觉，实在太可怕了。"

    lxc_ "那个是真顶不住，我坐上去也手心冒汗。"


    show sy cat_mouth at bounce_small
    sy_ "本小姐倒是觉得还不够刺激，还有没有更吓人的设施啊？"

    lxc_ "就算有，恐怕也得你自己去玩了。"


    show sy pout at disappointed_droop
    sy_ "欸~那多没意思，要大家一起玩才热闹嘛！"

    lxc_ "我看你是想看我俩被吓得大叫的样子吧。"


    show sy cat_mouth with dissolve
    sy_ "哎呀，这都被你发现啦？"

    lxc_ "你那点小心思哪里藏得住……不过要找一个大家都喜欢的项目还真不容易。"
    lxc_ "你看，你爱刺激，星弥喜欢安稳，喜好差得还挺远。"


    show sy shy at shy_shrink
    sy_ "其实……也没差那么多啦。"

    "时语瞄了我和星弥一眼，不知道在想什么。"


    show xm smile_close with dissolve

    "星弥似乎听懂了她话里的意思，抿嘴轻轻笑了笑。"


    show xm smile at bounce_small
    xm_ "我也觉得！只要是林先生带我们去的地方，我们都会喜欢的！"

    lxc_ "你这么说……我突然压力好大啊。"


    show xm bewilderment at shy_shrink
    xm_ "我、我不是那个意思！我是想说，只要和大家在一起，去哪都好玩！"



    xm_ "而且，您还没说您自己喜欢玩什么呢？"


    show xm focus at lean_in
    xm_ "是您带我们来的，下一个项目该选您喜欢的才对！"

    lxc_ "我喜欢的啊……那就选那个吧。"

    "我指了指游乐园里最显眼的地标。"


    show sy focus with dissolve
    sy_ "那个大轮子……是摩天轮吧？"


    show xm clothes2_front3_no astonished at emphasis_pop
    xm_ "摩天轮！听说升到最高处时，能看到整个游乐园的风景呢！"

    lxc_ "对。既不会太刺激，升到高空时又有点恰到好处的紧张感，应该挺适合我们一起坐的。"


    show xm bewilderment with dissolve
    xm_ "但，这只是适合我和时语吧？"
    xm_ "……林先生您自己，喜欢摩天轮吗？"

    lxc_ "我？哼哼，能坐着不动就能游玩的项目，我怎么会不喜欢？"


    show xm smile_close at bounce_small
    xm_ "这样啊……嗯，您喜欢就好！"


    show sy despise at look_away_small
    sy_ "果然，你就是想趁机偷懒吧……"

    lxc_ "看破别说破嘛。"
    lxc_ "时间也差不多了，走吧，我们一起去排队。"

    scene bg_sky_1
    with fade

    pause 0.5

    scene bg_sky_5
    with dissolve

    "其实，我也是第一次来游乐园，玩什么都觉得新鲜。"
    "所以，只要是能一起玩的项目，我都会喜欢的。"


    hide sy
    hide xm
    with dissolve

    play music bgm_20 fadeout 1.0 fadein 1.0
    scene cg5
    with Fade(0.5, 0.5, 0.5)

    "我们三个人挤在一个小小的、透明的轿厢里。摩天轮缓缓上升，脚下的景物逐渐变小。"
    "游乐园的喧闹声也渐渐远去，轿厢里变得异常安静，只能听到机器运转的轻微嗡鸣。"


    show xm clothes2_front3_no laugh_open:
        yalign -3.0
    xm_ "哇……真的好高！下面的房子和人都变得像小积木一样！"


    show cg52 with dis_master
    show sy clothes2_front1 calm:
        yalign -3.0
    sy_ "不过是比平时飞得高一点而已，但……给人的感觉还真不一样。"

    "夕阳的余晖将天空染成了温暖的橘红色，云朵的边缘像是被点燃了一样。"
    "整个游乐园的轮廓在脚下铺展开来，远处的城市也笼罩在一片宁静的暮色之中。"


    show cg51 with dis_master
    show sy smile_close with dissolve
    sy_ "好美的风景……"

    lxc_ "从这个角度看，感觉整个世界都变得不一样了。"


    show cg53 with dis_master
    show xm calm with dissolve
    xm_ "嗯，感觉……好安静，好和平。好像所有的烦恼都变得微不足道了。"

    "她眺望着远方，心绪似乎也飘散在了云层之中。"


    show cg54 with dis_master
    show sy sigh with dissolve
    sy_ "是啊……这种感觉，在古堡里可体验不到。"
    sy_ "那里虽然能看见整片星空，但总觉得……有点冷清了。"

    "她静静看着窗外，侧脸在夕阳下显得格外柔和。"
    "我能感觉到，此刻她们都放下了平时的心防，流露出最真实的样子。"


    show cg55 with dis_master
    show xm smile_close with dissolve
    xm_ "能和林先生、时语一起看这么美的景色……就像在做梦一样。"


    show cg56 with dis_master
    sy_ smile "嗯……我也这么觉得。" with dissolve

    lxc_ "看到你们这么开心，这趟游乐园就算没白来了。"

    "轿厢里陷入一阵沉默，却并不尴尬，反而充满一种舒适的温暖。"
    "我们就这样静静坐着，享受这份难得的宁静。"
    "直到摩天轮缓缓接近最高点。"


    show sy smile
    sy_ "要是……时间能停在这一刻就好了。"


    hide cg5
    show cg5 with dis_master
    xm_ laugh_open "嗯！真希望这个摩天轮，能一直、一直转下去……" with dissolve

    "我看着她们俩被夕阳勾勒出的侧影，心里也涌起同样的感慨。"

    lxc_ "是啊……"

    "要是这样的时光能永远持续下去，该有多好。"
    "落日的余晖将我们的影子拉长，交融在一起，仿佛在预示着什么。"
    "摩天轮缓缓驶向最高点，将这个美好的瞬间，定格在了暮色之中。"

    jump after_menu_2

label after_menu_2:


    play music bgm_9 fadeout 1.0 fadein 1.0
    scene bg_living_room_1 with Fade(0.5, 0.5, 0.5)

    "周末的午后，客厅里总是会洋溢着悠闲而惬意的氛围。"

    scene cg420 with dissolve



    "时语整个人陷在柔软的沙发里，手指在手柄上飞快地操作着。"

    scene bg_living_room_1 with dissolve


    show xm clothes2_front2_no cat_mouth at center with dissolve

    "星弥则躺在沙发上，小腿轻轻晃着，每舀起一勺冰淇凌，脸上都会露出满足的表情。"

    "「 滴滴 」，手机的记账软件不合时宜地弹出一条月度提醒。"
    "我盯着上面的信息，眉头不自觉地皱了起来。"

    lxc_ "那个……星弥啊。"


    show xm smile with dissolve
    xm_ "嗯？林先生，怎么了？"

    "星弥舔了舔勺子上的冰淇凌，随后抬头看向我。"

    lxc_ "你还记得这是这个月吃的第几个冰淇淋了吗？"


    show xm bewilderment with dissolve
    xm_ "第十……不，应该是第二十个？具体我也记不清啦~"


    show xm cat_mouth at bounce_small
    xm_ "嘻嘻，人类的甜品真的很好吃呢！"

    lxc_ "呃……"

    "看来得换个角度切入……"

    scene cg420 with dissolve

    lxc_ "时语。"

    show cg421 with dis_master

    show sy pout:
        yalign -3.0
    sy_ "干嘛？我正打到最关键的地方呢！"

    lxc_ "这个月你通关了多少个单机游戏？"


    show cg422 with dis_master
    show sy despise
    sy_ "平均一周一到两个吧，怎么突然问这个……"


    show cg423 with dis_master
    sy_ astonished "啊，我懂了！" with dissolve
    "难道说，理解我的人居然是时语吗……！"


    show cg424 with dis_master
    show sy cachinnation at celebrate_jump
    sy_ "你是想称赞本小姐高超的游戏水平吗？哼哼，不用害羞，尽管膜拜我吧！"

    lxc_ "啊，可恶……！"

    "会对你有所期待的我真是笨蛋！！！"

    scene bg_living_room_1 with dissolve
    show sy clothes2_front1 despise at left with dissolve
    show xm clothes2_front2_no smile at right with dissolve

    sy_ "说实话，我一直觉得你对本小姐的态度太随意了。"
    sy_ "哪怕你是这里的主人，也该对我怀有一点敬畏之心才对！"


    show sy bewilderment at emphasis_pop
    sy_ "……欸，人类，你手上拿着的是什么？"

    "我拿出鸡毛掸子——然后拔下一根毛。"


    show sy oo at shocked_step_back
    sy_ "喂、喂！你要做什么？！不要过来——！"


    show sy cachinnation at glare_shake
    with vpunch
    sy_ "噫~那里不行！我还在打游戏呢……呀！好痒啊！哈哈！"

    "在我的攻势下，时语眼角笑出了泪花。"


    show xm shy skin_shy at shy_shrink

    "一旁观战的星弥早已面红耳赤，神情甚至带着一丝期待。"
    "事先声明，我真的只是在用鸡毛给她挠痒痒而已。"

    lxc_ "好了，该干正事了。"


    show xm skin_blush bewilderment with dissolve
    xm_ "我明白您有事要找我们商量了……但具体是要聊什么呢？"


    show sy sigh skin_blush with dissolve

    "星弥一边安抚笑瘫的时语，一边轻声问。"

    lxc_ "现在有一个比较严峻的问题。"
    lxc_ "这个月的日常支出，已经快要超过我的工资了。"

    "我把手机上的账单递给她们看，两人凑过来，表情逐渐凝重。"


    show xm cry at shy_shrink
    xm_ "对、对不起，林先生……我没想到会花这么多……"


    show sy calm at nod_small
    sy_ "……毕竟你是普通人类，要养两个人确实有点勉强了呢。"

    "一向高傲的时语也意识到问题的严重性，抱起手臂，抿了抿嘴。"


    "之前一个人生活惯了，多了两个人后不知不觉就超了预算。"
    "距离约定的日子还有一段时间，既然如此，得注意一下才行。"

    lxc_ "再加上新买的电饭煲……存款也快要动用了。"


    show sy bewilderment with dissolve
    sy_ "但存款存起来，不就是为了用吗？"


    show xm clothes2_side1 calm with dissolve
    xm_ "唔……存款更多是为了应对未来的不时之需呀。"
    xm_ "如果每个月都透支，存款就会越来越少了……林先生也是这么想的吧？"

    lxc_ "嗯，星弥说得对。"


    show sy calm at nod_small
    sy_ "……也对，布莱菲特家的财富也不是一朝一夕就出现的。"

    lxc_ "所以，为了长远考虑，我们得想办法『 开源节流 』。"
    lxc_ "首先是『 节流 』……日常娱乐的花销得控制一下。"


    show sy bewilderment with dissolve
    sy_ "比如？"

    lxc_ "比如给你买游戏，从一周一个新作，改成两周……不，三周一个。"


    show sy pout at angry_stomp
    sy_ "欸——没新游戏玩好无聊的！"

    lxc_ "趁这机会培养点新爱好？比如插花、茶艺什么的，真正的大小姐爱好。"


    show sy despise at glare_shake
    sy_ "我才不要！我离家出走就是因为厌倦那些事了！"

    lxc_ "也是。"


    show xm bewilderment at shy_shrink
    xm_ "那、那我呢？林先生……"

    lxc_ "你嘛……或许用事实告诉你更直观。"

    "我双手搭在了星弥的肩膀上。"

    lxc_ "虽然这可能有点残酷。"


    show xm oo kp2wl at shocked_step_back
    xm_ "欸？这、这是怎么了？"

    lxc_ "你……准备好接受真相了吗？"


    show xm bewilderment hide_fx with dissolve
    xm_ "？？？"

    lxc_ "星弥，你来我家之后……有称过体重吗？"


    show xm oo with dissolve
    xm_ "……欸？"

    "我把体重秤放到了星弥面前。"

    scene sd4
    with fade

    "她小心翼翼地踩上去，显示屏上的数字跳动几下，最后停在了一个让她眼睛瞬间睁大的数值。"


    show xm cry skin_cry:
        ypos 5000
    with vpunch
    xm_ "欸欸欸——！不可能！您的体重秤一定是坏掉了！！！"


    xm_ cry skin_cry "我以前在里世界的时候根本不是这样的！" with dissolve


    sy_ cat_mouth "呜哇，人类你真坏啊。" with dissolve

    lxc_ "我说了会有点残酷嘛。"

    sy_ "不过，放着星弥不管真的好吗？再这样下去体重秤也要变得和你一样『 坏 』了哦？" with dissolve

    lxc_ "……！手下留情！体重秤真的没坏啊！"

    scene bg_living_room_1 with dissolve
    show sy clothes2_front1 sigh at left with dissolve
    show xm clothes2_front2_no sigh at right with dissolve

    lxc_ "总之，现在你们明白情况的严重性了吧？"


    show sy sigh with dissolve
    sy_ "嗯……"


    show xm sigh skin_blush at disappointed_droop
    xm_ "我知道了……"

    lxc_ "不过，也不是非得要这么做——除了节流，我们还可以『 开源 』。"


    show xm bewilderment with dissolve
    xm_ "开源？"

    lxc_ "就是赚钱。我在想，星弥你的魔法那么厉害，能不能……用一些低调的方式帮我们赚点外快？比如……"


    show sy focus at emphasis_pop
    sy_ "不行。"

    "时语的表情罕见地严肃起来。"

    lxc_ "为什么？"

    sy_ "因为这违反了《大隐匿协议》。"

    lxc_ "那是什么？"


    show xm calm with dissolve
    xm_ "就是……里世界的居民不能随意在表世界使用超自然力量干涉社会运转，尤其是不能用于牟利，否则会被仲裁会追责的……"

    lxc_ "这还真是第一次听你们说……等等。那星弥用魔法保存冰淇凌之类的……不算违反协议吗？"


    show sy calm with dissolve
    sy_ "那属于『 非主动干预社会 』的私人生活范畴，在灰色地带。"
    sy_ "协议的核心是『 隐匿 』。只要不引起普通社会的大规模注意，仲裁会通常睁一只眼闭一只眼。"
    sy_ "但直接用魔法赚钱，是明确禁止的红线。"

    lxc_ "这规矩比公司的报销制度还复杂……"
    lxc_ "那你们留在我这里，也不违反『 隐匿 』原则吗？"


    show sy calm with dissolve
    sy_ "这个世界上，有不能做却可以做的事，也有能做却不该做的事。"
    sy_ "我们留在这里，属于前者；而用魔法赚钱，属于后者。"

    lxc_ "好吧，我明白了。就像人类社会中，有些事是『 擦边球 』，有些是『 底线 』。"
    lxc_ "不过，这样的话就只能继续节约开支了，真遗憾。"


    show xm smile at emphasis_pop
    xm_ "唔……其实我有一个提议。"


    show sy smile at emphasis_pop
    sy_ "本小姐有一个想法！"


    xm_ bewilderment "欸，时语你……" with dissolve


    sy_ smile "嗯，看来我们想到一块去了。" with dissolve

    "两人异口同声，随后轻声笑了笑。"


    show xm smile at bounce_small
    xm_ "只要我们也出去工作不就好了吗？"


    show sy cachinnation at celebrate_jump
    sy_ "没错！本小姐可不是什么好吃懒做的人！"
    sy_ "哪怕不靠魔法，自力更生的方法也多的是！"

    lxc_ "不，你们是笨蛋吗？"


    show sy oo kp32wl at shocked_step_back
    sy_ "……什喵？！"

    "或许是太过激动，她说话都咬到舌头。"


    show xm bewilderment with dissolve
    xm_ "林先生，这是什么意思？"

    lxc_ "该从哪里开始说明好呢……我先问个问题吧：你们是怎么来到这个世界的？"


    show sy shy hide_fx at shy_shrink
    sy_ "呃，偷偷穿过传送门……"


    show xm shy at shy_shrink
    xm_ "传送魔法失误……"

    lxc_ "这意味着，你们没有表世界的合法身份。"
    lxc_ "在这边，没有身份证明可没法工作哦？"


    show xm sigh at disappointed_droop
    xm_ "怎么这样……"

    lxc_ "而且，别人看到你们的外表，恐怕都会避而远之。"
    lxc_ "雇用童工在人类世界可是大忌。"



    show sy pout at angry_stomp
    sy_ "哈？本小姐可是三百多岁的血族！怎么能凭外表判断——"

    lxc_ "你是要违反《大隐匿协议》，告诉别人你是血族吗？"


    show sy bewilderment with dissolve
    sy_ "我……"

    "她一时语塞，嘴唇张了又合，却找不到反驳的话。"


    show sy pout at look_away_small

    "最后气鼓鼓地「 哼 」了一声，一把抓过抱枕侧躺在沙发上，只留下一个银发乱糟糟的后脑勺。"

    sy_ "……烦死了，这种麻烦的规矩……"


    xm_ bewilderment "那我们岂不是帮不上忙了？" with dissolve

    lxc_ "没有啊？"
    lxc_ "星弥你帮忙做饭，时语陪我打游戏，大家一起聊天、出门……我觉得这些都已经帮了我很多。"


    show xm sigh with dissolve
    xm_ "但和您的付出相比，我们做的太微不足道了……"

    lxc_ "价值观不同吧。对我来说，这些都是很有意义的事。"
    lxc_ "总之，赚钱的事不急，省着点用，总会有办法的。"


    show xm calm at nod_small
    xm_ "嗯……"


    sy_ calm "……我去丢垃圾。" with dissolve

    "眼看话题结束，时语起身提着垃圾袋就往门外走，就连奇怪的口癖都不说了。"

    "星弥看了我一眼后，点点头，也跟了过去。"


    show xm bewilderment with dissolve
    xm_ "我、我也去帮忙！"


    hide sy
    hide xm
    with dissolve

    scene bg_living_room_1
    with Fade(0.5,0.5,0.5)

    lxc_ "嗯……"

    "我是不是把话说得太重了？"
    "十分钟过去了，她们还是没有回来。"
    "该不会是两人都离家出走了吧？"
    "难道我说话的语气真的很重？"
    "但她们离家出走后又能去哪儿呢？"
    "……算了，与其在这里胡思乱想，不如直接出去找她们。"


    scene bg_community_1 with dissolve

    "走出门，看见她们俩站在一楼，神情有些紧张，似乎在和谁说话。"
    "没乱跑就好……不过，她们是在和谁聊天？"


    scene black with Fade(0.3, 0.3, 0.3)

    $ heroine = True
    $ heroine_name = "星弥的视角"

    play music bgm_2 fadeout 1.0 fadein 1.0
    scene bg_community_1 with Fade(0.3, 0.3, 0.3)

    "「 十分钟前。 」"


    show xm clothes2_front2_no smile at right with dissolve
    xm_ "时语，你一个人提垃圾袋很重吧？我来帮你！"


    show sy clothes2_front1 sigh at left with dissolve
    sy_ "嗯，谢谢……"


    show xm
    xm_ bewilderment "你……是不是在生气呀？" with dissolve


    show sy sigh at disappointed_droop
    sy_ "……没有啦。只是有点郁闷，感觉自己什么都帮不上。"
    sy_ "我不像星弥，又会做饭，又体贴人……"


    show xm shy at deny_shake_small
    xm_ "啊……其实我也没有你说的那么好啦。"
    xm_ "我也只是习惯了这么做而已，哈哈……"


    show xm astonished at emphasis_pop
    xm_ "——啊，不行！要是连我都变得低落的话，林先生会更担心的！"

    "我深呼吸了一下，努力振作起来。"


    show xm
    xm_ smile "其实我觉得，你已经帮了林先生很多哦！" with dissolve


    show sy
    sy_ bewilderment "……真的吗？" with dissolve


    show xm smile_close kp4wl at bounce_small
    xm_ "嗯！林先生和你打游戏的时候，笑得特别开心！"
    xm_ "而且你没发现吗？他和你相处时特别放松，还会互相斗嘴~"


    show sy
    sy_ calm "……这倒是。他对我好像越来越随意了，明明我是高贵的血族……" with dissolve
    show sy bewilderment with dissolve
    sy_ "我还以为他是故意气我的。"


    show xm
    xm_ smile hide_fx "与其说是故意，不如说是下意识吧。" with dissolve
    xm_ "因为我和林先生有点像，所以我能懂——他那么放松，是因为信任你呀！"
    xm_ "他把你当成了真正的朋友，甚至可以说是……『 损友 』哦！"


    show sy
    sy_ shy "……是这样吗？" with dissolve


    show xm smile at nod_small
    xm_ "是的！请相信一直看着你们的我！"


    show sy
    sy_ shy "好吧……谢谢你，星弥。" with dissolve


    show xm cat_mouth at bounce_small
    xm_ "不客气，毕竟我们是一起住在林先生家的同伴嘛！"


    show sy smile_close at nod_small
    sy_ "嗯……！"


    xm_ smile "垃圾丢完啦，我们回去吧！" with dissolve


    sy_ smile "好！" with dissolve

    scene bg_community_1
    with Fade(0.3, 0.3, 0.3)


    show bg_community_1:
        zoom 1.08
        xalign 0.15
        yalign 1.0
    with dissolve
    fd_ "啊呀，你们是……？"


    show sy astonished at left with dissolve
    sy_ "……您好。"


    show xm clothes2_front3_no smile at right, nod_small with dissolve
    xm_ "您是……房东奶奶，对吗？"

    fd_ "是的，没想到我们公寓里住了这么可爱的小朋友……你们是谁家的孩子呀？"


    show sy pout at angry_stomp
    sy_ "本小姐才不是小……唔！星弥你别捂我的嘴……！"


    show xm bewilderment at shy_shrink
    xm_ "啊哈哈，我、我们是林小凑家的……那个……"

    fd_ "是小林啊？没想到他也会带客人回来呢。"


    show xm focus with dissolve
    xm_ "欸，这是什么意思呀？"

    fd_ "他一直都是独来独往的哦。"
    fd_ "虽然是个有礼貌、很善良的好孩子……"
    fd_ "但总让人觉得有些孤单呢。"


    show sy focus with dissolve
    sy_ "……他一直都这样吗？"

    fd_ "从住在这里开始就是这样。"


    show sy sigh at disappointed_droop
    sy_ "……"

    fd_ "不过看到你们，我就放心多了。"
    fd_ "至少说明他也有自己的社交圈子。"


    show sy calm at nod_small
    sy_ "嗯……"


    show xm smile at excited_lean_forward
    xm_ "虽然平时看不出来，但林先生其实是个很温柔的人哦！"
    xm_ "所以您不用太担心的！"
    show xm smile at excited_lean_forward_undo

    fd_ "呵呵，是我多虑就好。"
    fd_ "话说回来，你们是小林的……？"


    show xm bewilderment at shy_shrink
    xm_ "呃，我、我们是他的——"

    scene bg_community_1
    with fade
    $ heroine = False

    lxc_ "——她们是乡下来的远房表妹。"
    lxc_ "左边是时语，右边是星弥。没给您添麻烦吧？"

    fd_ "没有没有，只是好奇这么可爱的孩子是谁家的呢。"


    show sy bewilderment at left, lean_in
    sy_ "（喂，你什么时候出来的？）"

    "时语凑到我耳边轻声说。"

    lxc_ "（刚刚看你们一直没回来，有点担心。）"


    show sy shy skin_blush with dissolve
    sy_ "（哦……）"

    fd_ "哎呀，没想到孩子们都和你这么亲近呢。"
    fd_ "一般来说这年纪的孩子都想独立一点的。"

    lxc_ "还、还好吧……"

    "时语姑且不论，星弥的话……"
    lxc_ "（你什么时候躲到我身后的？！）"


    show xm clothes2_side1 smile at right, shy_shrink
    xm_ "（不是林先生您把我们护在身后的吗？嘻嘻~）"

    lxc_ "（……行吧。）"


    show sy pout skin_blush kp8wl at deny_shake_small
    sy_ "我、我才没有和他很亲近呢！"

    fd_ "呵呵，这孩子真有意思。"

    lxc_ "她们刚从国外回来，人生地不熟，粘人了点……"

    fd_ "国外？可你刚才不是说从乡下……"

    lxc_ "啊、是国外乡下的远亲！哈哈……"

    fd_ "这样啊。"


    show sy bewilderment hide_fx at lean_in
    sy_ "（喂，为什么说我们是国外来的啊？）"

    lxc_ "（不然你这银头发怎么解释？说染的吗？）"


    show sy black with dissolve
    sy_ "（……好吧。）"

    fd_ "对了，最近晚上你房间常传出热闹的声音是……？"

    lxc_ "是我和时语打游戏时的声音……"

    fd_ "那前段时间突然断电是……？"

    lxc_ "星弥学做饭时不小心碰到电源了……"

    fd_ "还有，你房间偶尔会闪奇怪的光……"

    lxc_ "呃，这个是……"

    lxc_ "（喂，你们趁我不在时到底做了什么啊！）"


    show xm cry at shy_shrink
    xm_ "（对、对不起……可能是我试验传送魔法时不小心发光了……）"

    lxc_ "（别拿我家当实验室啊！）"

    fd_ "你流了好多汗呢，没事吧？"

    lxc_ "没、没事！毕竟太阳有点大嘛……"

    fd_ "可今天是多云哦？"

    lxc_ "就是那个……紫外线！紫外线挺强的！"

    fd_ "唔……"

    "房东眯起了眼睛，表情变得严肃。"

    fd_ "说起来，她们长得和你一点也不像呢。"
    fd_ "该不会……其实不是你的表妹吧？"


    show sy oo at shocked_step_back
    show xm oo at shocked_step_back

    lxc_ "……！"

    fd_ "难道你在做什么不该做的事？"

    lxc_ "我……"

    "就算我问心无愧，但收留无家可归的少女本身就不寻常，别人会怀疑也很正常……该怎么解释才好？"
    "正当我绞尽脑汁时——两位少女却抢先开口了。"


    show xm focus at excited_lean_forward
    xm_ "不是的！林先生没有做错任何事！"
    show xm focus at excited_lean_forward_undo


    show sy focus at angry_stomp
    sy_ "是啊！他只是帮助了我们而已！不是坏人！"

    "两人不约而同地挡在我前面，急切地向房东解释。"

    lxc_ "你们……"


    show sy calm at excited_lean_forward
    sy_ "真要追究的话，错的是我们才对！"
    show sy calm at excited_lean_forward_undo


    show xm cry at shy_shrink
    xm_ "嗯！所以请您不要责怪他……"

    fd_ "哎呀呀……我本来只是想问清楚情况，现在倒显得我像恶人了。"
    fd_ "好吧，既然你们都这么说了，我就不多问啦。"
    fd_ "你会处理好这一切的，对吧？"

    "房东注视着我，眼神里既有担忧，也包含了信任。"

    lxc_ "嗯，我会的。"

    fd_ "那就好，不打扰你们了，我先回去啦。"

    lxc_ "您慢走。"

    fd_ "哦对了，有件事忘了说——"
    fd_ "其实前段时间根本没有停过电哦？"

    lxc_ "呃……"

    "她看着我愣住的表情，满意地笑了笑，挥挥手，转身回了房间。"
    "姜还是老的辣啊……"


    show sy smile with dissolve
    sy_ "她是个好人呢。"


    xm_ smile_close "是啊，明明早就看出有问题，却还是选择相信我们。" with dissolve

    lxc_ "房东她就是这样的人。"

    lxc_ "我刚出来打工的时候，因为工资被拖欠，甚至还欠过她房租......但她还是让我继续住下了。"
    lxc_ "我现在能用低廉租金住在这么好的公寓，也是多亏了她的照顾。"
    show sy calm with dissolve
    sy_ "所以，这也是你愿意让我们住下的原因？"
    lxc_ "谁知道呢。"

    lxc_ "好了，我们回去吧。"


    show sy smile
    show xm smile at nod_small
    syxm_ "嗯！"

    play music bgm_21 fadeout 1.0 fadein 1.0
    scene bg_living_room_1
    with fade


    show sy shy skin_blush at left, shy_shrink with dissolve
    show xm clothes2_front3_no smile at right with dissolve
    sy_ "……总之，谢谢你了。"

    lxc_ "怎么突然说这个？"


    show sy calm skin_blush with dissolve
    sy_ "没什么，只是觉得……你也挺不容易的。"
    sy_ "而且还一直照顾着我们。"

    lxc_ "从大小姐嘴里听到感谢，还真不习惯啊。"


    show sy pout skin_shy at look_away_small
    sy_ "那你可得早点习惯！因为我……咳，没什么！"

    "她翘起双手，红着脸扭过头。"


    show xm smile_close with dissolve
    xm_ "我也很感谢您，林先生……托您的福，这段日子我非常快乐。"


    show xm sigh at disappointed_droop
    xm_ "但刚才的事让我意识到，我们留在您身边可能会带来危险。"
    xm_ "我珍惜现在的每一天，但不想因此而连累您……"


    show sy bewilderment skin_blush with dissolve
    sy_ "星弥……"


    show xm clothes2_front3 not_good skin_blush with dissolve
    xm_ "所以我想到一个方法——可以用魔法抹去房东和相关人士关于我们的记忆。"
    show xm clothes2_front3 bewilderment skin_blush with dissolve
    xm_ "这样……您就安全了吧？"

    "她脸上带着笑，但握着法杖的手却在微微发抖。"

    lxc_ "谢谢你为我着想……但这样可不行。"

    "我轻轻摸了摸她的头。"
    "我并不习惯这种行为，但总觉得，这个时候就得这么做。"
    lxc_ "无论是和房东的回忆，还是和其他人相遇的经历，都是珍贵的东西。"

    lxc_ "也许在别人眼里微不足道，也许很快会被遗忘……"
    lxc_ "但人与人的联系，正是由这些微小的记忆一点一点编织而成的。"
    lxc_ "就像时语说过的——『 世界上有不能做却可以做的事，也有能做却不该做的事 』。"
    lxc_ "把你们收留在我家，是前者；而消除别人的记忆，是后者。"
    lxc_ "所以，我们不能这样做。"


    show xm smile_close clothes2_front3_no at nod_small
    xm_ "……嗯，我明白了。"

    "星弥放下了法杖，她或许本就不想这么做，只是那份想保护我的心意，一时压过了理智。"


    show sy shy skin_blush with dissolve
    sy_ "我说过的话你还真是记得清楚呢……"

    lxc_ "大小姐说过的话我可都好好记着呢。"


    show sy shy skin_blush at look_away_small

    show sy shy skin_blush with dissolve
    lxc_ "总之，我的事你们不用太担心。"
    lxc_ "至少在这段时间里，都不会出问题的。"
    lxc_ "好了，严肃的话题就到此为止。"
    lxc_ "我突然好饿，好想吃热乎乎的饭菜啊。"
    lxc_ "可以拜托你吗，星弥？"


    show xm laugh_open at celebrate_jump
    xm_ "……嗯！这次我会尽全力做出最好吃的饭菜！"

    lxc_ "也不用这么卖力，平常的就好。"


    show xm smile at bounce_small
    xm_ "好！我这就去做饭！"


    show sy cat_mouth at bounce_small
    sy_ "既然如此，在饭做好之前，你来陪我打游戏吧！"

    lxc_ "好啊。"


    show sy laugh_open at excited_lean_forward
    sy_ "我和你说，上次我打到了一个超~厉害的装备！"
    show sy laugh_open at excited_lean_forward_undo

    scene bg_sky_5 at bg_pan_right
    with Dissolve(1.0)

    "时语兴奋地拉着我的手朝电脑走去，银发在灯光下轻轻晃动，仿佛将刚才的忧虑一扫而空。"
    "而星弥已经系上围裙，重新挂起笑脸走进了厨房。"
    "暮色渐沉，屋内的灯光却格外温暖——我们又回到了属于自己的日常中。"

    $ choice_sum = first_choice + second_choice

    jump story_826_part1
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
