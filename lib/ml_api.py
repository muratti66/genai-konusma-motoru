import torch
from components.load_window import LoadWindow
from conf.config import Config
from conf.static import Messages
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline, Pipeline


class MLAPI:
    __ml_stt_pipe: Pipeline | None = None
    __local_files_only = False
    __force_download = False
    __code_revision = False
    __use_fast = True

    @staticmethod
    def init():
        LoadWindow.update_loading_msg(Messages.COMP_STARTING.format(MLAPI.__name__))
        if Config.HUGGING_FACE_DOWNLOAD_ALLOW:
            __local_files_only = True
            __force_download = True
            __code_revision = True
            __use_fast = False

        MLAPI.__init_speech_to_text()
        LoadWindow.update_loading_msg(Messages.COMP_STARTED.format(MLAPI.__name__))

    @staticmethod
    def __init_speech_to_text() -> None:
        device = "cuda:0" if torch.cuda.is_available() else 'cpu'
        torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            Config.HUGGING_FACE_STT_MODEL,
            torch_dtype=torch_dtype,
            low_cpu_mem_usage=True,
            use_safetensors=True,
            local_files_only=MLAPI.__local_files_only,
            force_download=MLAPI.__force_download,
            code_revision=MLAPI.__code_revision
        )
        model.to(device)
        processor = AutoProcessor.from_pretrained(Config.HUGGING_FACE_STT_MODEL)
        MLAPI.__ml_stt_pipe = pipeline(
            Config.HUGGING_FACE_STT_TASK,
            model=model,
            tokenizer=processor.tokenizer,
            feature_extractor=processor.feature_extractor,
            max_new_tokens=Config.HUGGING_FACE_STT_MAX_NEW_TOKENS,  # def.: max_new_tokens=128,
            chunk_length_s=Config.HUGGING_FACE_STT_CHUNK_LEN,  # def.: chunk_length_s=30,
            batch_size=Config.HUGGING_FACE_STT_BATCH_SIZE,  # def.: batch_size=16,
            return_timestamps=True,
            torch_dtype=torch_dtype,
            device=device,
            use_fast=MLAPI.__use_fast
        )

    @staticmethod
    def get_stt_w_file(file: str) -> str:
        """
        Get Text Speech To Text ML Module
        :param file: str sound file name
        :return: str
        """
        return MLAPI.__ml_stt_pipe(
            file, return_timestamps=True, generate_kwargs=Config.HUGGING_FACE_STT_LANG_CONF
        )['text']

    @staticmethod
    def close() -> None:
        pass
