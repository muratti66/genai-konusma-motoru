
class Config:
    GEMINI_API_KEY = '********'
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
    WINDOW_GEOMETRY = '575x586+900+100'
    MAC_VOICE_CMD = ["say", "-r", "180", "--quality=127"]
