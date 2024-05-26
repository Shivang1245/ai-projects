# # For Photos generation
# from ctransformers import AutoModelForCausalLM
from diffusers import DiffusionPipeline
# from transformers import pipeline
# from transformers import AutoTokenizer, AutoModelForCausalLM


# for images
# pipeline = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0")

# This model is for image refining using stable diffusion refiner
# pipeline = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-refiner-1.0")

# for Colouring Book generation

pipeline = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0")
pipeline.load_lora_weights("artificialguybr/ColoringBookRedmond-V2")

# For Voice Transcription
# Use a pipeline as a high-level helper

# pipe = pipeline("automatic-speech-recognition", model="openai/whisper-medium")

# Lama Model
# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
# llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7b-Chat-GGUF", model_file="llama-2-7b-chat.q4_K_M.gguf", model_type="llama", gpu_layers=50)
# Load model directly


# Load Mistral Models
# 1. Mistral 7B instruct v2
# tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
# model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")

# 2. mixtral 8x22B v0.1
# tokenizer = AutoTokenizer.from_pretrained("mistral-community/Mixtral-8x22B-v0.1")
# model = AutoModelForCausalLM.fromh_pretrained("mistral-community/Mixtral-8x22B-v0.1")
