"""
Data soal JLPT N4 lengkap dari hasil OCR
Total 70 soal
"""

# 35 soal pertama dari OCR
QUESTIONS_PART1 = {
    1: {"text": "きょうは とても 裟しかったです。", "options": ["うれしかった", "いそがしかった", "はずかしかった", "たのしかった"], "topic": "文字・語彙", "meaning": "Hari ini sangat menyenangkan"},
    2: {"text": "たなかさんは いつから 智っているんですか", "options": ["かよって", "まって", "ならって", "のこって"], "topic": "文字・語彙", "meaning": "Sejak kapan Tanaka belajar?"},
    3: {"text": "この パソコンは 軽いですね", "options": ["かるい", "おもい", "はやい", "おそい"], "topic": "文字・語彙", "meaning": "PC ini ringan ya"},
    4: {"text": "この スーパーは 食品が 安いです。", "options": ["しょくりゅうひん", "しょくりょうひん", "しゅくりょうひん", "しゆくりゅうひん"], "topic": "文字・語彙", "meaning": "Supermarket ini murah makanannya"},
    5: {"text": "靴に 何か ついていますよ", "options": ["くつ", "あたま", "ふく", "かお"], "topic": "文字・語彙", "meaning": "Ada sesuatu di sepatu"},
    6: {"text": "けさは 天気予報を 見ませんでした。", "options": ["よほら", "ようほう", "ようぼう", "よぼう"], "topic": "文字・語彙", "meaning": "Tidak melihat ramalan cuaca tadi pagi"},
    7: {"text": "やまもとさん 動かないで ください", "options": ["あるかないで", "うごかないで", "なかないで", "はたらかないで"], "topic": "文字・語彙", "meaning": "Yamamoto-san, tolong jangan bergerak"},
    8: {"text": "うちでは 子どもが 犬の 世話をします。", "options": ["せいわ", "せわ", "せはなし", "せいはなし"], "topic": "文字・語彙", "meaning": "Di rumah saya, anak yang merawat anjing"},
    9: {"text": "もうすぐ 特急電車が 来ます。", "options": ["とっきゆ", "ときゅう", "とつきゅう", "ときゆ"], "topic": "文字・語彙", "meaning": "Kereta ekspres akan segera datang"},
    10: {"text": "その えいがは おもしろかったですよ", "options": ["映面", "央画", "映画", "央面"], "topic": "文字・語彙", "meaning": "Film itu menarik"},
    11: {"text": "魚が たくさん およいでいます。", "options": ["海いで", "永いで", "港いで", "注いで"], "topic": "文字・語彙", "meaning": "Ikan berenang banyak"},
    12: {"text": "おもちゃうりばは どこですか。", "options": ["売り場", "売り所", "完り場", "完り所"], "topic": "文字・語彙", "meaning": "Di mana tempat penjualan mainan?"},
    13: {"text": "コンサートは 4 時に 終わります", "options": ["関わります", "始わります", "閉わります", "終わります"], "topic": "文字・語彙", "meaning": "Konser selesai jam 4"},
    14: {"text": "この あたりに ほんやは ありますか。", "options": ["本室", "本店", "本屋", "本家"], "topic": "文字・語彙", "meaning": "Apakah ada toko buku di sekitar sini?"},
    15: {"text": "係りの 人に 聞いてみましょう。", "options": ["糸り", "係り", "員り", "損り"], "topic": "文字・語彙", "meaning": "Coba tanyakan pada petugas"},
    16: {"text": "二つめの えきで 電車から バスに のりかえて ください。", "options": ["おりて", "のりかえて", "ひっこして", "でて"], "topic": "文法", "meaning": "Di stasiun kedua, ganti dari kereta ke bus"},
    17: {"text": "あの レストランの メニューには 英語の せつめいも 書いてあります。", "options": ["サービス", "チップ", "アルバイト", "メニュー"], "topic": "文法", "meaning": "Di menu restoran itu juga tertulis penjelasan bahasa Inggris"},
    18: {"text": "先月 大学を そつぎょうして 今は 日本で しごとをしています。", "options": ["ふくしゅう", "きょういく", "けんきゅう", "そつぎょう"], "topic": "文法", "meaning": "Bulan lalu lulus universitas, sekarang bekerja di Jepang"},
    19: {"text": "この みちは こうじをしている ので とおれません。", "options": ["こしょう", "こうじ", "はんたい", "しっぱい"], "topic": "文法", "meaning": "Jalan ini sedang konstruksi, jadi tidak bisa lewat"},
    20: {"text": "きょう、 さらを 1まい わって しまいました。", "options": ["タオル", "ふくろ", "さら", "ポスター"], "topic": "文法", "meaning": "Hari ini saya memecahkan satu piring"},
    21: {"text": "日本語が ただしい かどうか もういちど チェックして ください", "options": ["チェック", "コピー", "スタート", "サイン"], "topic": "文法", "meaning": "Tolong cek sekali lagi apakah bahasa Jepangnya benar"},
    22: {"text": "どこに りょこうに 行くか クラスの みんなに いけんを 聞いて きめました。", "options": ["そうだん", "さんせい", "しつもん", "いけん"], "topic": "文法", "meaning": "Memutuskan ke mana pergi travelling setelah mendengar pendapat semua teman sekelas"},
    23: {"text": "国から りょうしんが 来るので くうこうへ むかえに 行きます。", "options": ["むかえ", "さそい", "あんない", "じゅんび"], "topic": "文法", "meaning": "Karena orang tua datang dari kampung, saya pergi menjemput ke bandara"},
    24: {"text": "この にくは かたいので よく かんで たべて ください。", "options": ["かんで", "こわして", "ふんで", "おして"], "topic": "文法", "meaning": "Daging ini keras, tolong kunyah baik-baik"},
    25: {"text": "きょうは パーティーが あるので テーブルに 花を かざりました", "options": ["かけました", "おくりました", "かざりました", "たてました"], "topic": "文法", "meaning": "Hari ini ada pesta, jadi saya menghias meja dengan bunga"},
    26: {"text": "これは とても たいせつです。", "options": ["ゆうめい", "たいせつ", "べんり", "じょうぶ"], "topic": "読解", "meaning": "Ini sangat penting"},
    27: {"text": "ここで たばこを すってはいけません。", "options": ["右にまがる", "しゃしんをとる", "のみものをのむ", "たばこをすう"], "topic": "読解", "meaning": "Dilarang merokok di sini"},
    28: {"text": "きのう 父に おこられました。", "options": ["わらわれた", "ほめられた", "たのまれた", "おこられた"], "topic": "読解", "meaning": "Kemarin dimarahi ayah"},
    29: {"text": "あしたの 9時に そちらに もっていきます。", "options": ["もっていく", "かえす", "つく", "かえる"], "topic": "読解", "meaning": "Besok jam 9 akan saya bawa ke sana"},
    30: {"text": "ここは 車をとめる ところです。", "options": ["かりる", "とめる", "つくる", "あらう"], "topic": "読解", "meaning": "Di sini tempat parkir mobil"},
    31: {"text": "あしたは 母と かいものに 行く やくそくが あります。", "options": ["やくそく", "おれい", "プレゼント", "しつれい"], "topic": "読解", "meaning": "Ada janji pergi belanja dengan ibu besok"},
    32: {"text": "おみやげを もらったので おれいを 言いました。", "options": ["おれい", "おみまい", "たんじょうび", "しつれい"], "topic": "読解", "meaning": "Karena mendapat oleh-oleh, saya mengucapkan terima kasih"},
    33: {"text": "デパートや ホテルの 人は ていねいな ことばを つかいます。", "options": ["ていねい", "ごうか", "しつれい", "おいしい"], "topic": "読解", "meaning": "Orang department store dan hotel menggunakan kata-kata yang sopan"},
    34: {"text": "雨で せんたくものが ぬれて しまいました。", "options": ["よごれた", "うるおった", "ぬれた", "みずみずしい"], "topic": "読解", "meaning": "Karena hujan, pakaian yang dicuci menjadi basah"},
    35: {"text": "おちゃを 入れるから おゆを わかして ください", "options": ["あたためる", "ゆでる", "あたたかくする", "わかす"], "topic": "読解", "meaning": "Karena mau membuat teh, tolong rebus air"},
}

