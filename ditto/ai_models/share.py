import ditto.ai_models.config as config

from ditto.ai_models.cldm.hack import disable_verbosity, enable_sliced_attention


disable_verbosity()

if config.save_memory:
    enable_sliced_attention()