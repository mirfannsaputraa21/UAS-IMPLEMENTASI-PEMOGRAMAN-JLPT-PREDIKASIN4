"""
Database soal JLPT N4 dan konstanta global
Sesuai standar penilaian JLPT N4 resmi
"""

# ============================================
# TARGET KELULUSAN (GABUNGAN 4 KATEGORI)
# ============================================
# JLPT N4: 言語知識・読解 digabung jadi satu nilai
# - Skor maksimal: 120 poin
# - Minimal lulus: 38 poin
#
# Input 4 kategori (Kanji, Kosakata, Grammar, Reading) dalam persen (0-100)
# Masing-masing berkontribusi 30 poin (120/4 = 30)
# Total Poin = (Kanji + Kosakata + Grammar + Reading) × 0.3

TOTAL_SCORE_TARGET = 38           # Target minimal lulus (38 poin)
MAX_SCORE = 120                   # Skor maksimal (120 poin)

# Warna untuk visualisasi
COLORS = {
    "primary": "#667eea",
    "success": "#22c55e",
    "warning": "#f59e0b",
    "danger": "#dc2626",
    "info": "#3b82f6"
}

# Status readiness
READINESS_STATUS = {
    0: {"label": "Belum Siap", "emoji": "🔴", "color": "danger"},
    1: {"label": "Hampir Siap", "emoji": "🟡", "color": "warning"},
    2: {"label": "Siap", "emoji": "🟢", "color": "success"}
}

# Tips belajar per topik
STUDY_TIPS = {
    "文字・語彙": {
        "tips": "📖 Perbanyak hafalan kosakata dan kanji JLPT N4 menggunakan flashcards",
        "resources": ["Minna no Nihongo Bab 26-50", "Try! JLPT N4 Vocabulary", "Anki Decks JLPT N4"],
        "daily_target": "15-20 kosakata + 5-10 kanji/hari"
    },
    "文法": {
        "tips": "📐 Latihan pola kalimat N4 setiap hari minimal 5 pola",
        "resources": ["Try! JLPT N4 Grammar", "Shin Kanzen Master Grammar N4", "Bunpro.jp"],
        "daily_target": "5-7 pola kalimat/hari"
    },
    "読解": {
        "tips": "📚 Baca teks pendek bahasa Jepang setiap hari 20 menit",
        "resources": ["Nihongo So-matome Reading N4", "NHK News Easy", "Satori Reader"],
        "daily_target": "2-3 teks pendek/hari"
    }
}

