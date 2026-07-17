


label story_826_part4:



    play music bgm_19 fadeout 1.0 fadein 1.0
    scene bg_living_room_2
    with fade
    show bg_living_room_2:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve
    $ heroine = False

    "窗外天色越来越暗，乌云低垂，空气里弥漫着潮湿的味道。"
    "……看来真的要下雨了。"
    "我一边把晾在阳台的最后一件衬衫收下来，一边有些心不在焉地自言自语。"
    "这已经是我今天第三次收衣服了。"
    "收下来觉得还能再晾会儿，挂回去；过会儿看天色不对，又收下来……如此反复。"
    "……哎，其实我只是想找点事做，缓解心里的忐忑。"
    "也不知道星弥考虑得怎么样了……她在房间里待了快一个小时，一点动静都没有。"

    show bg_living_room_2:
        zoom 1.08
        xalign 0.5
        yalign 1.0
    with dissolve

    lxc_ "星弥，你还好吗？准备下雨了，记得关窗哦。"
    "我最后还是没忍住，轻轻敲了敲星弥的房门。"
    "没有回应……睡着了？"
    lxc_ "星弥？我进来咯？"
    "门没锁。我轻轻推开门——"

    scene bg_bedroom_3
    with fade

    "房间里空无一人。"
    play music bgm_3 fadeout 1.0 fadein 1.0
    "不好的预感涌上心头，我快步走进去，发现桌上盖着一张纸条。"
    xm_ "林先生："
    xm_ "我真的很喜欢您送我的礼物。"
    xm_ "但是，对不起，我需要一个人冷静一下，理清自己的想法。不用担心我，我很快就会回来的。"
    xm_ "星弥。"

    "明明还没下雨，但纸条上却有明显的水痕，像是被什么打湿过。"
    "我送的那束白色满天星和星星手链，都完好地放在旁边，她一样都没带走。"
    "窗外的风吹进来，带着雨前特有的凉意。"
    lxc_ "……真是的，一个两个都不好好从正门走。"


    scene bg_sky_2
    with fade

    "雨开始下了，虽然不大，却让人觉得有点厌烦。"
    "虽然很着急，但越是这种时候越要冷静。"
    "星弥突然离开，一定是发生了什么。"
    "……会和那封信有关吗？"
    "明明是寄到我家的信，却写着给星弥……我该多留个心眼的。"
    "现在想来，我选择今天告白，时机可能真的不太好。"
    "——不，这些都不是关键，眼下最重要的是找到她。"
    "她是魔女，如果真的想躲起来，我肯定找不到。"
    "但她留下了纸条，说明她希望被我找到。"
    "既然如此，那她应该不会走太远。"
    "离家不算远，还容易被人找到的地方……只有那里了吧。"


    scene cg9
    with Fade(0.5, 0.5, 0.5)

    play music bgm_19 fadeout 1.0 fadein 1.0
    $ heroine = True
    $ heroine_name = "星弥的视角"

    show xm clothes2_side1 sigh:
        yoffset 5000

    "失败了。"
    "明明是我最熟悉、最擅长的魔法，这次却彻彻底底地失败了。"
    "占星术占卜的结果，是一片空白。"
    "不管是自己对林先生的感情，还是接下来该怎么做，魔法都没有给我任何回应。"
    "无论尝试多少次，无论多么努力地集中精神，魔法阵总是在即将完成时消散了。"

    show xm bewilderment
    show cg91 with dis_master
    xm_ "……为什么会不行呢。"

    "我坐在逐渐潮湿的秋千上，小声地问着没有答案的问题。"



    show xm clothes2_side1 bewilderment

    xm_ "林先生……"

    "我就这样跑出来，他肯定会担心的。"
    "唉……我真是越来越弄不懂自己了。"
    "这样的我，在别人眼里，大概很像一个在闹别扭、不懂事的小孩子吧？"
    "哪怕按年龄算，我比许多表世界的人都要年长，可说到底，我只是个和外表一样不成熟的魔女而已。"

    show xm cry
    hide cg9
    show cg9 with dis_master
    "……是啊，无论我怎么逞强，怎么努力，最后好像还是什么都做不好。"

    show xm cry skin_cry at shy_shrink
    "正是因为我不够成熟，不够可靠，连自己最依赖的魔法，这次都选择「 抛弃 」我了吗？"

    show xm cry skin_cry with dissolve
    "在里世界，我是个除了魔法几乎一无是处的魔女。"
    "遇到的几乎所有难题，我都会下意识地用魔法去解决。"
    "而在这里，在表世界，在林先生身边，我好像变成了一个没有他就什么都做不好的人。"
    "不会用那些方便的电器，做家务总是笨手笨脚搞砸，现在甚至连自己的心情都弄不明白。"

    "这样的我……真的有资格，接受林先生那份真诚的喜欢吗？"

    "冰凉的雨点落在脸上，像是天空也在嘲笑我的狼狈和不堪。"
    "……我明明离那份温暖那么近，明明有机会握住那只伸向我的手，却因为自己的懦弱、胆怯，还有自卑，亲手把他推开了。"
    "……不，说到底，是我先对他有所隐瞒，是我先用虚假的理由留在他身边。"
    "现在有这样的结果，或许只是我应得的吧。"



    "——就在我快要被自责的情绪淹没时，头顶忽然感觉不到冰凉的雨滴了。"

    lxc_ "真巧，你也在这里躲雨？"
    lxc_ "不过啊，下雨了还在公园玩秋千，可是会很容易感冒的。"

    show cg92 with dis_master
    xm_ focus skin_blush "啊……" with dissolve

    "这声音，这语气……"
    "如同阴郁雨幕中忽然照进来的光，如同寒冷冬日里适时递来的温暖。"

    "那个让我心乱如麻、却又无比想念的，熟悉而可靠的身影，就这样撑着伞，出现在了我的身旁。"

    scene bg_sky_2
    with Fade(0.5, 0.5, 0.5)

    $ heroine = False



    "雨越下越大了。"
    "我小跑着冲进公园，远远就看到秋千架下那个小小的身影。"


    scene cg912
    with Fade(0.5, 0.5, 0.5)

    "她坐在湿漉漉的秋千上，没有撑伞，也没有用魔法挡雨。"
    "雨水打湿了她的棕色长发，一缕缕地贴在苍白的脸颊上。"

    "看到她这副样子，我有点心疼，但还是压抑住情绪，快步走过去，把伞举到她头顶。"
    lxc_ "真巧，你也在这里躲雨？"

    show cg9 with dis_master

    "她抬起头，绿色的眼睛湿漉漉的，分不清是雨水还是泪水。"

    lxc_ "不过啊，下雨了还在公园玩秋千，可是会很容易感冒的。"

    show xm clothes2_side1 shy:
        yoffset 5000

    show cg93 with dis_master

    xm_ "啊……林、林先生……"

    "或许是从我的眼神中看出了自己的窘态，她赶紧用袖子擦了擦脸。"

    show xm sigh
    show cg94 with dis_master

    xm_ "我——"
    lxc_ "原来你说的『 冷静 』一下，是这么一回事啊。"
    "我伸手擦掉她脸上剩下的水珠，轻轻弹了下她的额头。"
    lxc_ "嗯，用雨水来冷静自己，确实是星弥才会有的想法。"
    xm_ "我……我不是……"
    lxc_ "那难道是因为刚刚的秋千还没玩够？"
    lxc_ "早知道你这么喜欢，就该让你多玩一会儿的。"

    show cg95 with dis_master
    show xm calm
    xm_ "……"
    "看到她欲言又止的样子，我也不忍心逗她了。"
    lxc_ "开玩笑的。"
    xm_ "……嗯，我知道。"
    "之后，我没有再说话，只是静静地站在她身边，陪她一起看雨。"
    "雨声淅淅沥沥，整个世界只剩下我们两个人。"



    xm_ "林先生……您没有什么要问我的吗？"
    "过了好一会儿，她才小声地开口。"
    lxc_ "有啊，我有很多想问的。"
    lxc_ "比如到底发生了什么，为什么突然跑出来，又为什么一个人掉眼泪……"
    lxc_ "我甚至想敲一敲你的小脑袋，看看里面到底装了什么，才会做出这么让人担心的事。"
    lxc_ "——但我放弃了，有些事，或许等你自己愿意说出来，会更好吧。"

    show xm sigh
    hide cg94
    show cg94 with dis_master

    xm_ "我、我脑袋里本来就空空的……就算您敲了，也找不到答案的……"
    lxc_ "……我在开玩笑啦。"
    xm_ "我知道。"

    show xm shy
    hide cg9
    show cg9 with dis_master

    xm_ "但我怕……自己要是再不回应的话，您是不是就会从我身边消失了。"
    lxc_ "……明明是我担心你会消失才对。"
    lxc_ "突然就跑出来，还不带伞，我会很担心的。"
    xm_ "……对不起。"
    lxc_ "嗯，知道错就好。作为道歉的诚意，把手伸出来吧。"

    show xm bewilderment skin_blush
    show cg96 with dis_master

    "她迟疑了一下，还是乖乖伸出手，手心向上——大概以为我要打她手心惩罚她。"
    "但我想做的，只是握住她的手而已。"
    "小小的，凉凉的，还在微微发抖。"
    lxc_ "在这场雨停之前，我哪里都不会去的。"

    show xm astonished
    show cg97 with dis_master

    xm_ "……欸？"
    "她有点惊讶地抬起头。"

    lxc_ "怎么，你以为我要打你手心？"
    hide cg94
    show cg94 with dis_master
    xm_ sigh "嗯……" with dissolve
    lxc_ "你又不是小孩子，打手心多丢人。"

    xm_ "……可我现在的样子，正常人都会觉得是小孩子吧。"
    xm_ "不管是因为魔法意外导致的外貌，还是内心那些幼稚的想法，我都还远远算不上一个大人……"
    lxc_ "……"
    lxc_ "可就算是大人，内心也一样会有幼稚，天真，不成熟的想法啊。"
    lxc_ "会看气氛说话、会照顾人，对喜欢的东西会有克制的想法……我倒觉得，你比很多大人都要成熟。"

    show xm shy
    hide cg9
    show cg9 with dis_master

    xm_ "但、但是我，只是因为接受不了魔法失败，就离家出走……"
    lxc_ "你以为大人就不会这样子吗？"
    "我笑了笑。"
    lxc_ "大人也会有失败的时候，也会心情不好、钻牛角尖啊。"
    lxc_ "就比如说，你眼前的这个『 大人 』。"
    lxc_ "曾经刚毕业就失业，觉得自己前半生学的东西在社会上完全用不上。"
    lxc_ "那时候我也觉得天都塌了，觉得自己永远都找不到工作。"
    lxc_ "但最后……哈哈，还不是成了一个称职的社畜。"

    show xm bewilderment
    hide cg96
    show cg96 with dis_master

    xm_ "……林先生也会这样吗？"
    lxc_ "是啊。失败也好，心情不好钻牛角尖也好，都是人生常态。"
    "我握紧了她的手。"
    lxc_ "这和是不是大人、是不是小孩子，其实没有太大关系。"
    "星弥安静地听着，手指轻轻回握住我的手。"
    lxc_ "说到底，大人和小孩的界限，究竟是什么呢？"
    "我望向远方被雨幕笼罩的街景。"
    lxc_ "能被允许做更多的事，可以做小时候能做但不应该做的事，那就是大人吗？"
    lxc_ "我倒觉得，能承认自己的不成熟，然后愿意去尝试、去改变，才更像是大人的样子。"



    "星弥沉默了一会儿。片刻后，她抬起头，那双碧绿的眼睛在雨幕中显得格外清澈。"

    show xm shy skin_shy
    show cg98 with dis_master

    xm_ "林先生……你为什么要对我这么好呢？明明我……"
    lxc_ "因为我喜欢你啊。"


    xm_ "但是……真正的我，没有你想的那么好啊……"
    "她有些激动地晃了晃，秋千的铁链跟着发出轻微的响声。"


    xm_ "我最开始想留在你家里，不只是因为没有地方住。"
    xm_ "有些古老的血族，外貌是随着心理年龄变化的……而时语她，刚好就属于这一部分。"
    xm_ "她明明比我年长那么多，可看起来却像个小孩子……所以当她打算住在你家时，我就很担心。"
    xm_ "虽然时语说你身上有种让人安心的味道，但我还是放不下心来。"
    xm_ "所以，从那时起，我就一直……悄悄地戒备着你。"
    xm_ "一边装作乖巧的样子，一边了解这个世界，一边……留意着你的一举一动。"

    show xm sigh skin_blush
    hide cg94
    show cg94 with dis_master

    lxc_ "……"

    scene bg_living_room_1

    show xm clothes2_front2 calm at center
    show expression Solid("#ffa200") as yellow_tint:
        alpha 0.12
    with fade
    pause 0.5

    scene cg94
    with fade


    "原来是这样……"
    "怪不得刚开始和她相处时，她在家里也时不时拿着法杖。"
    "那时要是做了什么奇怪的举动，恐怕会被她用魔法制裁吧。"


    show xm shy skin_shy:
        yoffset 5000
    hide cg98
    show cg98 with dis_master

    xm_ "……但事实证明我错了。时语并不像我想象的那么天真。"
    xm_ "而愿意收留我们的您，也从未有过不好的想法。"
    xm_ "一切都只是我一个人……在胡思乱想罢了。"
    lxc_ "……所以，你对我用敬语，也是伪装的一环？"
    xm_ "最开始确实是这样……但后来，我是发自真心尊重您的。"
    "难怪她偶尔激动时，会忘记使用敬语。"
    lxc_ "那之后呢？你和我相处时的样子，都只是演技吗？"


    xm_ "……如果只是演技的话，我现在就不会这么烦恼了。"
    "她轻轻摇了摇头。"



    show xm bewilderment
    hide cg96
    show cg96 with dis_master

    "看着她这副样子，我反而忍不住笑了一下。"
    lxc_ "既然如此，那还有什么好烦恼的？"
    lxc_ "虽然最初的目的有所隐瞒，但也是出于善意的担心。除此以外，你从来没有欺骗过我什么。"
    lxc_ "最重要的是——你和我在一起时，那些开心的笑容都是真的，这样就够了。"
    lxc_ "你在里世界旅行了那么久，见过各种各样的人和事，对陌生人保持警惕是再自然不过的事。"
    "我松开一直握住她的手，轻轻拨了拨她那垂到额前的发丝。"
    lxc_ "倒不如说，你这么小心，反而证明了你是一个可靠的大人，不是吗？"

    show xm astonished
    hide cg97
    show cg97 with dis_master

    "她睁大眼睛，愣愣地看着我。"

    "接着，她慢慢低下头，肩膀微微颤动起来。"

    show xm shy skin_blush
    hide cg9
    show cg9 with dis_master

    xm_ "但是……我什么都做不好，还总是给您添麻烦……"
    lxc_ "人活在世上，哪有不给别人添麻烦的。"
    "我蹲下身，让自己的视线和她齐平。"
    lxc_ "而且你只是缺乏自信而已。"
    lxc_ "只要去做，很多事情都能做好的——做饭也好，家务也好，你最后不都做得挺棒的吗？"
    "我伸出手，轻轻地摸了摸她的头。"
    lxc_ "你已经很努力了。"



    xm_ "我、我……"
    "她扑进我的怀里，声音带着哭腔。"
    "雨突然变大了，硕大的雨声几乎盖过了一切。"
    "但在这喧嚣中，我还是听到了她那细微的抽泣声。"
    "我什么也没说，只是轻轻拍着她的背。"
    "过了好一会儿，雨声渐渐变小，她的哭声也渐渐停歇。"



    show xm sigh skin_blush
    hide cg94
    show cg94 with dis_master

    "她从我怀里抬起头，眼睛和鼻子都红红的，像只小兔子。"
    "在我松开她时，她还依依不舍地回握住我的手。"
    "虽然很轻，却没有放开。"

    show xm shy skin_shy
    hide cg98
    show cg98 with dis_master

    xm_ "……林先生您，真是个很奇怪的人呢。"
    xm_ "我自己纠结了那么久的事，在您眼里就好像没什么大不了一样。"
    xm_ "一般人听到这种事，第一反应都会生气吧？"

    show xm pout skin_blush
    show cg99 with dis_master

    "她认真地看着我，小嘴甚至还微微嘟了起来。"
    xm_ "您这么善良，在社会上可是很容易吃亏的。"
    lxc_ "这个嘛……其实我没你想的那么好，我也不是什么正经的好人。"
    xm_ "骗人，您这么说肯定是想安慰我。"
    lxc_ "真不是。"
    lxc_ "虽然我看起来像个好人，但其实……我会偷看你不经意间露出来的脖子。"

    show xm astonished
    hide cg97
    show cg97 with dis_master

    xm_ "……欸？"

    lxc_ "你刚洗完澡，头发湿漉漉地从我身边走过时，我也会偷偷闻你身上的香味。"

    "她的脸一下子变红了。"
    lxc_ "你给我膝枕的时候，我会悄悄感受你大腿的温度。"
    lxc_ "你坐在沙发上看书，脚丫轻轻晃来晃去时，我也会忍不住多看两眼……"

    show xm shy skin_shy
    hide cg98
    show cg98 with dis_master

    xm_ "等、等等！"

    "她慌忙抬起一只手，挡住了通红的脸。"
    xm_ "您、您真的会做这种事？！"
    lxc_ "是啊，我只是个普通人，有这些想法也很正常吧？"
    lxc_ "你连这一点都没看穿，我看你也不是很警惕我嘛。"


    xm_ "……！！"
    xm_ "我、我……"
    "她有些手足无措地看着我，可抓着我的那只手，却一点也没有松开。"
    lxc_ "觉得尴尬的话，也可以松手哦？"


    xm_ "不、不行！"
    "她反而握得更紧了，表情既认真又害羞。"
    xm_ "您想法这么坏……我得好好看着您才行！"
    xm_ "……林先生你就是，所谓的萝莉控吧？"
    lxc_ "没有啊，不要乱说啊……"
    "我心虚地避开了她的视线。"
    lxc_ "不过，刚才说的都是真话，我并没有你想象中那么好，所以——你会对我失望吗？"

    show xm smile skin_blush
    show cg910 with dis_master

    xm_ "……不会。知道您是这样的人之后……我反而觉得更亲近了。"
    lxc_ "嗯，我刚刚也是这么想的。"
    lxc_ "所以，哪怕曾经对我有所隐瞒，也不必一直放在心上。"
    "待人有礼，不代表内心没有自己的欲望。"
    "真诚待人，不代表内心没有自己的秘密。"
    lxc_ "毕竟，无论是魔女还是人类，其实都没什么不同嘛。"

    show xm smile_close
    show cg911 with dis_master

    xm_ "……嗯，我明白了。"
    xm_ "谢谢您，林先生。就算不用魔法，我也明白自己该怎么做了。"
    xm_ "真的……各种意义上都很感谢您。"



    "她抬起头，对我露出一个小小的、却无比真诚的笑容。"

    show xm smile
    hide cg910
    show cg910 with dis_master

    "雨停了。"
    "天空露出清澈的蓝色，远处的阳光把湿漉漉的地面照得闪闪发亮。"
    lxc_ "不客气。那，我们回家？"

    call achievement (15) from _call_achievement_19


    xm_ "嗯。不过……在那之前，您看。"
    "她松开手，指了指我的身后。"

    scene bg_park_4
    with dissolve

    "我回过头，公园远处的天空，正挂着一道淡淡的彩虹。"
    lxc_ "真美啊。"

    xm_ clothes2_front3_no shy skin_shy "这边……其实也有一道哦？"
    lxc_ "真的？"

    scene black
    with ImageDissolve("rule/eyeclose.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)
    scene bg_park_4
    with ImageDissolve("rule/eyeopen.jpg", 0.5,ramplen=256,mipmap=True,reverse=True)
    show xm clothes2_front3_no smile skin_shy at center:
        zoom 1.5
        yoffset 1300
    with dissolve

    pause 0.3

    show xm smile_close:
        ease 0.3 zoom 1.9 yoffset 2000
    pause 0.3
    show xm smile:
        ease 0.3 zoom 1.5 yoffset 1300

    "我转回来，然后，唇上就传来了柔软而温暖的触感。"
    lxc_ "……！"

    show xm shy skin_shy at center with dissolve

    "星弥轻轻踮起脚尖，在我嘴唇上飞快地碰了一下，又迅速退开。"
    xm_ "这、这可是魔女的诅咒哦？"
    xm_ "中了这个，你就永远都是我的人了……"
    "她的脸已经红透了，却还强装镇定地解释着。"
    lxc_ "……"
    "我愣在原地，感觉自己的脸也有点发烫。"
    xm_ "你、你倒是说点什么呀……我第一次做这种事，也不知道做得对不对……"
    lxc_ "……我也是第一次。所以……可以再来一次吗？"
    lxc_ "刚刚有点太快了，我还没好好感受到。"


    show xm smile skin_blush with dissolve

    xm_ "真、真拿你没办法呢……"

    show xm smile_close skin_blush with dissolve

    "她闭上眼睛，微微仰起了脸。"
    xm_ "我喜欢你，林小凑。"
    lxc_ "我也喜欢你，星弥。"
    "我俯下身，轻轻吻住她。"

    show bg_park_4:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    show xm:
        zoom 1.7
        yoffset 1700
    with dissolve
    "这次，不再是一触即离，而是温柔地、小心翼翼地互相触碰。"

    pause 1.0



    stop music
    scene black with fade

    $ renpy.block_rollback()
    if persistent.ed_2_watched:
        $ renpy.movie_cutscene("images/ed2.webm")
    else:
        $ _skipping = False
        $ _rollback = False
        show expression Movie(play="images/ed2.webm", size=(2560, 1440),loop=False) as ed_2_movie
        $ renpy.pause(112.7, hard=True)
        hide ed_2_movie
        $ _rollback = True
        $ persistent.ed_2_watched = True
        $ _skipping = True



    $ persistent.gallery_unlocked = True

    $ persistent.route_xingmi_done = True


    scene bg_sky_3
    with Fade(0.5, 0.5, 0.5)

    play music bgm_14 fadeout 1.0 fadein 1.0
    "和星弥正式交往之后，我们的日常似乎没什么不同，依旧平稳而温和。"
    "没有什么惊天动地的展开，也没有戏剧般的波折。"
    "不过，这当中确实发生了一些细微的改变。"


    scene bg_living_room_2
    show bg_living_room_2:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with fade

    show xm clothes2_front3_no smile at center with dissolve

    xm_ "啊，小凑，你回来了！"
    show xm laugh_open at bounce_small
    xm_ "抱抱~"
    "其中最明显的就是，现在的星弥似乎变得有点粘人了。"
    "每次我刚回到家，她都会小跑着迎上来。"
    lxc_ "嗯，我回来了。"
    "不过，我一点也不讨厌就是了。"
    show xm smile_close with dissolve
    xm_ "……我每天都缠着要抱你，你会不会觉得烦啊？"
    "她把脸埋在我胸口，蹭来蹭去。"
    lxc_ "怎么会，有这么可爱的女朋友天天缠着我，我高兴都来不及。"
    show xm cat_mouth with dissolve
    xm_ "嗯，就算你嫌我烦，我也不会放手的~"
    lxc_ "只要你不嫌弃我身上有汗味就好。"
    show xm focus with dissolve
    xm_ "才不会呢！那是你辛苦工作的证明！"
    "她为了表明自己真的不在乎，更加用力地蹭了蹭，像只撒娇的小猫。"
    lxc_ "好好好，那先让我进去吧。"
    show xm smile at nod_small
    xm_ "嗯！"
    "我顺手把她抱起，轻轻放回沙发上。"
    "养在桌上的满天星散发着淡淡的清香，紧接着飘来的是饭菜的香味。"
    "工作之后才更加明白——每天回到家，能有人为你准备好热腾腾的饭菜，真的是一件让人从心底感到幸福的事。"
    "现在的我，最大的烦恼大概就是……该思考先吃哪一道菜吧。"


    scene bg_kitchen_2
    with fade

    show xm clothes2_front2_no calm at center with dissolve

    xm_ "小凑……不，林先生，有件事我想和您商量一下。"
    "吃完饭后，星弥忽然叫住了我，表情显得有些认真。"
    lxc_ "好啊。不过……怎么突然又用回这个称呼了？"
    "自从交往后，她已经慢慢习惯直接叫我名字，很少再用「 林先生 」了。"
    "如今久违地听到她这么说，竟让我有些怀念。"
    show xm focus with dissolve
    xm_ "……毕竟是比较严肃的事嘛。"
    "她坐直身体，双手放在膝盖上，一副郑重其事的模样。"
    xm_ "您愿意……成为我的仆从吗？"
    lxc_ "仆从？"
    show xm smile at nod_small
    xm_ "嗯——"
    "她开始认真地解释起来。"
    lxc_ "——原来如此，你是想用最古老的契约魔法，让我成为你的『 仆从 』，也就是使魔。"
    lxc_ "这样我就能共享你的生命，和你一样长寿，可以……和你一直在一起。"
    show xm bewilderment with dissolve
    xm_ "嗯……您愿意吗？"
    lxc_ "当然，我也很想和你一直在一起，没什么理由拒绝吧？"
    show xm shy skin_blush with dissolve
    xm_ "毕竟名义上是要成为我的使魔，我担心您会介意嘛……"
    "听到我的回答，她悄悄松了口气。"
    lxc_ "我们都已经在交往了，这种事除了让我们之间再多一层联系外，也没什么不好吧？"
    lxc_ "而且，成为使魔后，会对我现在的身体或者日常生活有什么影响吗？"
    show xm focus with dissolve
    xm_ "不会的！我以魔女的名义担保，除了寿命外，您的其他方面都不会改变！"
    xm_ "这个魔法，我也已经在冥想时练习了很多遍！不会出问题的。"
    lxc_ "那应该没什么好担心的……啊，我懂了。"
    lxc_ "你是不是担心我成为你的使魔后，要叫你『 主人 』？"
    "我故意调侃她一下。"
    show xm oo kp1wl skin_blush at emphasis_pop
    xm_ "不、不用！您像平时一样叫我名字就好！"
    "她的脸瞬间变得通红，连连摆手。"
    show xm shy skin_blush hide_fx with dissolve
    xm_ "我只是怕您会介意而已！"
    lxc_ "我没关系的。而且，你这么做是为了我们的未来着想，我反而很高兴。"
    lxc_ "这说明你很在乎我，不是吗？"
    show xm smile_close skin_blush with dissolve
    xm_ "……嗯！"
    "听到我这么说，她的脸上重新露出安心的笑容。"
    show xm smile at nod_small
    xm_ "那我现在立刻去做准备！"


    scene bg_living_room_3
    show bg_living_room_3:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with fade

    "没过多久，星弥已经换上了那身正式的魔女服，在客厅中央布置好了仪式用的魔法阵。"
    "她的手腕上，依然佩戴着我告白时送她的那条手链。"
    "据说她在上面施加了好几层防御魔法，哪怕是顶级的攻击魔法，一时半会儿也弄不坏。"
    "虽然我说过不用这么谨慎，但她还是坚持这么做。"
    "她想通过这种方式，把这份礼物、这份心意，好好保护起来。"

    show xm clothes1_front3 calm at center with dissolve

    xm_ "林先生，您准备好了吗？"
    lxc_ "嗯，准备好了。"
    "她向我伸出手，把我拉到魔法阵的中间。"
    "或许是因为紧张，她的手心出了一点汗。"
    lxc_ "没问题的，相信你自己。"
    "我稍稍用力回握住她的手。"
    lxc_ "毕竟，星弥你可是我家最自豪的小魔女啊？"
    show xm smile_close with dissolve
    xm_ "……是啊，这次可是有您在我身边呢。"
    xm_ "没什么好怕的。"
    show xm focus with dissolve
    "她深吸一口气，肩膀放松下来，脸上浮现出坚定的神情。"


    scene cg10
    with Fade(0.5, 0.5, 0.5)

    play music bgm_5 fadeout 1.0 fadein 1.0
    "她举起法杖，身下的魔法阵开始浮现出柔和的光芒，各种我看不懂的符文在空气中若隐若现。"
    show cg101 with dis_master
    xm_ clothes1_front1 "——契约者林小凑，试问，你是否愿意与我，魔女星弥，签下契约，成为我的使魔？"
    lxc_ "我，林小凑，愿意。"
    hide cg10
    show cg10 with dis_master
    "随着我的回应，符文绽放出更加耀眼的光芒。"
    "星弥对我微微一笑，开始吟唱起古老而优美的咒语。"
    "更加绚丽的魔法符文从法阵中延伸开来，光芒流转，最后如同星光般弥漫在整个客厅。"
    "即便长发和披风都因为魔力的涌动而在空中飘动，她的神情却始终专注而认真，展现出一种平时少见的、属于魔女的自信与魅力。"
    "此刻的她，比任何时候都更美丽。"
    "我就这样静静地注视着她，仿佛时间也在这一刻为她停留。"
    "——不知过了多久，魔法阵的光芒渐渐消散，客厅重新恢复了平静。"


    scene bg_living_room_3
    show bg_living_room_3:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with Fade(0.5, 0.5, 0.5)

    show xm clothes1_front3 smile_close at center with dissolve

    "星弥缓缓闭上眼，似乎在通过魔法感知着什么。"
    "随后，她脸上露出了如释重负的笑容。"
    show xm smile with dissolve
    xm_ "成功了……"
    "我立刻上前，在她腿软之前扶住了她。"
    xm_ "小凑，我成功了……"
    lxc_ "嗯，我一直都相信你能做到的。"
    "她靠在我怀里，声音里带着喜悦和一点点疲惫。"
    show xm smile_close skin_blush with dissolve
    xm_ "……嘻嘻，这样一来，我就能永远陪在你身边了。"

    call achievement (16) from _call_achievement_20
    lxc_ "应该是我能永远陪在你身边才对吧。"
    show xm smile skin_blush with dissolve
    xm_ "嗯……我很庆幸自己可以遇到你。"
    xm_ "因为你，我才学会了那么多东西，才明白了……什么是真正重要的心意。"
    lxc_ "……我也很庆幸，自己能够遇到你。"
    "我低头，轻轻蹭了蹭她的额头。"
    lxc_ "我们彼此能遇到对方，真是太好了。"


    hide xm
    with dissolve

    scene bg_sky_3
    show bg_sky_3 at bg_zoom_in
    with fade

    "我们相视一笑，手牵着手，一起望向窗外繁星点点的夜空，共同感受着这份平静而幸福的时刻。"
    "在遥远的未来，我们一定还能一起度过许多个，与此刻相似的温馨时光。"


    $ renpy.block_rollback()
    call splashscreen from _call_splashscreen_2
    $ renpy.block_rollback()
    $ MainMenu(confirm=False, save=False)()
    return

label hougong_route:

    scene bg_sky_1
    with Fade(0.5, 0.5, 0.5)

    $ heroine = False

    call achievement (7) from _call_achievement_10

    play music bgm_6 fadeout 1.0 fadein 1.0
    "周五，我向公司请了年假。"
    "反正项目进度已经延期，我再怎么努力也改变不了现状，还不如好好休息一天。"


    scene bg_living_room_1
    show bg_living_room_1:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve

    "不过，真的不用早起赶地铁之后，反而有点不习惯了。"
    "明明是难得的休息日，但因为不是周末，总觉得哪里怪怪的。"
    "……还是找点事做吧。"
    "最近一直是她们在做饭，今天不如由我下厨好了。"


    scene bg_kitchen_1
    with fade

    "我在厨房里忙着准备早餐，煎饼的香气慢慢飘散开来。"

    show xm clothes2_front2_no smile_close at center with dissolve

    xm_ "啊，林先生，早上好……"
    "身后传来软绵绵的声音。"
    "我回过头，看见星弥正揉着惺忪的睡眼，慢慢朝我走来。"
    lxc_ "早上好。"
    show xm bewilderment with dissolve
    xm_ "您今天不用上班吗？"
    lxc_ "嗯，请假休息了。"
    show xm smile_close with dissolve
    xm_ "这样啊，明明平时都没见您请过假呢……啊呜……"
    "她打了个小小的哈欠，刚起床有点迷迷糊糊的样子显得格外可爱。"
    lxc_ "仔细想想，工作之后我几乎都没怎么请过假。"
    lxc_ "平时总是忙着赶项目进度，也不敢随便请假。"
    "上学的时候总以为工作后就自由了，结果……好像根本不是这样。"
    show xm focus with dissolve
    xm_ "嗯……虽然由我来说可能不太合适，但我觉得您确实该好好放松一下。"
    xm_ "不是为了别人，而是为了自己。"
    lxc_ "……是啊，星弥你说得对。"
    "可能我有时候确实把自己逼得太紧了。"
    "是害怕被开除？还是害怕其他什么？我自己也不是很明白。"
    show xm smile at nod_small
    xm_ "要是觉得累了，也可以多依靠一下我这个大姐姐……啊呜……"
    "她半眯着眼睛，努力挺起胸膛，想要摆出可靠的模样，却又忍不住打了个可爱的哈欠。"
    lxc_ "……好。"
    show xm smile_close with dissolve
    xm_ "嗯！刚睡醒肚子就饿了……好香呢，林先生做的早餐还是那么吸引人。"
    lxc_ "就是普通的煎饼和粥而已，星弥你自己也会做啊？"
    show xm cat_mouth with dissolve
    xm_ "自己做和别人做，感觉不一样的嘛……而且还是林先生做的……"
    lxc_ "是吗？"
    "我仔细想了想，好像真是这样。"
    "星弥做饭的时候，我也会觉得更开心一点。"
    "和食材的香味、厨艺的高低都没关系，只是「 对方为自己做饭 」这件事本身，就让人觉得喜悦。"
    lxc_ "这么一说，好像确实是这样……啊，你头发乱了，我帮你弄一下。"
    "我伸出手，把她额前那缕翘起的头发轻轻拨到耳后。"
    show xm shy skin_blush with dissolve
    xm_ "嗯……"
    "她小声应着，脸颊不自觉地蹭了蹭我的手掌。"
    show xm smile_close skin_blush with dissolve
    xm_ "林先生的手，好暖和呢……"
    "她的脸也很温暖，像只刚睡醒的小猫。"
    "我顺势轻轻挠了挠她的下巴，她就舒服地眯起眼睛，发出满足的「 呼噜 」声。"
    "幸好手上没有沾到油，不然她就要变成小花猫了。"
    lxc_ "好了，快去洗脸吧。"
    lxc_ "如果时语醒了，也叫她一起来吃早餐。"
    show xm smile at nod_small
    xm_ "嗯，嘻嘻……"
    "她脸上挂着满足的傻笑，脚步轻快地朝洗手间走去。"


    hide xm
    with dissolve

    "准备好早餐后，我把煎饼和粥端到餐桌上。"

    show xm clothes2_front3_no shy skin_blush at left with dissolve
    show sy clothes2_front1 calm at right with dissolve

    "她们两人已经坐好了。"
    "不过，星弥的脸红扑扑的，正低着头小口小口地喝着粥。"
    "大概是睡醒之后，终于回想起刚才被我摸脸的事，觉得害羞了。"
    "我多少也有点责任，于是把自己盘子里的煎饼分了一半给她。"
    "不知是不是我的错觉，坐在对面的时语一直用奇怪的表情盯着我。"
    "既不像没睡醒，也不像是不满……更像是有点紧张和疑惑。"
    lxc_ "我手上的煎饼只剩一半了哦？"
    show sy despise with dissolve
    sy_ "……我又不像星弥那么贪吃。"
    "她无语地瞥了我一眼。"
    show xm oo kp1wl at emphasis_pop
    xm_ "喔、喔野布事狠摊尺啦！（我、我也不是很贪吃啦！）"
    lxc_ "好了好了，先把嘴里的东西咽下去再说话。"
    show xm shy skin_blush hide_fx with dissolve

    show sy sigh with dissolve
    "时语轻轻叹了口气，目光在我和窗外之间不断流转。"
    sy_ "我只是在想，我和星弥在这里也住了挺久了。"
    lxc_ "是啊，是有一段时间了。"
    "听到我这么轻描淡写的回答，她微微挑了挑眉。"
    show sy focus with dissolve
    sy_ "你……没有什么想说的吗？"
    lxc_ "我？"
    "我避开了她的目光，抬头看了看天花板。"
    lxc_ "嗯……这位客人，您是对本餐厅的早餐有什么不满吗？"
    show sy pout with dissolve
    sy_ "……没有。"
    "她用力咬了一口煎饼，一副欲言又止的样子。"
    show sy sigh with dissolve
    sy_ "算了，你忘了反而更好。"
    "桌子下面，我感觉有什么轻轻碰了碰我的脚背。"
    "低头一看——是时语光着的小脚丫，正悄悄地挠着我的脚。"
    lxc_ "……？"
    show sy cat_mouth with dissolve
    sy_ "不喜欢的话，就挪开啊。"
    "她歪了歪头，嘴上的笑容带着一丝狡黠。"
    lxc_ "不是喜不喜欢的问题，正在吃饭呢……嗯？我拖鞋呢？"
    "低头一看，左脚的拖鞋已经不知道飞到哪里去了。"
    lxc_ "你……"
    show sy laugh_open at bounce_small
    sy_ "哼哼哼，这是对你的惩罚！我明明都准备那么多说辞了，结果都用不上！"
    lxc_ "这是不是有点太不讲理了……喂！别把另外一只也偷走啊！"
    "我赶紧伸出脚，试图抢救我仅存的拖鞋。"
    show xm oo with dissolve
    xm_ "呀！林先生，那只鞋子是我的啦……"
    lxc_ "啊，抱歉抱歉。"
    show xm smile_close with dissolve
    "在桌下一番「 脚上功夫 」后，我总算保住了自己的一只拖鞋。"
    "抬起头，却发现我碗里剩下的那一小块煎饼不见了。"
    "时语正小口吃着什么，嘴角还带着一点饼屑，脸上挂着计划得逞的得意笑容。"
    show sy smile with dissolve
    lxc_ "我说你啊……那可是我吃过的哦？"
    show sy cat_mouth with dissolve
    sy_ "我又不介意。"
    "我介意啊……虽然很想故意这么吐槽，但感觉说出来她肯定会生气。"
    "幸好我还有后手准备。"
    "我起身，从锅里端出了最后一块煎饼。"
    show sy astonished kp1wl at shocked_step_back
    sy_ "居然还藏了一块……"
    show sy hide_fx with dissolve
    lxc_ "这种煎饼一包有十个，分完刚好剩最后一个。"
    "我拿出小刀，慢慢把煎饼切成三等份。"
    lxc_ "这最后一块，我们就每人分一点吧。"
    show sy bewilderment with dissolve
    "看到我的举动，时语露出有点意外的表情。星弥则眼睛一亮，但马上又摇摇头。"
    sy_ "……还是你吃吧，你自己都没吃到一个完整的。"
    show xm smile_close with dis_master
    xm_ "是啊，虽然我很想吃啦……但我觉得还是留给您比较好。"
    lxc_ "你们两个怎么突然这么大方了……"
    lxc_ "一起吃吧。好东西一起分享，才会更好吃。"
    show sy smile_close with dissolve
    sy_ "……好吧。"
    show xm smile at nod_small
    xm_ "嗯！"
    "时语小口咬着自己的那份，星弥则接过小刀，把她那份又小心地切成两半。"
    "然后，两人不约而同地把剩下的煎饼都夹到了我面前。"
    show sy pout skin_blush with dissolve
    sy_ "先说好，这只是礼尚往来而已……"
    show xm cat_mouth skin_blush with dissolve
    xm_ "有好东西一起分享，这可是您刚刚说的哦？"
    lxc_ "你们……"
    show sy cat_mouth with dissolve
    sy_ "快点吃啦，我的手一直举着很累的！"
    show xm laugh_open at bounce_small
    xm_ "就是啊，等下凉了可就不好吃了哦？"
    lxc_ "好好好，别一起凑过来啦！"
    lxc_ "我嘴巴没那么大，不能一下子都吃完的！"

    scene bg_sky_1
    with Fade(0.5, 0.5, 0.5)

    scene bg_sky_5
    with Dissolve(1.0)

    scene bg_sky_3
    with Dissolve(1.0)




    scene bg_living_room_3
    with Fade(0.5, 0.5, 0.5)
    show bg_living_room_3:
        zoom 1.06
        xalign 0.5
        yalign 1.0
    with dissolve

    play music bgm_13 fadeout 1.0 fadein 1.0
    "半夜醒来，迷迷糊糊间，好像做了个……恶梦。"
    "梦的内容其实很普通。"
    "我去公司上班，像往常一样对接工作，然后像往常一样回家，独自生活。"
    "明明是再熟悉不过、早已习以为常的日子，却不知为什么，觉得那是个恶梦。"
    "……有点渴，去喝口水好了。"
    "刚想坐起来，帐篷的拉链却自己轻轻拉开了。"
    "……？"

    scene bg_living_room_3:
        zoom 1.2
        xalign 0.5
        yalign 1.0
    with dissolve

    "朦胧的月光下，我眯着眼睛，隐约看到一个小小的脑袋从拉链缝隙探了进来。"
    "是……星弥？"


    scene bg_living_room_3
    with Fade(0.5, 0.5, 0.5)
    scene bg_living_room_3:
        zoom 1.06
        xalign 0.5
        yalign 1.0
    with dissolve
    $ heroine = True
    $ heroine_name = "星弥的视角"

    play music bgm_7 fadeout 1.0 fadein 1.0

    show xm clothes2_front3_no smile at center with dissolve

    "从洗手间出来后，我悄悄地来到了林先生的帐篷前。"
    "这么晚了，他应该已经睡着了吧。"
    "给自己施加一个静音魔法后，我小心翼翼地拉开了一点点拉链。"
    "帐篷里，林先生呼吸很轻，很平稳，就是……睡姿好像有点奇怪？"
    "我轻手轻脚地钻进去，来到他身边，伸手轻轻碰了碰他的额头——有点湿湿的，出了一点汗。"
    "我拿出纸巾，小心地替他擦了擦。"
    "平时都辛苦你啦。"
    show xm smile_close with dissolve
    xm_ "……嘻嘻。"
    "啊，不好不好……差点就笑出声音了。"
    "我赶紧看向林先生，还好，他还和刚才一样，睡得正熟。"
    "晚上偶尔醒来时，我就会像这样偷偷来看看熟睡的林先生。"
    "只要待在他身边，就会觉得特别安心，特别踏实。"
    "好啦，看到他睡得安稳我也放心了，该回去——等等！"
    "帐篷外，月光映出了一道熟悉的身影。"
    show xm astonished kp1wl at shocked_step_back
    "……是时语？！她也来了？"
    "不行不行，要是被她看到我在这里，肯定会误会的！得想办法躲起来才行！"
    show xm hide_fx with dissolve
    "……啊，有了！隐身魔法！"
    show xm focus at nod_small
    "至于躲在哪里……就先躺在林先生旁边吧！"

    hide xm with dissolve


    scene bg_living_room_3
    with Fade(0.5, 0.5, 0.5)
    scene bg_living_room_3:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve
    $ heroine_name = "时语的视角"

    show sy clothes2_front1 smile at center with dissolve

    "没事的，星弥去洗手间了，不会发现的……"
    "而且我又不是去做什么坏事，只是去看看他睡得好不好而已。"
    "……毕竟他把床让给我们睡，自己一直睡帐篷，总归没那么舒服吧！"
    show sy focus with dissolve
    "对！所以我去看看他睡得怎么样，是很正常的事！"
    show sy pout skin_blush with dissolve
    "绝对不是做什么亏心事！"


    scene bg_living_room_3:
        zoom 1.2
        xalign 0.5
        yalign 1.0
    with dissolve

    "做好心理准备后，我踮起脚尖，轻轻来到林小凑的帐篷前。"
    "……嗯？拉链怎么没拉好？"
    "我俯身钻进帐篷，看到他额头上出了不少汗。"
    "出了这么多汗也不知道开个风扇或空调……真是的。"
    show sy calm with dissolve
    "我拿起纸巾，轻轻替他擦掉额头的汗珠。"
    "月光透过帐篷的缝隙，落在他熟睡的脸上。"
    "他的眉毛微微皱着，不知道是不是梦到了什么。"
    show sy sigh with dissolve
    "平时总是把事情揽在自己身上……偶尔也依靠一下我和星弥嘛。"
    "……虽然我知道，现在的我们还帮不上太多忙就是了。"
    show sy smile_close skin_blush with dissolve
    "在心里小小抱怨完，我准备起身离开。"
    "……嗯？嗅嗅……这个味道……"
    show sy bewilderment with dissolve
    "我仔细看了看帐篷，忽然明白了什么。"
    show sy astonished kp17wl with dissolve
    "……原来是这样啊。"
    show sy hide_fx with dissolve

    hide sy with dissolve


    scene bg_living_room_3
    with Fade(0.5, 0.5, 0.5)
    scene bg_living_room_3:
        zoom 1.3
        xalign 0.5
        yalign 1.0
    with dissolve
    $ heroine = False

    "我想，今晚大概是最近最「 热闹 」的一个晚上了。"
    "先是星弥悄悄钻进了我的帐篷，然后时语也来了，吓得星弥赶紧躲了起来——多半是用了什么魔法。"
    "于是，一个小小的帐篷里，现在「 藏 」着三个人。"
    if third_choice == 3:
        "虽然以前她们也进来过，但这次的情况……明显不太一样。"
    "……明明我什么都没做错，但为什么会有种微妙的背德感啊……"
    "黑暗中，不知道是我的心跳声，还是星弥的，又或者是时语的。"
    "总之，心脏跳动的声音在这安静的夜里显得格外清晰。"
    "——然后，我的嘴唇被什么轻轻碰了一下。"
    "……？"
    "虽然能感觉到是手指的触感，但上面明显带着一点湿润。"

    show sy clothes2_front1 shy skin_shy at left with dissolve

    "我还没来得及细想，时语就匆匆抽回手指，慌慌张张地离开了帐篷。"

    hide sy with dissolve

    "躲在一旁的星弥确认时语离开后，呼吸终于平缓了一些，呼在我耳边的气息也没那么让人发痒了。"
    "好了好了，星弥你也快点回去吧，我装睡也是很辛苦的……嗯？"

    show xm clothes2_front3_no shy skin_shy at right with dissolve

    "脸颊上又传来一阵相似的、柔软的触感。"

    hide xm with dissolve

    "然后，星弥好像比时语还要慌张，一下子逃出了帐篷。"
    "我回味似的抿了抿嘴唇，又摸了摸脸上还残留着的一点湿润触感。"
    "……唉。"
    "今晚恐怕是睡不着了。"

    scene bg_sky_3
    with Fade(0.5, 0.5, 0.5)

    scene bg_sky_1
    with Dissolve(1.0)

    scene bg_sky_5
    with Dissolve(1.0)

    scene bg_sky_3
    with Dissolve(1.0)



    scene bg_living_room_2
    with Fade(0.5, 0.5, 0.5)
    show bg_living_room_2:
        zoom 1.06
        xalign 0.5
        yalign 1.0
    with dissolve
    show sy clothes2_front1 smile at left with dissolve
    show xm clothes2_front2_no smile at right with dissolve

    "周五晚上，我像往常一样回到了家中。"
    lxc_ "我回来了。"
    "听到我的声音，拿着扫把的时语和捧着书的星弥同时抬起了头。"
    sy_ "回来啦。"
    xm_ "欢迎回来，林先生！" with dissolve
    "看到她们的样子，我偶尔会回想起那天晚上的事，有时甚至会觉得有点害羞。"
    "但我最后还是决定，假装什么都不知道。"
    "时语放下扫把，接过我手里抱着的纸箱。"
    sy_ "这是什么？"
    lxc_ "……嘘。"
    "我故意压低声音，假装神秘地竖起了食指。"
    lxc_ "这个啊，在某种意义上，可是违禁品哦。"
    "虽然里面其实只是普通的烟花而已。"
    show sy astonished kp1wl at shocked_step_back
    sy_ "什喵？！"
    "时语一下子睁大眼睛，抱着箱子的手都抖了一下。"
    show sy hide_fx with dissolve
    show xm focus at lean_in
    xm_ "唔……是火药的味道呢。林先生，您买这个是要做什么呀？"
    lxc_ "这个嘛，其实是——"
    show sy bewilderment with dissolve
    sy_ "你不会是想走私违禁品吧……？"
    "时语打断我的话，声音里带着明显的慌张。"
    lxc_ "不是，其实——"
    sy_ "你、你不要做这么危险的事啊……"
    lxc_ "呃……"
    "这……不对吧？时语你的反应，不应该是疑惑地吐槽我吗？"
    "等你吐槽之后，我再打个哈哈说「 开玩笑的 」才对啊？"
    "现在你这么认真地担心我，反而让我觉得很过意不去……"
    show xm clothes2_front2_no smile at right with dissolve
    show sy focus with dissolve
    "我立刻看向一旁的星弥，希望她能帮忙打个圆场，缓和一下气氛。"
    "星弥看到我的眼神，立刻点了点头。"
    show xm cat_mouth at bounce_small
    xm_ "林先生，做坏事是不好的哦？"
    "……不是让你说这个啊！"
    "看着时语那真切的眼神，我决定还是实话实说。"
    lxc_ "时语，对不起。"
    "我轻轻把双手搭在她肩膀上。"
    sy_ "嗯，现在回头还来得及的……"
    lxc_ "其实里面是……普通的烟花。"
    "……"
    "客厅里一下子安静下来。"

    "我心虚地移开视线，不敢看时语的眼睛。"
    "但就算不看，我也能想象到她表情变化的精彩程度。"
    show sy clothes2_side1 not_good skin_blush at left, angry_stomp
    sy_ "你、我……啊，可恶的臭人类！！！"


    scene bg_street_2
    show bg_street_2:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with fade
    show sy clothes2_front1 pout at left with dissolve
    show xm clothes2_front2_no smile at right with dissolve

    lxc_ "抱歉抱歉，我认错，不要再打啦……"
    "从家到公园的路上，时语一直气鼓鼓地用她的小拳头捶我。"
    lxc_ "我本来只是想开个玩笑，活跃一下气氛的……"
    sy_ "真是的……"
    "她又轻轻捶了我一下，力度很轻，更像是在撒娇。"
    sy_ "一点都不好笑。"
    show xm smile_close with dissolve
    "走在另一边的星弥看着我们的互动，捂着嘴偷偷笑。"
    xm_ "就是呀，林先生这次确实有点太坏了。"
    xm_ "时语虽然没有表现出来，但她平时可是一直都很担心您的哦？"
    show sy shy skin_blush at left, look_away_small
    sy_ "……我才没有担心他呢。"
    "时语瞥了我一眼，故作生气地看向别处。"
    show sy pout skin_blush at left with dissolve
    "我想起了之前晚上，她们悄悄钻进我帐篷的事。"
    lxc_ "我知道……是我不好，抱歉。"
    sy_ "哼~"

    "听到我道歉，时语的脸颊还是鼓鼓的，但态度明显软了下来。"
    show sy smile_close with dis_master
    show xm smile with dissolve
    xm_ "不过呀，我在闻到火药味时就觉得有点奇怪。量太少了，而且也不是危险的那种火药。"
    xm_ "血族的鼻子这么灵敏，应该更容易闻出来吧？"
    show xm cat_mouth at lean_in
    xm_ "{size=-10}我懂了，这就是所谓的『 关心则乱 』吧？{/size}"
    "她说话时呼出的气息弄得我耳朵痒痒的。"
    lxc_ "是这样啊……"
    show sy smile with dissolve
    sy_ "顺带一提，血族的耳朵也是很灵敏的哦？"
    show xm shy skin_shy with dis_master
    show sy shy skin_shy with dis_master
    xm_ "啊，好像是这样呢……"
    "星弥的脸一下子红了。"
    "时语的脸上也染上了一抹红晕，在夜色中格外显眼。"

    "她装出很凶的样子，狠狠地瞪了我一眼。"
    lxc_ "……这次应该不关我事吧？"
    sy_ pout skin_blush "我不管，都怪你！" with dissolve
    lxc_ "好吧，怪我咯。"
    "我换了个姿势抱住纸箱。"
    show xm focus skin_blush with dissolve
    show sy calm skin_blush with dissolve
    xm_ "所以，时语刚刚为什么那么紧张？"
    xm_ "都有点不像平时的你了。"
    "星弥的表情认真了一点，替我问出了我想问的事。"
    show sy bewilderment with dissolve
    sy_ "……以前在家族里见过类似的人。"
    sy_ "为了保护重要的人，那些人走上了极端，最后……没有好下场。"
    show sy focus with dissolve
    "她抬起头，红色的眼睛认真地看着我。"
    sy_ "我不希望……你也变成那样。"

    xm_ sigh "……是啊，我在旅行的时候，也见过不少类似的人呢。" with dissolve
    xm_ "为了活下去，不得不做出各种艰难的选择……"

    sy_ smile_close "听你这么说……我觉得自己还真是幸运。" with dissolve

    xm_ smile_close "能遇到林先生，能像现在这样平静地生活。" with dissolve
    xm_ "我觉得，我们都挺幸运的。"
    lxc_ "……突然间说起了很现实的话题呢。"
    "不管在什么地方，都有人会面对艰难的抉择，会为了珍视的东西做出牺牲吧。"
    lxc_ "不过放心吧，我很珍惜和你们一起的生活，不会做那种事的。"


    play music bgm_13 fadeout 1.0 fadein 1.0
    scene bg_park_3
    with Fade(0.5, 0.5, 0.5)
    show bg_park_3:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve
    show sy clothes2_front1 smile at left with dissolve
    show xm clothes2_front3_no smile at right with dissolve

    "一路闲聊着，我们很快就到了公园。"
    "夜晚的公园很安静，只有几盏路灯散发着柔和的光。"
    "我们找了个远离居民区的空地。"
    lxc_ "今晚公园没人，刚好让我们包场了，一起玩吧。"
    "我把纸箱放在地上，两人立刻好奇地凑了过来。"
    show xm astonished kp1wl at lean_in
    xm_ "喔，原来里面的东西是长这样呢……"
    show xm hide_fx with dissolve
    xm_ "我知道这个点燃了就能玩，但这个透明的该怎么用呢？"
    show sy clothes2_side1 cat_mouth with dissolve
    "她指了指箱子里的荧光棒。"
    sy_ "这个是荧光棒啦，把它掰弯了就会发光哦。"
    "时语拿出一根，示范了一下使用方法。"
    show xm laugh_open at bounce_small
    xm_ "哇，就像森林里的萤火虫一样呢。"
    "星弥兴奋地挥舞着荧光棒，像拿到新玩具的孩子一样。"
    show sy smile at left with dissolve
    "时语则点燃一根线香烟花，在空中画着一个又一个的圈圈，动作里既有淘气，又带着一份优雅。"
    lxc_ "真漂亮呢。"
    "看到她们开心的样子，我觉得自己买烟花回来的决定是对的。"

    scene cg14 with dissolve

    sy_ "别傻愣着啦，过来一起玩吧。"
    xm_ clothes2_front2_no "是啊，只有我们两个玩得开心，那就不算大家一起玩了吧？"
    lxc_ "嗯，也是。"
    "我左手接过线香烟花，轻轻挥动，金色的火花在夜色中划出明亮的光弧。"
    "右手接过的荧光棒，蓝绿色的光芒在夜空中静静闪耀。"

    show cg140 with dis_master

    sy_ smile_close "……人类是不是都很喜欢这种转瞬即逝的东西呢？" with dissolve
    "时语眼中闪烁着亮光，语气里带着一丝不易察觉的感慨。"
    lxc_ "既有人喜欢，也有人讨厌吧。"

    show cg141 with dis_master

    xm_ calm "我是觉得，正因为会消失，或许才更想好好珍惜吧。" with dissolve
    "星弥举起手，在空中又画了一个亮闪闪的星星。"

    show cg142 with dis_master

    xm_ laugh_open "就像林先生做的菜，虽然很快就吃完了，但每次都很开心！" with dissolve

    show cg143 with dis_master

    sy_ cat_mouth "确定不是因为你自己贪吃？" with dissolve

    show cg144 with dis_master

    xm_ pout "才不是呢！明明是因为林先生做得太好吃了！" with dissolve
    "星弥鼓起脸颊，故意把荧光棒往时语那边晃了晃，吓得时语连忙把线香烟花收到身后。"

    show cg145 with dis_master

    sy_ not_good "笨蛋！别靠这么近！会烧到你自己的！" with dissolve

    show cg146 with dis_master

    xm_ cat_mouth "真正的魔女才不怕被烧呢！" with dissolve

    show cg147 with dis_master

    sy_ pout "我又不是在说这个！" with dissolve

    hide cg14
    show cg14 with dis_master

    "看着她们打闹的样子，我开心地笑了笑。"
    "哪怕是这样普通又平常的夜晚，只要和她们在一起，就会变得格外开心。"

    scene bg_park_3 with fade

    show xm clothes2_front2_no smile at right with dissolve
    show sy smile at left with dissolve
    "不过，快乐的时光总是过得很快。"
    "没多久，线香烟花和荧光棒都玩完了。"
    show xm bewilderment with dissolve
    xm_ "啊……这就没了吗？"
    "星弥有点失落地看着空空的箱子。"
    show sy sigh with dissolve
    sy_ "好可惜……我还没玩够呢。"
    lxc_ "是啊，我运气不太好，店里就剩下这些小型烟花了。"
    "我把用完的烟花棒整理好。"
    lxc_ "至于大型烟花，市区里就算能买到，也不允许放的。"
    "不如说，那家卖烟花的店现在还开着，本身就已经很神奇了……"
    sy_ "毕竟城市里人和建筑太多，安全第一呀。"
    lxc_ "好了，我们收拾一下，确保周围没有隐患就回去吧——"
    show xm focus at emphasis_pop
    xm_ "可是，别人不允许做的事，我们就真的不能做吗？"
    "星弥忽然说出了这句话。"
    show xm shy with dissolve
    xm_ "啊，我不是说那些坏坏的事啦。"
    show xm smile with dissolve
    "怕我们误会，她连忙摆了摆手。"
    xm_ "我是想说……只要不影响到别人，我们自己偷偷玩烟花，也没关系吧？"
    show sy astonished kp17wl at emphasis_pop
    sy_ "但哪里还有不会影响到别人的烟花……啊。"
    sy_ "难道你是想……"
    show sy hide_fx with dissolve
    show xm wink at nod_small
    xm_ "嗯，时语你猜对啦~"
    "星弥俏皮地眨了眨眼，可我还是一头雾水。"
    lxc_ "什么意思？"
    show xm clothes2_front3_no cat_mouth at bounce_small
    xm_ "哼哼，林先生你忘了吗？星弥我可是魔女哦？"
    xm_ "只有我们三个人看到的幻象魔法，可一点都不难。"
    show xm focus with dissolve
    "她闭上眼睛，小声念起咒语。"


    scene bg_sky_10 with Fade(0.5, 0.5, 0.5)

    "接着，第一朵「 烟花 」在空中绽放了。"
    "不是普通的烟花，而是由无数细小的光点组成的，像星星一样闪烁，又像花瓣般缓缓飘落。"
    "梦幻的紫蓝色，在夜空中显得格外神秘。"
    lxcsy_ focus "哇……" with dissolve
    "我和时语同时发出惊叹。"

    show bg_sky_7
    with dis_master

    "紧接着，更多「 烟花 」绽放开来。"


    show bg_sky_8
    with dis_master


    "有的像流动的银河，有的像飞舞的精灵，有的甚至还会变换形状——从花朵变成动物，再变成各种可爱的图案。"


    show bg_sky_9
    with dis_master


    xm_ clothes2_front3_no smile "怎么样？很漂亮吧？" with dissolve

    hide bg_sky_8
    show bg_sky_8
    with dis_master

    "星弥得意地笑着，手指轻轻一点，夜空中的「 烟花 」便自动地绽放开来。"
    lxc_ "嗯，很好看，星弥果然是很厉害的魔女呢。"

    hide bg_sky_7
    show bg_sky_7
    with dis_master
    "以前还没有这么深的感触，但现在，我真心觉得她是一位很厉害的魔女。"

    sy_ clothes2_front1 smile "并行施法以及序列施法……星弥的魔法水平真的很厉害呢。" with dissolve

    hide bg_sky_9
    show bg_sky_9
    with dis_master
    xm_ smile_close "嘻嘻，也没有那么厉害啦~" with dissolve
    "我们三人并排站着，抬头望向这片只属于我们的魔法天空。"
    "五彩斑斓的光芒映在我们脸上，周围很安静，只有远处偶尔传来的虫鸣，和轻微的呼吸声。"


    play music bgm_20 fadeout 1.0 fadein 1.0
    scene bg_park_3
    with Fade(0.5, 0.5, 0.5)
    show bg_park_3:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve
    show sy clothes2_front1 smile_close skin_blush at left with dissolve
    show xm clothes2_front2_no smile skin_blush at right with dissolve

    "不知不觉间，我们之间的距离越来越近，直到彼此的手臂轻轻碰到了一起。"
    lxc_ "要是以后……还有机会再一起看烟花就好了。"
    "明明天上的烟花还没有结束，我却没来由地发出了这样的感叹。"
    lxc_ "呃，抱歉。我在说什么呢，明明——"

    show sy laugh_open at left, look_at_right
    show xm laugh_open at right, look_at_left

    syxm_ "会有机会的。"
    "她们两人异口同声地回答。"


    "就连她们自己都惊讶会同时说出这句话，互相看了看对方，然后一起笑了起来。"

    show sy smile_close at look_away_small
    show xm smile at look_away_small

    xm_ "下次，我们一起去放真正的烟花吧。"
    sy_ "只要你愿意，我们都会陪你去看的。"


    "她们抬起头，轻轻握住了我的手。"
    lxc_ "……嗯，谢谢你们。"
    "我也回握住了她们的手。"
    "她们的手小小的，却都很温暖。"
    lxc_ "下次，我们一起找个可以随便放烟花的地方吧。"


    scene bg_sky_3 with Fade(0.5, 0.5, 0.5)

    "最后的烟花在空中绽放，随后如萤火般在夜色中渐渐消散。"
    "但我并不觉得遗憾。"
    "因为对我来说，最绚烂的夜光，早已留在了我的身边。"

    call achievement (17) from _call_achievement_21


    play music bgm_14 fadeout 1.0 fadein 1.0
    scene bg_living_room_2
    with Fade(0.5, 0.5, 0.5)
    show bg_living_room_2:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve

    $ heroine = True
    $ heroine_name = "第三人称视角"

    "窗外下着小雨，淅淅沥沥的雨声让客厅显得格外安静。"
    "两位少女坐在沙发上，电视上正播着一部不知名的电影——讲的是三个人在相处中逐渐意识到彼此心意的故事。"
    "星弥怀里抱着一袋还没开封的薯片，两根食指无意识地对着点了点，一副欲言又止的样子。"

    show sy clothes2_front1 bewilderment at left with dissolve
    show xm clothes2_front3_no shy at right with dissolve

    sy_ "怎么了？电影不好看吗？"
    sy_ "连桌上的薯片你都不吃，很少见呢。"


    xm_ bewilderment "不是啦……看这个电影的时候，我想到了一个问题而已。" with dissolve
    "星弥想起了那天晚上，她曾在帐篷里看到时语的身影。"

    show xm focus with dissolve

    xm_ "……时语你是不是……喜欢林先生啊？"

    show sy oo kp1wl at emphasis_pop
    sy_ "啊？！你、你在说什么啊，我、我才没……"
    "时语被这句话吓得手里的薯片都掉在了地上。"
    show sy hide_fx with dissolve

    show xm smile_close with dissolve

    xm_ "但要是不喜欢的话，你也不会愿意一直住在这里吧？"

    sy_ pout "我只是……还没好好报答他而已。" with dissolve
    sy_ "而且你不也在这里住了这么久嘛……你对他又是怎么想的？"

    xm_ smile "我的话……其实自己也不太清楚。" with dissolve
    xm_ "刚认识他的时候，我觉得林先生还蛮奇怪的。"
    xm_ "你想想，他居然愿意让两个来历不明的陌生人住在他家。"
    xm_ "不仅没有警惕心，脾气也很好，几乎不怎么生气。"

    sy_ focus "嗯……作为一个普通人类，他这么做确实挺危险的。" with dissolve
    sy_ "虽然我很感激他啦。但如果我们真是坏人，他恐怕早就被吃得连骨头都不剩了。"


    xm_ smile "是啊……最初我的想法是，等约定的时间到了，就向林先生道别，然后离开这里。" with dissolve
    xm_ "可是不知不觉，就在这里住了三个多月了。"
    "星弥转过头，看着时语的眼睛。"

    xm_ "和林先生，还有和时语你一起相处的日子，我觉得很开心。"
    xm_ "……就像是……在一个很温暖、很安心的避风港里一样。"

    sy_ smile_close "嗯，我也很喜欢这种……没有距离感，可以放松地做自己，互相陪伴的感觉。" with dissolve
    "——「 但继续下去的话，是不行的吧。」"
    "两位少女的心里，都不约而同地浮现出这句话，但谁也没有说出口。"

    show sy bewilderment with dissolve
    show xm sigh with dissolve

    xm_ "……"
    sy_ "……"

    sy_ "……怎么感觉话题突然间变得好沉重。"

    xm_ smile "那我们换个话题吧。" with dissolve
    "星弥深吸一口气，重新打起精神。"

    show xm cat_mouth with dissolve
    xm_ "……时语你其实也喜欢林先生吧？"

    show sy oo kp13wl at emphasis_pop
    sy_ "怎么又绕回这个话题了？！"
    show sy hide_fx with dissolve

    xm_ smile_close "这句话和刚刚的其实有点不同啦。" with dissolve

    sy_ despise "哪里不一样了？" with dissolve

    xm_ cat_mouth "你就告诉我你的想法嘛，又不会怎么样。" with dissolve
    "星弥凑近了一些，碧绿的眼睛里带着强烈的好奇心。"

    sy_ shy "我、我不行，太害羞了……" with dissolve
    "时语别过脸，脸颊泛红。"

    sy_ "而且，要说的话，明明星弥你自己也喜欢他吧？"
    sy_ "晚上偷偷跑去林小凑的帐篷里，还不带我！"

    show xm astonished kp1wl at shocked_step_back
    xm_ "欸？你怎么知道的……我明明已经用了隐身魔法的……"
    show xm hide_fx with dissolve
    xm_ "不对不对！我那不是喜欢，我只是……担心林先生踢被子会感冒而已！"

    sy_ cat_mouth "……他这么大的人，哪里还会踢被子。" with dissolve

    xm_ shy "那、那时语你是怎么知道我去了帐篷的呢？" with dissolve
    "听到星弥这么问，时语露出了有点心虚的表情。"

    show sy focus with dissolve
    sy_ "……我只是刚好路过而已……"
    sy_ "而且重点是，你明明就是喜欢林小凑吧？"

    xm_ shy "那真要说的话，时语你自己不也喜欢吗？明明喜欢还不承认……" with dissolve

    sy_ shy "我、我只是……" with dissolve
    "正当两位少女小声争论时，门口传来了钥匙转动的声音。"

    show sy astonished at look_at_right
    show xm astonished at look_at_left

    pause 0.5

    hide sy with dissolve
    hide xm with dissolve

    pause 0.5

    lxc_ "我回来了……咦？客厅没人？"


    scene bg_bedroom_4
    with fade
    show bg_bedroom_4:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve

    show sy clothes2_front1 focus at left with dissolve
    show xm clothes2_front3_no shy at right with dissolve

    "房门悄悄打开了一条缝。"

    xm_ "所以说，我们为什么要躲起来啊？"

    sy_ pout "你是要在我们刚争辩完谁喜欢林小凑的时候，出去和他聊天吗？" with dissolve

    xm_ oo "好像是哦……要是现在和他说话，肯定会很害羞的。" with dissolve

    show sy smile_close at nod_small
    sy_ "就是啊。所以先在这里待一会儿，等心情平复了再出去。"

    show xm smile at nod_small
    xm_ "嗯嗯……"
    "星弥透过门缝，看到林小凑坐在沙发上，手里似乎还拿着什么东西。"

    show xm focus at lean_in
    xm_ "不过，时语你看……林先生手上拿着的，是信吗？"

    sy_ focus "我看看……好像是哦，谁给他写的信呢？" with dissolve


    play music bgm_11 fadeout 1.0 fadein 1.0
    scene bg_living_room_2
    with Fade(0.5, 0.5, 0.5)

    $ heroine = False

    lxc_ "我回来了……嗯？客厅没人？"
    "回到家，时语和星弥都不在客厅里。"
    "不过，茶几上放着两杯冒着热气的红茶，电视还开着，只是停在主菜单界面，显然刚才还有人在。"
    "这两个人……刚刚是在客厅看电影吗？"


    "我来到洗手间找了条毛巾，擦了擦湿漉漉的头发。"
    "出门买东西的时候突然下起了雨。"
    "更倒霉的是，放在超市门口的伞不知道被谁拿走了……算了，反正家离超市也不远。"


    show bg_living_room_2:
        zoom 1.05
        xalign 0.5
        yalign 1.0
    with dissolve

    "擦干头发后，我仔细看了看刚才在门口拿到的两封信。"
    "浅褐色的信封，上面分别用两种漂亮的字体写着我的名字。"
    "没有邮票，也没有邮戳，就像是被人直接放在这里的。"
    "奇怪。这年头居然还会有人寄信，而且还是两封？"
    "我想了想，印象中也没有会给我寄信的人。"
    "先拆开看看吧。"


    play music bgm_19 fadeout 1.0 fadein 1.0

    show expression Solid("#000000") as letterbox_top at letterbox_top(0, 180, 2.5)
    show expression Solid("#000000") as letterbox_bottom at letterbox_bottom(0, 180, 2.5)

    show bg_living_room_2 at bg_pan_right

    "我拆开信封，慢慢读了起来。"
    lxc_ "……"
    "但随着我一字一句地往下看，眉头不自觉地越皱越紧。"
    "读完两封信后，我才发现信纸的边缘已经被我捏出了细微的皱褶。"
    "这不是普通的信。"
    "而是……分别写给时语和星弥的信。"
    "给时语的信，是她的管家写的。"
    "信里的语气看起来很客气，但字里行间却流露着希望她能尽早回去，不要在外面玩太久的意思。"
    "而给星弥的信，则是魔女茶话会的管理者写的。"
    "虽然语气看起来很轻松随意，但行文却带着一丝警告的意味，提醒星弥不要在表世界过分使用魔法。"


    with dissolve

    "看完两份信，我深深地叹了一口气。"
    "这一天，终究还是来了。"
    "但为什么……要寄给我？"
    "我看着桌上还没收拾的零食和红茶，看着沙发上随意放着的抱枕，看着这个家里属于她们的生活痕迹——我忽然明白了。"


    "因为我是她们在表世界的「 联系人 」。"
    "这两份信，实际上是为了警告我——警告我，她们不属于这里，警告我，这样的日子不会永远持续下去。"
    "意识到这点后，心脏像被什么东西轻轻攥了一下，有点闷，有点疼，就连呼吸也不自觉地变重了。"
    lxc_ "……冷静点。"
    "我把信小心地折好，放回茶几上，闭上眼，慢慢平复自己的心情。"
    "客厅很安静，只有窗外雨滴打在玻璃的滴答声，和远处隐约传来的车流声。"


    scene bg_living_room_2
    show sy clothes1_front1 smile at left
    show xm clothes1_front3_no smile at right
    show expression Solid("#ffa200") as yellow_tint:
        alpha 0.12
    with Fade(0.5, 0.5, 0.5)



    "和她们一起生活的这三个月，像一场温柔得不太真实的梦。"


    show cg2
    hide yellow_tint
    show expression Solid("#ffa200") as yellow_tint:
        alpha 0.12
    with dissolve

    "每天早上醒来，会看到时语抱着抱枕、迷迷糊糊地从房间出来，银色的长发乱糟糟的。"

    show cg6
    hide yellow_tint
    show expression Solid("#ffa200") as yellow_tint:
        alpha 0.12
    with dissolve

    "会听到星弥在厨房哼着歌准备早餐，偶尔传来「 哎呀 」的小声惊呼，大概是又差点把什么弄翻了。"

    hide bg_living_room_2
    show bg_living_room_2
    hide yellow_tint
    show expression Solid("#ffa200") as yellow_tint:
        alpha 0.12
    with dissolve

    "下班回家，客厅的灯总是亮着。"

    show cg415
    hide yellow_tint
    show expression Solid("#ffa200") as yellow_tint:
        alpha 0.12
    with dissolve

    "时语会坐在沙发上打游戏，听到开门声时会暂停一下，转过头来说「 你回来了 」。"

    hide bg_living_room_2
    show bg_living_room_2
    hide xm
    show xm clothes2_front3_no laugh_open at center
    hide yellow_tint
    show expression Solid("#ffa200") as yellow_tint:
        alpha 0.12
    with dissolve


    "星弥会小跑过来，带着开心的笑容说「 今天工作辛苦了 」。"

    show bg_shop_1
    hide xm
    show xm clothes2_front3_no smile at right
    hide sy
    show sy clothes2_front1 smile at left
    hide yellow_tint
    show expression Solid("#ffa200") as yellow_tint:
        alpha 0.12
    with dissolve

    "周末我们会一起出去逛逛，一起玩游戏，一起做各种各样平常又开心的事。"

    show bg_living_room_3
    hide xm
    show xm clothes2_front3_no smile_close at right
    hide sy
    show sy clothes2_front1 smile_close at left
    hide yellow_tint
    show expression Solid("#ffa200") as yellow_tint:
        alpha 0.12
    with dissolve

    "晚上窝在沙发上看电影，时语会不知不觉靠在我肩上睡着，星弥会抱着抱枕坐在地毯上，脑袋轻轻靠在我腿边。"


    scene bg_living_room_2
    with Fade(0.5, 0.5, 0.5)
    show bg_living_room_2:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve

    "这样的日常，简单，温暖，让我这个习惯了独居的社畜，体会到「 有人陪伴 」是什么样的感觉。"
    "但……这一切，其实都建立在她们是「 特殊 」的基础上。"
    "如果当初推开门看到的是两个成年女性，我大概会立刻报警。"
    "如果她们只是普通的人类女孩，我可能会请她们离开，或者帮她们联系家人。"
    "但她们不是。"
    "她们有着少女的外表，却是活了上百年的血族和魔女。"
    "这种巨大的反差，让我从一开始就给自己找了个借口——"


    scene black
    with Fade(0.5, 0.5, 0.5)

    "她们会魔法，我反抗不了。"
    "她们看起来没有恶意，就先让她们住下吧。"
    "反正只是暂时的。"


    scene bg_living_room_2
    with Fade(0.5, 0.5, 0.5)
    show bg_living_room_2:
        zoom 1.06
        xalign 0.5
        yalign 1.0
    with dissolve

    "我用这些理由说服自己，让自己相信，留下她们是不得已的选择。"
    "——但真的是这样吗？"
    "真的只是因为「 无法反抗 」吗？"

    show bg_living_room_2:
        zoom 1.10
        xalign 0.5
        yalign 1.0
    with dissolve

    "还是说……其实是我自己，想要有人陪伴？"
    "……是啊。"
    "从家乡来到这座城市工作后，我就日复一日地过着两点一线的生活。"
    "在这个陌生的地方，我渴望生活能有些不一样，渴望有人能陪伴在身边，让这个家不再那么安静。"
    "但大城市的人太过冷漠，而活在大城市的我，也太过懦弱。"
    "我没有主动迈出那一步的勇气……直到她们的出现。"

    show bg_living_room_2:
        zoom 1.14
        xalign 0.5
        yalign 1.0
    with dissolve

    "……没错。"
    "是我自己，害怕回到那个空荡荡、静悄悄的家。"
    "是我自己，害怕再次回到只有自己的日子。"
    "是我自己，贪恋这份有人陪伴的温暖，所以才装作不知道三个月的约定早已过去，装作这样的日子可以一直持续下去，不用面对任何改变。"
    "但现实是……她们随时可能离开。"
    "是我需要她们，不是她们需要我。"

    show bg_living_room_2:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve

    "信纸在茶几上静静躺着，像两道无声的宣告。"
    "如果她们选择离开……这个家，就会变回只有我自己一个人的样子了。"
    "既然如此，只要没有这两封信，她们是不是就不会离开我呢？"
    "我甚至萌生出了想把信藏起来、假装没看到的想法。"
    "……不，那么做也只是在自欺欺人而已。"
    "深呼吸，调整好情绪后，我拿起这两封信，准备把信上的事告诉她们。"
    "——然后，我看到了茶几上放着的几张便签。"
    "有的是时语写的，上面工工整整地记着我教她的游戏攻略。"
    "有的是星弥写的，上面认真记着我教她做家务时的注意事项。"


    scene bg_living_room_2
    with Fade(0.5, 0.5, 0.5)

    "看到这几张便签，和她们相处的点点滴滴又一次浮现在脑海里。"
    lxc_ "哈。"
    "……这样啊。"

    play music bgm_19 fadeout 1.0 fadein 1.0

    "确实，我需要她们，需要得不得了。"
    "但这并不意味着，这只是我单方面的想法。"
    "至少，在听到她们真实的想法之前，我还不能就这样放弃。"
    "我再次调整自己内心的情绪，逐渐平息这份涌动出来的不安、郁闷和纠结。"
    "这份感情……或许就是喜欢吧。"
    "我喜欢时语故作高傲却会偷偷关心人的样子，喜欢星弥天真烂漫却敏感细腻的内心。"
    "两种喜欢，一样多，一样重要。"
    "这很贪心吗？也许吧。"
    "但从最开始，在我决定让她们住下来的那一刻开始，这个选择本身就带着我自己的私心。"
    "哪怕明白这是不能做的事，但当时的我，还是为了自己的私心而这么做了。"
    "既然如此，那现在不过是用另一份私心，再做一件同样不该做的事而已。"
    "这就是我真实的想法。我不想再骗自己，更不想欺骗她们。"
    "这份由私心开始的关系，就让它因为私心而结束吧。"


    scene bg_living_room_2
    with Fade(0.5, 0.5, 0.5)
    show bg_living_room_2:
        zoom 1.04
        xalign 0.5
        yalign 1.0
    with dissolve

    lxc_ "时语，星弥，我有话要和你们说。"
    "我伸手准备敲门，房门却先一步从里面打开了。"

    show sy clothes2_front1 focus at left with dissolve
    show xm clothes2_front3_no bewilderment at right with dissolve

    sy_ "怎么了？"
    xm_ "林先生，是发生了什么事吗？"

    lxc_ "嗯，有些话想告诉你们。"
    "我尽量让声音听起来平静一点，但手心已经在微微冒汗了。"
    "她们对视一眼，慢慢从房间里走出来。"
    "我走到茶几前，拿起那两封信。"

    show xm oo kp1wl at emphasis_pop
    xm_ "这是……老师寄过来的信？"
    "星弥看到信封上熟悉的字迹，手指不自觉地握紧了。"
    show xm hide_fx with dissolve

    lxc_ "刚才我回来的时候，发现它们放在了门口。"
    lxc_ "明明是给你们的信，但收信人写的却是我，真是奇怪呢。"
    "时语接过信，看到里面的内容时，眉头微微皱起。"

    show sy sigh with dissolve
    "星弥也接过自己的那封信，表情变得认真起来。"

    show xm focus with dissolve
    play music bgm_15 fadeout 1.0 fadein 1.0
    "客厅里很安静，只有信纸展开的沙沙声。"
    "我坐在她们对面，看着她们读信时的表情——时语的嘴唇抿得紧紧的，星弥的小腿无意识地轻轻晃动着，透露出内心的不安。"

    lxc_ "看完了吗？"

    show sy bewilderment with dissolve
    show xm sigh with dissolve

    sy_ "嗯。"
    xm_ "我看完了……"
    "看到她们的表情，不用说我也能猜到她们现在的心情了。"
    "我走到窗边，轻轻推开了窗户，让傍晚微凉的风吹进来。"

    lxc_ "你们觉得在这边的生活怎么样？"
    lxc_ "比起里世界，会不会差很多？"

    show sy focus with dissolve
    sy_ "……至少从我来到表世界后，在这里是过得最开心的。"
    sy_ "比在城堡里自在很多，和你……相处得也很融洽。"
    "她侧过头，撩了撩自己的银发，用带着点暗示的眼神瞥了我一眼。"

    sy_ "如果回去之后，也有这么舒服的环境就好了。"

    show xm smile at nod_small
    xm_ "嗯，我也是这么想的。"
    xm_ "虽然我没在表世界的其他地方住过，但林先生家是我开始旅行后，住得最舒服的地方！"

    lxc_ "你们住得开心，那就好。"
    "我坐回座位上。"

    lxc_ "其实，我有想过偷偷把这两封信藏起来的。"

    show xm oo kp1wl at emphasis_pop
    xm_ "欸？"
    show xm hide_fx with dissolve

    show sy bewilderment with dissolve
    sy_ "那你为什么没这么做呢？"

    show xm shy with dis_master

    lxc_ "毕竟这样做，既不尊重你们，也是在自欺欺人嘛。"
    lxc_ "至少在和你们相关的事情上，我想靠自己认可的方法来争取。"
    lxc_ "也许不是最好的，但至少是我觉得最正确的方法。"
    lxc_ "我也……挺喜欢和你们相处的这段时间。"
    "我顿了顿，感觉喉咙有点干。"

    lxc_ "不，不仅仅是挺喜欢，是非常喜欢才对。"
    lxc_ "所以，我希望你们能留下来。"
    lxc_ "我希望，以后也能和你们一起生活下去。"
    lxc_ "因为我——"

    show sy pout at angry_stomp
    sy_ "但我们留下来的话，会给你带来麻烦的哦？"
    "时语突然开口，打断了我原本想说的话。"

    lxc_ "……即便如此，我还是希望你们能留下来。"
    lxc_ "毕竟——"

    show sy clothes2_side2 cat_mouth with dissolve
    sy_ "哼哼，这样啊，你就这么~想和我们住在一起啊。"
    sy_ "真拿你没办法呢。"
    "时语似乎很满意我的回答，又一次打断了我的话。"

    sy_ "星弥你呢？既然他都这么说了，你愿意留下来吗？"

    show xm smile at nod_small
    xm_ "嗯嗯，我当然愿意！"
    xm_ "我也很想继续和大家一起生活！"
    xm_ "不过，这样的话就得给老师回信才行。"
    "她托着下巴，开始认真思考起来。"

    show sy bewilderment with dissolve
    sy_ "呼……"
    "时语松了口气，嗔怪地看了我一眼。"

    show xm smile at nod_small
    xm_ "既然信能寄过来，那老师她多半也知道我们这边的情况。"
    xm_ "不过，我还没有向她正式介绍过大家呢。"
    show xm shy at nod_small
    xm_ "该怎么介绍好呢？时语是好朋友，林先生的话……"

    xm_ "是啊……我们和林先生之间的关系该怎么说好呢……"
    show sy sigh with dis_master
    xm_ "朋友？同居人？还是……哎？时语你为什么要这样看着我？"
    xm_ "还有林先生也是，第一次见您露出这样的表情呢。"


    "时语的表情有点复杂，想必我自己的表情也不太自然吧。"

    show xm bewilderment with dissolve
    xm_ "是我问了什么奇怪的问题吗？"
    "恐怕星弥会这么问，也超出了时语的预料。"

    sy_ "……没，星弥你什么都没做错。"
    sy_ "只是这个笨蛋……唉。"
    "时语猜到了我要做什么，有些无奈地轻轻摇头。"

    lxc_ "……嗯，和时语说的一样，星弥你什么也没做错。"
    lxc_ "不如说，你做得很对，谢谢。"
    lxc_ "还有，时语也一样，谢谢你。"
    "或许是因为时语刚才刻意地引导，让我差点逃避了一直悬挂在我们头顶的问题。"
    "但正是星弥这份单纯的疑问，让我不得不再次正视它。"
    "如果想得到什么，就要付出相应的代价。"
    "如果我贪求什么，就要有拿出相应觉悟的勇气。"

    play music bgm_13 fadeout 1.0 fadein 1.0

    lxc_ "我希望你们能留下来，其实还有一个很简单的理由。"
    lxc_ "我喜欢你们。"
    lxc_ "不是单独喜欢其中一个，而是……时语和星弥我都喜欢。"
    lxc_ "和你们一起相处，一起生活的这段时间，我很开心，很难忘，我不希望你们离开我。"
    lxc_ "我害怕你们离开，害怕失去你们之后，自己又会变回原来那个样子。"

    call achievement (18) from _call_achievement_22

    show xm oo kp1wl at shocked_step_back
    "听到我这么说，星弥惊讶地张开嘴巴。"
    show xm hide_fx with dissolve

    show sy pout with dissolve
    "时语则像是早有预料，露出有点生气的表情。"

    sy_ "……你知道自己在说什么吗？"

    lxc_ "我知道，我也考虑过后果了，但我不会后悔的。"

    show xm oo at emphasis_pop
    xm_ "等等，我、我有点乱了……"
    xm_ "林先生喜欢我……？但又不只是喜欢我……还喜欢时语……"
    xm_ "在这边，一个人是可以同时喜欢上两个人的吗？"

    lxc_ "不，一般来说是不行的。"
    lxc_ "至少，这样的行为在大众眼里是不被允许的。"
    lxc_ "所以，我刚刚说的话，其实是很任性的。"

    show xm shy skin_blush at look_away_small
    xm_ "这样啊……"
    "星弥低下头，手指不安地抓着裙摆。"

    xm_ "抱歉，喜欢之类的感情，对我来说有点太……"
    xm_ "而且林先生还是一次喜欢上了我们两个……我想自己需要点时间冷静一下……！"
    hide xm with dissolve
    show sy at center with dissolve
    "她抱起沙发上的抱枕，把脸埋了进去，只露出微微发红的耳尖。"

    show sy pout at angry_stomp
    sy_ "……哼，你满意了？"
    sy_ "让星弥感到困惑，让我觉得生气，唯独自己一股脑地发泄完想法……这就是你想要的结果？"
    "时语看向我，赤红的眼瞳里带着复杂的情绪。"

    lxc_ "怎么可能，我从来没有想过让你们难过。"
    lxc_ "我只是希望在结束前，向你们表达自己的真实想法。"

    show sy bewilderment with dissolve
    sy_ "……"
    sy_ "我刚刚都已经在尽力阻止事情发展到这个地步了，结果还是……"
    "她咬了咬嘴唇，表情有点不甘。"

    sy_ "我是希望你说让我们能留下，但我没想到你会主动选择表白。"
    sy_ "……哪怕你不提这个事，假装和以前一样糊弄过去也好啊。"
    sy_ "你主动说了喜欢我们，那我们现在的关系还怎么维持下去啊……"

    lxc_ "哪怕这次逃避了，以后也迟早会遇到同样的问题。"
    lxc_ "难道要等里世界的人把你们带走了，等你们不在了，我才说吗？"
    lxc_ "我已经欺骗自己够久了，我不想再连你们也骗了。"

    show sy astonished kp1wl with dissolve
    "听到我这么说，时语终于露出了惊讶的表情。"
    show sy hide_fx with dissolve

    sy_ "……那你就没想过，我和星弥可能会因为你这么说而离开吗？"
    "她站起来，走到我面前，仰起脸看着我。"

    lxc_ "我想过，不如说你们这么做才是正常的。"
    lxc_ "但至少，我这么说了之后，你们是因为我的告白而主动选择离开，而不是因为什么家族命令，不情不愿地离开，不是吗？"

    show sy pout at angry_stomp
    sy_ "啧，你这别扭的男人啊……"
    "时语抓住我的衣袖，明明应该是很生气的样子，但她的语气里却听不出太多的怒意。"
    "而且，因为身高的关系，她这样仰头看着我的样子，反而有点像在……撒娇。"

    sy_ "这种时候你强硬一点不就——"
    show sy at left with dis_master
    show xm clothes2_front3_no bewilderment kp15wl at right with dissolve
    xm_ "——不、不要吵架了！！！"
    show xm hide_fx with dissolve
    "一直躲在抱枕后的星弥，听到我们的争论，终于忍不住出声阻止了。"

    show sy astonished kp1wl at shocked_step_back
    "时语张了张嘴，却发不出声音。"
    show sy hide_fx with dissolve

    "我也想说些什么，同样发不出声音。"
    "看来是星弥用了某种让人暂时沉默的魔法。"

    show xm pout at angry_stomp
    xm_ "明明时语和林先生都是在为对方着想，但是为什么要吵起来呢……"

    show sy shy at look_away_small
    "时语抱起手臂，满脸「 我才没有为这个家伙着想呢 」的表情。"
    "我也无奈地看向别处，也没法解释「 我们其实没在争吵 」。"

    "等我们都冷静下来后，星弥才解除了魔法。"

    show xm focus with dissolve
    xm_ "我刚刚一直在思考，林先生说那番话的含义。"
    xm_ "在我眼里，林先生很善良，但同时又……有点随性，不会对什么事都特别较真。"
    xm_ "您接纳了我们，这份接纳却不是溺爱，也不是毫无原则的纵容。"

    show xm smile with dissolve
    "星弥走到我身边，轻轻握住我的手。"

    xm_ "明明没有义务，但您还是选择了让我们住下。"
    xm_ "明明可以提出要求，但您却几乎没有对我们说过『 必须这样做 』。"
    xm_ "林先生真的……是一个很奇怪的人呢，明明这样做，对您自己完全没有好处啊。"
    "她握着我的手微微用力。"

    xm_ "但正因为您是这样的人，所以我们在这里生活的这段时间，才会过得如此自由和开心。"
    xm_ "所以我才会……打从心底里相信您，信赖您。"

    show sy smile_close with dissolve

    xm_ "而这样的您，现在却主动选择用这么任性的方式向我们表白。"
    xm_ "这说明，在您眼中，我和时语就是这么重要吧。"
    xm_ "重要到，让您做出了平时不会做的事，说出了平时不会说的话。"

    lxc_ "星弥……"

    show xm focus at nod_small
    xm_ "虽然我还不太懂自己内心的这股感情是什么，虽然我还只是一个不懂爱的魔女。"
    xm_ "但现在，我想弄明白，我想好好回应您的这份心意。"
    "星弥抬起手，轻轻擦了擦眼角。"

    xm_ "所以，我想继续这样的日子。"

    show xm smile skin_blush with dissolve
    xm_ "在接下来的时间里，和林先生、还有时语一起，慢慢找到自己内心的答案。"

    "说实话，她的回答超出了我的意料。"

    lxc_ "但是，这样的话……"
    "看到星弥真诚的眼神，我一时间不知道该怎么面对，连忙移开视线，看向时语。"
    "只见她对星弥的话很满意，完全没有生气和不满。"

    lxc_ "时语你呢？你能接受吗？明明刚刚还挺生气的……"

    show sy cat_mouth at look_away_small
    sy_ "干嘛，你自己擅自表的白，现在倒是害怕起来了？"
    "时语轻轻掐了我的手臂一下。"

    sy_ "我刚才生气的主要原因，不是因为你同时向我们表白。"

    lxc_ "……啊？"

    show sy shy with dissolve
    sy_ "硬要说的话可能会有一点点生气吧。"
    "她又轻轻掐了一下。"

    sy_ "但我真正在意的，或者说害怕的是……我担心这个家会因此变得和以前不一样了。"
    sy_ "你那样贸然告白，我害怕我们之间的关系再也回不到以前那样了。"
    sy_ "也许有些事迟早会改变，但我不希望是今天，不希望是因为这种猝不及防的方式。"

    lxc_ "时语……"

    show sy sigh with dissolve
    sy_ "不然你以为我刚刚为什么那么刻意地想阻止你表白啊？"

    show xm focus at emphasis_pop
    xm_ "啊，怪不得刚刚时语好几次打断了林先生说话呢。"

    "星弥这才恍然大悟。"

    show sy not_good with dissolve
    sy_ "是啊，结果还是……唉。"
    "时语看向我和星弥，叹了口气。"

    sy_ "哪有人一上来就直接表白的啊……至少平时多暗示一下，让我们有个心理准备也好呀？"

    lxc_ "等等……你们真的，愿意接受我刚刚的表白？"
    lxc_ "这可是意味着，我们要三个人一起……"

    show sy shy skin_blush at look_away_small
    sy_ "自从我意识到自己喜欢你之后，我就想过这种可能性了。"
    sy_ "毕竟是我们自己擅自闯入你的生活，所以……总得负点责任吧？"

    show xm smile skin_blush at nod_small
    xm_ "难道林先生并不愿意？明明已经表白了？"

    lxc_ "不，我只是……没想过你们真的会接受。"
    "各种情绪涌上心头，让我的大脑一时难以理清。"
    "我原本以为，她们会生气，会失望，会听从信上的劝告离开。"
    "哪怕理想一点，我也只会觉得她们会友好地和我道别。"
    "我并没有奢求过她们会真的接受。"
    "但现在——"

    lxc_ "毕竟这是我完全任性的行为啊……"

    show sy smile_close with dissolve
    sy_ "明明最初你都愿意让我们住下来了，现在任性一点又有什么关系呢？"

    show xm smile_close with dissolve
    xm_ "是啊，您可是即将成为魔女伴侣的人，随心所欲一点也没关系吧？"

    lxc_ "是吗，这样啊……"
    "我低下头，感觉脸颊在发烫。"
    "恐怕我的脸已经红得不像样了。"
    "血液好像在沸腾，大脑也在发热。"

    lxc_ "明明是应该开心的事，但我却感觉有点……"

    show sy cat_mouth with dissolve
    sy_ "嗯嗯，我懂我懂。"
    sy_ "这种情况叫什么……内心的负罪感来着？"
    sy_ "一件本不被期待发生的事，以一种意料之外的方式实现了。"
    sy_ "所以就一时之间有点难以接受，对吧？"

    show xm astonished kp1wl with dissolve
    xm_ "欸……是这样吗？"
    show xm hide_fx with dissolve

    show sy cat_mouth at lean_in
    sy_ "是啊，所以这时候就应该——"
    "时语踮起脚靠到我耳边，压低声音，带着一点捉弄的语气。"
    sy_ "渣男，变态，萝莉控~"

    lxc_ "……最后一个也太过分了吧。"

    show sy cat_mouth at look_away_small
    sy_ "反正你就是想被骂几句吧？被说了之后，是不是心里的负担就轻松一点了呢？"

    lxc_ "我不是，我没有……"

    sy_ "哼……反正你也知道我没有真的在骂你，你就让我过过嘴瘾嘛。"
    "看到时语的行为，星弥也有样学样地俯身到我另一边耳朵。"

    show xm shy skin_blush at lean_in
    xm_ "我、我……我不会骂人啊，呜呜……"

    show sy smile with dissolve
    sy_ "没关系的，你想到什么就说什么就好。"

    show xm cat_mouth with dissolve
    xm_ "那……其实，我曾经有段时间并不太信任林先生你哦？"

    lxc_ "欸，不会吧？"

    xm_ "真的哦，虽然只是刚认识没多久的时候就是啦……"
    "那么善解人意的星弥，居然怀疑过我……"
    "我两腿一软，差点倒在地上。"

    show xm oo kp1wl at shocked_step_back
    xm_ "林先生？！"

    show sy oo kp1wl at shocked_step_back
    sy_ "别突然倒下啊？！"
    show xm hide_fx with dissolve
    show sy hide_fx with dissolve
    "她们两个连忙把我扶住。"

    show sy bewilderment with dissolve
    sy_ "不会是因为刚刚骂得太狠了吧……？"

    lxc_ "和那个没关系……就是有点冷而已……阿嚏！"
    "啊，有点不妙呢，回过神来全身都有点发冷……"
    "大概是因为，刚刚淋了那场雨吧。"

    show sy oo kp1wl at emphasis_pop
    sy_ "你、你的额头好烫啊！"

    show xm oo kp1wl at emphasis_pop
    xm_ "……我立刻用魔法给你冰敷！"
    show sy hide_fx with dissolve
    show xm hide_fx with dissolve
    "她们两个一左一右搀扶着我，手忙脚乱的样子。"
    "总感觉，这一幕有点像我们刚见面的时候呢。"
    "明明额头烫得厉害，我却不自觉地回想起了那天的事。"

    lxc_ "……哈哈。"

    show xm cry skin_cry at look_away_small
    xm_ "呜呜，林先生脑子被烧坏了……！"

    show sy pout at angry_stomp
    sy_ "你别傻笑啦！真的很吓人啊！"

    jump story_826_part5
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
