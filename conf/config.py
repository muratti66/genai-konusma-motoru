
class Config:
    GEMINI_API_KEY = '***********'
    GEMINI_MODEL = 'gemini-pro'
    HUGGING_FACE_DOWNLOAD_ALLOW = False
    HUGGING_FACE_STT_MODEL = 'openai/whisper-small'
    HUGGING_FACE_STT_LANG_CONF = {'language': 'turkish'}
    HUGGING_FACE_STT_TASK = 'automatic-speech-recognition'
    HUGGING_FACE_STT_BATCH_SIZE = 4
    HUGGING_FACE_STT_CHUNK_LEN = 3
    HUGGING_FACE_STT_MAX_NEW_TOKENS = 128
    MICROPHONE_SAMPLE_RATE = 44100
    MICROPHONE_FRAMES_PER_BUFFER = 1024
    MAIN_WINDOW_GEOMETRY = '575x620+20+20'
    LOAD_WINDOW_GEOMETRY = '240x90+180+120'
    MAC_VOICE_CMD = ["say", "-r", "180", "--quality=127"]