# ============================================
# DATA SOAL LENGKAP (70 SOAL)
# ============================================
QUESTIONS = {
    1: {"text": "きょうは とても 楽しかったです。", "options": ["うれしかった", "いそがしかった", "はずかしかった", "たのしかった"], "topic": "文字・語彙"},
    2: {"text": "たなかさんは いつから 習っているんですか", "options": ["かよって", "まって", "ならって", "のこって"], "topic": "文字・語彙"},
    3: {"text": "この パソコンは 軽いですね", "options": ["かるい", "おもい", "はやい", "おそい"], "topic": "文字・語彙"},
    4: {"text": "この スーパーは 食料品が 安いです。", "options": ["しょくりゅうひん", "しょくりょうひん", "しゅくりょうひん", "しゅくりゅうひん"], "topic": "文字・語彙"},
    5: {"text": "顔に 何か ついていますよ", "options": ["くつ", "あたま", "ふく", "かお"], "topic": "文字・語彙"},
    6: {"text": "けさは 天気予報を 見ませんでした。", "options": ["よほう", "ようほう", "ようぼう", "よぼう"], "topic": "文字・語彙"},
    7: {"text": "やまもとさん 動かないで ください", "options": ["あるかないで", "うごかないで", "なかないで", "はたらかないで"], "topic": "文字・語彙"},
    8: {"text": "うちでは 子どもが 犬の 世話をします。", "options": ["せいわ", "せわ", "せはなし", "せいはなし"], "topic": "文字・語彙"},
    9: {"text": "もうすぐ 特急電車が 来ます。", "options": ["とっきゅ", "ときゅう", "とっきゅう", "ときゅ"], "topic": "文字・語彙"},
    10: {"text": "その えいがは おもしろかったですよ", "options": ["映面", "央画", "映画", "央面"], "topic": "文字・語彙"},
    11: {"text": "魚が たくさん 泳いでいます。", "options": ["海いで", "泳いで", "港いで", "注いで"], "topic": "文字・語彙"},
    12: {"text": "おもちゃの 売り場は どこですか。", "options": ["売り場", "売り所", "完り場", "完り所"], "topic": "文字・語彙"},
    13: {"text": "コンサートは 4時に 終わります", "options": ["関わります", "始わります", "閉わります", "終わります"], "topic": "文字・語彙"},
    14: {"text": "この ちかくに 本屋は ありますか。", "options": ["本室", "本店", "本屋", "本家"], "topic": "文字・語彙"},
    15: {"text": "係りの 人に 聞いてみましょう。", "options": ["糸り", "係り", "員り", "損り"], "topic": "文字・語彙"},
    16: {"text": "二つめの 駅で 電車から バスに 乗り換えて ください。", "options": ["おりて", "のりかえて", "ひっこして", "でて"], "topic": "文法"},
    17: {"text": "あの レストランの メニューには 英語の 説明も 書いてあります。", "options": ["サービス", "チップ", "アルバイト", "メニュー"], "topic": "文法"},
    18: {"text": "先月 大学を 卒業して 今は 日本で 仕事をしています。", "options": ["復習", "教育", "研究", "卒業"], "topic": "文法"},
    19: {"text": "この 道は 工事をしている ので 通れません。", "options": ["故障", "工事", "反対", "失敗"], "topic": "文法"},
    20: {"text": "今日、皿を 1枚 割って しまいました。", "options": ["タオル", "袋", "皿", "ポスター"], "topic": "文法"},
    21: {"text": "日本語が 正しい かどうか もう一度 チェックして ください", "options": ["チェック", "コピー", "スタート", "サイン"], "topic": "文法"},
    22: {"text": "どこに 旅行に 行くか クラスの みんなに 意見を 聞いて 決めました。", "options": ["相談", "賛成", "質問", "意見"], "topic": "文法"},
    23: {"text": "国から 両親が 来るので 空港へ 迎えに 行きます。", "options": ["迎え", "誘い", "案内", "準備"], "topic": "文法"},
    24: {"text": "この 肉は 硬いので よく 噛んで 食べて ください。", "options": ["噛んで", "壊して", "踏んで", "押して"], "topic": "文法"},
    25: {"text": "今日は パーティーが あるので テーブルに 花を 飾りました", "options": ["掛けました", "送りました", "飾りました", "立てました"], "topic": "文法"},
    26: {"text": "これは とても 大切です。", "options": ["有名", "大切", "便利", "丈夫"], "topic": "読解"},
    27: {"text": "ここは 禁煙です。", "options": ["右に曲がる", "写真を撮る", "飲み物を飲む", "たばこを吸う"], "topic": "読解"},
    28: {"text": "昨日 父に 叱られました。", "options": ["笑われた", "褒められた", "頼まれた", "怒られた"], "topic": "読解"},
    29: {"text": "明日の 9時に そちらに 届けます。", "options": ["持っていく", "返す", "着く", "帰る"], "topic": "読解"},
    30: {"text": "ここは 車を 生産する ところです。", "options": ["借りる", "止める", "作る", "洗う"], "topic": "読解"},
    31: {"text": "約束", "options": ["予定", "約束", "予約", "日程"], "topic": "読解"},
    32: {"text": "お礼", "options": ["お礼", "お見舞い", "プレゼント", "失礼"], "topic": "読解"},
    33: {"text": "丁寧", "options": ["丁寧", "豪華", "失礼", "美味しい"], "topic": "読解"},
    34: {"text": "濡れる", "options": ["汚れた", "潤った", "濡れた", "みずみずしい"], "topic": "読解"},
    35: {"text": "沸かす", "options": ["暖める", "茹でる", "温かくする", "沸かす"], "topic": "読解"},
    36: {"text": "毎日 日本語を 勉強して います。", "options": ["毎日", "毎日", "毎日", "毎日"], "topic": "文字・語彙"},
    37: {"text": "これは 私の 本です。", "options": ["私", "私", "私", "私"], "topic": "文字・語彙"},
    38: {"text": "明日 友達と 映画を 見ます。", "options": ["明日", "明日", "明日", "明日"], "topic": "文字・語彙"},
    39: {"text": "この レストランは 高いです。", "options": ["高い", "低い", "安い", "大きい"], "topic": "文字・語彙"},
    40: {"text": "電車に 遅れました。", "options": ["遅れました", "間に合いました", "乗りました", "降りました"], "topic": "文字・語彙"},
    41: {"text": "風邪を ひいて しまいました。", "options": ["病気", "怪我", "風邪", "熱"], "topic": "文字・語彙"},
    42: {"text": "夏休みに 海へ 行きます。", "options": ["夏休み", "夏休み", "夏休み", "夏休み"], "topic": "文字・語彙"},
    43: {"text": "この 鞄は 重いです。", "options": ["重い", "軽い", "大きい", "小さい"], "topic": "文字・語彙"},
    44: {"text": "友達に 手紙を 書きました。", "options": ["手紙", "手紙", "手紙", "手紙"], "topic": "文字・語彙"},
    45: {"text": "今朝 7時に 起きました。", "options": ["起きました", "寝ました", "食べました", "飲みました"], "topic": "文字・語彙"},
    46: {"text": "この 仕事は 大変です。", "options": ["大変", "容易", "簡単", "難しい"], "topic": "文字・語彙"},
    47: {"text": "私は コーヒーを 飲みます。", "options": ["飲みます", "食べます", "入れます", "持ちます"], "topic": "文法"},
    48: {"text": "明日は 雨が 降る でしょう。", "options": ["降る", "曇る", "晴れる", "降る"], "topic": "文法"},
    49: {"text": "この ケーキは 食べられません。", "options": ["食べられません", "食べません", "食べます", "食べたい"], "topic": "文法"},
    50: {"text": "日本に 行った ことが あります。", "options": ["行った", "行った", "行った", "行った"], "topic": "文法"},
    51: {"text": "もっと 勉強 すれば よかった。", "options": ["すれば", "したら", "すると", "して"], "topic": "文法"},
    52: {"text": "この 花は きれいですね。", "options": ["きれい", "美しい", "汚い", "きれいだ"], "topic": "文法"},
    53: {"text": "私は ピアノを 弾く ことが できます。", "options": ["弾く", "弾く", "弾く", "弾く"], "topic": "文法"},
    54: {"text": "この ニュースを 聞いて びっくりした。", "options": ["聞いて", "見て", "読んで", "書いて"], "topic": "文法"},
    55: {"text": "電車の中では 電話を しては いけません。", "options": ["してはいけません", "してもいいです", "しなければなりません", "しなくてもいいです"], "topic": "文法"},
    56: {"text": "JLPT N4 に 合格 したいです。", "options": ["合格", "失敗", "合格", "合格"], "topic": "読解"},
    57: {"text": "この 文章の テーマは 何ですか。", "options": ["テーマ", "問題", "内容", "文章"], "topic": "読解"},
    58: {"text": "筆者は 何を 伝えたい ですか。", "options": ["伝えたい", "知りたい", "分からない", "教えたい"], "topic": "読解"},
    59: {"text": "この グラフから 何が わかりますか。", "options": ["グラフ", "表", "図表", "チャート"], "topic": "読解"},
    60: {"text": "次の 文と 同じ 意味の ものは どれですか。", "options": ["同じ", "違う", "似た", "表す"], "topic": "読解"},
    61: {"text": "この 広告の 目的は 何ですか。", "options": ["目的", "理由", "わけ", "意味"], "topic": "読解"},
    62: {"text": "著者の 意見に 最も 近い ものは どれですか。", "options": ["意見", "考え", "理論", "説明"], "topic": "読解"},
    63: {"text": "この 記事の 内容を 要約 して ください。", "options": ["要約", "まとめ", "紹介", "説明"], "topic": "読解"},
    64: {"text": "この 表から 読み取れる ことは 何ですか。", "options": ["読み取れる", "分かる", "見える", "聞こえる"], "topic": "読解"},
    65: {"text": "この 会話が 行われて いる 場所は どこですか。", "options": ["行われている", "している", "あった", "続いている"], "topic": "読解"},
    66: {"text": "話し手の 気持ちは どの ようなものか。", "options": ["気持ち", "感情", "意志", "気持ち"], "topic": "読解"},
    67: {"text": "この 文章を 読んで 感じた ことは 何ですか。", "options": ["感じた", "思った", "考えた", "分かった"], "topic": "読解"},
    68: {"text": "タイトルとして 最も 適切な ものは どれですか。", "options": ["タイトル", "題名", "名前", "表題"], "topic": "読解"},
    69: {"text": "この 資料の 特徴を 説明 して ください。", "options": ["特徴", "性質", "特性", "違い"], "topic": "読解"},
    70: {"text": "最後に 筆者が 言いたい ことは 何ですか。", "options": ["最後", "終わり", "最後", "最後"], "topic": "読解"},
}

