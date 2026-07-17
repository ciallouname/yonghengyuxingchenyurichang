


label after_menu_3:

    call achievement (7) from _call_achievement_8



    play music bgm_14 fadein 1.0
    scene bg_office_1
    with Fade(0.5, 0.5, 0.5)
    show bg_office_1:
        zoom 1.04
        xalign 0.55
        yalign 1.0
    $ heroine = False

    with dissolve

    "第二天回到公司，我预想中的情况并没有发生。"
    "没有因为左脚先进公司而被开除，也没有被人事主管叫去谈话，只有测试组照常发来的BUG报告。"
    "所以昨天的事就这么过去了？亏我还一直担心会被穿小鞋。"
    "不过在职场上，平安无事就是最好的消息了。"


    play music bgm_2 fadeout 1.0 fadein 1.0
    scene bg_living_room_2
    with fade

    "多亏昨晚的谈心，今天心情轻松了不少，回到家时也没那么疲惫了。"
    "推开家门，厨房飘来一阵陌生的焦香，让我愣了一下。"

    scene bg_kitchen_2
    with fade

    show sy clothes2_front1 smile at center with dissolve

    sy_ "你回来了。"
    lxc_ "嗯，回来了。没想到今天是你下厨。"
    show sy smile_close at nod_small
    sy_ "之前不是说好了要学做饭嘛。"
    lxc_ "也对。说起来，星弥呢？怎么没见到她？"
    show sy clothes2_front1 bewilderment kp29wl with dissolve
    sy_ "星弥她……"
    "时语突然变得支支吾吾。"
    lxc_ "怎么了？"
    show sy sigh hide_fx at look_away_small
    sy_ "……她今天早上回里世界了。"
    lxc_ "啊？这么突然？"
    sy_ "……你还记得我们刚来时，说好的约定吗？"
    lxc_ "之前的约定……啊。"
    "我想起来了。"
    lxc_ "原来已经三个月了……"
    sy_ "嗯，她想遵守约定，不想再给你添麻烦。"
    lxc_ "……"
    "我环顾四周，客厅比平时整洁许多，但沙发角落却堆着几个空甜点盒——是星弥最爱吃的那种。"
    "看着那些被拆开过的包装盒，心里有点空落落的。"
    "三个月来，已经习惯了推开门就能听到两个女孩吵吵闹闹的声音，现在只剩下时语一个人，竟然有些不习惯。"
    show sy clothes2_front1 sigh with dissolve
    sy_ "还有……这个给你。"
    "时语从怀里取出一封带有魔女帽标志的信件。"
    lxc_ "这是……？"
    show sy bewilderment with dissolve
    sy_ "星弥托我交给你的信。"
    "我取出信件，上面是工整中带着点可爱的、属于星弥的字迹。"

    hide sy with dissolve

    xm_ clothes1_front3_no "给林小凑先生："
    xm_ "林先生，当您看到这封信时，我已经回到里世界了。"
    xm_ "如果正式向您道别，我怕自己会忍不住哭出来，所以请允许我用这样的方式告别。"
    xm_ "在您家住的这三个月，给您添了很多麻烦，真的很抱歉>_<"
    xm_ "我很庆幸自己在表世界初次遇到的人是您和时语，也因为你们经历了许多开心和有趣的事，真的很感谢！"
    xm_ "现在我要回去竞选魔女茶话会的管理者了，不用担心，我会努力的！等有空了我会寄谢礼过来的！"
    xm_ "所以，您和时语也要好好地一起生活！"
    xm_ "——星弥"

    show sy clothes2_front1 bewilderment with dissolve

    "这样啊……"
    "虽然难免会寂寞，但既然是星弥自己做出的决定，我会支持她的。"
    "我轻轻折好信纸，抬头正对上时语担忧的目光。"
    show sy bewilderment with dissolve
    sy_ "……你还好吧？"
    lxc_ "没事，只是觉得有点突然而已。"
    "我收起有些失落的表情，对她笑了笑。"
    lxc_ "没想到家里之前住着这么厉害的一位魔女，都能去竞选管理者了。"
    lxc_ "好了，得打起精神来才行，星弥肯定也不想看到我们这么低落的样子。"
    lxc_ "有点饿了，让我尝尝你做的番茄炒蛋吧。"

    show sy focus kp1wl at emphasis_pop
    sy_ "……等等。"
    "刚伸出去的筷子被她轻轻夹住了。"
    lxc_ "怎么了？哦，还没洗手是吧，稍等——"
    show sy clothes2_front1 pout hide_fx at angry_stomp
    sy_ "不是这个！你……没什么要问我的吗？"
    "「 问什么 」——这句话我差点脱口而出。"
    "但看到她微微发抖的肩膀，我立刻明白了她的意思。"
    lxc_ "时语，你在表世界这边租过房子吗？"
    sy_ "……怎么突然问这个？"
    lxc_ "一看你就是没吃过租房的亏啊。"
    "我推了推不存在的眼镜，摆出一副房产中介的样子。"
    lxc_ "哪怕合同上只签了三个月短租，要是到期前没提前通知房东——合同就会自动续满一年。"
    show sy astonished kp1wl at emphasis_pop
    sy_ "你在说什么——"
    lxc_ "所以，现在想取消也来不及了，你至少得在这儿住满一年！"
    lxc_ "怎么样？人类世界的租房合约可是很黑暗的，你现在想逃也逃不掉了！"
    show sy clothes2_front1 bewilderment skin_blush hide_fx with dissolve
    sy_ "你……"
    "她脸上浮现出复杂的表情，欲言又止。"
    "等她再次抬起头时，已经恢复了平日里那副略带高傲的神情。"
    show sy clothes2_side1 cat_mouth with dissolve
    sy_ "您可真会说笑呢，本小姐可不记得签过什么合同啊？"
    lxc_ "……啧，可惜，这都骗不了你。"
    "我收起夸张的姿势，变回平时的样子。"
    show sy clothes2_front1 shy skin_blush at look_away_small
    sy_ "虽然之前没签，但现在可以补嘛……"
    lxc_ "嗯？"
    show sy shy skin_shy at shy_shrink
    sy_ "没、没什么！我乱说的！"
    lxc_ "行吧。反正我的意思是，你想住多久都行，不用在意那个期限。"
    lxc_ "毕竟和你相处的日子……我过得挺开心的。"
    show sy smile skin_blush with dissolve
    sy_ "……嗯，我也是。"
    lxc_ "是吗？那就好。"
    lxc_ "能让大小姐开心，是我的荣幸。"
    show sy clothes2_side1 smile_close skin_blush with dissolve
    sy_ "……哼，不过是个普通人类，可别得意忘形了。"
    "虽然她嘴上嫌弃，却藏不住眼神里的笑意。"
    "能在这三个月里赢得她的信任，感觉还不错。"
    lxc_ "既然事情聊完，那番茄炒蛋我就不客气了。"
    lxc_ "啊……嗯？这味道……"
    show sy clothes2_front1 bewilderment with dissolve
    sy_ "怎么了？我知道自己水平一般，但也不用这么夸张吧？"
    lxc_ "不是不是，你自己尝尝看。"
    "我夹起一块递到她面前。"
    sy_ "让我试试……咦？怎么没味道？"
    lxc_ "因为大小姐你忘记放盐了啊。"
    show sy oo kp1wl at emphasis_pop
    sy_ "啊，好像是忘了……可恶！"
    lxc_ "有人自己做完菜都不试吃一下啊，真是粗心呢。"
    show sy pout kp13wl at angry_stomp
    sy_ "我、我刚做完你就回来了，哪有空试吃嘛！"
    show sy clothes2_front1 focus hide_fx with dissolve
    sy_ "我去厨房拿点酱油！"

    hide sy with dissolve

    "酱油配番茄炒蛋？好吧，也不是不行。"
    "原本还想借机好好称赞她一下的，看来只能等下次了。"
    "虽然也可以为了让她高兴说些违心的话，但我不想那样做。"
    "至少在这个家，在和她相处时，我希望彼此的关系能纯粹一点。"
    "滴滴——"
    "手机弹出新消息。"
    lxc_ "这是什么……啊？"
    sy_ "怎么了？"
    lxc_ "项目群发了个新通知。"
    "我把手机递给她看。"
    show sy clothes2_front1 focus with dissolve
    sy_ "项目检讨会？"
    lxc_ "嗯，之前负责的项目延期了，管理层肯定要找人背锅。"
    if third_choice != 1:
        "我将公司的情况简单告诉了她。"
    show sy clothes2_front1 focus with dissolve
    sy_ "……你很可能是那个头号人选。"
    lxc_ "对，人事主管很可能和程序那边串通好，把锅全甩到我身上。"
    "怪不得今天公司这么平静，原来是在为这件事准备。"
    show sy pout with dissolve
    sy_ "明明是程序的问题，却硬要推到别人头上，这些人还真是……"
    lxc_ "屁股决定脑袋嘛，先有了立场，后面才有规矩。"
    show sy clothes2_side1 sigh with dissolve
    sy_ "也是，血族这边也好不到哪去就是了。"
    sy_ focus "不过……这种事，人类这边可以用决斗来解决吗？" with dissolve
    "时语优雅地叉起一块蘸了酱油的炒蛋，送入口中。"
    lxc_ "……决斗？"
    sy_ "嗯，按照血族的传统，被污蔑时可以要求决斗证明自己的清白。"
    sy_ "赢家获得一切，输家接受惩罚。"
    lxc_ "这规矩在中世纪或许还行得通，但现代社会可不行。"
    lxc_ "打赢了进派出所丢工作，打输了进医院丢工作，结果没区别。"
    show sy clothes2_front1 focus with dissolve
    sy_ "那换个方式，让他们开会那天上不了班怎么样？"
    sy_ "比如在上班路上偷偷打晕，或者——"
    lxc_ "停停停！这种事可是违法的哦？"
    show sy clothes2_front1 oo kp20wl at shocked_step_back
    sy_ "欸，人类的规矩真多呢……"
    "她撅起嘴，泄气地趴在桌上。"
    "是你们血族的规矩太「 自由 」了吧……贵族都这么蛮不讲理吗？"
    lxc_ "不用太烦恼，我一个普通员工，能做的事本来就有限。"
    show sy bewilderment hide_fx with dissolve
    sy_ "但是……我真的很想帮上你的忙啊？"
    "她把下巴搁在手臂上，从桌边抬起头望向我，像只想讨人欢心又不知道怎么做的小猫。"
    "……她什么时候变得这么可爱了？"
    "在我印象中，她更多时候是个会抢你薯片，打游戏输了还不服输的、有点小任性的宅友。"
    show sy clothes2_front2 astonished kp17wl at emphasis_pop
    sy_ "等等，我想到个好主意了！"
    "她猛地坐直身子。"
    sy_ "用你们人类的古话，叫什么『 以其人之道 』……"
    lxc_ "『 还治其人之身 』？"
    show sy clothes2_front2 smile hide_fx at nod_small
    sy_ "对，就是这句！"
    sy_ focus "既然他们想甩锅，你就将计就计——" with dissolve
    "她兴奋地把自己的想法告诉了我。"
    "虽然听起来简单，但仔细一想，还真有可能奏效，特别是对于人事主管这种特别在意「 体面 」的人来说。"
    lxc_ "……说不定真的能行。"
    show sy clothes2_front2 laugh_open at bounce_small
    sy_ "对吧？本小姐这三百年的阅历可不是白费的！"

    sy_ clothes2_side1 cat_mouth "当年有个伯爵想陷害我们家族，结果反而被他自己定的规矩绊倒……" with dissolve
    sy_ "人类社会的公司不是很喜欢定规矩吗？那就把规矩变成他们的枷锁好了！"
    "时语得意地笑了出来，那神情和她最初来到这里时一模一样。"
    "高傲，自信，又可爱。"
    "……啊，原来是这样。"
    "看着眼前开心地扬起双马尾的少女，我忽然明白自己为什么会有刚刚的想法了。"
    "无论是现在这个高傲自信的她，还是打游戏时懒惰任性的她，我都——"

    call achievement (8) from _call_achievement_11


    play music bgm_17 fadeout 1.0 fadein 1.0
    scene bg_office_4
    with Fade(0.5, 0.5, 0.5)

    "回到公司，人事主管很快就召集了项目检讨会。"
    "看来是想速战速决。"

    scene bg_office_5
    with Fade(0.5, 0.5, 0.5)

    "会议室的长桌两侧坐满了人，或许是因为空调温度太低，每个人都表情紧绷，让我也不自觉地咽了咽口水。"
    rszg_ "今天开这个会不为别的，就是想和各位好好聊聊项目延期的事。"
    "他的声音在安静的会议室里显得格外清晰。"
    rszg_ "项目原定上线时间是——"
    "会议室里都是项目组的人，看来他是想在组内先定性，这倒是正合我意。"
    "至于为什么是他来主持会议？"
    "策划主管在外出差，美术归属中台，而程序部的负责人又站在他那边——自然就轮到这位兼管测试部的人事主管了。"
    rszg_ "——现在比计划晚了两周，确实不应该。"
    rszg_ "大家有什么要说的吗？"
    "这种问题就是走个形式，谁也不会真在这种场合提什么意见。"
    rszg_ "咳咳，既然没问题，那我就说说这次项目出现的主要问题——"
    "就算有人真想为项目提建议，话说重了，反而容易被人当成针对个人。"
    "到头来，还是走个过场罢了。"
    rszg_ "——综合来看，项目延期的关键原因，是策划案写得不清楚，导致程序出了很多预料之外的BUG。"
    rszg_ "关于这点，执行策划小林，你有什么要说的吗？"
    lxc_ "有，不过不算问题，算是个建议。"
    "我接话很快，他明显愣了一下。"
    "平时这种场合我多少会争辩几句，今天这么干脆，反而让他有点意外。"
    "但我可不是来认栽的。"
    lxc_ "为了避免其他项目也出现类似问题，我建议把这次的处理结果邮件同步全公司。"
    lxc_ "并附带说明：今后策划案必须严格按照公司标准，写得比本次策划案更清晰明确，否则程序出BUG时，一律由策划承担责任。希望其他组引以为戒。"
    "说完，我不动声色地观察他的表情。"
    "他先是错愕，随即皱起眉头，脸上浮出愠怒又尴尬的神色。"
    rszg_ "小林啊，这次会议主要是项目组内部反思，没必要把问题上升到全公司层面。"
    lxc_ "但我觉得，如果每次出问题都模糊处理，对其他认真工作的同事不公平，对项目进展也不是好事。"
    lxc_ "明确责任归属，能让策划更认真地对待需求文档，提升整体效率。"
    lxc_ "李主管一向重视公司效率，应该也希望项目能运转得更顺畅吧？"
    "他张了张嘴，似乎想发火，但视线扫过会议室里其他人，又闭上了嘴。"
    "几秒钟的沉默后，他才压低声音说。"
    rszg_ "……感谢小林同学的建议。不过公司规定的调整需要慎重讨论，要从长计议。"
    "果然，让时语猜中了。"


    scene bg_living_room_2

    show sy clothes2_side2 cat_mouth at center
    show expression Solid("#ffa200") as yellow_tint:
        alpha 0.12
    with Fade(0.3, 0.3, 0.3)

    sy_ "到时候你就这么做：既然他甩锅说策划案不清晰导致BUG，那就顺水推舟，把『 BUG责任归策划 』变成公司规定！"
    show sy laugh_open at bounce_small
    sy_ "把所有策划都拉下水，看这个主管敢不敢接手这个烫手山芋！"
    show sy clothes2_side1 cat_mouth with dissolve
    sy_ "不过我估计……像他这种势利的人，是一点额外的责任都不想沾的。"


    scene bg_office_5
    show bg_office_5:
        zoom 1.08
        xalign 0.6
        yalign 1.0
    with Fade(0.3, 0.3, 0.3)

    "说实话，时语这招有点冒险，但值得一试。"
    "反正局面已经够糟了，赌一把也无妨。"
    "当然，语气上我还是留了余地，免得真的闹僵。"
    rszg_ "……项目出现问题，原因是多方面的，比如美术细节、部门协作等等。"
    rszg_ "我相信在座各位有能力处理好。"
    rszg_ "最近大家加班也辛苦，出现疏漏可以理解。"
    rszg_ "今天开会主要是为了内部反思，争取下次改进，没必要扩大影响范围。"
    "他合上笔记本，做出总结的姿态。"
    rszg_ "好了，散会吧，为了不影响开发进度，大家回去继续工作。"
    "有事内部消化，没事全员通报。"
    "老狐狸就是老狐狸，和稀泥的本事一流。"


    play music bgm_14 fadeout 1.0 fadein 1.0
    scene bg_office_4
    with fade

    "走出会议室，我松了口气，顺手关掉了手机录音。"
    "回头得好好谢谢时语才行。"


    scene bg_sky_4
    show bg_sky_4 at bg_pan_left
    with fade

    "其实我敢这么做，也不全是凭运气。"
    "这次项目的策划案，我写得比公司标准要细致得多，全公司没几个策划会写到这程度。"
    "人事主管心里也清楚，要是真把这事闹大，他那套说法根本站不住脚，反而会引来更多麻烦。"
    "所以最后他选择息事宁人，大家就当无事发生。"
    "……唉，当初听说程序是个新人，我才把策划案写那么细，想着帮他降低理解成本。"
    "没想到最后，这反而成了我自保的筹码，想想还真是有点讽刺。"
    "要是每个程序员都像以前合作过的那位一样靠谱，该多好。"




    play music bgm_13 fadeout 1.0 fadein 1.0
    scene bg_living_room_1
    with fade

    $ heroine = True
    $ heroine_name = "时语的视角"

    show sy clothes2_front1 bewilderment at center with dissolve

    "今天是林小凑去公司开项目检讨会的日子。"
    "不知道结果怎么样了……"
    "虽然他出门时一副胸有成竹的样子，但按他之前的描述，情况未必能一帆风顺。"
    "不过，既然他那么说了，我还是选择相信他好了。"
    "实在不行的话……我就、就像上次那样用膝枕安慰他好了……不对不对！我在乱想些什么啊！"
    show sy shy skin_shy kp15wl at shy_shrink
    "怎么能动不动就想着去安慰他啊！"
    "……可是，万一他真的很难过呢？我总不能装作没看见吧？"
    show sy clothes2_side1 shy skin_blush hide_fx at look_away_small
    "那也用不着像上次那样……吧？"
    "……但上次的方法确实最有效啊？"
    "哎呀，好烦！越想越乱，等他回来再说吧！"
    show sy pout at angry_stomp
    "我在沙发上翻来覆去，感觉脑子里像有两个小人在吵架。"
    "现在先找点事情做——对了，打扫卫生吧！"
    "先从收拾桌子开始——"
    "叮咚。"
    "门铃突然响了。"

    show sy clothes2_front1 focus with dissolve
    "客人？我在这里住了三个月，从来没见过有客人上门。"
    "房东？房东一般也不会不打招呼就直接过来。"
    "该不会……是什么可疑的人吧？"
    show sy smile_close with dissolve
    "之前林小凑反复叮嘱过，说什么“你们在家千万别随便开门，你俩长相太显眼，但身材又很……特别，容易招惹奇怪的人……"
    show sy smile with dissolve
    "就好像把我们当成什么需要保护的小孩子一样。"
    show sy pout with dissolve
    "真是的，我和星弥长得哪里奇怪了？"
    "何况本小姐可是堂堂正正的淑女！"
    show sy smile with dissolve
    "不过，按门铃的人确实可疑——只按了一声，像完成任务一样。"
    "难道是恶作剧？"
    show sy clothes2_front1 bewilderment with dissolve
    "我搬了把椅子到门口，踮起脚从猫眼往外看。"
    "走廊空荡荡的，一个人影都没有。"
    "我小心推开门，只见地上静静地放着一封信。"
    show sy clothes2_front1 astonished kp1wl at emphasis_pop
    sy_ "这是……"
    "看到封面上那个熟悉的蝙蝠家徽，我的眉头不自觉地皱紧了。"
    show sy clothes2_front1 focus hide_fx with dissolve
    "家族的人……还是找过来了。"


    play music bgm_14 fadeout 1.0 fadein 1.0
    scene bg_bedroom_1
    show bg_bedroom_1 at bg_zoom_in
    with fade
    show sy clothes2_front1 calm at center with dissolve

    "我把信带回房间中，躺在床上，看着上面的内容，不知不觉地回想起了过去的事。"

    show bg_sky_1 at bg_pan_right
    show expression Solid("#ffa200") as yellow_tint:
        alpha 0.12
    with Fade(0.5,1.0,0.5)

    play music bgm_5 fadeout 1.0 fadein 1.0
    "银发少女回想起了那些遥远过去的日子。"
    "年幼的时候她便知道，为了实现目的，贵族们的手段，往往不像他们对外宣称的那么光明正大，有时甚至……有些不堪。"
    "她讨厌那些虚伪的贵族，也讨厌那些为了达到目的、不择手段的大人。"
    "可即使是像布莱菲特家这样，一直以「 行事正派 」出名的家族，有时为了在争斗中保全自己、抗衡对手，也不得不采用一些不那么光彩的策略。"
    "她心里都清楚，也明白家族能延续到今天，背后少不了各种各样的手段。"
    "她自己也在这样的环境中，看着、听着，不知不觉就学会了许多手段——那些她并不喜欢，却又不得不了解、不得不记住的方法。"
    "但她不服输，也不想就这么轻易地向「 大人的规矩 」低头、妥协。"
    "于是，这个古老血族的少女，悄悄在心里做了一个有点任性、甚至可以说是天真的决定。"
    "她「 拒绝 」长大，拒绝让自己的内心，也变得像她讨厌的那些大人一样复杂、冷漠、充满算计。"
    "而「 相由心生 」这个属于古老血族的特性，也让她的外貌，在长达三百年的漫长时光里，一直保持着这副少女般的模样。"
    "仿佛时光的流逝，从未在她身上，留下任何「 长大 」的痕迹。"


    $ heroine = False

    play music bgm_7 fadeout 1.0 fadein 1.0
    scene bg_living_room_3
    with Fade(0.5, 0.5, 0.5)

    lxc_ "我回来了。"
    "开完项目检讨会后，工作进展十分顺利，难得不用加班了。"
    "……不知不觉间，我也越来越像个合格的社畜了，居然会因为不用加班而感到开心。"
    show bg_living_room_2 with dissolve
    "打开灯，客厅里没有看到时语。她人呢？"
    "平时这个时间她总会窝在沙发里打游戏，但今天却不见人影。"
    "虽然她没必要每天都在客厅等我，但没听到那句熟悉的「 你回来了 」，心里难免有些失落。"
    "仔细看发现，整个房间变得格外整洁，像是被彻底打扫过一样。"
    "等等，一尘不染的屋子，消失的时语……该不会……"
    show sy clothes2_front1 smile at center with dissolve
    sy_ "啊呜~人类你回来啦。"
    "声音从卧室方向传来，一个睡眼惺忪的银发脑袋从门后探了出来。"
    "头发略显凌乱，衣领也有些歪斜，带着几分慵懒和可爱。"
    show sy bewilderment with dissolve
    sy_ "你……怎么一副松了口气的表情？"
    lxc_ "有吗？"
    show sy clothes2_side1 cat_mouth at lean_in
    sy_ "唔~该不会是以为本小姐不在了，感到寂寞了吧？"
    lxc_ "……回家后没能第一时间见到你，确实有点不习惯。"
    "虽然被时语猜中了有点不爽，但我确实是这么想的。"
    show sy shy skin_blush at shy_shrink
    sy_ "你，你怎么突然这么直白啊……"
    sy_ "害得我都不好意思继续捉弄你了。"
    lxc_ "这么理直气壮的『 犯罪宣言 』还真是少见。"
    lxc_ "家变得这么干净，都是你打扫的？"
    show sy clothes2_front2 laugh_open at bounce_small
    sy_ "没错！忙了一整天，累死了，搞定后就倒头睡到现在。"
    "原来是这样。"
    show sy clothes2_front1 focus with dissolve
    sy_ "所以，公司那边的事情怎么样了？"
    lxc_ "这个嘛……"
    show sy bewilderment with dissolve
    sy_ "……难道搞砸了？"
    lxc_ "假如我说是的话，会怎么样？"
    show sy shy skin_blush at emphasis_pop
    sy_ "那、那样的话我就……不对不对！"
    "她突然意识到什么，凑近轻轻嗅了嗅。"
    show sy clothes2_side1 focus at lean_in
    sy_ "你今天的味道……闻起来还不错。"
    lxc_ "……刚闻完我就说这种话，听起来就像在闻食物一样。"
    show sy clothes2_front1 pout with dissolve
    sy_ "我才不会随便吸血呢！"
    show sy focus with dissolve
    sy_ "别打岔，味道不错说明你今天的生命力很活跃，心情应该不错！"
    sy_ "公司的事都解决了？"
    lxc_ "不算完全解决，只能说被『 和稀泥 』糊弄过去了。"
    "我将会议的经过简单告诉了她。"
    lxc_ "最后大家就当无事发生，谁也没占便宜，谁也没吃亏。"
    show sy clothes2_side1 despise with dissolve
    sy_ "啧，这些职场老狐狸真狡猾。"
    lxc_ "能争取到这样的结果已经很不错了。"
    lxc_ "这也多亏了你的建议，真的很感谢。"
    show sy clothes2_front1 shy skin_blush at look_away_small
    sy_ "……我只是突然想到的而已，不用特地道谢。"
    "时语微微侧过头，避开了我的视线。"
    show sy clothes2_side1 cat_mouth skin_blush with dissolve
    sy_ "咳咳！再说了，帮助像你这样的普通人类，本来就是本小姐的义务！"
    "咕~"
    "她刚说完这番帅气的话，肚子里就传来了不合时宜的响声。"
    show sy oo skin_shy kp8wl at shocked_step_back
    sy_ "……"
    lxc_ "……今天天气真不错啊。"
    show sy pout skin_blush kp13wl at angry_stomp
    sy_ "这种时候就不要装傻啦！我饿了，带我去吃饭嘛！"
    "时语抡起小拳头向我挥来，脸颊红得都能蒸熟鸡蛋了。"
    show sy pout skin_blush hide_fx with dissolve
    lxc_ "好好好，都听你的。想去哪里吃？"
    show sy clothes2_front1 smile kp17wl at emphasis_pop
    sy_ "商场五楼那家肥牛店！"
    lxc_ "你还惦记着那家店啊？"
    show sy clothes2_front2 cat_mouth hide_fx at bounce_small
    sy_ "当然！要是吃不到的话，我会一直缠着你的！"
    lxc_ "听起来有点可怕呢。"
    sy_ "别废话了，快点出门快点出门！"
    lxc_ "别急，你刚睡醒至少得梳个头发吧？"
    sy_ "那你快点帮我梳一下嘛！"
    lxc_ "是是。"
    "这位血族大小姐，还真是有点不让人省心啊。"


    scene bg_sky_4
    with fade

    "那之后的日子平静又有趣，我原以为这样的日常能一直持续下去。"
    "但没想到——"


    scene bg_shop_4
    with fade
    show sy clothes2_side1 black skin_black at center with dissolve

    sy_ "说起来，在电影院里做了那种事后，你居然还能一脸平静地喝咖啡。"
    sy_ "真厉害呢，林小凑先生。"
    "咖啡店内到处都是穿着各种吸血鬼服装的人，而我差点因为她这句话把刚喝的咖啡喷了出来。"
    "这家伙，绝对是故意的……"
    lxc_ "怎么突然用上敬语了……呜啊，好苦。"
    show sy despise skin_blush with dissolve
    sy_ "别转移话题。"
    "她脸上挂着微笑，眼里却毫无笑意。"
    "唉，事情怎么会变成这样呢？"


    play music bgm_11 fadeout 1.0 fadein 1.0
    scene bg_living_room_1
    with Fade(0.5, 0.5, 0.5)
    show sy clothes2_front1 smile at center with dissolve

    "（时间回到这一天的早上）"
    "周末——光是听到就让人心情愉快起来的词。"
    "连续工作了五天之后，终于迎来了休息日。"
    "这周末做点什么好呢……"
    "看着身旁一边打游戏一边轻轻晃着腿的时语，我忽然有了个想法。"
    lxc_ "时语，要出去玩吗？"
    "之前多亏她的建议，公司里的麻烦少了很多，正好趁周末好好感谢她一下。"
    show sy focus with dissolve
    sy_ "出去玩？玩什么？"
    lxc_ "看电影，喝咖啡，随便逛逛？"
    show sy smile_close at nod_small
    sy_ "好吧，反正游戏的日常任务都做完了。"
    show sy astonished skin_blush kp1wl at emphasis_pop
    sy_ "等等！休息日就我们两个出去，还是看电影喝咖啡……那不就是约……"
    lxc_ "说话声怎么越来越小？出去玩有什么问题吗？"
    show sy clothes2_side1 pout skin_blush hide_fx at look_away_small
    sy_ "……哼，没有。我去准备一下！"
    "她眼神古怪地瞥了我一眼，然后飞快地溜进了洗手间。"
    scene bg_living_room_1
    with fade
    show sy clothes2_front1 smile at center with dissolve
    sy_ "我准备好了！看起来没问题吧？"
    lxc_ "嗯，和平时一样好看……不过发带是不是有点歪了？"
    show sy astonished with dissolve
    sy_ "是吗？我看看……真的哎，你怎么看出来的？"
    "她拿起小镜子照了照，迅速调整了绑着双马尾的发带。"
    lxc_ "这个嘛……"
    "最近天天都和你打游戏，很难不注意到这些细节。"
    lxc_ "刚好发现的。准备好了就出发吧。"
    sy_ "好吧。"


    scene bg_shop_1
    with fade
    show sy clothes2_front1 smile at center with dissolve

    show sy focus with dissolve
    sy_ "所以，我们要看什么电影？"
    "周末的商业街人来人往，我们不自觉地靠得近了一些。"
    lxc_ "我看看正在上映的……有《残缺的纳西索斯》、《月上的公主》……"
    sy_ "还有《郁金香的救赎》、《夜空下的魔法使》，看起来都不错。"
    lxc_ "要不要试试这个？"
    sy_ "这个好像不错！"
    "我们同时指向了同一部电影——《逃离十二世纪》。"
    show sy oo kp1wl at emphasis_pop
    sy_ "欸？你也想看这个？"
    lxc_ "嗯，看来不用为了选片拼个你死我活了，可惜。"
    show sy bewilderment hide_fx with dissolve
    sy_ "……有什么好可惜的？"
    lxc_ "毕竟猜拳我肯定赢。"
    show sy clothes2_side1 despise with dissolve
    sy_ "……幼稚鬼。"
    "无视时语的鄙视眼神，我走向售票处。"
    lxc_ "你好，两张《逃离十二世纪》。"
    fwy_ "好的。小朋友看电影有优惠，需要吗？"
    show sy clothes2_front1 pout at angry_stomp
    sy_ "本小姐可不是什么小——唔唔！"
    lxc_ "不用了谢谢！再加一桶爆米花！"
    "拿到票和爆米花，我赶紧拉着时语走进放映厅。"
    "总觉得类似的情况以前也发生过。"


    scene cg160
    with Fade(0.5, 0.5, 0.5)

    sy_ clothes2_front1 pout "气死我了！那个服务员太没眼光了！"
    lxc_ "我早说过，你们的外貌确实容易让人误会……"
    sy_ "哼！本小姐是古老血族，单看外表根本判断不了年龄！"
    lxc_ "大人有大量，别计较这种小事嘛。"

    show cg163
    with dis_master
    "电影开始了。"
    "故事讲述一个现代年轻人吃了某地特产的蘑菇后，穿越到一个类似中世纪的地方。"
    "他惊慌失措地寻找回到现代的方法，却却慢慢发现，这里并非过去，而是一个充满魔法的异界。"
    "当剧情推进到主角发现魔法存在时，时语轻轻感叹了一声。"


    show cg162
    with dis_master
    sy_ focus "这个设定......简直像穿越到里世界一样。"
    "但实际上，这里既非中世纪也非异界，而是未来的地球。"
    "剧情高潮揭示地球曾因一场巨大灾难变成这样，而灾难就发生在主角穿越后不久。"
    "是留在未来逃避灾难，还是回到过去，直面注定到来的死亡？"
    "主角最终选择再次吃下蘑菇，回到过去，为了更多人的未来而战。"
    "因为，必须有人警告过去的人们：灾难即将来临。"
    lxc_ "嗯……情绪调动还不错，就是吃蘑菇穿越是什么整蛊设定……"

    "我边小声吐槽边伸手去拿爆米花，却摸到了一样细长、温热的东西。"

    show cg161
    with dis_master

    "服务员把薯条混进来了？还炸得软绵绵的——我去这薯条怎么还会动！"
    "我转过头，只见时语满脸通红地瞪着我，而我手里握着的，自然不是什么薯条。"
    "好险，差点下意识就舔下去了。"
    "时语顿时炸毛。"

    with vpunch

    lxc_ "（大小姐！还在电影院呢！冷静点！）"
    sy_ shy skin_shy "（你……！林小凑你绝对是故意的！！！）"
    "情急之下，我握紧了她的手，防止她在放映厅里暴走。"

    "起初她还挣扎了几下，但随着电影的片尾曲响起，她渐渐平静下来。"
    "也许是片尾的旋律，唤起了她对剧情的共鸣吧。"
    "因为握着她的手，我不可避免地感受到了她的体温。"
    "手小小的，有点温暖，甚至因为紧张还出了点小汗……喂，别挠我掌心啊！"
    "我们保持着这个有点奇怪、但谁也没有放开的姿势，直到片尾曲完全结束。"

    call achievement (11) from _call_achievement_15


    scene bg_shop_1
    with fade
    show sy clothes2_front1 shy at center with dissolve

    "离开影院后，我们很有默契地同时松开了手。"
    "我走在前面，她跟在后面，两人之间保持着微妙的距离。"
    lxc_ "前面那家咖啡店今天好像有特别活动，要不去看看？"
    show sy shy skin_blush at look_away_small
    sy_ "嗯。"
    "我用尽量平常的语气说话，她听起来似乎也没有在生气。"
    "难道是我想多了？"
    "或许是因为主题活动，这家咖啡店前也排起了队伍，不过还好人没有特别多。"
    "取号后，我和时语静静站在路边等候。"
    "她望着街上来来往往的行人，显得有些出神。"
    lxc_ "……生气了？"
    show sy clothes2_front1 bewilderment with dissolve
    sy_ "没有，只是在想事情。"
    show sy clothes2_side1 focus with dissolve
    sy_ "你觉得……刚才电影的主角，应该选择回到过去吗？"
    "她微微瞥了我一眼，语气听起来很随意。"
    lxc_ "嗯……从故事来说，他选择回去确实更感人，也更能调动观众的情绪。"
    show sy sigh with dissolve
    sy_ "也就是说，你觉得他回去会更好？"
    "听到我的回答，她连睫毛都微微垂低了几分。"
    lxc_ "不，那只是从『 讲故事 』的角度。对我个人来说，我觉得怎样都可以。"
    lxc_ "作为『 主角 』，他理应去拯救世人，表现出一个英雄该有的样子。"
    lxc_ "但抛开这层光环，他也只是个偶然间穿越了时间的普通人。"
    lxc_ "没人有资格指责他选择眼前安稳的生活，也没人能否定他回去的勇气。"
    lxc_ "更何况这只是一部普通的爆米花电影，不用想太多。"
    show sy sigh at bounce_small
    sy_ "……也是啊，只是一部电影而已。"
    "时语抬起鞋尖，轻轻蹭了蹭地面，接着又用脚尖轻轻碰了碰我的鞋。"
    sy_ "……你是不是猜到我在想什么了？"
    lxc_ "有一点，但那确实是我的真实想法。"
    "我也提起鞋尖，轻轻踮了踮她的鞋尖。"
    lxc_ "很多事，当时觉得非做不可，但时间久了回头再看，其实也没什么大不了的。"
    lxc_ "做或不做，怎么选都好，关键是自己要觉得开心，觉得有意义。"
    lxc_ "虽然我这个社畜说这些，好像没什么说服力就是了。"
    show sy smile_close with dissolve
    sy_ "……是啊，很多事确实没什么大不了的。"
    "她用手轻掩住嘴，终于露出了笑容。"
    "她果然还是笑起来更好看。"


    scene bg_shop_4
    with fade
    show bg_shop_4:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve
    show sy clothes2_front1 calm at center with dissolve

    "今天咖啡店在举办吸血鬼主题活动，多数店员都穿着黑斗篷、戴着尖牙装饰走来走去。"
    "对时语这个真正的血族来说，这场面大概有点滑稽。"
    fwy_ "先生小姐，您的咖啡，请慢用。"
    lxc_ "谢谢。"
    "等服务员走远，时语托着下巴打量四周。"
    show sy clothes2_side1 focus with dissolve
    sy_ "领结歪了，披风的材质也太廉价了……不过勉强还算有模有样。"
    lxc_ "只是普通的店铺活动，要求别那么高，肯定比不上真正的血族啦。"
    lxc_ "不过那边那位，风格还挺特别的。"
    "我朝不远处一位金发店员指了指——她没穿斗篷，而是白色毛衣配紫色长裙，搭着黑色丝袜。"
    show sy clothes2_side1 black skin_black kp28wl at glare_shake
    sy_ "……看得还真仔细呢。"
    "她突然凑近了些，把声音压低。"
    show sy black skin_black at glare_shake
    sy_ "原来你喜欢那种风格啊？"
    lxc_ "只是觉得和其他人不太一样。而且总觉得在哪里见过……"
    lxc_ "对了，像之前和你一起玩的那个格斗游戏里的女主角。"
    "我边回忆边端起咖啡，准备好好品尝一下。"
    sy_ "说起来，在电影院里做了那种事后，你居然还能一脸平静地喝咖啡。"
    sy_ "真厉害呢，林小凑先生。"
    "刚到嘴边的咖啡差点喷了出来。"
    "这家伙，绝对是故意的……"
    "她脸上挂着微笑，眼里却毫无笑意。"
    "明明刚才在店外排队时气氛还挺好的，怎么一转眼又生气了？"
    lxc_ "怎么突然用上敬语了……呜啊，好苦。"
    show sy clothes2_side1 despise skin_blush hide_fx with dissolve
    sy_ "别转移话题。"
    show sy focus with dissolve
    sy_ "关于电影院里的事，你是不是该说明一下？"
    "「 我问心无愧 」——虽然很想这么说，但仔细想想，我后面好像确实掺了点私心……"
    lxc_ "抱歉，当时情急之下就握住了你的手，没多考虑你的感受。"
    "我郑重地向她道歉。"
    show sy clothes2_front1 pout skin_blush with dissolve
    sy_ "……哼，居然这么干脆就认错，没意思。"
    lxc_ "？"
    show sy shy skin_blush at look_away_small
    sy_ "再假装生气，不就显得我无理取闹了嘛……"
    lxc_ "……假装？"
    show sy clothes2_front1 focus skin_blush with dissolve
    sy_ "咳咳，别打岔，现在是我对你的审讯时间。除此以外没别的要说了？"
    lxc_ "……应该没了吧？"
    "我努力回想是不是还有其他冒犯到她的地方。"
    sy_ "真的？"
    lxc_ "真的。"
    show sy shy skin_blush at look_away_small
    sy_ "那……你就没有什么别的想法吗？"
    "她用手指轻轻卷起了发梢，耳尖微微泛红。"
    "想法？要犯错的人讲述自己的想法，这算是审讯现场，还是犯罪心理学访谈节目？"
    lxc_ "嗯……让我想想。"
    sy_ "快说快说。"
    lxc_ "我最大的想法是——下次一定要买两桶爆米花。"
    show sy clothes2_side1 despise with dissolve
    "时语露出了无语的表情。"
    lxc_ "干嘛这副表情……从根源上解决问题，这回答不错吧？"

    sy_ "谁要听这个啊……"
    lxc_ "那你想问什么？"
    show sy clothes2_front1 shy skin_shy at look_away_small
    sy_ "是……是手的触感啦！摸了本小姐的手，总得有点评价吧！"
    show sy shy skin_shy at look_away_small
    sy_ "这种话还要我亲自说出来，笨蛋……"

    "她的脸越来越红，连带着我也有些不好意思了。"
    "明明之前还有过更亲密的接触……"
    lxc_ "……挺软的。"
    sy_ "什么？"
    lxc_ "小小的，软软的，摸着很舒服。"
    "自暴自弃地说完，我猛喝一口咖啡……奇怪，好像没那么苦了。"
    show sy clothes2_side2 focus skin_blush with dissolve
    sy_ "这、这样啊……不过你为什么不看着我说？"
    lxc_ "……"
    show sy cat_mouth skin_blush at look_away_small
    sy_ "难道你也害羞了？"

    lxc_ "没有。"
    sy_ "那你看着我。"
    lxc_ "不行。"
    sy_ "为什么？"
    lxc_ "窗外的风景挺好看的。"
    sy_ "比本小姐还好看？"
    lxc_ "……"
    "我只好乖乖把头扭回来。"
    show sy clothes2_side1 cat_mouth skin_blush with dissolve
    sy_ "……哼，原来你也会害羞嘛。"
    lxc_ "我只是个普通人，会害羞很正常。"
    "尤其还是在当事人面前，评价对方的手……"
    show sy shy skin_blush with dissolve
    sy_ "有什么关系嘛……至少让我知道，不是只有我一个人在不好意思。"
    sy_ "而且啊……"
    "她忽然凑近，在我耳边轻声说。"
    show sy clothes2_side1 cat_mouth skin_blush at lean_in
    sy_ "你可是第一个这样子摸我手的男生哦~"
    lxc_ "……！"
    "如果有镜子，我肯定能看到自己的耳朵也红了。"
    "真是输给她了，明明刚才还一副很生气的样子，现在却笑得这么开心。"
    "唉，这咖啡怎么越喝越甜了。"


    scene bg_street_1
    with fade
    show sy clothes2_front1 smile at center with dissolve

    show sy smile_close with dissolve
    sy_ "接下来有什么打算？"
    "离开咖啡店，她轻快地走在前面，我缓步跟在后面，和来时的顺序正好相反。"
    lxc_ "随便逛逛吧。"
    lxc_ "不过说好一起喝咖啡，结果你就尝了一口，剩下的全推给我。"
    show sy clothes2_side1 sigh with dissolve
    sy_ "……只是咖啡不适合血族而已，而且你自己不也喝得很起劲吗？"
    show sy pout with dissolve
    sy_ "哪有人像喝水一样喝咖啡的啊！"
    lxc_ "为了促进面部散热，适当的冷却液是很有必要的。"
    show sy despise with dissolve
    sy_ "这人在说什么鬼话呢……"
    show sy clothes2_front1 calm with dissolve
    sy_ "总之，比起咖啡，我更喜欢红茶。"
    "她用余光偷偷瞄了我一眼。"
    lxc_ "下次吧。红茶的话，是不加糖的那种？"
    show sy shy skin_blush at look_away_small
    sy_ "……还是加一点吧。"
    lxc_ "噗。"
    show sy pout skin_blush kp13wl at emphasis_pop
    sy_ "不许笑！"
    show sy pout at angry_stomp
    lxc_ "好好，不笑。"
    show sy pout hide_fx with dissolve
    "那我在心里偷偷笑。"
    sy_ "……偷偷笑也不行！"
    lxc_ "……这你也能猜到？"
    show sy clothes2_side2 cat_mouth with dissolve
    sy_ "哼，和你相处了这么久，你的表情我早看透了。"
    sy_ cat_mouth "我看你就是故意想捉弄我……" with dissolve
    lxc_ "哪敢。"
    "虽然确实是想逗逗她。"
    "不过，她刚才明明也捉弄过我，这会儿倒说得理直气壮。"
    lxc_ "说正经的，往前逛一圈就回家吧。"
    show sy clothes2_front1 smile skin_blush with dissolve
    sy_ "……嗯。"
    "她悄悄放慢了一点脚步，我配合着稍稍加快了些，两人最终并肩走在了一起。"
    "彼此都心照不宣地，想让这段并肩而行的时光，再慢一点，再长一点。"


    scene bg_street_4
    with fade
    show sy clothes2_front1 smile at center with dissolve

    "走到商业街尽头，这里的行人少了许多，两旁的店铺也显得更老旧一些。"
    "没想到这种地方还有这些商店，以前从没留意过。"
    "正打算往回走时，时语在一家店前停下了脚步。"
    lxc_ "古董店？"
    show sy focus with dissolve
    sy_ "嗯，有样东西很在意。"
    "顺着她的视线，我看到玻璃柜角落放着一枚双月形状的旧徽章。"
    "银制的表面已经有些氧化发暗，但纹路依然清晰。"
    lxc_ "要进去看看吗？"
    show sy sigh with dissolve
    sy_ "不用，只是有点意外。"
    show sy clothes2_side1 calm with dissolve
    sy_ "这是一百年前，里世界某个显赫家族的徽章。"
    sy_ "虽然和我们布莱菲特家没什么交情，但至少听说过他们的名号。"
    lxc_ "里世界的徽章出现在这里，岂不是说明……"
    show sy focus with dissolve
    sy_ "嗯，很可能有同族也来到了表世界，甚至在这里生活了很久。"
    show sy calm with dissolve
    sy_ "原来……不止我一个啊……"
    lxc_ "……"
    "我一时不知该说什么才好。"
    show sy clothes2_front1 smile_close with dissolve
    sy_ "好了，我们回家吧。"
    show sy smile with dissolve
    sy_ "逛街好累，还是宅家打游戏舒服……你干嘛？"
    "我正想着该怎么安慰她，她却显得意外地轻松，反而让我伸到一半的手僵在了半空。"
    lxc_ "……手有点酸，活动一下。"
    show sy smile_close with dissolve
    sy_ "噗，好烂的借口。"
    sy_ "我又没那么容易难过……不过，谢谢啦。"

    show sy:
        zoom 1.1
        yoffset 250
    with dissolve

    "她靠过来，肩膀轻轻贴着我，距离比刚才并肩走时要近了许多。"
    lxc_ "我还以为你会有点伤感呢。"
    show sy clothes2_front1 calm with dissolve
    sy_ "比起伤感，更多是觉得……释然吧。"
    lxc_ "释然？"
    show sy focus with dissolve
    sy_ "嗯。其实不久前，我收到了家族寄来的一封信。"
    show sy clothes2_side1 bewilderment with dissolve
    sy_ "信上写了一些让我回去之类的话。"
    show sy sigh with dissolve
    sy_ "那天我特别烦躁，一气之下就把你家彻底打扫了一遍。"
    lxc_ "怪不得那天家里特别干净。"
    show sy clothes2_side1 bewilderment with dissolve
    sy_ "虽然私心上，我早就决定要留下来了。"
    sy_ "但作为家族的一员，总觉得这么做太任性了。"
    sy_ "特别是看完刚才那部电影后，这种想法更强烈了。"
    "看来我没猜错，她之前问我电影的问题，就是在纠结这件事。"
    "会对故乡和家族感到犹豫，也是人之常情。"
    show sy clothes2_front1 calm with dissolve
    sy_ "但看到那枚徽章后，我意识到自己不是第一个这么做的人。"
    show sy clothes2_front1 smile with dissolve
    sy_ "所以反而松了口气。"
    "原来如此。"
    "因为有同族做过类似的事，所以她心里的负担就轻了一些。"
    "她找到了除私心之外，一个能让她理直气壮留下来的理由。"
    "对时语来说，这是很合理的事。"
    "但是——"
    lxc_ "就算没有这件事，任性一点也没什么不好吧？"
    "我更希望她留下来的理由，能更纯粹一点。"
    lxc_ "毕竟，你平时已经够懂事了。"
    show sy astonished kp2wl at look_away_small
    sy_ "我？懂事？你认真的？"
    lxc_ "是啊。虽然你生活上确实很随性，会耍大小姐脾气，也会像阿宅一样赖在沙发上一整天。"
    lxc_ "但在重要的事情上，你一直很有原则。"
    show sy astonished hide_fx with dissolve

    show sy:
        zoom 1.2
        yoffset 500
    with dissolve
    "我朝她的方向轻轻迈了一步，离她更近些。"
    lxc_ "你从没在我面前用过魔法或血族的能力，也会强烈反对我用魔法走捷径赚钱。"
    lxc_ "可能你自己没察觉，但时语，你骨子里其实是个很讲规矩的人。"
    "正因为她是这样的人，所以才会一直守着家族的规矩，在那座古堡里生活了近三百年，从未离开。"
    show sy shy skin_blush with dissolve
    sy_ "……你一直有留意到这些事啊。"
    lxc_ "嗯。时语的事，我一直都记得很清楚。"
    lxc_ "既然你这么守规矩，偶尔任性一点又有什么关系呢？"
    show sy shy skin_blush with dissolve
    sy_ "我、我只是……"
    "她低下头，手指无意识地卷着裙角，声音越来越小。"
    lxc_ "我明白你有自己的坚持。"
    lxc_ "但说真的，你要是不任性一点，我反而会很困扰。"
    show sy bewilderment skin_blush with dissolve
    sy_ "……为什么？"
    lxc_ "因为，如果不是你任性离家出走，我就没机会遇见你了。"
    "我认真地看着她，说出心底的话。"
    lxc_ "所以，就算任性一点也没关系，我希望你留在我身边。"
    show sy astonished skin_blush kp1wl at look_away_small
    sy_ "你……"
    "她睁大眼睛，表情从惊讶渐渐转为触动，嘴巴微微张开，却一时说不出话。"
    "最后，随着脸颊慢慢泛红，她又变回了我熟悉的、略带傲娇的模样。"
    show sy clothes2_side1 pout skin_blush hide_fx with dissolve
    sy_ "……哼，净会说些好听的话。"
    show sy clothes2_side2 cat_mouth skin_blush with dissolve
    sy_ "你就是用这套，专门骗天真可爱的少女回家吧？"
    lxc_ "是啊，我就是专门把主动找上门的美少女拐走的坏蛋。"
    "我轻轻擦去她眼角的泪光，指尖传来温暖的触感。"
    show sy smile skin_blush with dissolve
    sy_ "……也就本小姐会上你的当了。"
    "这一次，她主动握紧了我的手。"
    show sy smile_close skin_blush with dissolve
    sy_ "带我回家吧，回我们的家。"
    lxc_ "嗯。"
    "虽然我对她的过去还知之甚少，但至少未来，我们可以慢慢地了解彼此。"
    "为了这个目标，我悄悄下定了决心。"
    "夕阳把我们的影子拉得很长，在街道上缓缓交错、重叠。"
    "她的手很暖，也很轻，像握住了一片羽毛，又像握住了……整个世界。"
    window hide
    hide sy
    show bg_sky_5

    with fade


    pause 0.5


    show bg_sky_3 with dissolve
    pause 0.5

    show bg_sky_1 with dissolve

    pause 0.5
    hide bg_sky_5
    show bg_sky_5 with dissolve
    pause 0.5
    hide bg_sky_3
    show bg_sky_3 with dissolve



    $ heroine = True
    $ heroine_name = "时语的视角"

    play music bgm_7 fadeout 1.0 fadein 1.0
    scene bg_living_room_2
    with Fade(0.5, 0.5, 0.5)
    show sy clothes2_front1 focus at center with dissolve

    lxc_ "我回来了……你怎么表情怪怪的？"
    show sy clothes2_side2 cat_mouth with dissolve
    sy_ "没什么，就是好奇你最近明明天天加班，心情却好像挺不错的样子。"
    "我凑近他身边，轻轻嗅了嗅。"
    show sy clothes2_side1 focus at lean_in
    sy_ "身上的味道也挺清爽。"
    lxc_ "这个嘛……只是最近忙的事没那么让人心累而已。"
    lxc_ "……话说有必要靠这么近吗？"
    show sy shy skin_blush at shy_shrink
    sy_ "我、我又不是故意靠这么近的……而且你身上一股汗味！"


    scene cg425
    with dissolve

    "我别过脸，快步退回沙发，抱起平板假装专心打游戏。"
    "自那天之后，我就正式在林小凑家住了下来。"
    "……虽说是正式，其实和之前的生活也没什么差别。"
    "白天他去上班，我在家做家务，空闲时就玩下游戏，偶尔在网上搜搜我能自己赚钱的办法。"
    "周末和他一起联机打游戏，打发掉一个个慵懒的午后。"
    show cg426
    with dissolve
    "这样的日常平淡又安心……可是，他的反应是不是有点太平静了？！"
    "明明之前还说过「 希望你留在我身边 」那种话……那、那不就是告白的意思吗？！"
    "为什么他还能像什么都没发生过一样，这么自然地相处啊！"
    "难道是我们之间的相处方式太稀松平常了，他才会这么若无其事吗……"
    lxc_ "怎么玩个手游表情还这么丰富……"
    lxc_ "今天晚上做宵夜了吗？"
    hide cg427
    show cg427
    with dissolve
    sy_ despise "没有！"
    lxc_ "可我好像闻到了炒饭的香味哎？"
    hide cg426
    show cg426
    with dissolve
    sy_ bewilderment "……自己去厨房拿啦。"
    lxc_ "好嘞，谢了。"
    sy_ "唔唔唔……！"
    "就是他这种自然而然的态度才让人火大！"
    "搞得好像只有我一个人在为那天的事纠结一样。"
    "算了，不管他了，先打两局游戏泄愤！"
    "滴滴——"
    hide cg425
    show cg425
    with dissolve
    "推送栏突然弹出了一条新消息。"

    scene bg_living_room_2
    with dissolve

    show sy clothes2_front1 oo kp1wl at center, emphasis_pop
    sy_ "欸？！"
    lxc_ "怎么突然这么大动静？难道炒饭又忘记放盐了？"
    show sy clothes2_front1 pout kp13wl at angry_stomp
    sy_ "才没有！我这次可是好好加了酱油的！"
    show sy smile hide_fx with dissolve
    sy_ "是这个啦！"
    "我把平板举到他面前。"
    lxc_ "『 猛汉狩猎传新作参展CX展，现场开放试玩 』……你想去CX展？"
    show sy smile_close at nod_small
    sy_ "嗯。"
    lxc_ "这种动漫游戏综合展的现场可是会人挤人，还很累的，你确定要去吗？"
    show sy bewilderment with dissolve
    sy_ "唔……可是有新作的试玩，我真的很想去嘛。"
    show sy clothes2_side2 cat_mouth with dissolve
    sy_ "而且就算累了，不还有你吗？到时候你背我就好啦。"
    lxc_ "……行吧。"
    show sy bewilderment with dissolve
    sy_ "你干嘛用手捂住嘴？"
    lxc_ "我怕偷笑的表情被你看见。"
    sy_ "有什么好笑的？"
    lxc_ "就是觉得……眼前这只正在撒娇的生物太可爱了，有点忍不住想笑。"
    show sy astonished skin_blush kp1wl at emphasis_pop
    sy_ "哪来的生物，你面前不就只——"
    "我猛然反应过来他在说什么，脸颊一下子变烫了。"
    show sy shy skin_shy hide_fx at shy_look_away
    sy_ "……乱、乱说什么呢！"
    "我抓起沙发上的抱枕朝他丢了过去。"
    with vpunch
    lxc_ "哇！枕头袭击是犯规的！"


    $ heroine = False

    play music bgm_19 fadeout 1.0 fadein 1.0

    scene bg_sky_3
    with fade

    pause 1.0

    scene bg_sky_1
    with Dissolve(1.0)

    pause 1.0

    scene bg_shop_6
    with Fade(0.5, 0.5, 0.5)

    "在场外排了将近一小时的队后，我们终于踏进了CX展的会场。"

    scene cg7
    with Fade(0.5, 0.5, 0.5)


    show sy clothes1_front1 smile:
        yoffset 5000

    "时语今天穿了她自己的那身衣服——那身黑白相间的贵族礼服。"
    show cg71 with dis_master
    "周围到处都是各种角色扮演的、五花八门的服装，我本以为她这样穿应该不会太显眼。"
    show cg73 with dis_master
    "——直到时不时有扛着「 长枪短炮 」的摄影师凑过来，礼貌地问：「 可以给您拍几张照吗？」「 您出的是哪个角色？还原度好高啊！ 」"
    "我才意识到，她或许比我想象中还要引人注目。"
    "精致的礼服，出众的容貌，还有那种与生俱来的优雅气质，再加上那恰到好处的身高，都让她在人群中格外亮眼。"

    "在那些追求细节和氛围感的爱好者眼里，她甚至有着天然的优势——无需刻意扮演，她只要做她自己，就已经像是从故事里走出来的、活生生的贵族少女。"
    show cg72 with dis_master
    "一开始时语还会礼貌地摇头婉拒，到后来实在有点烦了，她干脆整个人贴到我身边，把问题全推给我。"
    "她那副无言的表情简直像在说「 要问什么就问我的经纪人吧 」。"
    "周围本来就人潮汹涌，我的表情也不自觉绷得更紧了，反倒让那些跃跃欲试的摄影师感到了一点「 生人勿近 」的气息。"
    show cg74 with dis_master
    "多亏如此，围在我们身边的人群终于逐渐散开了。"
    lxc_ "没想到你这么受欢迎……不过你反应还挺淡定的。"
    show cg75 with dis_master
    sy_ sigh "还好吧，浮于表面的夸奖在贵族茶会上早就听腻了。"
    hide cg7
    show cg7 with dis_master
    sy_ laugh_open "比起这些无聊的事，我们快去《猛汉》的试玩区吧！地图上写着是在K3馆！"
    "她晃了晃手里的地图，兴奋地拉着我的手。"
    lxc_ "知道了知道了，你别拽着我走啊……"
    "这丫头哪来这么大力气……"
    "为了防止我的袖子被她扯坏，我只能努力跟上她轻快的脚步。"


    scene bg_shop_6
    with Fade(0.5, 0.5, 0.5)
    show bg_shop_6:
        zoom 1.08
        xalign 0.55
        yalign 1.0
    with dissolve
    show sy clothes1_front1 astonished at center with dissolve

    "好不容易挤过重重人流，来到《猛汉》展区前——然后我们看见了一条蜿蜒曲折、一眼望不到头的长队，目测至少要排一个半小时以上。"
    "主办方显然早有预料，不仅划出了专门的排队区，还设置了取号牌和分流通道。"
    show sy bewilderment with dissolve
    sy_ "怎么这么多人呀……要是我们刚刚走快一点就好了，说不定还能排在前面些。"
    lxc_ "说真的，除非我们半夜就来门口守着，不然好像都没太大区别。"
    show sy pout with dissolve
    sy_ "怎么这样嘛……明明试玩台就在眼前了……"
    "她眼巴巴地望着不远处那些正在试玩的玩家，表情写满了渴望。"
    lxc_ "没办法，大型展会就是这样……人实在太多了。"
    "虽然来之前就有心理准备，但亲眼见到这场面，还是难免感到震撼。"
    "幸好，提前做了一些准备……唯独这种时候，我特别感激自己学过的专业。"
    "我看了眼手机上新收到的消息，转头对时语说。"
    lxc_ "排队还要很久，要不我们先去别的地方逛逛？等人少一点再回来。"
    show sy sigh at disappointed_droop
    sy_ "……好吧。"
    "她不太情愿地点了点头，脚尖还无意识地蹭了蹭地面。"
    "明明真实年龄比我大得多，闹起小脾气来却还像个孩子呢。"


    scene bg_shop_6
    with Fade(1.0,1.0,1.0)
    show sy clothes1_front1 smile at center with dissolve

    "把整个展馆逛完一圈后，我和时语手上都提满了各种免费领取的小礼物。"
    "虽然大部分都是些装饰为主的东西，但数量多起来后，还是会让人有种满足的成就感。"
    show sy clothes1_front1 focus with dissolve
    sy_ "游戏试玩、虚拟偶像舞台、插画展、作者签售、同人本贩售……CX展的项目还真不少。"
    lxc_ "在大型商业展里，同类主题的展区越多越好。"
    lxc_ "一来能吸引更多参展商入驻，二来也能让进场的人有更多地方逛、有更多东西想买。"
    lxc_ "说白了，就是能赚更多钱。"
    show sy astonished with dissolve
    sy_ "你对这些还挺了解的嘛。"
    "她用略带意外的眼神看了看我。"
    lxc_ "毕竟也算专门学过一点相关的东西，不过我也只是懂些皮毛。"
    show sy clothes1_side1 focus with dissolve
    sy_ "你出门前准备好水、零食、充电宝，还特地塞了双拖鞋在包里……也是因为这个？"
    lxc_ "这个倒纯属经验。展馆里的东西又贵又不好吃，而且万一鞋子磨脚，还能换上拖鞋救急。"
    show sy clothes1_side2 cat_mouth with dissolve
    sy_ "还真是熟练呢……以前经常和别人一起来逛这种展？"
    lxc_ "也不算经常。"
    sy_ "……女朋友？"
    show sy focus with dissolve
    "她微微眯起眼睛。"
    lxc_ "……你看我这样子，像是有过女朋友的人吗？"
    "我回了她一个「 你在开什么玩笑 」的无语表情。"
    lxc_ "是和同学、朋友一起来的。"
    show sy smile_close with dissolve
    sy_ "喔，这样啊……没想到你还会有朋友呢。"
    show sy clothes1_side2 cat_mouth with dissolve
    lxc_ "喂，别突然人身攻击啊。"
    "不知道为什么，听到我的回答后，她好像心情变得很好的样子，还带着点小得意似的，轻轻地用拳头锤了锤我的手臂。"
    "算了，她开心就好。"


    scene bg_shop_6
    with fade
    show bg_shop_6:
        zoom 1.04
        xalign 0.45
        yalign 1.0
    with dissolve
    show sy clothes1_front1 sigh at center with dissolve

    "逛到腿都开始发酸之后，我和时语靠在周边贩卖区附近的一根柱子旁休息。"
    "时语望着周围密密麻麻的人群，又看了看餐饮区前排成长龙、几乎没有移动迹象的队伍，忍不住叹了口气。"
    sy_ "……我现在彻底明白，你昨天为什么说逛展会会很累了。"
    lxc_ "不光是身体累，精神上也会很疲惫。"
    lxc_ "虽然现在大家看上去都挺开心的，但背地里偶尔也会发生些不太愉快的事。"
    lxc_ "比如假装聋哑人让你捐款的、用假钱找茬的、还有分发奇怪『 试吃品 』的陌生人……以前的漫展还挺常遇到这些事的。"
    show sy clothes1_front1 astonished with dissolve
    sy_ "欸，这样啊……我还以为来这里的都是善良友好的阿宅呢……"
    "她有点惊讶，对面有路人经过时，还下意识往我身边靠了靠。"
    show sy clothes1_side1 bewilderment with dissolve
    lxc_ "现在已经比以前好很多了，倒不用太担心。"
    lxc_ "不过，要是我这些话让你对漫展幻灭了，我先说声抱歉。"
    show sy clothes1_side1 smile with dissolve
    sy_ "……也不用道歉啦，我本来对漫展就没有太多滤镜，只是因为有《猛汉》的试玩才想来的。"
    sy_ "而且，正因为是你告诉我这些，我反而更庆幸是和你一起来逛展。"
    lxc_ "嗯？为什么会这么想？"
    show sy clothes1_front1 smile_close with dissolve
    sy_ "因为有你在我身边，我就不会遇到那些麻烦事呀。"
    sy_ "而且，你告诉我这些，不也是为了让我能更小心、更安全吗？"
    lxc_ "……话是这么说没错。"
    lxc_ "但你有时候，还真会说些让人意外的话呢……"
    "我用手背轻轻碰了碰自己的脸。"
    show sy clothes1_side2 cat_mouth skin_blush with dissolve
    sy_ "……哼哼，怎么样？是不是对本小姐有点心动了？"
    "虽然她语气装得游刃有余，但我注意到她耳尖已经微微泛红了。"
    lxc_ "既然自己都会害羞，就不要强行说这种话了。"
    "我伸手，轻轻弹了下她的额头。"
    show sy oo skin_blush kp13wl at emphasis_pop
    sy_ "……可恶！"
    "她鼓起脸颊，一副不服气的样子。"
    show sy oo skin_blush hide_fx with dissolve

    scene bg_shop_6
    with fade
    show bg_shop_6:
        zoom 1.04
        xalign 0.45
        yalign 1.0
    with dissolve

    show sy clothes1_front1 smile at left
    show syq_ clothes2_front smile at right

    tz_ "两位好，这是我的作品，请问有兴趣拿一本样本看看吗？"

    "或许是因为我们在摊位旁站了有一会儿，摊主主动向我们打了招呼。"
    lxc_ "啊，好的，谢谢。"
    "我从对方手里接过两本样刊，和时语一起翻看。"
    "画中是少女独自仰望星空的场景。"
    "线条细腻，用色温柔，光影处理得尤其生动——从我的经验看，这至少是商业插画的水准。"
    "S.Y.Q……这好像是个挺有名的画师，难怪刚刚有那么多人在排队。"
    "要不买一本回去好了——正当我这么想时，口袋里的手机忽然响了。"
    lxc_ "……时间到了。"
    lxc_ "我去一趟洗手间，你留在这儿继续看看画册？"
    sy_ "嗯，可以呀。"
    lxc_ "别乱跑哦？"
    show sy clothes1_front1 smile at nod_small
    sy_ "知道啦，我又不是小孩子。"
    "她头也没抬，只是朝我摆了摆手，眼睛还专注地盯着手里的画册。"
    "嗯，快去快回吧。"

    scene bg_shop_6
    with fade
    show bg_shop_6:
        zoom 1.04
        xalign 0.45
        yalign 1.0
    with dissolve

    $ heroine = True
    $ heroine_name = "时语的视角"


    show syq_ clothes2_front smile at right
    show sy clothes1_front1 focus at left

    tz_ "怎么样？喜欢吗？"

    sy_ "……嗯？你、你是在和我说话吗？"
    "我还沉浸在画册所描绘的画面里，摊主突然的搭话让我回过神来。"
    show syq_ clothes2_front calm with dis_master
    tz_ "对呀，现在摊位前就剩你在看了。"
    tz_ "唔，忙了这么久，总算能稍微喘口气了。"
    "对方是个和我身高差不多的女生，穿着一身小恶魔般的洋装。"
    "什么嘛，人类里不也有和我体型差不多的人吗？林小凑那家伙还老说我的外表会很显眼……"
    show sy clothes1_front1 calm with dis_master
    sy_ "画得不错。虽然本小姐……咳咳，虽然我对绘画不算特别了解，但从笔触能看出你画得很用心。"
    tz_ smile_close "谢谢夸奖~要买一本正式版的画册吗？里面的内容比样刊更丰富哦？" with dissolve
    "对方很自然地推销起自己的作品，该说是对作品很有自信吗？"
    "我看了眼标价，并不贵。"
    show sy smile with dis_master
    sy_ "那麻烦给我拿两本……不，一本就好。"

    tz_ wink "我倒是不介意，不过不帮刚刚那位先生也带一本吗？" with dissolve

    sy_ clothes1_side1 smile "反正拿回去也是一起看，一本就够了。" with dissolve
    "……还能省点钱。"
    show syq_ clothes2_front laugh_open with dis_master
    tz_ "哎~好像听到了什么有意思的事情呢。"

    tz_ cat_mouth "……是男朋友？" with dissolve

    show sy shy skin_shy kp15wl with dis_master
    sy_ "……！你、你在说什么呀！"
    "这摊主怎么一副自来熟的样子？！"
    show syq_ clothes2_front cachinnation with dis_master
    tz_ "从你刚刚说的话，还有你们两人之间的气氛来看，怎么也不像普通朋友吧？"

    sy_ shy skin_blush hide_fx "虽然是这样没错……但我们还不是那种关系……" with dissolve
    show syq_ clothes2_front surprised_but with dis_master
    tz_ "还不是？"
    "她敏锐地捕捉到了我的用词，笑容里多了点玩味。"
    show syq_ clothes2_front laugh_open with dis_master
    tz_ "那就是快要是了？"

    show sy shy at shy_shrink
    sy_ "……我、我不知道你在说什么！"
    "我抬脚想走，可想起林小凑离开前的叮嘱，迈出去的步子又收了回来。"
    "在别人看来，我肯定像个在原地打转的笨蛋吧……可恶，他怎么还不回来！"
    show syq_ clothes2_front smile_close with dis_master
    tz_ "咳咳，好像有点捉弄过头了呢。"

    tz_ calm "我只是想说，感情这种事啊，很容易转瞬即逝的。" with dissolve
    tz_ "要是不好好把握住，说不定就会错过了哦？"

    sy_ clothes1_side1 bewilderment skin_blush "……" with dissolve
    "是啊，我和他相识也不过短短几个月。"
    "无论是在他的人生里，还是在我漫长的岁月中，都只是一小段时光。"
    "如果发生什么意外……"
    show sy clothes1_side1 focus with dis_master
    sy_ "……我和你只是陌生人吧，为什么要对我说这些？"

    tz_ clothes2_front smile_close "唔……大概是因为看到你们的样子，不自觉地想起了自己和男朋友的经历吧。" with dissolve

    tz_ clothes2_front smile "而且，既然你喜欢我的画，那就是我的粉丝了。" with dissolve
    tz_ "给自己的粉丝一点小小的鼓励，不是理所当然的嘛？"

    sy_ sigh "……真是个奇怪的人呢。" with dissolve

    sy_ clothes1_front1 smile "不过，谢谢。我会好好想想接下来该怎么做的。" with dissolve

    tz_ clothes2_front smile_close "不客气，能帮到你就好~" with dissolve
    "其实我心里早就清楚自己的心意了。"
    "我或许……只是在等一个合适的契机，一个能让我鼓起勇气的时机。"
    "但机会不会一直主动找上门，如果自己不做点什么的话。"
    show syq_ clothes2_front focus with dis_master
    tz_ "说起来，你今天这身打扮真好看……是原创角色的COS吗？设计细节做得好精致。"

    tz_ clothes2_front surprised_but "是在哪家店买的？还是说是请人专门定做的？" with dissolve

    sy_ bewilderment "这、这个是……" with dissolve
    "我不知道该怎么解释，面对她直率而好奇的目光，一时语塞。"
    "林小凑……你快点回来啊！"

    call achievement (22) from _call_achievement_12


    scene bg_shop_6
    with fade
    show bg_shop_6:
        zoom 1.04
        xalign 0.45
        yalign 1.0
    with dissolve

    $ heroine = False
    show sy clothes1_front1 sigh at center with dissolve

    lxc_ "我回来了……你怎么一脸疲惫的样子？"
    sy_ "别说了……你怎么去了那么久？"
    lxc_ "稍微绕了点路，去取了这个。"
    "我亮出手里的两张票。"
    show sy oo kp1wl at emphasis_pop
    sy_ "《猛汉》现场试玩票……？！这么多人，你怎么拿到的？！"
    lxc_ "有个认识的同学正好在展馆这边工作，我拜托他在人少一点、有空档的时候通知我。"
    lxc_ "这样我们就不用去排那条长队了。"
    show sy clothes1_front1 laugh_open hide_fx with dissolve
    sy_ "喔喔！太好了，终于能去玩了！"
    show sy laugh_open at celebrate_jump
    sy_ "那我们快点过去吧……等等，你刚才为什么不直接带我去取票？那样不是更快吗？"
    lxc_ "毕竟解释起来有点麻烦嘛……而且我也不太想让他见到你。"
    "我移开视线，看向旁边的人群。"
    show sy clothes1_side1 cat_mouth skin_blush with dissolve
    sy_ "欸~你还有这种想法啊？"
    show sy clothes1_side1 cat_mouth skin_blush at lean_in
    "她似乎察觉到了什么，轻轻伸出手指，在我心脏的位置轻轻画了个圈。"
    sy_ "是莫名其妙的占有欲？"
    lxc_ "……我不否认。"
    "话说回来，她什么时候变得这么大胆了？在这么多人面前也做这么亲昵的动作……"
    show sy cat_mouth skin_blush with dissolve
    sy_ "哼哼，是吗？毕竟是本小姐，你会这么想也很正常嘛。"

    scene cg7 with dissolve

    "她似乎对我的回答很满意，顺势挽住了我的手臂。"
    show sy clothes1_front1 smile skin_blush:
        yoffset 5000
    with dissolve
    sy_ "但你还真是笨呢，我们现在过去不也有可能会被他看到嘛~"
    sy_ "既然早晚都会被看到，还不如大大方方地被人看见呢。"
    show sy smile_close skin_blush with dissolve
    sy_ "快点过去玩吧，我等这个试玩等好久了！"
    lxc_ "……嗯，我也挺想试试新作的。"


    scene bg_shop_6
    with fade
    show bg_shop_6:
        zoom 1.04
        xalign 0.45
        yalign 1.0
    with dissolve

    "最后，在试玩时间结束前，我们都一直留在试玩机前。"
    "虽然试玩版的画面色调还有点灰蒙蒙的，帧数也不是特别稳，但毕竟只是测试版本。"
    "我和时语都相信，等正式版出来，一定和以前的版本一样好玩。"
    "真期待正式版发售的那天啊。"


    call achievement (9) from _call_achievement_13



    scene bg_sky_5
    with Fade(0.5, 0.5, 0.5)

    "我们并肩走在回家的路上，夕阳的余晖为她的银发镀上了一层浅浅的金色。"
    "她开心地走在我身旁，似乎还在回味着刚刚游戏的体验，嘴角一直微微上扬。"
    "而我忽然觉得，或许不止是游戏——"
    "和她在一起的每一天，也都让人忍不住开始期待明天。"

    play music bgm_13 fadeout 1.0 fadein 1.0
    scene bg_living_room_2
    with Fade(0.5, 0.5, 0.5)


    $ heroine = True
    $ heroine_name = "时语的视角"


    show sy clothes1_front1 shy skin_blush at center with dissolve

    "自从我们从漫展约会回来，已经过去整整一周了。"
    show sy shy skin_blush kp17wl at emphasis_pop
    "我决定——今天就向林小凑告白！"
    "为了这件事，这一周我做了好多好多准备。"
    "比如写信告诉家族那边，我决定在表世界长住了……要是他们敢来找麻烦，我就把他们通通打回去！"
    show sy clothes1_front1 pout skin_blush hide_fx with dissolve
    "还拜托了星弥，让她通过魔女会的渠道帮忙查资料，找到了把人类转化成眷属的方法。"
    "她还在信末贴心地补充一句「 林先生一定会愿意的！ 」。"
    "真是的！我明明从来都没说过要对谁这么做呀！"
    "最后，我还偷偷上网搜了「 怎么告白比较自然 」「 约会后该如何推进关系 」……查完后还要慌张地删掉浏览记录，生怕被他发现。"
    "总之，该做的准备都做了，该有的心理建设也完成了。"
    show sy shy skin_blush with dissolve
    "剩下的……就只有「 鼓起勇气，踏出那一步 」了。"
    "虽然我早就喜欢上他了，也能感觉到他应该也喜欢我……"
    "可一想到真的要告白，还是会忍不住心跳加速、脸颊发烫。"
    "毕竟在这三百年里，我从来没做过类似的事啊……"
    "偏偏他今天早上说有事，提着笔记本电脑就出门了。"
    show sy pout skin_blush at angry_stomp
    "可恶，就不能体谅一下少女心，早点回来嘛！"
    lxc_ "我回来了——"
    show sy oo kp1wl at shocked_step_back
    sy_ "喵呀！"
    lxc_ "……怎么一回来就发出怪叫。"
    show sy pout skin_blush kp13wl at angry_stomp
    sy_ "都怪你回来得这么突然！"
    show sy pout skin_blush hide_fx with dissolve
    lxc_ "这不能怪我吧？事情刚做完，就想着早点回来嘛。"
    show sy clothes1_side1 pout skin_blush with dissolve
    sy_ "哼。"
    lxc_ "今天怎么穿回这身衣服了？"
    show sy clothes1_side1 shy skin_blush with dissolve
    sy_ "……心情好，就想着穿一下，不行吗？"
    lxc_ "当然可以，不如说……嗯，挺好的，穿起来和以前一样好看。"
    sy_ "……"
    "看着他那张和平时没什么两样的脸，我心里那股既紧张又期待的情绪又翻涌起来。"
    "……不就是告白嘛，按计划行动就好了！"
    "在心里给自己鼓足劲后，我深吸一口气，开口了。"
    show sy clothes1_front1 focus with dissolve
    sy_ "林小凑。"
    lxc_ "嗯？"
    show sy shy skin_blush with dissolve
    sy_ "我、我对你——"
    lxc_ "说起来，我这里有个新游戏你要玩吗？"
    "他突然凑过来，让我不自觉地心跳加快。"
    show sy oo skin_blush kp1wl at emphasis_pop
    sy_ "欸？但、但是我……"
    lxc_ "玩一下试试吧，这个是……独立游戏界一个叫XL的新人做的。"
    "他的语气带着点请求的意味，让我原本到了嘴边的话又咽了回去。"
    show sy clothes1_side1 sigh hide_fx with dissolve
    sy_ "……好吧。"
    "他把U盘插在电脑上，屏幕上显示出一个红色龙头的文件。"
    show sy clothes1_front1 focus with dissolve
    sy_ "是双人游戏？"
    lxc_ "不，应该算是文字冒险类吧。"
    "他把手柄递给我，很自然地坐在沙发另一头，和我隔了小半个人的距离。"
    "……也不用坐这么远吧。"
    "看到他这样的举动，刚刚激动的心情稍稍平复了一些。"
    show sy clothes1_front1 smile with dissolve
    sy_ "既然是你推荐的游戏，那我就试试看吧。"
    "……可恶，明明今天计划要告白的。"
    "游戏开头的剧情简单又有点套路。"
    "孤独的主角在旅途中意外穿越到异世界的城堡，而城堡的主人是一位神秘的吸血鬼。"
    "无家可归的主角只好留在城堡里生活。"
    show sy clothes1_side1 focus with dissolve
    sy_ "这设定……和之前那部电影有点像呢。"
    lxc_ "是啊，说不定作者就是从那里取材的。"
    "游戏玩法很简单，玩家需要探索城堡，了解这里的事物，并提升其他人对自己的好感。"
    "起初主角对一切都感到害怕，未知的事物让他十分恐惧。"
    "但随着在城堡生活的时间变长，他和蝙蝠怪、南瓜灯渐渐熟络起来，和那位看似高冷的吸血鬼城主也走得越来越近。"
    show sy clothes1_front1 focus with dissolve
    sy_ "这游戏细节做得还不错嘛，虽然画面简单，但提升好感时的画面、台词、音效反馈都挺用心的。"
    sy_ "就是这城主的人设……白长发、黑礼服，而且也是吸血鬼。"
    show sy pout at angry_stomp
    sy_ "怎么和我这么像啊！明明是我先的！"
    lxc_ "……这个嘛，只是巧合而已吧。"
    "随着剧情推进，主角发现眼前的吸血鬼少女并不像表面看上去那么完美。"
    "她有很多不擅长的事，也有很多弱点，但她依然选择努力做好自己，默默维护着城堡里的一切。"
    "在与她相处的日子里，主角有时会被她的处事风格折服，有时也会因为她偶尔的笨拙而哭笑不得。"
    "渐渐地，主角心里萌生了不一样的情感。"
    "他喜欢上了城堡里的少女，想为她做点什么，想一直陪在她身边。"
    show sy clothes1_front1 focus with dissolve
    sy_ "……"

    scene bg_living_room_2
    with Fade(0.5, 0.5, 0.5)

    $ heroine = False
    show sy clothes1_front1 focus at center with dissolve

    "我坐在时语身旁，看着她玩我做的游戏，自己的心跳声格外地清晰。"
    "游戏剧情推进到城里的魔法师找上主角，告诉他找到了返回地球的方法。"
    "城堡主人知道这件事后，变回最初高冷的模样，将主角逐出城堡，要他立刻返回原本的世界。"
    "但主角拒绝了。他在这里还有必须完成的事。"
    "终于到了剧情的高潮——雨夜中，主角与吸血鬼对峙，紧接着就该是主角鼓起勇气告白的场景了……嗯？画面怎么不动了？"
    show sy shy with dis_master
    "我转头看向时语，发现她正一动不动地盯着我。"
    lxc_ "怎么了？"
    "她没有回答，只是用难以捉摸的表情看着我。"
    "……难道她发现了？"
    "不，就算她猜出游戏是我做的，应该也想不到后面的具体内容吧？"
    show sy clothes1_side1 calm with dissolve
    sy_ "……你过来一点。"
    "她拍了拍身边的位置。"
    lxc_ "再过去就很挤了哦？"
    show sy clothes1_side2 cat_mouth skin_blush with dissolve
    sy_ "有什么关系嘛，你不过来我就过去了。"
    lxc_ "……好吧。"
    "原本的计划是等她玩完游戏的……现在只能硬着头皮上了。"
    "唉，怎么偏偏卡在这么尴尬的地方……"
    "我原本的安排，就像现在的游戏进度一样，被意外打断了。"


    show sy:
        zoom 1.2
        yoffset 500
    with dissolve

    "我慢慢挪到她身旁，直到我们几乎肩贴着肩。"

    "此刻，我们之间的气氛，就像屏幕上暂停的画面——主角与城主在雨中对峙。"
    "为了推进「 剧情 」，我决定先开口。"
    lxc_ "……不继续玩了吗？"
    show sy clothes1_side1 smile skin_blush with dissolve
    sy_ "先等等……你看，那个像月亮的东西是什么？"
    lxc_ "月亮？画面中是雨夜场景，根本没有月亮啊。"
    lxc_ "你是不是看错了……"

    show sy:
        zoom 1.9
        yoffset 2300
    with dissolve


    "我转头看向她，却发现她已经凑到了我面前。"
    show sy clothes1_side1 smile skin_blush at look_away_small
    "红色的眼眸里映着我的倒影，微微湿润的嘴唇弯成了一道小小的月牙。"
    "啊……原来月亮，就在我眼前啊。"
    "我正有些出神，她轻声开口了。"
    show sy shy skin_shy with dissolve


    sy_ "……讨厌你。"
    lxc_ "欸？"
    show sy smile_close
    with dissolve

    show sy smile_close skin_shy:
        ease 0.3 zoom 2.2 yoffset 2800
    pause 0.3
    show sy smile_close skin_shy:
        ease 0.3 zoom 1.9 yoffset 2300

    "还没等我理解这句话的意思，唇上就传来了柔软的触感。"

    show sy shy
    with dissolve

    sy_ "但是我也好喜欢你。"
    "与其说是吻，不如说是牙齿和嘴唇撞在了一起——我的上唇好像还被她磕破了一点。"
    "但我确实感觉到了，那份生涩、却又无比真实的触碰。"
    show sy smile_close skin_blush:
        zoom 1.2
        yoffset 500
    with dissolve
    "还没等我反应过来，她已经退了回去，得意地擦了擦嘴唇，似乎很满意自己这次的偷袭。"
    lxc_ "你……"
    "她的举动让我有点发懵，原本的计划全被打乱，脑子里一片空白。"
    show sy clothes1_front1 pout skin_blush with dissolve
    sy_ "……区区人类，竟然还想抢在本小姐之前告白！哼，讨厌！"
    show sy clothes1_side1 pout skin_blush at look_away_small
    "她的呼吸有点凌乱，胸口微微起伏，看来是情急之下才这么做的。"
    lxc_ "……原来你刚刚说的是这个意思。"
    lxc_ "我……我还以为自己藏得挺好的。"
    "她刚才的举动和话语带来的冲击有点大，我连说话都有点结巴。"
    show sy clothes1_side2 cat_mouth skin_blush with dissolve
    sy_ "做得这么明显，我怎么可能看不出来……那两个主角的原型不就是你和我嘛。"
    sy_ "你之前『 加班 』，都是为了偷偷做这个游戏吧？"
    lxc_ "是啊，本来想着给你个惊喜的。"
    show sy clothes1_side1 shy skin_blush with dissolve
    sy_ "刚刚还说什么这游戏是新人XL做的，那不就是你名字『 小林 』的缩写嘛……"
    lxc_ "呃……创作者有几个马甲还挺正常的，对吧？"
    show sy clothes1_front1 shy skin_blush with dissolve
    sy_ "哼……"
    "她嗔怪地瞪着我，脸蛋红扑扑的，我猜自己的脸大概也差不多。"
    lxc_ "所以，你……也喜欢我？"
    show sy astonished skin_blush kp1wl at look_at_left
    sy_ "『 也 』是什么意思啊……我都愿意一直留在你家了，除了喜欢你，还能有什么别的原因吗？"
    lxc_ "啊……不是不是，我的意思是，我也一样。"
    show sy astonished skin_blush hide_fx with dissolve
    "看着她害羞又无比认真的样子，我逐渐恢复平时的理智。"
    lxc_ "我做这个游戏，就是想告诉你——哪怕我们的处境对调，哪怕是我去了里世界……"
    lxc_ "我也一定会因为你，而选择留在那里，留在你身边。"
    lxc_ "我喜欢你，时语。"
    show sy shy skin_shy at look_at_right
    "我认真地说出了这句告白。"
    "虽然她原本脸就很红，但听完这句话后，连脖子和耳根都红透了。"
    show sy shy skin_shy at look_away_small
    sy_ "……你什么时候喜欢上我的？"
    lxc_ "这个……其实我自己也不太确定。"
    lxc_ "一开始只是把你当作一起打游戏的宅友。"
    lxc_ "但相处久了，我发现了你的很多优点，也觉得你越来越可爱。"
    lxc_ "我慢慢开始习惯，有你陪着自己一起打游戏的日子。"
    lxc_ "大概就是这样，不知不觉就喜欢上你了。"
    show sy smile_close skin_blush with dissolve
    sy_ "……哦。"
    "她不自觉地用手指卷着发梢，目光一会儿飘向旁边，一会儿又忍不住偷偷瞄回来。"
    lxc_ "那你呢？你是什么时候喜欢上我的？"
    show sy clothes1_side1 shy skin_shy at look_away_small
    sy_ "我……不要问我这么难为情的问题啦。"
    lxc_ "只有我一个人说了，会不会有点不公平呢？"
    sy_ "……讨厌。"
    "虽然她一副不情愿、很害羞的样子，最后还是老老实实地说了出来。"
    show sy clothes1_front1 shy skin_blush with dissolve
    sy_ "……和你一起生活、打游戏、约会，互相帮忙，甚至斗嘴，每件事都让我很开心。"
    sy_ "但最让我在意的，是你对待我的态度。"
    sy_ "你不会因为我是血族就有奇怪的想法，也不会刻意讨好我或疏远我。"
    sy_ "渐渐地，我就被这样的你所吸引了。"
    sy_ "等回过神的时候，『 想和这个人一起生活下去 』的念头，就已经在心里扎根了。"
    lxc_ "这样看来，我们是两情相悦呢。"
    show sy clothes1_front1 smile skin_blush with dissolve
    sy_ "……嗯。是啊。"
    show sy smile_close skin_blush with dissolve
    sy_ "那，我们现在就是恋人了？"
    lxc_ "应该是吧？"
    show sy clothes1_side2 cat_mouth skin_blush with dissolve
    sy_ "那……要不要来做点恋人之间才能做的事？"

    lxc_ "欸？"
    "这、这么直接吗？时语平时是这样的性格吗？"
    "虽然说恋爱会使人盲目，但不管怎么说……"
    show sy shy skin_shy at look_away_small
    sy_ "不愿意吗？"
    lxc_ "……倒没有，只是觉得有点突然。"

    jump story_826_part3
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
