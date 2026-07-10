from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from peft.peft_model import PeftModel
from transformers import (
    AutoModelForSeq2SeqLM,
    BitsAndBytesConfig,
    PreTrainedTokenizerBase,
    Trainer,
    TrainingArguments
)
from transformers.modeling_utils import PreTrainedModel