# ============================================
# DISTRIBUSI TOPIK PER NOMOR SOAL
# ============================================
TOPIC_DISTRIBUTION = {
    "文字・語彙": list(range(1, 16)) + list(range(36, 47)),
    "文法": list(range(16, 26)) + list(range(47, 56)),
    "読解": list(range(26, 36)) + list(range(56, 71)),
}

# ============================================
# FUNGSI UNTUK MENGHITUNG SKOR
# ============================================

def calculate_score(jawaban_peserta):
    """
    Menghitung skor per topik dalam persen (%)
    jawaban_peserta: dict {nomor_soal: jawaban} (1-4)
    """
    from kunci_jawaban import KUNCI_JAWABAN
    
    hasil = {}
    
    for topik, soal_list in TOPIC_DISTRIBUTION.items():
        if topik not in ["文字・語彙", "文法", "読解"]:
            continue
        
        benar = 0
        total = 0
        
        for nomor in soal_list:
            if nomor in jawaban_peserta and nomor in KUNCI_JAWABAN:
                total += 1
                if jawaban_peserta[nomor] == KUNCI_JAWABAN[nomor]:
                    benar += 1
        
        if total > 0:
            hasil[topik] = (benar / total) * 100
        else:
            hasil[topik] = 0
    
    return hasil