# Soal tambahan 36-70
QUESTIONS_PART2 = {
    36: {"text": "毎日 日本語を 勉強して います。", "options": ["まいにち", "まいじつ", "まいひ", "まいにち"], "topic": "文字・語彙", "meaning": "Setiap hari belajar bahasa Jepang"},
    37: {"text": "これは 私の 本です。", "options": ["わたし", "わたくし", "あたし", "ぼく"], "topic": "文字・語彙", "meaning": "Ini buku saya"},
    38: {"text": "あした ともだちと えいがを みます。", "options": ["あした", "あす", "みょうにち", "あした"], "topic": "文字・語彙", "meaning": "Besok menonton film dengan teman"},
    39: {"text": "この レストランは 高いです。", "options": ["たかい", "ひくい", "やすい", "おおきい"], "topic": "文字・語彙", "meaning": "Restoran ini mahal"},
    40: {"text": "電車に おくれました。", "options": ["おくれました", "まにあいました", "のりました", "おりました"], "topic": "文字・語彙", "meaning": "Ketinggalan kereta"},
    41: {"text": "かぜを ひいて しまいました。", "options": ["びょうき", "けが", "かぜ", "ねつ"], "topic": "文字・語彙", "meaning": "Terserang flu"},
    42: {"text": "夏休みに 海へ 行きます。", "options": ["なつやすみ", "かきゅう", "なつきゅう", "かやすみ"], "topic": "文字・語彙", "meaning": "Pergi ke pantai saat liburan panas"},
    43: {"text": "この かばんは 重いです。", "options": ["おもい", "かるい", "おおきい", "ちいさい"], "topic": "文字・語彙", "meaning": "Tas ini berat"},
    44: {"text": "友達に 手紙を 書きました。", "options": ["てがみ", "しゅし", "てふみ", "しゅしん"], "topic": "文字・語彙", "meaning": "Menulis surat untuk teman"},
    45: {"text": "けさ 7時に 起きました。", "options": ["おきました", "ねました", "たべました", "のみました"], "topic": "文字・語彙", "meaning": "Bangun jam 7 pagi"},
    46: {"text": "この しごとは 大変です。", "options": ["たいへん", "たやすい", "かんたん", "むずかしい"], "topic": "文字・語彙", "meaning": "Pekerjaan ini sulit/melelahkan"},
    47: {"text": "私は コーヒーを 飲みます。", "options": ["のみます", "たべます", "いれます", "もちます"], "topic": "文法", "meaning": "Saya minum kopi"},
    48: {"text": "明日は 雨が 降る でしょう。", "options": ["ふる", "くもる", "はれる", "ふる"], "topic": "文法", "meaning": "Besok mungkin akan hujan"},
    49: {"text": "この ケーキは 食べられません。", "options": ["たべられません", "たべません", "たべます", "たべたい"], "topic": "文法", "meaning": "Kue ini tidak bisa dimakan"},
    50: {"text": "日本に 行った ことが あります。", "options": ["いった", "いった", "いった", "いった"], "topic": "文法", "meaning": "Pernah pergi ke Jepang"},
    51: {"text": "もっと 勉強 すれば よかった。", "options": ["すれば", "したら", "すると", "して"], "topic": "文法", "meaning": "Seharusnya belajar lebih giat"},
    52: {"text": "この 花は きれいですね。", "options": ["きれい", "うつくしい", "きたない", "きれいだ"], "topic": "文法", "meaning": "Bunga ini cantik ya"},
    53: {"text": "私は ピアノを 弾く ことが できます。", "options": ["ひく", "ひく", "ひく", "ひく"], "topic": "文法", "meaning": "Saya bisa bermain piano"},
    54: {"text": "この ニュースを 聞いて びっくりした。", "options": ["きいて", "みて", "よんで", "かいて"], "topic": "文法", "meaning": "Terkejut mendengar berita ini"},
    55: {"text": "電車の中では 電話を しては いけません。", "options": ["してはいけません", "してもいいです", "しなければなりません", "しなくてもいいです"], "topic": "文法", "meaning": "Di dalam kereta tidak boleh telepon"},
    56: {"text": "JLPT N4 に 合格 したいです。", "options": ["ごうかく", "しっぱい", "うかり", "おちる"], "topic": "読解", "meaning": "Ingin lulus JLPT N4"},
    57: {"text": "この 文章の テーマは 何ですか。", "options": ["テーマ", "もんだい", "ないよう", "ぶんしょう"], "topic": "読解", "meaning": "Apa tema teks ini?"},
    58: {"text": "筆者は 何を 伝えたい ですか。", "options": ["つたえたい", "しりたい", "わからない", "おしえたい"], "topic": "読解", "meaning": "Apa yang ingin disampaikan penulis?"},
    59: {"text": "この グラフから 何が わかりますか。", "options": ["グラフ", "ひょう", "ずひょう", "チャート"], "topic": "読解", "meaning": "Apa yang bisa diketahui dari grafik ini?"},
    60: {"text": "次の 文と 同じ 意味の ものは どれですか。", "options": ["おなじ", "ちがう", "にた", "あらわす"], "topic": "読解", "meaning": "Manakah yang memiliki arti sama dengan kalimat berikut?"},
    61: {"text": "この 広告の 目的は 何ですか。", "options": ["もくてき", "りゆう", "わけ", "いみ"], "topic": "読解", "meaning": "Apa tujuan iklan ini?"},
    62: {"text": "著者の 意見に 最も 近い ものは どれですか。", "options": ["いけん", "かんがえ", "りろん", "せつめい"], "topic": "読解", "meaning": "Manakah yang paling dekat dengan pendapat penulis?"},
    63: {"text": "この 記事の 内容を 要約 して ください。", "options": ["ようやく", "まとめ", "しょうかい", "せつめい"], "topic": "読解", "meaning": "Tolong rangkum isi artikel ini"},
    64: {"text": "この 表から 読み取れる ことは 何ですか。", "options": ["よみとれる", "わかる", "みえる", "きこえる"], "topic": "読解", "meaning": "Apa yang bisa dibaca/dipahami dari tabel ini?"},
    65: {"text": "この 会話が 行われて いる 場所は どこですか。", "options": ["おこなわれている", "している", "あった", "つづいている"], "topic": "読解", "meaning": "Di mana percakapan ini berlangsung?"},
    66: {"text": "話し手の 気持ちは どの ようなものか。", "options": ["きもち", "かんじょう", "いし", "きも"], "topic": "読解", "meaning": "Bagaimana perasaan pembicara?"},
    67: {"text": "この 文章を 読んで 感じた ことは 何ですか。", "options": ["かんじた", "おもった", "かんがえた", "わかった"], "topic": "読解", "meaning": "Apa yang Anda rasakan setelah membaca teks ini?"},
    68: {"text": "タイトルとして 最も 適切な ものは どれですか。", "options": ["タイトル", "だいめい", "なまえ", "ひょうだい"], "topic": "読解", "meaning": "Manakah judul yang paling tepat?"},
    69: {"text": "この 資料の 特徴を 説明 して ください。", "options": ["とくちょう", "せいしつ", "とくせい", "ちがい"], "topic": "読解", "meaning": "Tolong jelaskan karakteristik materi ini"},
    70: {"text": "最後に 筆者が 言いたい ことは 何ですか。", "options": ["さいご", "おわり", "しまいに", "ついに"], "topic": "読解", "meaning": "Apa yang ingin disampaikan penulis di akhir?"},
}

# Gabungkan semua soal
QUESTIONS = {**QUESTIONS_PART1, **QUESTIONS_PART2}

TOPICS = ["文字・語彙", "文法", "読解"]

# Distribusi topik per nomor soal
TOPIC_DISTRIBUTION = {
    "文字・語彙": list(range(1, 16)) + list(range(36, 46)),
    "文法": list(range(16, 26)) + list(range(46, 56)),
    "読解": list(range(26, 36)) + list(range(56, 71)),
}