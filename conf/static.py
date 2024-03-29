class StaticValues:
    AUTHOR = 'Murat B.'
    DEFAULT_QUESTION = 'Yazılı soruyu yazınız..'
    DEFAULT_ANSWER = """* Yazılı soruda yazıp ENTER'a basıldığında:

1. Kullanıcı bir yazılı soru girer.
2. Soru, metin tabanlı bir yapay zeka modelinin işleneceği bir sunucuya gönderilir.
3. Model, soruya en iyi yanıtı oluşturmak için eğitim verilerini ve algoritmasını kullanır.
4. Yanıt, kullanıcının ekranında görüntülenir.

* Konuşma için düğmeye basılı tutulduğunda:

1. Kullanıcı, düğmeye basılı tutarak bir konuşma başlatır.
2. Konuşma, konuşma tanıma teknolojisi tarafından işlenir.
3. Tanınan konuşma, metin tabanlı bir yapay zeka modelinin işleneceği bir sunucuya gönderilir.
4. Model, konuşmaya en iyi yanıtı oluşturmak için eğitim verilerini ve algoritmasını kullanır.
5. Yanıt, konuşma sentezi teknolojisi kullanılarak kullanıcıya sesli olarak iletilir.

* Hazırlayan: {}
""".format(AUTHOR)

    GEMINI_ANSWER_MSG = '== Gemini Cevabı == \n\n'
    MAIN_WINDOW_TITLE = 'Gemini AI Konuşma Motoru    /    Murat B.'
    LOAD_WINDOW_TITLE = 'Açılıyor...'
    STATUS_PREFIX = 'DURUM: '
    FIRST_RUN_PARAM = '--first-run'


class FilePaths:
    REC_TMP_FILE_PATH = 'tmp/recorded_audio.wav'
    ANSWER_TMP_FILE_PATH = 'tmp/answer_audio.mp3'
    VOICE_ICON = 'icons/ses_icon.png'
    PROG_ICON = 'icons/program_icon.png'


class Messages:
    AUDIO_SAVE = 'Audio saved.'
    REC_STARTED = 'Recording started.'
    REC_STOPPED = 'Recording stopped.'
    COMP_STARTING = '{} başlatılıyor..'
    COMP_STARTED = '{} başladı.'
    COMP_STOPPED = '{} durduruludu.'
    COMP_INIT_DONE = '{} init tamamlandı..'
    REQ_LOADING = 'Gereksinimler yükleniyor...'
    APP_STARTING = 'Uygulama başlatılıyor..'
    APP_STARTED = 'Uygulama başlatıldı.'
    VOICE_LISTENING = 'Soru mikrafondan dinleniyor..'
    VOICE_LISTENED = 'Dinleme tamamlandı.'
    VOICE_TO_TEXT = 'Ses metine çeviriliyor..'
    VOICE_TO_TEXT_DONE = 'Ses metine çevirildi.'
    TEXT_TO_GENAI = 'Soru Gemini\'ye gönderiliyor..'
    ANSWER_FROM_GENAI = 'Cevap Geminiden alındı.'
    ANSWER_TO_VOICE = 'Cevap seslendirildi.'
    COPY_TO_CLIPBOARD = 'Cevap panoya kopyalandı.'


class ShortCuts:
    RETURN = '<Return>'
    CMD_S = '<Command-s>'
    CMD_C = '<Command-c>'
    BTN_PRESS = '<ButtonPress>'
    BTN_RELEASE = '<ButtonRelease>'


class OSValues:
    MACOSX = 'Darwin'
    WINDOWS = 'Windows'
    LINUX = 'Linux'
