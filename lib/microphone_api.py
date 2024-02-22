import pyaudio
import numpy as np
import wave
import threading
from components.load_window import LoadWindow
from conf.config import Config
from conf.static import FilePaths, Messages


class MicrophoneAPI:
    __sample_rate: int
    __frames = list()
    __p = None
    __stream = None
    __is_recording = False
    __process_done = False
    __lock: threading.Lock

    @staticmethod
    def init(sample_rate: int = Config.MICROPHONE_SAMPLE_RATE):
        LoadWindow.update_loading_msg(Messages.COMP_STARTING.format(MicrophoneAPI.__name__))
        MicrophoneAPI.__sample_rate = sample_rate
        MicrophoneAPI.__frames = []
        MicrophoneAPI.__p = pyaudio.PyAudio()
        MicrophoneAPI.__is_recording = False
        MicrophoneAPI.__process_done = False
        MicrophoneAPI.__lock = threading.Lock()
        LoadWindow.update_loading_msg(Messages.COMP_STARTED.format(MicrophoneAPI.__name__))

    @staticmethod
    def start_recording():
        MicrophoneAPI.__frames = []
        MicrophoneAPI.__is_recording = True
        MicrophoneAPI.__process_done = False
        threading.Thread(target=MicrophoneAPI.__record_audio).start()

    @staticmethod
    def __record_audio():
        with MicrophoneAPI.__lock:
            MicrophoneAPI.__stream = MicrophoneAPI.__p.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=MicrophoneAPI.__sample_rate,
                input=True,
                frames_per_buffer=Config.MICROPHONE_FRAMES_PER_BUFFER
            )

            print(Messages.REC_STARTED)

            while MicrophoneAPI.__is_recording:
                data = np.frombuffer(MicrophoneAPI.__stream.read(Config.MICROPHONE_FRAMES_PER_BUFFER), dtype=np.int16)
                MicrophoneAPI.__frames.append(data.tostring())

            print(Messages.REC_STOPPED)

            if MicrophoneAPI.__stream:
                MicrophoneAPI.__stream.stop_stream()
                MicrophoneAPI.__stream.close()
            MicrophoneAPI.__p.terminate()
            MicrophoneAPI.__save_audio()

    @staticmethod
    def stop_recording():
        MicrophoneAPI.__is_recording = False
        while not MicrophoneAPI.__process_done:
            pass

    @staticmethod
    def __save_audio():
        if MicrophoneAPI.__frames:
            audio_data = b''.join(MicrophoneAPI.__frames)
            wf = wave.open(FilePaths.REC_TMP_FILE_PATH, 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(MicrophoneAPI.__p.get_sample_size(pyaudio.paInt16))
            wf.setframerate(MicrophoneAPI.__sample_rate)
            wf.writeframes(audio_data)
            wf.close()
            print(Messages.AUDIO_SAVE)
        MicrophoneAPI.__process_done = True