def get_total_poin(kanji_persen, kosakata_persen, grammar_persen, reading_persen):
    """
    Menghitung total poin JLPT dari 4 kategori
    Masing-masing kategori maksimal 30 poin (120/4)
    Total = (K1 + K2 + K3 + K4) × 0.3
    """
    total_persen = kanji_persen + kosakata_persen + grammar_persen + reading_persen
    total_poin = total_persen * 0.3
    return round(total_poin, 1)


def predict_readiness_from_scores(kanji, kosakata, grammar, reading):
    """
    Memprediksi kesiapan dari skor persen (0-100) masing-masing kategori
    """
    total_poin = get_total_poin(kanji, kosakata, grammar, reading)
    
    if total_poin >= TOTAL_SCORE_TARGET:
        return 2, total_poin  # Siap
    elif total_poin >= TOTAL_SCORE_TARGET - 10:
        return 1, total_poin  # Hampir Siap
    else:
        return 0, total_poin  # Belum Siap


def predict_readiness(jawaban_peserta):
    """
    Memprediksi kesiapan dari jawaban peserta
    """
    skor_persen = calculate_score(jawaban_peserta)
    
    kanji_persen = skor_persen.get("文字・語彙", 0)
    grammar_persen = skor_persen.get("文法", 0)
    reading_persen = skor_persen.get("読解", 0)
    kosakata_persen = skor_persen.get("文字・語彙", 0)  # Sama dengan kanji
    
    total_poin = get_total_poin(kanji_persen, kosakata_persen, grammar_persen, reading_persen)
    
    if total_poin >= TOTAL_SCORE_TARGET:
        return 2  # Siap
    elif total_poin >= TOTAL_SCORE_TARGET - 10:
        return 1  # Hampir Siap
    else:
        return 0  # Belum Siap


def get_section_scores(jawaban_peserta):
    """
    Mendapatkan skor per bagian dalam persen
    """
    return calculate_score(jawaban_peserta)